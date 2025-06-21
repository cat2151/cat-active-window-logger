import re
import win32gui
import win32process
import win32api
import win32con
import psutil

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
