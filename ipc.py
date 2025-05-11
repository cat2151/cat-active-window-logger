from contextlib import contextmanager
import win32pipe
import win32file
import os

def ipc_send_message(pipe_name, message):
    try:
        with ipc_create_pipe_handle(pipe_name) as ipc_handle:
            win32file.WriteFile(ipc_handle, message.encode())
            resp = win32file.ReadFile(ipc_handle, 64 * 1024)
            print(f"Server response: {resp[1].decode()}")
    except (win32file.error, OSError) as e:
        print(f"\nERROR : Exception: {e}")
        print(f"Error during IPC communication: {e}\n")
        os._exit(1)

@contextmanager
def ipc_create_pipe_handle(pipe_name):
    try:
        timeout_msec = 5000
        win32pipe.WaitNamedPipe(pipe_name, timeout_msec)
        handle = win32file.CreateFile(
            pipe_name,
            win32file.GENERIC_READ | win32file.GENERIC_WRITE,
            0, None,
            win32file.OPEN_EXISTING,
            0, None
        )
    except (OSError, win32file.error) as e:
        print(f"\nERROR : Exception: {e}")
        print(f"ERROR : server側が起動済みであることと、名前付きパイプ名が一致していることを確認してください（名前付きパイプ名：{pipe_name}）\n")
        os._exit(1)

    try:
        yield handle
    finally:
        win32file.CloseHandle(handle)
