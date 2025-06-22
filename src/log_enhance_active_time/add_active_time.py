from datetime import datetime
import toml
from logger.utils import get_args, update_args_by_toml

def main():
    args = get_args()
    args = update_args_by_toml(args, args.config_filename)
    args = replace_today_in_args(args)

    input_log = parse_log(args.input_log_filename)
    infos = input_log['active_window_information']

    infos = add_elapsed_time(infos, args.time_format)
    write_output_log(args.output_log_filename, infos)

def replace_today_in_args(args):
    args.input_log_filename = replace_today_placeholder(args.input_log_filename)
    args.output_log_filename = replace_today_placeholder(args.output_log_filename)
    return args

def replace_today_placeholder(path: str) -> str:
    """{today} を今日の日付(YYYYMMDD)に置換"""
    today_str = datetime.today().strftime('%Y%m%d')
    return path.replace('{today}', today_str)

def parse_log(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = toml.load(f)
    return data

def add_elapsed_time(infos, time_format):
    for i, info in enumerate(infos):
        ts = datetime.strptime(info['timestamp'], time_format)
        if i + 1 < len(infos):
            next_ts = datetime.strptime(infos[i+1]['timestamp'], time_format)
            delta = next_ts - ts
            total_seconds = int(delta.total_seconds())
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            info['elapsed_time'] = f"{hours:02}:{minutes:02}:{seconds:02}"
        else:
            info['elapsed_time'] = ''
    return infos

def write_output_log(output_path, infos):
    with open(output_path, 'w', encoding='utf-8') as f:
        toml.dump({'active_window_information': infos}, f)
