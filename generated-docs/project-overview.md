Last updated: 2025-09-20

# Project Overview

## プロジェクト概要
- アクティブウィンドウの情報を継続的に記録し、利用者のニーズに合わせたカスタムロガーを容易に構築するための検証プロジェクトです。
- 記録されたログデータは、アクティブ時間の分析や特定のウィンドウイベントの把握に活用されることを想定しています。
- 現在は実験段階であり、Web Audio API (Tone.js, MML) の統合により、将来的に音響を通じた通知やデータ表現の可能性も探られています。

## 技術スタック
- フロントエンド: プロジェクトの主要な目的はバックグラウンドでのロギングですが、将来的にはWeb Audio API (Tone.js, Web Audio API) を用いて、ログデータに基づいた音響フィードバックや可視化が検討されており、この部分がWeb技術との接点となります。
- 音楽・オーディオ:
    - Tone.js: Web Audio APIをより簡単に扱うためのJavaScriptライブラリ。Webブラウザ上で複雑な音声合成やエフェクトを実現します。
    - Web Audio API: ウェブブラウザ上で高度な音声処理を行うための標準API。Tone.jsを介して利用されます。
    - MML (Music Macro Language): テキスト形式で音楽を記述するための言語。Tone.jsと組み合わせて、音楽的表現を生成するのに利用されます。
- 開発ツール:
    - Node.js runtime: JavaScriptの実行環境。主に開発ワークフローやビルドツール、ユーティリティスクリプトの実行に利用されます。
- テスト: 現時点では具体的なテストツールは記載されていませんが、`tests/` ディレクトリが存在します。
- ビルドツール: プロジェクト情報に直接のビルドツールは記載されていません。
- 言語機能: プロジェクトの主要な言語はPythonと推測されますが、特定の言語機能は記載されていません。
- 自動化・CI/CD:
    - GitHub Actions: コードの変更やIssue管理などのイベントをトリガーに、自動化されたワークフローを実行するCI/CDサービス。
        - プロジェクト要約自動生成: プロジェクトの概要を自動的に生成するワークフロー。
        - Issue自動管理: Issueの作成、更新、クローズなどのイベントに基づいて、自動的に処理を行うワークフロー。
- 開発標準:
    - EditorConfig: 異なるエディタやIDEを使用する開発者の間で、インデントスタイル、文字コード、改行コードなどのコーディングスタイルを統一するための設定ファイルです。

