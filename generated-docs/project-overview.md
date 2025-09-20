Last updated: 2025-09-21

# Project Overview

## プロジェクト概要
- アクティブウィンドウの操作ログを柔軟に記録・分析するための実験的なプロジェクトです。
- ユーザー固有の要件に合わせて、アクティブウィンドウのタイトルやプロセス情報を記録できます。
- ログデータの収集だけでなく、変動するタイトルや全てのタイトルを効率的に把握するための機能検討も含まれます。

## 技術スタック
- フロントエンド: 情報が提供されていないため、特定できません。
- 音楽・オーディオ:
    - Tone.js: Web Audio APIを抽象化し、Webブラウザ上で高品質な音楽やオーディオ処理を可能にするJavaScriptライブラリ。
    - Web Audio API: Webブラウザに組み込まれた音声処理API。Tone.jsを介して利用され、複雑な音声合成やエフェクト処理を可能にする。
    - MML (Music Macro Language): 音楽をテキスト形式で記述するための記法。楽譜をプログラム的に表現し、音声合成などに利用される。
- 開発ツール:
    - Node.js runtime: Google ChromeのV8 JavaScriptエンジン上で動作するJavaScript実行環境。サーバーサイドや開発ツールとして使用される。
- テスト: 情報が提供されていないため、特定できません。
- ビルドツール: 情報が提供されていないため、特定できません。
- 言語機能: 情報が提供されていないため、特定できません。（ただし、ファイル構造からPythonが主言語と推測されます）
- 自動化・CI/CD:
    - GitHub Actions: コードの変更を検知し、自動的にビルド、テスト、デプロイなどのワークフローを実行するGitHubのCI/CDサービス。本プロジェクトでは「プロジェクト要約自動生成」と「Issue自動管理」の2つのワークフローが設定されています。
- 開発標準:
    - EditorConfig: 異なるIDEやエディタを使用する開発者の間で、インデントスタイル、文字コード、改行コードなどのコードフォーマットを統一するための設定ファイル形式。

## ファイル階層ツリー
```
📄 .editorconfig
📄 .gitignore
📄 .pylintrc
📁 .vscode/
  📊 settings.json
📄 LICENSE
📖 README.md
📄 aggregate_process_time.bat
📄 cat_active_window_logger.bat
📄 dump_log.bat
📁 generated-docs/
📁 issue-notes/
  📖 1.md
  📖 10.md
  📖 2.md
  📖 3.md
  📖 4.md
  📖 5.md
  📖 6.md
  📖 7.md
  📖 8.md
  📖 9.md
📄 log_enhance_active_time.bat
📁 src/
  📁 log_enhance_active_time/
    📄 __init__.py
    📄 __main__.py
    📄 add_active_time.py
  📁 log_processor/
    📄 aggregate_process_time.py
    📄 dump_log.py
  📁 logger/
    📄 action_by_ipc.py
    📄 cat_active_window_logger.py
    📄 dated_log.py
    📄 get_window_info.py
    📄 ipc.py
    📄 log_and_display.py
    📄 utils.py
📁 tests/
  📄 __init__.py
  📄 test_add_active_time.py
```

