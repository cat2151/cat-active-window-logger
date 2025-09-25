Last updated: 2025-09-26

# Project Overview

## プロジェクト概要
- アクティブなウィンドウ情報を記録し、その挙動をユーザーのニーズに合わせて柔軟にカスタマイズできるロガーの開発検証を行っています。
- 本プロジェクトは、特定の用途に特化したロガーを効率的に作成する可能性を探るための実験的なオープンソースプロジェクトです。
- 現在は実験段階であり、変動するウィンドウタイトルのリストアップや、これまでのログから多様なウィンドウタイトルを網羅的に把握する機能の実現を目指しています。

## 技術スタック
- フロントエンド: 該当する技術は明記されていません。
- 音楽・オーディオ:
    - Tone.js: Web Audio APIをJavaScriptから簡単に操作するためのライブラリで、ブラウザ上でのリッチなオーディオ体験を実現します。
    - Web Audio API: ウェブブラウザに標準搭載されている音声処理APIで、複雑な音声の合成、加工、分析が可能です（Tone.jsを介して使用）。
    - MML (Music Macro Language): 音楽をテキストベースで記述するためのシンプルな記法で、特定のフォーマットで音楽を表現・解析する際に利用されます。
- 開発ツール:
    - Node.js runtime: JavaScriptの実行環境で、サーバーサイドやデスクトップアプリケーション、各種開発ツールの実行に利用されます。
- テスト: 該当する技術は明記されていません。
- ビルドツール: 該当する技術は明記されていません。
- 言語機能: 該当する特定の言語機能は明記されていません。
- 自動化・CI/CD:
    - GitHub Actions: コードの変更やIssue管理などのイベントをトリガーに、ビルド、テスト、デプロイなどのワークフローを自動化するサービスです。
        - プロジェクト要約自動生成: プロジェクトの概要を自動的に生成・更新するワークフロー。
        - Issue自動管理: 開発中の課題やタスクの管理を自動化するワークフロー。
- 開発標準:
    - EditorConfig: 異なるエディタやIDE間で一貫したコーディングスタイルを定義し、プロジェクト全体のコードの統一性を保つための設定ファイル形式です。

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
-   `.editorconfig`: 異なる開発環境でも一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイル。
-   `.gitignore`: Gitのバージョン管理から除外するファイルやディレクトリを指定するファイル。
-   `.pylintrc`: Pythonの静的解析ツールPylintの設定ファイル。コード品質の検査ルールを定義します。
-   `.vscode/settings.json`: Visual Studio Codeエディタのワークスペース固有の設定ファイル。
-   `LICENSE`: プロジェクトの配布条件や利用許諾を定めるライセンス情報。
-   `README.md`: プロジェクトの概要、インストール方法、使い方などを説明するメインドキュメント。
-   `aggregate_process_time.bat`: ログデータからプロセスごとの利用時間を集計するPythonスクリプト（`src/log_processor/aggregate_process_time.py`）を実行するためのバッチファイル。
-   `cat_active_window_logger.bat`: アクティブウィンドウの情報をログに記録するメインのPythonスクリプト（`src/logger/cat_active_window_logger.py`）を実行するためのバッチファイル。
-   `dump_log.bat`: 既存のログファイルの内容を整形して出力するPythonスクリプト（`src/log_processor/dump_log.py`）を実行するためのバッチファイル。
-   `generated-docs/`: GitHub Actionsなどによって自動生成されたドキュメントを格納するためのディレクトリ。
-   `issue-notes/`: 開発中に発生した課題や検討事項、メモなどをマークダウン形式で記録したファイル群。
-   `log_enhance_active_time.bat`: ログにアクティブタイム情報を追加するPythonスクリプト（`src/log_enhance_active_time/__main__.py`）を実行するためのバッチファイル。
-   `src/`: プロジェクトの主要なソースコードが格納されているディレクトリ。
    -   `active_time_reminder/`: ユーザーのアクティブタイムに関するリマインダー機能を提供するモジュール。
        -   `gui.py`: リマインダー機能のグラフィカルユーザーインターフェース（GUI）関連の処理を記述。
    -   `log_enhance_active_time/`: ログデータにユーザーのアクティブな時間帯の情報などを追加・強化する機能のモジュール。
        -   `__init__.py`: Pythonパッケージの初期化ファイル。
        -   `__main__.py`: `log_enhance_active_time`モジュールが直接実行された際のエントリーポイント。
        -   `add_active_time.py`: 既存のログにアクティブタイム情報を計算し、追加する具体的なロジックを実装。
    -   `log_processor/`: ログデータの解析や集計を行う機能のモジュール。
        -   `aggregate_process_time.py`: 記録されたログから、各プロセスが使用された合計時間や回数を集計するスクリプト。
        -   `dump_log.py`: ログファイルの内容を読み込み、整形された形式で出力するスクリプト。
    -   `logger/`: アクティブウィンドウの情報を取得し、ログに記録する主要な機能のモジュール。
        -   `action_by_ipc.py`: プロセス間通信（IPC）を利用して、特定のアクションを実行する処理。
        -   `cat_active_window_logger.py`: アクティブなウィンドウのタイトル、プロセス名、IDなどを定期的に取得し、ログファイルに記録するメインのロギングスクリプト。
        -   `dated_log.py`: 日付に基づいたログファイルの管理（例：日ごとに新しいログファイルを作成）を行う機能。
        -   `get_window_info.py`: 現在アクティブなウィンドウの詳細情報（タイトル、プロセス名、プロセスIDなど）を取得するOS依存の処理。
        -   `ipc.py`: プロセス間でデータを交換するための通信メカニズムを実装したモジュール。
        -   `log_and_display.py`: ウィンドウ情報をログに記録すると同時に、ユーザーインターフェースやコンソールに表示する機能。
        -   `utils.py`: ロガー機能全体で共有される汎用的なユーティリティ関数やヘルパー関数群。
