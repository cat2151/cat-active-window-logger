Last updated: 2025-10-30

# Project Overview

## プロジェクト概要
- ユーザーがカスタマイズしやすいアクティブウィンドウの動作ロガーを検証するオープンソースプロジェクトです。
- 現在は実験段階で、アクティブウィンドウのタイトル変動や履歴の可視化を目的としています。
- `Cat is watching you`をコンセプトに、特定のイベントを検出しログを収集するツール作成の基盤を提供します。

## 技術スタック
- フロントエンド: Tone.js (Web Audio APIをラップするJavaScriptライブラリ。オーディオ機能を通じてユーザー体験に貢献する可能性があります。)
- 音楽・オーディオ:
    - Tone.js: Web Audio APIをラップした強力なJavaScriptライブラリで、Webブラウザ上で複雑なオーディオ処理やシンセサイザーの構築を可能にします。
    - Web Audio API: ウェブブラウザに組み込まれた音声処理APIで、高機能なオーディオエフェクトや合成、分析を実現します（Tone.js経由で利用）。
    - MML (Music Macro Language): 音楽をテキストで記述するための記法で、特定の音楽表現をプログラムで生成・解析するために使用されます。
- 開発ツール:
    - Node.js runtime: JavaScriptコードを実行するための環境で、主に開発スクリプトやツールチェインの実行に使用されます。
- テスト: [テスト関連技術の具体的な情報はありません]
- ビルドツール: [ビルド・パース関連技術の具体的な情報はありません]
- 言語機能: [言語仕様・機能の具体的な情報はありません]
- 自動化・CI/CD:
    - GitHub Actions: コードの変更を検知して自動的に様々なタスクを実行するCI/CDプラットフォーム。以下の4つのワークフローが利用されています。
        - プロジェクト要約自動生成: プロジェクトの概要を自動で生成します。
        - Issue自動管理: GitHub Issuesの管理を自動化します。
        - README多言語翻訳: READMEファイルを多言語に自動翻訳します。
        - i18n automation: 国際化（i18n）関連の自動翻訳ワークフロー。
- 開発標準:
    - EditorConfig: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。

## ファイル階層ツリー
```
📄 .editorconfig
📄 .gitignore
📄 .pylintrc
📁 .vscode/
  📊 settings.json
📄 LICENSE
📖 README.ja.md
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
- **.editorconfig**: 異なる開発環境でコードのインデントや文字コードなどのスタイル設定を統一するための設定ファイルです。
- **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリ（例: ビルド成果物、ログファイルなど）を指定します。
- **.pylintrc**: Pythonコードの静的解析ツールPylintの設定ファイルで、コード品質の維持と統一されたコーディング規約の適用に役立ちます。
- **.vscode/settings.json**: Visual Studio Codeエディタのワークスペース固有の設定を定義し、プロジェクトチーム間での開発環境の統一を支援します。
- **LICENSE**: プロジェクトのライセンス情報が記載されており、プロジェクトの利用条件や再配布に関する権利を示します。
- **README.ja.md**: プロジェクトの概要、目的、使い方、インストール方法などが日本語で記述された主要なドキュメントです。
- **aggregate_process_time.bat**: Windows環境で、ログから特定のプロセスのアクティブ時間を集計するPythonスクリプトを実行するためのバッチファイルです。
- **cat_active_window_logger.bat**: Windows環境で、アクティブウィンドウの情報を収集しログに記録するメインのロガースクリプトを起動するためのバッチファイルです。
- **dump_log.bat**: Windows環境で、収集されたログデータを整形してコンソールやファイルに出力するためのバッチファイルです。
- **generated-docs/**: 自動生成されたドキュメントやレポートを格納するためのディレクトリです。
- **issue-notes/**: GitHub Issuesに関する詳細なメモや補足情報を格納するためのディレクトリです。
    - **1.md - 10.md**: 個々のIssueに関する詳細な記述や議論、解決策のメモなどが記録されています。
- **log_enhance_active_time.bat**: Windows環境で、アクティブ時間のログデータをさらに補強・加工するためのPythonスクリプトを実行するバッチファイルです。
- **src/**: プロジェクトの主要なPythonソースコードが格納されているディレクトリです。
    - **src/active_time_reminder/gui.py**: アクティブ時間のリマインダー機能に関連するグラフィカルユーザーインターフェース（GUI）を実装するPythonスクリプトです。
    - **src/log_enhance_active_time/__init__.py**: `log_enhance_active_time`パッケージの初期化ファイルです。
    - **src/log_enhance_active_time/__main__.py**: `log_enhance_active_time`パッケージが直接実行された際のエントリポイントとなるスクリプトです。
    - **src/log_enhance_active_time/add_active_time.py**: 収集されたログデータにアクティブ時間などの情報を追加・更新するロジックを実装したスクリプトです。
    - **src/log_processor/aggregate_process_time.py**: ログデータからプロセスごとの総アクティブ時間やその他の統計情報を集計する処理を実装したスクリプトです。
    - **src/log_processor/dump_log.py**: ログデータを特定の形式（例: TOML）で解析し、人間が読みやすい形式や機械処理しやすい形式で出力するスクリプトです。
    - **src/logger/action_by_ipc.py**: プロセス間通信（IPC）を利用して、他のプロセスからの指示に基づいて特定のアクション（例: ログ開始/停止）を実行するスクリプトです。
    - **src/logger/cat_active_window_logger.py**: アクティブウィンドウの状態（タイトル、プロセス名など）を監視し、定期的にログファイルに記録するメインのロガースクリプトです。
    - **src/logger/dated_log.py**: 日付に基づいてログファイルを管理し、日替わりで新しいログファイルを作成したり、古いログファイルをアーカイブしたりする機能を提供します。
    - **src/logger/get_window_info.py**: 現在フォーカスされているウィンドウのタイトル、プロセスID、プロセス名などの情報を取得するためのプラットフォーム依存の機能を提供します。
    - **src/logger/ipc.py**: プロセス間通信（Inter-Process Communication）を実装するための共通ユーティリティや基盤を提供するスクリプトです。
    - **src/logger/log_and_display.py**: 取得したウィンドウ情報をログに記録すると同時に、必要に応じてユーザーにリアルタイムで表示する機能を持つスクリプトです。
    - **src/logger/utils.py**: プロジェクト全体で利用される汎用的なヘルパー関数やユーティリティ関数を集めたスクリプトです。
- **tests/__init__.py**: `tests`パッケージの初期化ファイルです。
- **tests/test_add_active_time.py**: `src/log_enhance_active_time/add_active_time.py`に実装された機能が正しく動作するかを検証するための単体テストスクリプトです。

## 関数詳細説明
提供された情報には具体的な関数の詳細説明が含まれていません。このプロジェクトはPythonで実装されており、`src`ディレクトリ内の各スクリプトに、ウィンドウ情報の取得、ログの記録、ログデータの処理、GUI表示などを行う関数群が含まれています。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-10-30 07:08:44 JST
