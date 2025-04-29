import datetime
import time
import logging
import win32gui
import win32process
import win32api
import win32con
import psutil

def main():
    setup_logging("active_window_log.toml")
    previous_window_info = None
    while True:
        (foreground, topmost_window, are_windows_equal) = get_active_window_information()
        current_window_info = (foreground, topmost_window, are_windows_equal)
        if current_window_info and current_window_info != previous_window_info:
            previous_window_info = current_window_info
            current_time = datetime.datetime.now()
            log_window_info(foreground, current_time)
            display_window_info(foreground)
            if not are_windows_equal:
                display_window_info(topmost_window)
                log_window_info(topmost_window, current_time, True)
                print("Foreground and Topmost Window are different.")
        time.sleep(1)

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
    window_title, process_name, thread_id, pid, hwnd = current_window_info
    print("\033[H\033[J", end="")
    print(f"Active Window Title: {window_title}")
    print(f"Process Name: {process_name}")
    print(f"Window Handle: {hwnd}")
    print(f"Thread ID: {thread_id}")
    print(f"Process ID: {pid}")

def log_window_info(current_window_info, current_time, is_topmost=False):
    window_title, process_name, thread_id, pid, hwnd = current_window_info
    element_title = "[[topmost_window_information]]\n" if is_topmost else "[[active_window_information]]\n"
    log_message = (
        f"{element_title}"
        f"    timestamp = \"{current_time.strftime('%Y/%m/%d %H:%M:%S')}\"\n"
        f"    window_title = \"{window_title}\"\n"
        f"    process_name = \"{process_name}\"\n"
        f"    window_handle = {hwnd}\n"
        f"    thread_id = {thread_id}\n"
        f"    process_id = {pid}\n"
    )
    logging.info(log_message)

if __name__ == "__main__":
    main()
