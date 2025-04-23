import win32gui
import win32process
import psutil

def main():
    previous_window_info = None
    while True:
        try:
            current_window_info = get_active_window_information()
        except (psutil.NoSuchProcess) as e:
            print(f"Error retrieving window information: {e}")
            continue
        if current_window_info != previous_window_info:
            previous_window_info = current_window_info
            display_window_info(current_window_info)

def get_active_window_information():
    hwnd = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(hwnd)
    thread_id, pid = win32process.GetWindowThreadProcessId(hwnd)
    process_name = psutil.Process(pid).name()
    return window_title, process_name, thread_id, pid, hwnd

def display_window_info(current_window_info):
    window_title, process_name, thread_id, pid, hwnd = current_window_info
    print("\033[H\033[J", end="")
    print(f"Active Window Title: {window_title}")
    print(f"Process Name: {process_name}")
    print(f"Window Handle: {hwnd}")
    print(f"Thread ID: {thread_id}")
    print(f"Process ID: {pid}")

if __name__ == "__main__":
    main()
