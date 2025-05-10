import os
import argparse
import datetime
import re
import time
import logging
from contextlib import contextmanager
import toml
import win32pipe
import win32file
import win32gui
import win32process
import win32api
import win32con
import psutil

def main():
    args = get_args()
    args = update_args_by_toml(args, args.config_filename)
    setup_logging(args.log_filename)
    with ipc_create_pipe_handle(args.pipe_name) as ipc_handle:
        track_active_window(args, ipc_handle)

def get_args():
    parser = argparse.ArgumentParser(description="Log active window information.")
    parser.add_argument("--config-filename", type=str, help="Path to the config file")
    args = parser.parse_args()
    return args

def update_args_by_toml(args, config_filename=None):
    if not config_filename:
        config_filename = args.config_filename
    print(f'args : before: {args}')
    toml_data = read_toml(config_filename)
    print(f'TOML : {toml_data}')
    for key, value in toml_data.items():
        setattr(args, key, value)
    print(f'args : after : {args}')
    return args

def read_toml(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        toml_data = toml.load(f)
    return toml_data

def track_active_window(args, ipc_handle):
    previous_window_info = None
    previous_action = None  # 初期値を設定
    while True:
        current_window_info = get_active_window_information(args.ignore_process_regex)
        if is_window_info_changed(current_window_info, previous_window_info):
            previous_action = handle_window_change(
                current_window_info, args, ipc_handle, previous_window_info, previous_action
            )
            previous_window_info = current_window_info
        time.sleep(1)

def get_current_window_info():
    foreground, topmost_window, are_windows_equal = get_active_window_information()
    return foreground, topmost_window, are_windows_equal

def is_window_info_changed(current_window_info, previous_window_info):
    return current_window_info and current_window_info != previous_window_info

def handle_window_change(current_window_info, args, ipc_handle, previous_window_info, previous_action):
    foreground, topmost_window, are_windows_equal = current_window_info
    current_time = datetime.datetime.now()

    log_window_info(foreground, current_time)
    display_window_info(foreground)
    previous_action = handle_foreground_change_and_ipc(
        args, ipc_handle, previous_window_info, foreground, previous_action
    )

    if not are_windows_equal:
        display_window_info(topmost_window)
        log_window_info(topmost_window, current_time, is_topmost=True)
        print("Foreground and Topmost Window are different.")

    return previous_action

def handle_foreground_change_and_ipc(args, ipc_handle, previous_window_info, foreground, previous_action):
    if not (foreground and previous_window_info):
        return previous_action
    previous_foreground = previous_window_info[0]
    if foreground != previous_foreground:
        previous_action = check_and_ipc_by_window_info(foreground, args, ipc_handle, previous_action)
    else:
        print("previousと同じforegroundなのでskipします")
    return previous_action

def check_and_ipc_by_window_info(foreground, args, ipc_handle, previous_action):
    if not foreground:
        return previous_action
    window_title, _process_name, _thread_id, _pid, _hwnd = foreground

    for action in args.actions:
        action_executed, previous_action, is_same_previous_action = process_action_if_title_matches(
            action, previous_action, window_title, ipc_handle
        )
        if action_executed:
            break
        if is_same_previous_action:
            print("previousと同じactionなのでskipします")
            break
    return previous_action

def process_action_if_title_matches(action, previous_action, window_title, ipc_handle):
    print(f"Checking action: {action['action_name']}, previous: {previous_action['action_name'] if previous_action else None}")
    action_executed = False
    is_same_previous_action = False

    if not action.get("title_regex") or not re.search(action["title_regex"], window_title):
        return action_executed, previous_action, is_same_previous_action

    print(f"INFO : matchしました : regex: {action['title_regex']} : {window_title}")

    if action == previous_action:
        is_same_previous_action = True
        return action_executed, previous_action, is_same_previous_action

    message = action["message"]
    if message:
        ipc_send_message(ipc_handle, message)
        print(f"send message: {message}")
    action_executed = True
    previous_action = action
    return action_executed, previous_action, is_same_previous_action

def setup_logging(filename):
    logging.basicConfig(
        filename=filename,
        level=logging.INFO,
        format="%(message)s",
        encoding="utf-8"
    )

def get_active_window_information(ignore_process_regex):
    hwnd = win32gui.GetForegroundWindow()
    foreground = get_window_information(hwnd)

    hwnd = get_topmost_window_in_active_monitor(ignore_process_regex)
    topmost_window = get_window_information(hwnd)

    are_windows_equal = True
    if foreground and topmost_window:
        if foreground != topmost_window:
            are_windows_equal = False

    return foreground, topmost_window, are_windows_equal

def get_topmost_window_in_active_monitor(ignore_process_regex):
    active_monitor = get_active_monitor()

    def callback(hwnd, windows):
        if not (win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd)):
            return True

        rect = win32gui.GetWindowRect(hwnd)
        monitor = win32api.MonitorFromRect(rect, win32con.MONITOR_DEFAULTTONEAREST)
        if monitor != active_monitor or not win32gui.GetWindowText(hwnd):
            return True

        window_info = get_window_information(hwnd)
        if not window_info:
            return True

        process_name = window_info[1]
        # Check if the process matches any ignore regex
        if ignore_process_regex:
            for regex in ignore_process_regex:
                if re.search(regex, process_name):
                    print(f"INFO: Skipping process '{process_name}' due to ignore regex: {regex}")
                    return True

        windows.append(hwnd)
        return True

    windows = []
    win32gui.EnumWindows(callback, windows)

    return windows[0] if windows else None

