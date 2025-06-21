import re
from ipc import ipc_send_message

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
        action_executed, previous_action, is_same_previous_action = process_ipc_action_if_title_matches(
            action, previous_action, window_title, args.pipe_name
        )
        if action_executed or is_same_previous_action:
            if is_same_previous_action:
                print("previousと同じactionなのでskipします")
            break
    return previous_action

def process_ipc_action_if_title_matches(action, previous_action, window_title, pipe_name):
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
