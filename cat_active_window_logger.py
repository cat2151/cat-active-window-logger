import argparse
import datetime
import re
import subprocess
import time
import logging
import toml
import win32gui
import win32process
import win32api
import win32con
import psutil

def main():
    args = get_args()
    args = update_args_by_toml(args, args.config_filename)
    setup_logging(args.log_filename)
    previous_window_info = None
    while True:
        (foreground, topmost_window, are_windows_equal) = get_active_window_information()
        current_window_info = (foreground, topmost_window, are_windows_equal)
        if current_window_info and current_window_info != previous_window_info:
            previous_window_info = current_window_info
            current_time = datetime.datetime.now()
            log_window_info(foreground, current_time)
            display_window_info(foreground)
            check_and_exec_by_window_info(foreground, args)
            if not are_windows_equal:
                display_window_info(topmost_window)
                log_window_info(topmost_window, current_time, True)
                print("Foreground and Topmost Window are different.")
        time.sleep(1)

def check_and_exec_by_window_info(foreground, args):
    if foreground:
        window_title, _process_name, _thread_id, _pid, _hwnd = foreground
        if args.title_regex:
            if re.search(args.title_regex, window_title):
                print(f"Window title matches regex: {args.title_regex} : {window_title}")
                if args.exec_cmd:
                    try:
                        subprocess.run(args.exec_cmd, shell=True, check=True)
                    except subprocess.CalledProcessError as e:
                        print(f"Command failed with return code {e.returncode}: {e}")
                    except FileNotFoundError as e:
                        print(f"Command not found: {e}")

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

def setup_logging(filename):
    logging.basicConfig(
        filename=filename,
        level=logging.INFO,
        format="%(message)s",
        encoding="utf-8"
    )

def get_active_window_information():
    hwnd = win32gui.GetForegroundWindow()
    foreground = get_window_information(hwnd)

    hwnd = get_topmost_window_in_active_monitor()
    topmost_window = get_window_information(hwnd)

    are_windows_equal = True
    if foreground and topmost_window:
        if foreground != topmost_window:
            are_windows_equal = False

    return foreground, topmost_window, are_windows_equal

def get_topmost_window_in_active_monitor():
    active_monitor = get_active_window_monitor()

    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            rect = win32gui.GetWindowRect(hwnd)
            monitor = win32api.MonitorFromRect(rect, win32con.MONITOR_DEFAULTTONEAREST)
            if monitor == active_monitor and win32gui.GetWindowText(hwnd):
                windows.append(hwnd)
        return True

    windows = []
    win32gui.EnumWindows(callback, windows)

    return windows[0] if windows else None

def get_active_window_monitor():
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

if __name__ == "__main__":
    main()