-   `tests/`: プロジェクトのテストコードを格納するディレクトリ。
    -   `__init__.py`: Pythonパッケージの初期化ファイル。
    -   `test_add_active_time.py`: `src/log_enhance_active_time/add_active_time.py`の機能が正しく動作するかを検証するためのテストスクリプト。

## 関数詳細説明
このプロジェクトでは、主に以下の役割を持つ関数が想定されます。具体的な引数や戻り値はコードベースに依存しますが、一般的な機能概要を説明します。

-   **`src/logger/cat_active_window_logger.py`内の関数**:
    -   役割: アクティブウィンドウの情報を定期的に監視し、取得したデータをログに書き込むメインループを制御します。
    -   機能: ウィンドウ情報の取得指示、ログファイルへの書き込み処理の呼び出し、実行間隔の管理など。
-   **`src/logger/get_window_info.py`内の関数**:
    -   役割: 現在アクティブなウィンドウの識別情報（タイトル、プロセス名、プロセスIDなど）をOSから取得します。
    -   機能: OSのAPIを呼び出し、ウィンドウハンドルから各種情報を抽出し、整形して返します。
-   **`src/logger/dated_log.py`内の関数**:
    -   役割: ログデータを日付に基づいたファイル名で保存・管理します。
    -   機能: 現在の日付に対応するログファイルパスの生成、ログデータのファイルへの追記、古いログファイルの管理など。
-   **`src/logger/ipc.py`内の関数**:
    -   役割: プロセス間でのデータやコマンドの送受信を可能にするメカニズムを提供します。
    -   機能: メッセージキュー、ソケット通信、共有メモリなどを利用して、異なるプロセス間で通信を行います。
-   **`src/log_enhance_active_time/add_active_time.py`内の関数**:
    -   役割: 既存のログデータに、ユーザーが実際にアクティブであった時間帯に関する情報を追加・計算します。
    -   機能: ログファイルの読み込み、ウィンドウの活動状況分析、アクティブタイムの計算とログへの書き込み。
-   **`src/log_processor/aggregate_process_time.py`内の関数**:
    -   役割: ログデータから、各プロセスがアクティブだった合計時間や利用頻度を集計します。
    -   機能: ログファイルの解析、プロセスごとの時間集計、結果の出力（例：コンソール、TOMLファイル）。
-   **`src/log_processor/dump_log.py`内の関数**:
    -   役割: 指定されたログファイルの内容を読み込み、人間が読みやすい形式で出力します。
    -   機能: ログのパース、データの整形、標準出力またはファイルへの書き出し。
-   **`src/active_time_reminder/gui.py`内の関数**:
    -   役割: ユーザーインターフェースを構築し、アクティブタイムリマインダーの表示やユーザー操作への応答を処理します。
    -   機能: ウィンドウの描画、イベントハンドリング、リマインダーメッセージの表示。
-   **`src/logger/utils.py`内の関数**:
    -   役割: プロジェクト全体で利用される汎用的なヘルパー関数を提供します。
    -   機能: 日付・時刻のフォーマット、文字列操作、ファイルパス処理、設定値の読み込みなど。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-09-26 07:07:30 JST
