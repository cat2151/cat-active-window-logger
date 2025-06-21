import time
import datetime
from get_window_info import get_active_window_information
from log_and_display import display_window_info, log_window_info
from utils import get_args, update_args_by_toml
from dated_log import rotate_logfile_if_needed, initialize_dated_logging
from action_by_ipc import handle_foreground_change_and_ipc

def main():
    args = get_args()
    args = update_args_by_toml(args, args.config_filename)
    initialize_dated_logging(args)
    track_active_window(args)

def track_active_window(args):
    previous_window_info = None
    previous_action = None
    while True:
        rotate_logfile_if_needed(args)
        current_window_info = get_active_window_information(args.ignore_process_regex)
        if is_window_info_changed(current_window_info, previous_window_info):
            previous_action = handle_window_change(
                current_window_info, args, previous_window_info, previous_action
            )
            previous_window_info = current_window_info
        time.sleep(args.logging_interval_sec)

def is_window_info_changed(current_window_info, previous_window_info):
    return current_window_info and current_window_info != previous_window_info

def handle_window_change(current_window_info, args, previous_window_info, previous_action):
    foreground, topmost_window, are_windows_equal = current_window_info
    current_time = datetime.datetime.now()

    log_window_info(foreground, current_time)
    display_window_info(foreground)
    previous_action = handle_foreground_change_and_ipc(
        args, previous_window_info, foreground, previous_action
    )

    if not are_windows_equal:
        display_window_info(topmost_window)
        log_window_info(topmost_window, current_time, is_topmost=True)
        print("Foreground and Topmost Window are different.")

    return previous_action

if __name__ == "__main__":
    main()
