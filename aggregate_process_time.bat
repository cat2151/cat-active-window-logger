cd /d %~dp0
set PYTHONPATH=%CD%\src
python -m src.log_processor.aggregate_process_time --config-filename secrets\aggregate_process_time.toml
if not %errorlevel% == 0 (pause & exit /b 1)
