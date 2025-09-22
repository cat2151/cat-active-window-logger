Last updated: 2025-09-23

# Project Overview

## プロジェクト概要
-   アクティブなウィンドウの情報を記録するためのオープンソースロガープロジェクトです。
-   個人の特定のニーズに合わせてカスタマイズ可能なロガーの実現を目指しています。
-   本プロジェクトは現在、主要な機能や挙動を検証する実験段階にあります。

## 技術スタック
-   フロントエンド: (このプロジェクトでは直接的なフロントエンド技術の使用は明示されていません)
-   音楽・オーディオ:
    -   **Tone.js**: Web Audio APIを簡潔に扱うためのJavaScriptライブラリで、Webブラウザ上で複雑なオーディオ処理や音楽生成を可能にします。
    -   **Web Audio API**: ブラウザに内蔵された音声処理技術で、オーディオの生成、操作、分析をリアルタイムで行います。Tone.js経由で使用されます。
    -   **MML (Music Macro Language)**: 音楽をテキスト形式で記述するための簡易言語であり、本プロジェクトでは音楽記法の解析に利用されます。
-   開発ツール:
    -   **Node.js runtime**: JavaScriptコードを実行するための環境であり、開発時のスクリプト実行やツールチェーンの基盤として利用されます。
-   テスト: (このプロジェクトでは特定のテストフレームワークの使用は明示されていませんが、`tests/` ディレクトリが存在します)
-   ビルドツール: (このプロジェクトでは特定のビルドツールの使用は明示されていません)
-   言語機能: (このプロジェクトでは特定の言語機能の使用は明示されていません)
-   自動化・CI/CD:
    -   **GitHub Actions**: GitHub上でソフトウェア開発ワークフローを自動化するためのサービスです。本プロジェクトでは、プロジェクト要約の自動生成やIssueの自動管理に利用されます。
-   開発標準:
    -   **EditorConfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル形式で、コードの統一性を保ちます。

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
-   `.editorconfig`: コードエディタ間でインデント、改行コードなどのコーディングスタイルを統一するための設定ファイルです。
-   `.gitignore`: Gitによるバージョン管理から除外するファイルやディレクトリを指定するファイルです。
-   `.pylintrc`: Pythonコードの静的解析ツールであるPylintの設定を定義するファイルです。
-   `.vscode/settings.json`: Visual Studio Codeエディタのワークスペース固有の設定を記述するファイルです。
-   `LICENSE`: プロジェクトのライセンス情報が記載されています。
-   `README.md`: プロジェクトの概要、目的、使い方、インストール方法などが記述された主要なドキュメントファイルです。
-   `aggregate_process_time.bat`: `src/log_processor/aggregate_process_time.py` スクリプトを実行するためのWindowsバッチファイルです。
-   `cat_active_window_logger.bat`: `src/logger/cat_active_window_logger.py` スクリプトを実行するためのWindowsバッチファイルです。
-   `dump_log.bat`: `src/log_processor/dump_log.py` スクリプトを実行するためのWindowsバッチファイルです。
-   `generated-docs/`: GitHub Actionsによって自動生成されたドキュメントが格納されるディレクトリです。
-   `issue-notes/`: 開発中に発生した課題や検討事項を記録したMarkdownファイル群です。
-   `log_enhance_active_time.bat`: `src/log_enhance_active_time/__main__.py` スクリプトを実行するためのWindowsバッチファイルです。
-   `src/active_time_reminder/gui.py`: アクティブ時間のリマインダー機能を提供するグラフィカルユーザーインターフェース（GUI）を実装するPythonスクリプトです。
-   `src/log_enhance_active_time/__init__.py`: Pythonパッケージ `log_enhance_active_time` の初期化ファイルです。
-   `src/log_enhance_active_time/__main__.py`: `log_enhance_active_time` パッケージが直接実行された際のエントリポイントとなるPythonスクリプトです。
-   `src/log_enhance_active_time/add_active_time.py`: ログデータにアクティブ時間に関連する情報を追加するロジックを実装したPythonスクリプトです。
-   `src/log_processor/aggregate_process_time.py`: ログデータからプロセスごとのアクティブ時間を集計・分析するPythonスクリプトです。
-   `src/log_processor/dump_log.py`: ログデータを整形して出力する機能を提供するPythonスクリプトです。
-   `src/logger/action_by_ipc.py`: プロセス間通信（IPC）を通じて特定のアクションを実行するロジックを実装したPythonスクリプトです。
-   `src/logger/cat_active_window_logger.py`: システムのアクティブなウィンドウ情報を取得し、ログに記録する主要なロガー機能を提供するPythonスクリプトです。
-   `src/logger/dated_log.py`: 日付ごとにログファイルを管理する機能を提供するPythonスクリプトです。
-   `src/logger/get_window_info.py`: 現在アクティブなウィンドウのタイトルやプロセス名などの情報を取得するユーティリティ機能を提供するPythonスクリプトです。
-   `src/logger/ipc.py`: プロセス間通信（IPC）に関する共通機能やインターフェースを定義するPythonスクリプトです。
-   `src/logger/log_and_display.py`: ログの記録と同時に、その情報をユーザーインターフェースなどに表示する機能を提供するPythonスクリプトです。
-   `src/logger/utils.py`: ロガー関連の汎用的なヘルパー関数やユーティリティを集めたPythonスクリプトです。
-   `tests/__init__.py`: Pythonテストパッケージの初期化ファイルです。
-   `tests/test_add_active_time.py`: `src/log_enhance_active_time/add_active_time.py` の機能に対する単体テストを実装するPythonスクリプトです。

## 関数詳細説明
プロジェクト情報に関数ごとの詳細な情報（役割、引数、戻り値など）が提供されていないため、個々の関数の詳細説明はできません。
一般的に、本プロジェクトのPythonスクリプトには、以下のような機能を提供する関数が含まれると推測されます。
-   アクティブなウィンドウ情報の取得・監視
-   取得したウィンドウ情報のログファイルへの記録
-   ログデータの読み込み、解析、集計
-   プロセスごとのアクティブ時間の計算
-   プロセス間通信（IPC）によるデータ交換やコマンド実行
-   ユーザーインターフェース（GUI）の表示と操作
-   日付ごとのログファイル管理ユーティリティ
-   テスト機能の実行と検証

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-09-23 07:08:28 JST
