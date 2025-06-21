import re
import time
import datetime
from get_window_info import get_active_window_information
from ipc import ipc_send_message
from log_and_display import display_window_info, log_window_info
from utils import get_args, update_args_by_toml
from dated_log import rotate_logfile_if_needed, initialize_dated_logging

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

def handle_foreground_change_and_ipc(args, previous_window_info, foreground, previous_action):
    if not (foreground and previous_window_info):
        return previous_action
    previous_foreground = previous_window_info[0]
    if foreground != previous_foreground:
        previous_action = check_and_ipc_by_window_info(foreground, args, previous_action)
    else:
        print("previousと同じforegroundなのでskipします")
    return previous_action

def check_and_ipc_by_window_info(foreground, args, previous_action):
    if not foreground:
        return previous_action
    window_title, _process_name, _thread_id, _pid, _hwnd = foreground

    for action in args.actions:
        action_executed, previous_action, is_same_previous_action = process_action_if_title_matches(
            action, previous_action, window_title, args.pipe_name
        )
        if action_executed:
            break
        if is_same_previous_action:
            print("previousと同じactionなのでskipします")
            break
    return previous_action

def process_action_if_title_matches(action, previous_action, window_title, pipe_name):
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
        ipc_send_message(pipe_name, message)
        print(f"send message: {message}")
    action_executed = True
    previous_action = action
    return action_executed, previous_action, is_same_previous_action

if __name__ == "__main__":
    main()
