Last updated: 2025-09-27

# Project Overview

## プロジェクト概要
- アクティブなウィンドウ情報を記録し、ユーザーの利用状況を分析するためのカスタマイズ可能なロガープロジェクトです。
- 自分のニーズに合わせた独自のロガー挙動を簡単に構築・検証することを目指しています。
- 現在は実験段階であり、ウィンドウタイトルの変動監視や過去のタイトル一覧把握など、多様なログ収集と分析機能が検討されています。

## 技術スタック
- フロントエンド: このプロジェクトでは明示的なフロントエンド技術は使用されていません。
- 音楽・オーディオ:
    - **Tone.js**: Web Audio APIを抽象化し、Webブラウザ上で高品質な音楽やオーディオ処理を容易にするJavaScriptライブラリです。
    - **Web Audio API**: ブラウザに内蔵されている音声処理機能で、Tone.jsを通じて利用されます。
    - **MML (Music Macro Language)**: 音楽をテキストで記述するための簡易的な記法を解析するパーサーがプロジェクトで利用されています。
- 開発ツール:
    - **Node.js runtime**: JavaScriptコードを実行するためのオープンソースのサーバーサイド実行環境です。
- テスト: このプロジェクトでは明示的なテストフレームワークは指定されていませんが、テストファイルが存在します。
- ビルドツール: このプロジェクトでは明示的なビルドツールは使用されていません。
- 言語機能: このプロジェクトの主要言語はPythonですが、特定の言語機能は明示されていません。
- 自動化・CI/CD:
    - **GitHub Actions**: ソースコードの変更をトリガーに、自動的にテストの実行やデプロイ、ドキュメント生成などのワークフローを実行するCI/CDツールです。本プロジェクトでは「プロジェクト要約自動生成」と「Issue自動管理」の2つのワークフローが設定されています。
- 開発標準:
    - **EditorConfig**: 異なるIDEやエディタを使用する開発者間でも、インデントスタイルや文字コードなどのコーディングスタイルを統一するための設定ファイルです。

## ファイル階層ツリー
```
.editorconfig
.gitignore
.pylintrc
.vscode/
  settings.json
LICENSE
README.md
aggregate_process_time.bat
cat_active_window_logger.bat
dump_log.bat
generated-docs/
issue-notes/
  1.md
  10.md
  2.md
  3.md
  4.md
  5.md
  6.md
  7.md
  8.md
  9.md
log_enhance_active_time.bat
src/
  active_time_reminder/
    gui.py
  log_enhance_active_time/
    __init__.py
    __main__.py
    add_active_time.py
  log_processor/
    aggregate_process_time.py
    dump_log.py
  logger/
    action_by_ipc.py
    cat_active_window_logger.py
    dated_log.py
    get_window_info.py
    ipc.py
    log_and_display.py
    utils.py
tests/
  __init__.py
  test_add_active_time.py
```

## ファイル詳細説明
-   `.editorconfig`: コードの整形ルール（インデントスタイル、文字コードなど）を定義し、異なるエディタ間での統一を保証します。
-   `.gitignore`: Gitのバージョン管理から除外するファイルやディレクトリを指定します。
-   `.pylintrc`: Pythonの静的コード解析ツールであるPylintの設定を定義します。
-   `.vscode/settings.json`: VS Codeエディタのワークスペース固有の設定を記述します。
-   `LICENSE`: プロジェクトのライセンス情報が記載されており、利用条件を示します。
-   `README.md`: プロジェクトの概要、目的、使い方、インストール手順などが記述されたドキュメントです。
-   `aggregate_process_time.bat`: プロセスごとのアクティブ時間を集計するPythonスクリプトを呼び出すバッチファイルです。
-   `cat_active_window_logger.bat`: アクティブウィンドウ情報を継続的に記録する主要なロガースクリプトを起動するためのバッチファイルです。
-   `dump_log.bat`: 記録されたログデータを整形して出力するPythonスクリプトを呼び出すバッチファイルです。
-   `generated-docs/`: GitHub Actionsなどによって自動生成されたドキュメントが格納されるディレクトリです。
-   `issue-notes/`: 開発中の課題や検討事項に関するメモがIssue番号ごとにファイルとして格納されています。
-   `log_enhance_active_time.bat`: ログにアクティブ時間に関連する追加情報を付与するPythonスクリプトを起動するためのバッチファイルです。
-   `src/`: プロジェクトのPythonソースコードが格納されているルートディレクトリです。
    -   `src/active_time_reminder/gui.py`: アクティブ時間の通知やリマインダー表示のためのグラフィカルユーザーインターフェース (GUI) を実装しています。
    -   `src/log_enhance_active_time/__init__.py`: `log_enhance_active_time`パッケージの初期化ファイルです。
    -   `src/log_enhance_active_time/__main__.py`: `python -m log_enhance_active_time`としてパッケージを直接実行した際のエントリポイントです。
    -   `src/log_enhance_active_time/add_active_time.py`: 既存のログデータにアクティブ時間情報を追加・更新するロジックを実装しています。
    -   `src/log_processor/aggregate_process_time.py`: ログデータから各プロセスのアクティブな利用時間を集計・分析するスクリプトです。
    -   `src/log_processor/dump_log.py`: 記録されたログデータを読み込み、指定された形式で出力（ダンプ）するスクリプトです。
    -   `src/logger/action_by_ipc.py`: プロセス間通信 (IPC) を介して受け取ったコマンドやアクションを処理する機能を実装しています。
    -   `src/logger/cat_active_window_logger.py`: アクティブなウィンドウのタイトルやプロセス情報などを定期的に取得し、ログに記録する主要なロジックを実装しています。
    -   `src/logger/dated_log.py`: 日付に基づいたログファイルの生成、管理、ローテーションなどの機能を提供します。
    -   `src/logger/get_window_info.py`: OSのAPIを利用して、現在アクティブなウィンドウのタイトル、プロセス名、プロセスIDなどの情報を取得する機能を提供します。
    -   `src/logger/ipc.py`: プロセス間通信（Inter-Process Communication）のための共通モジュールで、異なるプロセス間でのデータ交換やコマンド送受信を可能にします。
    -   `src/logger/log_and_display.py`: ログの記録と、必要に応じてその情報をユーザーインターフェースやコンソールに表示する機能を担当します。
    -   `src/logger/utils.py`: ロガーモジュール内で共通して利用されるユーティリティ関数やヘルパー関数を集めたファイルです。
-   `tests/__init__.py`: テストディレクトリをPythonパッケージとして認識させるための初期化ファイルです。
-   `tests/test_add_active_time.py`: `src/log_enhance_active_time/add_active_time.py`に実装された機能が正しく動作するかを検証するためのテストコードです。

## 関数詳細説明
このプロジェクトにおける関数の詳細情報は、提供された情報からは分析できませんでした。
一般的に、関数は特定のタスクを実行するためのコードブロックであり、引数を受け取り、処理を行い、結果を戻り値として返します。
例として、`get_window_info.py`にはアクティブウィンドウの情報を取得する関数が、`add_active_time.py`にはログにアクティブ時間を追加する関数が存在すると推測されます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-09-27 07:08:06 JST
