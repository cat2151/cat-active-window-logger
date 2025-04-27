import time
import logging
import win32gui
import win32process
import win32api
import win32con
import psutil

def main():
    setup_logging("active_window_log.txt")
    previous_window_info = None
    while True:
        current_window_info = get_active_window_information()
        if current_window_info and current_window_info != previous_window_info:
            previous_window_info = current_window_info
            display_window_info(current_window_info)
            log_window_info(current_window_info)
        time.sleep(1)

def setup_logging(filename):
    logging.basicConfig(
        filename=filename,
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        encoding="utf-8"
    )

def get_active_window_information():
    hwnd = win32gui.GetForegroundWindow()
    foreground = get_window_information(hwnd)

    hwnd = get_topmost_window_in_active_monitor()
    topmost_window = get_window_information(hwnd)

    if foreground and topmost_window:
        if foreground != topmost_window:
            print("Foreground and Topmost Window are different.")
            print(f"Foreground Window: {foreground}")
            print(f"Topmost Window: {topmost_window}")

    return foreground

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

def log_window_info(current_window_info):
    window_title, process_name, thread_id, pid, hwnd = current_window_info
    log_message = (
        "Active Window Information:\n"
        f"Window Title: {window_title}\n"
        f"Process Name: {process_name}\n"
        f"Window Handle: {hwnd}\n"
        f"Thread ID: {thread_id}\n"
        f"Process ID: {pid}\n"
        + "-" * 40
    )
    logging.info(log_message)

if __name__ == "__main__":
    main()