## ファイル階層ツリー
```
📄 .editorconfig
📄 .gitignore
📄 .pylintrc
📁 .vscode/
  📊 settings.json
📄 LICENSE
📖 README.md
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
- `.editorconfig`: 開発環境（エディタ）間で、インデントや文字コードなどのコーディングスタイルを統一するための設定ファイルです。
- `.gitignore`: Gitのバージョン管理から除外するファイルやディレクトリを指定します。
- `.pylintrc`: Pythonの静的コード解析ツールであるPylintの設定ファイルで、コードの品質チェックルールを定義します。
- `.vscode/settings.json`: Visual Studio Codeのワークスペース固有の設定を定義するファイルです。
- `LICENSE`: このプロジェクトのソフトウェアライセンス情報が記載されています。
- `README.md`: プロジェクトの目的、セットアップ方法、使い方などが記述された主要なドキュメントファイルです。
- `cat_active_window_logger.bat`: Windows環境で、アクティブウィンドウロガーのメイン機能を起動するためのバッチスクリプトです。
- `dump_log.bat`: Windows環境で、収集されたログデータを処理またはダンプするためのバッチスクリプトです。
- `generated-docs/`: プロジェクトから自動生成されたドキュメントやレポートが格納されるディレクトリです。
- `issue-notes/`: 開発中に発生したIssueに関する詳細なメモや議論を記録するMarkdownファイル群を格納するディレクトリです。
- `log_enhance_active_time.bat`: Windows環境で、ログデータにアクティブ時間情報を追加したり、その情報を基にログを強化するためのバッチスクリプトです。
- `src/`: プロジェクトの主要なPythonソースコードが格納されているディレクトリです。
    - `log_enhance_active_time/`: アクティブ時間に関するログデータを処理・強化するためのPythonモジュールです。
        - `__init__.py`: Pythonパッケージの初期化ファイルです。
        - `__main__.py`: このパッケージが直接実行された際のエントリポイントとなるファイルです。
        - `add_active_time.py`: ログデータにアクティブ時間情報を計算して追加するロジックを実装しています。
    - `log_processor/`: ログデータの解析や変換を行うためのPythonモジュールです。
        - `dump_log.py`: 収集されたログデータを特定の形式で出力（ダンプ）する処理を実装しています。
    - `logger/`: アクティブウィンドウの情報を取得し、記録する主要なロギング機能を提供するPythonモジュールです。
        - `action_by_ipc.py`: プロセス間通信（IPC）を通じて、他のプロセスからの指示に応じてアクションを実行する機能です。
        - `cat_active_window_logger.py`: アクティブウィンドウのタイトル、プロセス名、IDなどを取得し、定期的にログに記録する主要なロガーのロジックを含んでいます。
        - `dated_log.py`: 日付に基づいてログファイルを管理し、整理する機能を提供します。
        - `get_window_info.py`: 現在アクティブなウィンドウの詳細情報（タイトル、プロセス名、IDなど）を取得するための低レベルなAPI呼び出しをラップしています。
        - `ipc.py`: プロセス間通信を確立し、メッセージの送受信を行うための汎用的なメカニズムを実装しています。
        - `log_and_display.py`: ログを記録するだけでなく、必要に応じてその情報をユーザーに表示（例: コンソール出力）する機能を含んでいます。
        - `utils.py`: ロガーモジュール内で広く利用される汎用的なヘルパー関数やユーティリティを提供します。
- `tests/`: プロジェクトの各モジュールや機能が正しく動作するかを検証するためのテストコードが格納されているディレクトリです。
    - `__init__.py`: Pythonパッケージの初期化ファイルです。
    - `test_add_active_time.py`: `add_active_time.py` モジュールの機能に関する単体テストを実装しています。

## 関数詳細説明
プロジェクト内の具体的な関数名やシグネチャは現時点では提供されていませんが、各モジュールの機能に基づき、以下のような役割を持つ関数群が存在すると考えられます。

- `src/log_enhance_active_time/add_active_time.py`
    - `calculate_active_time()`: ログエントリに基づいて、ユーザーが特定のウィンドウでアクティブだった時間を計算します。
    - `add_active_time_to_log()`: 既存のログファイルやデータ構造に、計算されたアクティブ時間情報を追加します。
- `src/log_processor/dump_log.py`
    - `load_log_data()`: 指定されたパスからログデータを読み込みます。
    - `process_and_dump_log()`: 読み込んだログデータを解析し、指定されたフォーマット（例: TOML, CSV）で出力します。
- `src/logger/action_by_ipc.py`
    - `handle_ipc_action()`: プロセス間通信で受信したコマンドやデータに応じた特定のアクションを実行します。
- `src/logger/cat_active_window_logger.py`
    - `start_logger()`: アクティブウィンドウ情報の取得と記録を開始するメインループを起動します。
    - `log_current_window_info()`: 現在アクティブなウィンドウの情報を取得し、ログファイルに書き込みます。
- `src/logger/dated_log.py`
    - `get_daily_log_file()`: 現在の日付に対応するログファイルパスを生成または取得します。
    - `rotate_logs()`: 一定期間経過した古いログファイルをアーカイブまたは削除する処理を行います。
- `src/logger/get_window_info.py`
    - `get_active_window_title()`: 現在アクティブなウィンドウのタイトル文字列を取得します。
    - `get_active_process_name()`: 現在アクティブなウィンドウを所有するプロセスの名前を取得します。
    - `get_active_process_id()`: 現在アクティブなウィンドウを所有するプロセスのIDを取得します。
- `src/logger/ipc.py`
    - `send_message()`: 特定のプロセスに対してメッセージを送信します。
    - `receive_message()`: 特定のプロセスからのメッセージを受信します。
- `src/logger/log_and_display.py`
    - `record_log_entry()`: 指定された情報をログシステムに記録します。
    - `display_log_info()`: 記録されたログ情報の一部をユーザーインターフェース（コンソールなど）に表示します。
- `src/logger/utils.py`
    - `format_timestamp()`: タイムスタンプを特定の文字列形式に変換します。
    - `load_config()`: 設定ファイル（例: TOML, JSON）を読み込み、設定値を返します。

## 関数呼び出し階層ツリー
```

---
Generated at: 2025-09-20 18:05:26 JST
