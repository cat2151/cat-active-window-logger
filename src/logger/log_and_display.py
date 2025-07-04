import logging

def setup_logging(filename):
    def close_and_remove_all_handlers(logger):
        if logger.handlers:
            for handler in logger.handlers[:]:
                handler.close()
                logger.removeHandler(handler)
    def add_file_handler(logger, filename):
        file_handler = logging.FileHandler(filename, encoding="utf-8")
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter("%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
    root = logging.getLogger()
    close_and_remove_all_handlers(root)
    add_file_handler(root, filename)

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