def is_ignore_window_process(args, current_window_info):
    if args.ignore_process_regex:
        for regex in args.ignore_process_regex:
            if re.search(regex, current_window_info[0][1]):
                print(f"INFO : {current_window_info[0][1]} is ignored by regex: {regex}")
                return True
    return False

def get_active_monitor():
    hwnd = win32gui.GetForegroundWindow()
    if not hwnd:
        return None

    rect = win32gui.GetWindowRect(hwnd)
    monitor = win32api.MonitorFromRect(rect, win32con.MONITOR_DEFAULTTONEAREST)
    return monitor

def get_window_information(hwnd):
    if not hwnd:
        return None

    window_title = win32gui.GetWindowText(hwnd)
    thread_id, pid = win32process.GetWindowThreadProcessId(hwnd)
    if pid <= 0:
        return None

    try:
        process_name = psutil.Process(pid).name()
    except psutil.NoSuchProcess:
        return None

    return window_title, process_name, thread_id, pid, hwnd

def display_window_info(current_window_info):
    if not current_window_info:
        return # こうしないとスクリーンセーバーで落ちる
    window_title, process_name, thread_id, pid, hwnd = current_window_info
    print("\033[H\033[J", end="")
    print(f"Active Window Title: {window_title}")
    print(f"Process Name: {process_name}")
    print(f"Window Handle: {hwnd}")
    print(f"Thread ID: {thread_id}")
    print(f"Process ID: {pid}")

def log_window_info(current_window_info, current_time, is_topmost=False):
    element_title = "[[topmost_window_information]]\n" if is_topmost else "[[active_window_information]]\n"
    log_message_base = (f"{element_title}"
                        f"    timestamp = \"{current_time.strftime('%Y/%m/%d %H:%M:%S')}\"\n"
    )
    log_message = None
    if current_window_info:
        window_title, process_name, thread_id, pid, hwnd = current_window_info
        log_message = (
            f"{log_message_base}"
            f"    window_title = \'{window_title}\'\n" # window_titleはシングルォーティングする。でないとbackslashを含むときに、dump tomlがエラーになる
            f"    process_name = \'{process_name}\'\n"
            f"    window_handle = {hwnd}\n"
            f"    thread_id = {thread_id}\n"
            f"    process_id = {pid}\n"
        )
    else:
        log_message = (
            f"{log_message_base}"
            f"    window_title = \'It seems that the screensaver might be active.\'\n"
        )
    logging.info(log_message)

@contextmanager
def ipc_create_pipe_handle(pipe_name):
    try:
        timeout_msec = 5000
        win32pipe.WaitNamedPipe(pipe_name, timeout_msec)
        handle = win32file.CreateFile(
            pipe_name,
            win32file.GENERIC_READ | win32file.GENERIC_WRITE,
            0, None,
            win32file.OPEN_EXISTING,
            0, None
        )
    except (OSError, win32file.error) as e:
        print(f"\nException: {e}")
        print(f"ERROR : server側が起動済みであることと、名前付きパイプ名が一致していることを確認してください（名前付きパイプ名：{pipe_name}）\n")
        os._exit(1)

    try:
        yield handle
    finally:
        win32file.CloseHandle(handle)

def ipc_send_message(ipc_handle, message):
    win32file.WriteFile(ipc_handle, message.encode())
    resp = win32file.ReadFile(ipc_handle, 64*1024)
    print(f"Server response: {resp[1].decode()}")

if __name__ == "__main__":
    main()
