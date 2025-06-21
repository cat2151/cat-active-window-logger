import datetime
from log_and_display import setup_logging

def initialize_dated_logging(args):
    dated_log_filename, today_str = get_dated_log_filename(args.base_log_filename)
    args.log_filename = dated_log_filename
    args.log_date = today_str
    setup_logging(args.log_filename)

def get_dated_log_filename(base_log_filename_format):
    date = datetime.datetime.now()
    log_filename = date.strftime(base_log_filename_format)
    today_str = date.strftime('%Y%m%d')
    return log_filename, today_str

def rotate_logfile_if_needed(args):
    date = datetime.datetime.now()
    today_str = date.strftime('%Y%m%d')
    if getattr(args, 'log_date', None) != today_str:
        new_log_filename, _ = get_dated_log_filename(args.base_log_filename)
        args.log_filename = new_log_filename
        args.log_date = today_str
        setup_logging(args.log_filename)
