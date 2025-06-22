import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from log_enhance_active_time.add_active_time import add_elapsed_time

def test_add_active_time():
    infos = [
        {
            'timestamp': '2025/01/01 12:34:56',
            'window_title': 'foo app',
            'process_name': 'foo_app.EXE',
            'window_handle': 12345,
            'thread_id': 23456,
            'process_id': 34567
        },
        {
            'timestamp': '2025/01/01 13:34:56',
            'window_title': 'foo2 app',
            'process_name': 'foo2_app.EXE',
            'window_handle': 12346,
            'thread_id': 23457,
            'process_id': 34568
        }
    ]
    result = add_elapsed_time(infos, "%Y/%m/%d %H:%M:%S")
    assert result[0]['elapsed_time'] == '01:00:00'
    assert result[1]['elapsed_time'] == ''
    print('test_add_active_time passed')

if __name__ == '__main__':
    test_add_active_time()