## ファイル詳細説明
- `.editorconfig`: プロジェクト全体でコードの書式設定（インデント、改行コードなど）を統一するための設定ファイルです。
- `.gitignore`: Gitのバージョン管理から除外するファイルやディレクトリ（例: 生成されたログファイル、一時ファイル、仮想環境など）を指定するファイルです。
- `.pylintrc`: Pythonコードの静的解析ツールPylintの設定ファイルで、コードの品質やコーディング規約に違反がないかをチェックするためのルールを定義します。
- `.vscode/settings.json`: Visual Studio Codeエディタのワークスペース固有の設定ファイルで、言語設定、拡張機能の設定、フォーマッタの指定などが含まれます。
- `LICENSE`: プロジェクトのライセンス情報が記載されたファイルで、本プロジェクトの利用条件や再配布に関する規約を示します。
- `README.md`: プロジェクトの概要、目的、使い方、インストール手順、貢献方法など、プロジェクトに関する包括的な情報が記述された主要なドキュメントです。
- `aggregate_process_time.bat`: `src/log_processor/aggregate_process_time.py`スクリプトを実行するためのWindowsバッチファイルです。おそらくログからプロセスごとの合計アクティブ時間を集計する処理を自動化します。
- `cat_active_window_logger.bat`: `src/logger/cat_active_window_logger.py`スクリプトを実行するためのWindowsバッチファイルです。アクティブウィンドウの情報を定期的に取得し、ログに記録するロガー機能を起動します。
- `dump_log.bat`: `src/log_processor/dump_log.py`スクリプトを実行するためのWindowsバッチファイルです。ログデータを特定の形式で出力または表示する処理を自動化します。
- `generated-docs/`: GitHub Actionsによって自動生成されたドキュメント（例: プロジェクト要約など）を格納するディレクトリです。
- `issue-notes/`: 開発中の課題やイシューに関する詳細なノートや情報を格納するディレクトリです。個別のMarkdownファイルがそれぞれのイシューに対応しています。
- `log_enhance_active_time.bat`: `src/log_enhance_active_time/__main__.py`スクリプトを実行するためのWindowsバッチファイルです。ログデータにアクティブ時間に関する追加情報を付加する処理を自動化します。
- `src/`: プロジェクトの主要なPythonソースコードを格納するルートディレクトリです。
    - `src/log_enhance_active_time/`: ログデータにアクティブ時間情報を付加する機能に関連するモジュール群。
        - `src/log_enhance_active_time/__init__.py`: Pythonパッケージの初期化ファイル。
        - `src/log_enhance_active_time/__main__.py`: `log_enhance_active_time`パッケージが直接実行されたときのエントリポイントとなるファイルです。
        - `src/log_enhance_active_time/add_active_time.py`: 既存のログデータにアクティブ時間の計算結果や関連情報を追加するためのロジックを実装したファイルです。
    - `src/log_processor/`: 記録されたログデータを処理・分析するためのモジュール群。
        - `src/log_processor/aggregate_process_time.py`: ログデータから各プロセスがアクティブだった合計時間を集計し、レポートを生成するロジックを実装したファイルです。
        - `src/log_processor/dump_log.py`: ログデータを読み込み、特定のフォーマット（例: TOML, CSV）で出力するためのロジックを実装したファイルです。
    - `src/logger/`: アクティブウィンドウの情報を取得し、記録するための主要なロガーモジュール群。
        - `src/logger/action_by_ipc.py`: プロセス間通信（IPC）を通じて、ロガーに対する特定のアクション（例: ログ開始/停止、設定変更）を制御するロジックを実装したファイルです。
        - `src/logger/cat_active_window_logger.py`: アクティブウィンドウのタイトル、プロセス名、プロセスIDなどの情報を継続的に取得し、ログファイルに記録する主要なロガー機能を提供します。
        - `src/logger/dated_log.py`: ログファイルを日付ごとに分割・管理するための機能（例: 日次ログファイルの作成、古いログのアーカイブ）を実装したファイルです。
        - `src/logger/get_window_info.py`: OSのAPIを使用して、現在アクティブなウィンドウのタイトル、プロセス名、プロセスIDなどの情報を取得するための関数群を提供します。
        - `src/logger/ipc.py`: 複数のプロセス間での安全なデータ交換やコマンド実行を可能にするプロセス間通信（IPC）の共通ユーティリティや基盤ロジックを実装したファイルです。
        - `src/logger/log_and_display.py`: 取得したログデータを記録するだけでなく、リアルタイムでコンソールやUIに表示する機能に関連するロジックを実装したファイルです。
        - `src/logger/utils.py`: ロガーモジュール内で広く利用される汎用的なユーティリティ関数やヘルパー関数（例: 時間計算、文字列処理）をまとめたファイルです。
- `tests/`: プロジェクトのユニットテストや統合テストのコードを格納するディレクトリです。
    - `tests/__init__.py`: Pythonパッケージの初期化ファイル。
    - `tests/test_add_active_time.py`: `src/log_enhance_active_time/add_active_time.py`モジュールの機能が正しく動作するかを検証するためのテストコードです。

## 関数詳細説明
プロジェクト情報には関数の具体的な詳細（役割、引数、戻り値など）が提供されていないため、詳細な説明はできません。各ファイルに含まれるであろう主要な関数について、ファイル名からの推測に基づく一般的な役割を以下に示します。

- **`src/log_enhance_active_time/add_active_time.py`**:
    - `add_active_time(log_data)`: ログデータにアクティブ時間情報を追加する関数。
- **`src/log_processor/aggregate_process_time.py`**:
    - `aggregate_process_time(log_data)`: ログデータからプロセスごとのアクティブ時間を集計する関数。
- **`src/log_processor/dump_log.py`**:
    - `dump_log(log_data, format)`: ログデータを指定されたフォーマットで出力する関数。
- **`src/logger/action_by_ipc.py`**:
    - `perform_action(action_type, *args)`: IPC経由で特定のアクションを実行する関数。
- **`src/logger/cat_active_window_logger.py`**:
    - `start_logging()`: アクティブウィンドウの情報を記録するロガーを開始する関数。
    - `stop_logging()`: ロガーを停止する関数。
- **`src/logger/dated_log.py`**:
    - `get_current_log_file()`: 現在の日付に対応するログファイルパスを取得する関数。
    - `write_to_log(data)`: データを日付付きログファイルに書き込む関数。
- **`src/logger/get_window_info.py`**:
    - `get_active_window_title()`: アクティブウィンドウのタイトルを取得する関数。
    - `get_active_process_info()`: アクティブプロセスの情報（名前、IDなど）を取得する関数。
- **`src/logger/ipc.py`**:
    - `send_message(message)`: IPCを通じてメッセージを送信する関数。
    - `receive_message()`: IPCを通じてメッセージを受信する関数。
- **`src/logger/log_and_display.py`**:
    - `log_and_display_info(info)`: 情報をログに記録し、同時に表示する関数。
- **`src/logger/utils.py`**:
    - `format_timestamp(timestamp)`: タイムスタンプを整形するユーティリティ関数。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2025-09-21 07:07:13 JST
