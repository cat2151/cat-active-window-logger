import win32gui
import win32process
import psutil

def get_active_window_information():
    hwnd = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(hwnd)
    thread_id, pid = win32process.GetWindowThreadProcessId(hwnd)
    process_name = psutil.Process(pid).name()
    return window_title, process_name, thread_id, pid, hwnd

def main():
    window_title, process_name, thread_id, pid, hwnd = get_active_window_information()
    print(f"Active Window Title: {window_title}")
    print(f"Process Name: {process_name}")
    print(f"Window Handle: {hwnd}")
    print(f"Thread ID: {thread_id}")
    print(f"Process ID: {pid}")

if __name__ == "__main__":
    main()
