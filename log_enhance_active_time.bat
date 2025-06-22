cd /d %~dp0
set PYTHONPATH=%CD%\src
python -m src.log_enhance_active_time --config-filename secrets\log_enhance_active_time.toml
if not %errorlevel% == 0 (pause & exit /b 1)
