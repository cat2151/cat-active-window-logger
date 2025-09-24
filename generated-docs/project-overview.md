Last updated: 2025-09-25

# Project Overview

## プロジェクト概要
- このプロジェクトは、アクティブなウィンドウの情報を記録する、カスタマイズ可能なロガーの検証を目的としています。
- ユーザーが自身の用途に合わせて挙動を調整できるロガーを容易に構築するための基盤を模索しています。
- 現在実験段階であり、オープンソースとして開発が進められています。

## 技術スタック
- フロントエンド: このプロジェクトには特定のフロントエンドフレームワークやライブラリは使用されていません。
- 音楽・オーディオ:
    - Tone.js: Web Audio APIを抽象化し、ブラウザ上で高度な音声処理や音楽作成を可能にするJavaScriptライブラリです。
    - Web Audio API: ウェブブラウザに内蔵された強力な音声処理機能で、Tone.jsを通じて利用されます。
    - MML (Music Macro Language): 音楽をテキストで記述するための簡易的な記法で、特定の音楽ロジックのパーシングに使用されます。
- 開発ツール:
    - Node.js runtime: JavaScriptコードを実行するための環境です。特定の開発スクリプトやツールに利用されます。
- テスト: このプロジェクトにはPythonのテストフレームワークなどは明示されていませんが、`tests/`ディレクトリでユニットテストが行われています。
- ビルドツール: このプロジェクトには特定のビルドツールは明示されていません。
- 言語機能: このプロジェクトの主要な実装言語はPythonです。
- 自動化・CI/CD:
    - GitHub Actions: コードの変更がリポジトリにプッシュされた際などに、自動でタスク（テスト、ドキュメント生成、Issue管理など）を実行するワークフロー自動化サービスです。このプロジェクトでは、プロジェクト要約の自動生成やIssueの自動管理に利用されています。
- 開発標準:
    - EditorConfig: 異なるエディタやIDE間で、インデントスタイル、文字コード、改行コードなどの基本的なコーディングスタイルを統一するための設定ファイルです。

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
  📁 active_time_reminder/
    📄 gui.py
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
-   `.editorconfig`: コードエディタ間でインデントや文字コードなどのコーディングスタイルを統一するための設定ファイルです。
-   `.gitignore`: Gitでバージョン管理しないファイルやディレクトリを指定するファイルです。
-   `.pylintrc`: Pythonコードの静的解析ツールPylintの設定ファイルで、コードの品質チェックルールを定義します。
-   `.vscode/settings.json`: Visual Studio Codeエディタのワークスペース固有の設定を定義するファイルです。
-   `LICENSE`: プロジェクトのオープンソースライセンス情報が記載されています。
-   `README.md`: プロジェクトの概要、目的、使い方などが記述された、プロジェクトの玄関となるドキュメントです。
-   `aggregate_process_time.bat`: Windowsのバッチファイルで、記録されたログからプロセスの実行時間を集計する処理を実行します。
-   `cat_active_window_logger.bat`: Windowsのバッチファイルで、アクティブなウィンドウの情報をログとして記録する処理を開始します。
-   `dump_log.bat`: Windowsのバッチファイルで、記録されたログの内容を表示（ダンプ）する処理を実行します。
-   `generated-docs/`: プロジェクトから自動生成されるドキュメントが格納されるディレクトリです。
-   `issue-notes/`: 開発中に発生した課題や検討事項、メモなどが格納されるディレクトリです。
-   `log_enhance_active_time.bat`: Windowsのバッチファイルで、既存のログにアクティブ時間に関する情報を追加・強化する処理を実行します。
-   `src/`: プロジェクトの主要なPythonソースコードが格納されているディレクトリです。
    -   `src/active_time_reminder/gui.py`: アクティブな時間を通知・リマインドするためのグラフィカルユーザーインターフェース (GUI) のロジックが含まれています。
    -   `src/log_enhance_active_time/`: ログにアクティブ時間情報を追加する機能に関連するモジュール群です。
        -   `__init__.py`: Pythonパッケージの初期化ファイルです。
        -   `__main__.py`: `log_enhance_active_time`パッケージが直接実行された際に呼び出されるエントリポイントです。
        -   `add_active_time.py`: ログデータにアクティブ時間に関する情報を計算・追加する具体的なロジックが含まれています。
    -   `src/log_processor/`: ログデータを処理・分析するためのモジュール群です。
        -   `aggregate_process_time.py`: ログから各プロセスの実行時間などを集計するロジックが含まれています。
        -   `dump_log.py`: ログデータを読み込み、特定の形式で出力（ダンプ）するロジックが含まれています。
    -   `src/logger/`: アクティブウィンドウのログ記録に関連する主要なモジュール群です。
        -   `action_by_ipc.py`: プロセス間通信 (IPC) を介して行われるアクションの処理ロジックが含まれています。
        -   `cat_active_window_logger.py`: アクティブなウィンドウのタイトルやプロセス名などを定期的に取得し、ログに記録する主要なロガーロジックが含まれています。
        -   `dated_log.py`: 日付に基づいたログファイルの管理や、ログエントリへの日付情報付加に関する機能が含まれています。
        -   `get_window_info.py`: 現在アクティブなウィンドウの詳細情報（タイトル、プロセスIDなど）を取得するためのOS連携ロジックが含まれています。
        -   `ipc.py`: プロセス間でデータをやり取りするための共通のプロセス間通信 (IPC) ユーティリティが含まれています。
        -   `log_and_display.py`: ログ記録と同時に、その情報をユーザーインターフェースやコンソールに表示する機能が含まれています。
        -   `utils.py`: `logger`モジュール内で利用される共通のユーティリティ関数やヘルパー関数が含まれています。
-   `tests/`: プロジェクトのテストコードが格納されているディレクトリです。
    -   `__init__.py`: Pythonパッケージの初期化ファイルです。
    -   `test_add_active_time.py`: `src/log_enhance_active_time/add_active_time.py`で実装された機能のテストコードです。

## 関数詳細説明
このプロジェクトから具体的な関数情報を検出できませんでした。
一般的なPythonプロジェクトでは、ファイル内に定義された関数が特定のタスク（例: データの読み込み、処理、書き込み、ウィンドウ情報の取得など）を実行します。各関数は、特定の引数を受け取り、処理を行い、結果を返すことで、プログラム全体の機能を実現します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2025-09-25 07:08:20 JST
