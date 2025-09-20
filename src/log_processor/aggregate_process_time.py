from datetime import datetime

import toml

from src.logger.utils import get_args, update_args_by_toml


def main():
    args = get_args()
    args = update_args_by_toml(args, args.config_filename)
    args = replace_today_in_args(args)

    log_data = load_enhanced_log(args.input_filename)

    total_time = calculate_process_total_time(log_data, args.target_process)

    output_result(args.output_filename, args.target_process, total_time)

    print(f"処理完了: {args.target_process} の合計アクティブ時間 = {total_time}")
    print(f"出力ファイル: {args.output_filename}")

def replace_today_in_args(args):
    args.input_filename = replace_today_placeholder(args.input_filename)
    args.output_filename = replace_today_placeholder(args.output_filename)
    return args

def replace_today_placeholder(path: str) -> str:
    today_str = datetime.today().strftime('%Y%m%d')
    return path.replace('{today}', today_str)

def load_enhanced_log(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = toml.load(f)
    return data['active_window_information']

def calculate_process_total_time(log_entries, target_process):
    total_seconds = 0

    for entry in log_entries:
        if (entry.get('process_name') == target_process and
            entry.get('elapsed_time') and
            entry['elapsed_time'] != ''):

            elapsed_time = entry['elapsed_time']
            seconds = parse_elapsed_time_to_seconds(elapsed_time)
            total_seconds += seconds

    return format_seconds_to_time(total_seconds)

def parse_elapsed_time_to_seconds(elapsed_time_str):
    time_parts = elapsed_time_str.split(':')
    if len(time_parts) == 3:
        hours = int(time_parts[0])
        minutes = int(time_parts[1])
        seconds = int(time_parts[2])
        return hours * 3600 + minutes * 60 + seconds
    else:
        # exceptionで早期エラーにし、問題を早期検知させる
        raise ValueError(f"Invalid time format: {elapsed_time_str}")

def format_seconds_to_time(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def output_result(output_filename, process_name, total_time):
    timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    result_data = {
        'process_time_summary': [{
            'timestamp': timestamp,
            'process_name': process_name,
            'total_active_time': total_time,
            'description': f'{process_name}の1日合計アクティブ時間'
        }]
    }

    with open(output_filename, 'w', encoding='utf-8') as f:
        toml.dump(result_data, f)
    print(f"結果をファイルに出力しました: {output_filename}")

if __name__ == "__main__":
    main()
