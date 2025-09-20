Last updated: 2025-09-20

# 開発状況生成プロンプト（開発者向け）

## 生成するもの：
- 現在openされているissuesを3行で要約する
- 次の一手の候補を3つlistする
- 次の一手の候補3つそれぞれについて、極力小さく分解して、その最初の小さな一歩を書く

## 生成しないもの：
- 「今日のissue目標」などuserに提案するもの
  - ハルシネーションの温床なので生成しない
- ハルシネーションしそうなものは生成しない（例、無価値なtaskや新issueを勝手に妄想してそれをuserに提案する等）
- プロジェクト構造情報（来訪者向け情報のため、別ファイルで管理）

## 「Agent実行プロンプト」生成ガイドライン：
「Agent実行プロンプト」作成時は以下の要素を必ず含めてください：

### 必須要素
1. **対象ファイル**: 分析/編集する具体的なファイルパス
2. **実行内容**: 具体的な分析や変更内容（「分析してください」ではなく「XXXファイルのYYY機能を分析し、ZZZの観点でmarkdown形式で出力してください」）
3. **確認事項**: 変更前に確認すべき依存関係や制約
4. **期待する出力**: markdown形式での結果や、具体的なファイル変更

### Agent実行プロンプト例

**良い例（上記「必須要素」4項目を含む具体的なプロンプト形式）**:
```
対象ファイル: `.github/workflows/translate-readme.yml`と`.github/workflows/call-translate-readme.yml`

実行内容: 対象ファイルについて、外部プロジェクトから利用する際に必要な設定項目を洗い出し、以下の観点から分析してください：
1) 必須入力パラメータ（target-branch等）
2) 必須シークレット（GEMINI_API_KEY）
3) ファイル配置の前提条件（README.ja.mdの存在）
4) 外部プロジェクトでの利用時に必要な追加設定

確認事項: 作業前に既存のworkflowファイルとの依存関係、および他のREADME関連ファイルとの整合性を確認してください。

期待する出力: 外部プロジェクトがこの`call-translate-readme.yml`を導入する際の手順書をmarkdown形式で生成してください。具体的には：必須パラメータの設定方法、シークレットの登録手順、前提条件の確認項目を含めてください。
```

**避けるべき例**:
- callgraphについて調べてください
- ワークフローを分析してください
- issue-noteの処理フローを確認してください

## 出力フォーマット：
以下のMarkdown形式で出力してください：

```markdown
# Development Status

## 現在のIssues
[以下の形式で3行でオープン中のissuesを要約。issue番号を必ず書く]
- [1行目の説明]
- [2行目の説明]
- [3行目の説明]

## 次の一手候補
1. [候補1のタイトル。issue番号を必ず書く]
   - 最初の小さな一歩: [具体的で実行可能な最初のアクション]
   - Agent実行プロンプト:
     ```
     対象ファイル: [分析/編集する具体的なファイルパス]

     実行内容: [具体的な分析や変更内容を記述]

     確認事項: [変更前に確認すべき依存関係や制約]

     期待する出力: [markdown形式での結果や、具体的なファイル変更の説明]
     ```

2. [候補2のタイトル。issue番号を必ず書く]
   - 最初の小さな一歩: [具体的で実行可能な最初のアクション]
   - Agent実行プロンプト:
     ```
     対象ファイル: [分析/編集する具体的なファイルパス]

     実行内容: [具体的な分析や変更内容を記述]

     確認事項: [変更前に確認すべき依存関係や制約]

     期待する出力: [markdown形式での結果や、具体的なファイル変更の説明]
     ```

3. [候補3のタイトル。issue番号を必ず書く]
   - 最初の小さな一歩: [具体的で実行可能な最初のアクション]
   - Agent実行プロンプト:
     ```
     対象ファイル: [分析/編集する具体的なファイルパス]

     実行内容: [具体的な分析や変更内容を記述]

     確認事項: [変更前に確認すべき依存関係や制約]

     期待する出力: [markdown形式での結果や、具体的なファイル変更の説明]
     ```
```


# 開発状況情報
- 以下の開発状況情報を参考にしてください。
- Issue番号を記載する際は、必ず [Issue #番号](../issue-notes/番号.md) の形式でMarkdownリンクとして記載してください。

## プロジェクトのファイル一覧
- .editorconfig
- .github/actions-tmp/.github/workflows/call-callgraph.yml
- .github/actions-tmp/.github/workflows/call-daily-project-summary.yml
- .github/actions-tmp/.github/workflows/call-issue-note.yml
- .github/actions-tmp/.github/workflows/call-translate-readme.yml
- .github/actions-tmp/.github/workflows/callgraph.yml
- .github/actions-tmp/.github/workflows/daily-project-summary.yml
- .github/actions-tmp/.github/workflows/issue-note.yml
- .github/actions-tmp/.github/workflows/translate-readme.yml
- .github/actions-tmp/.github_automation/callgraph/codeql-queries/callgraph.ql
- .github/actions-tmp/.github_automation/callgraph/codeql-queries/codeql-pack.lock.yml
- .github/actions-tmp/.github_automation/callgraph/codeql-queries/qlpack.yml
- .github/actions-tmp/.github_automation/callgraph/config/example.json
- .github/actions-tmp/.github_automation/callgraph/docs/callgraph.md
- .github/actions-tmp/.github_automation/callgraph/presets/callgraph.js
- .github/actions-tmp/.github_automation/callgraph/presets/style.css
- .github/actions-tmp/.github_automation/callgraph/scripts/analyze-codeql.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/callgraph-utils.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/check-codeql-exists.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/check-commits.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/check-node-version.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/common-utils.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/copy-commit-results.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/extract-sarif-info.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/find-process-results.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/generate-html-graph.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/generateHTML.cjs
- .github/actions-tmp/.github_automation/project_summary/docs/daily-summary-setup.md
- .github/actions-tmp/.github_automation/project_summary/prompts/development-status-prompt.md
- .github/actions-tmp/.github_automation/project_summary/prompts/project-overview-prompt.md
- .github/actions-tmp/.github_automation/project_summary/scripts/ProjectSummaryCoordinator.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/development/DevelopmentStatusGenerator.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/development/GitUtils.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/development/IssueTracker.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/generate-project-summary.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/overview/CodeAnalyzer.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/overview/ProjectAnalysisOrchestrator.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/overview/ProjectDataCollector.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/overview/ProjectDataFormatter.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/overview/ProjectOverviewGenerator.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/overview/TechStackAnalyzer.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/shared/BaseGenerator.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/shared/FileSystemUtils.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/shared/ProjectFileUtils.cjs
- .github/actions-tmp/.github_automation/translate/docs/TRANSLATION_SETUP.md
- .github/actions-tmp/.github_automation/translate/scripts/translate-readme.cjs
- .github/actions-tmp/.gitignore
- .github/actions-tmp/.vscode/settings.json
- .github/actions-tmp/LICENSE
- .github/actions-tmp/README.ja.md
- .github/actions-tmp/README.md
- .github/actions-tmp/generated-docs/callgraph.html
- .github/actions-tmp/generated-docs/callgraph.js
- .github/actions-tmp/generated-docs/development-status-generated-prompt.md
- .github/actions-tmp/generated-docs/development-status.md
- .github/actions-tmp/generated-docs/project-overview.md
- .github/actions-tmp/generated-docs/style.css
- .github/actions-tmp/issue-notes/10.md
- .github/actions-tmp/issue-notes/11.md
- .github/actions-tmp/issue-notes/12.md
- .github/actions-tmp/issue-notes/13.md
- .github/actions-tmp/issue-notes/14.md
- .github/actions-tmp/issue-notes/15.md
- .github/actions-tmp/issue-notes/16.md
- .github/actions-tmp/issue-notes/17.md
- .github/actions-tmp/issue-notes/18.md
- .github/actions-tmp/issue-notes/19.md
- .github/actions-tmp/issue-notes/2.md
- .github/actions-tmp/issue-notes/20.md
- .github/actions-tmp/issue-notes/21.md
- .github/actions-tmp/issue-notes/22.md
- .github/actions-tmp/issue-notes/23.md
- .github/actions-tmp/issue-notes/24.md
- .github/actions-tmp/issue-notes/25.md
- .github/actions-tmp/issue-notes/26.md
- .github/actions-tmp/issue-notes/27.md
- .github/actions-tmp/issue-notes/28.md
- .github/actions-tmp/issue-notes/3.md
- .github/actions-tmp/issue-notes/4.md
- .github/actions-tmp/issue-notes/7.md
- .github/actions-tmp/issue-notes/8.md
- .github/actions-tmp/issue-notes/9.md
- .github/actions-tmp/package-lock.json
- .github/actions-tmp/package.json
- .github/actions-tmp/src/main.js
- .github/workflows/call-daily-project-summary.yml
- .github/workflows/issue-note.yml
- .gitignore
- .pylintrc
- .vscode/settings.json
- LICENSE
- README.md
- cat_active_window_logger.bat
- dump_log.bat
- issue-notes/1.md
- issue-notes/10.md
- issue-notes/2.md
- issue-notes/3.md
- issue-notes/4.md
- issue-notes/5.md
- issue-notes/6.md
- issue-notes/7.md
- issue-notes/8.md
- issue-notes/9.md
- log_enhance_active_time.bat
- src/log_enhance_active_time/__init__.py
- src/log_enhance_active_time/__main__.py
- src/log_enhance_active_time/add_active_time.py
- src/log_processor/dump_log.py
- src/logger/action_by_ipc.py
- src/logger/cat_active_window_logger.py
- src/logger/dated_log.py
- src/logger/get_window_info.py
- src/logger/ipc.py
- src/logger/log_and_display.py
- src/logger/utils.py
- tests/__init__.py
- tests/test_add_active_time.py

## 現在のオープンIssues
## [Issue #10](../issue-notes/10.md): logのrotationの方針を洗い出して整理する
[issue-notes/10.md](https://github.com/cat2151/cat-active-window-logger/blob/main/issue-notes/10.md)...
ラベル: 
--- issue-notes/10.md の内容 ---

```markdown
# issue logのrotationの方針を洗い出して整理する #10
[issues #10](https://github.com/cat2151/cat-active-window-logger/issues/10)



```

## [Issue #9](../issue-notes/9.md): エンドユーザーが使うには向かない。どこまで自分以外のユーザーに使いやすくするか、project方針を整理する
[issue-notes/9.md](https://github.com/cat2151/cat-active-window-logger/blob/main/issue-notes/9.md)...
ラベル: 
--- issue-notes/9.md の内容 ---

```markdown
# issue エンドユーザーが使うには向かない。どこまで自分以外のユーザーに使いやすくするか、project方針を整理する #9
[issues #9](https://github.com/cat2151/cat-active-window-logger/issues/9)



```

## [Issue #7](../issue-notes/7.md): logが日をまたいだのに前日のfilenameのまま追記が続いてしまっている
[issue-notes/7.md](https://github.com/cat2151/cat-active-window-logger/blob/main/issue-notes/7.md)...
ラベル: 
--- issue-notes/7.md の内容 ---

```markdown
# issue logが日をまたいだのに前日のfilenameのまま追記が続いてしまっている #7
[issues #7](https://github.com/cat2151/cat-active-window-logger/issues/7)

# これまでの課題
- logが日をまたいだのに前日のfilenameのまま追記が続いてしまっている

# プロンプト案
- logが日をまたいだのに前日のfilenameのまま追記が続いてしまっています。
- 以下の挙動にしてください：
    - 日をまたいだのち初回のlog書き込み時は、
    - これまでのlogをcloseし、
    - 新たにその日のfilenameのlogへのappendを開始する
- コードベースのloggerのpyをreadして進めてください。

# 結果
- agentに書かせて、指摘して、修正させた
- close条件は、翌日にlogが期待値どおりの動作になっていること
- 様子見する

```

## [Issue #5](../issue-notes/5.md): process_nameでgroupingした合計時間logを入力とし、tkinterによるGUIで表示する
[issue-notes/5.md](https://github.com/cat2151/cat-active-window-logger/blob/main/issue-notes/5.md)...
ラベル: 
--- issue-notes/5.md の内容 ---

```markdown
# issue process_nameでgroupingした合計時間logを入力とし、tkinterによるGUIで表示する #5
[issues #5](https://github.com/cat2151/cat-active-window-logger/issues/5)

# これまでの課題
- 例えば何分SNSをしていたかが、GUIですぐにわからない
    - 例、今まさにSNSを、自分で決めた5分を超過してやってしまったら、
        - リマインダーとして、その旨を、GUIで表示する
            - GUIは
                - バルーン的に、フォーカスを奪わない
                - フォーカスを奪わないし、適切な条件で、最背面化し、邪魔にならない
                - これらは 別project 格ゲーボタンチャレンジ で実現済み

# 前提
- [issues #4](https://github.com/cat2151/cat-active-window-logger/issues/4)


↑あとで整理する

```

## [Issue #4](../issue-notes/4.md): 次のwindowに切り替わるまでの時間のlog、を入力とし、tomlで指定した条件例えばまずはprocess_nameでgroupingした合計時間logを出力する
[issue-notes/4.md](https://github.com/cat2151/cat-active-window-logger/blob/main/issue-notes/4.md)...
ラベル: 
--- issue-notes/4.md の内容 ---

```markdown
# issue 次のwindowに切り替わるまでの時間のlog、を入力とし、tomlで指定した条件例えばまずはprocess_nameでgroupingした合計時間logを出力する #4
[issues #4](https://github.com/cat2151/cat-active-window-logger/issues/4)

# これまでの課題
- 例えば何分SNSをしていたかがわからない

# 前提
- [issues #3](https://github.com/cat2151/cat-active-window-logger/issues/3)

# 対策案
- 時間のlog（時刻のlogを加工したもの）が得られた前提で、
- それを例えばprocess_name chrome.exe でgroupingする
- でcrhome.exeの合計時間のlogを出力する
- もちろん、これだけでは、何分SNSしていたかを知るには不足
    - 何が不足か、次の手はどれがいいか、の可視化のための検証である
        - 例えば、より細かいgrouping条件や、ロジックが必要な想定
            - それらを今の段階から想定するよりは、
                - まずデータを取ってからのほうがスムーズである想定
- まずハードコーディングでagentに実装させる
- のち仕様変更してagentに実装させる。issues 3 と同じ手法。

↑あとで整理する

```

## [Issue #2](../issue-notes/2.md): windowのlogだけでなく、toml actionsのlogを別途、1日単位のfileで出力する
[issue-notes/2.md](https://github.com/cat2151/cat-active-window-logger/blob/main/issue-notes/2.md)...
ラベル: 
--- issue-notes/2.md の内容 ---

```markdown
# issue windowのlogだけでなく、toml actionsのlogを別途、1日単位のfileで出力する #2
[issues #2](https://github.com/cat2151/cat-active-window-logger/issues/2)

# これまでの課題
- tomlでactionsを定義したのはいいが、
- 実際どれくらい何がactionされているか？が
- 可視化されていない

# 対策案
- 可視化したい
- ひとまずlogで可視化しよう

## 出力イメージ
- logs/ と別に、logs_actions/ を用意する、そこに出力する
- 内容ブレインストーミング：
    - イメージ：
        - この時刻に、このactionをしました
    - list：
        - `[[action_information]]`
            - `timestamp = "～"`
            - `actions = ～`
    - 詳細：
        - actions の内容はtomlのactionsのコピーそのものとする
            - もしあとからtoml変更しても、logには変更前のimmutableな情報が残せる
            - 毎回だと冗長だが、それでよい。いつでもtoml変更はありうるので。
            - log rotateしたあと圧縮すれば、冗長さは解決する。

↑あとでさらに整理する

```

## ドキュメントで言及されているファイルの内容
### .github/actions-tmp/issue-notes/10.md
```md
# issue callgraph を他projectから使いやすくする #10
[issues #10](https://github.com/cat2151/github-actions/issues/10)

# ブレインストーミング
- 洗い出し
    - 他projectから使う場合の問題を洗い出す、今見えている範囲で、手早く、このnoteに可視化する
    - 洗い出したものは、一部は別issueに切り分ける
- close条件
    - まずは4つそれぞれを個別のdirに切り分けてtest greenとなること、とするつもり
    - それ以外は別issueに切り分けるつもり
- 切り分け
    - 別dirに切り分ける
        - 課題、`codeql-queries/` が `.github/` 配下にある。対策、`.github_automation/callgraph_enhanced/codeql-queries/` とする
        - 課題、scriptも、`.github/`配下にある。対策、移動する
        - 方法、agentを試し、ハルシネーションで時間が取られるなら人力に切り替える
- test
    - local WSL + act でtestする
- 名前
    - 課題、名前 enhanced が不要。対策、名前から enhanced を削除してymlなどもそれぞれ同期して修正すべし
- docs
    - call導入手順を書く

# 状況
- 上記のうち、別dirへの切り分け等は実施済みのはず
- どうする？
    - それをここに可視化する。

```

### issue-notes/10.md
```md
# issue logのrotationの方針を洗い出して整理する #10
[issues #10](https://github.com/cat2151/cat-active-window-logger/issues/10)



```

### .github/actions-tmp/issue-notes/2.md
```md
# issue GitHub Actions「関数コールグラフhtmlビジュアライズ生成」を共通ワークフロー化する #2
[issues #2](https://github.com/cat2151/github-actions/issues/2)


# prompt
```
あなたはGitHub Actionsと共通ワークフローのスペシャリストです。
このymlファイルを、以下の2つのファイルに分割してください。
1. 共通ワークフロー       cat2151/github-actions/.github/workflows/callgraph_enhanced.yml
2. 呼び出し元ワークフロー cat2151/github-actions/.github/workflows/call-callgraph_enhanced.yml
まずplanしてください
```

# 結果
- indent
    - linter？がindentのエラーを出しているがyml内容は見た感じOK
    - テキストエディタとagentの相性問題と判断する
    - 別のテキストエディタでsaveしなおし、テキストエディタをreload
    - indentのエラーは解消した
- LLMレビュー
    - agent以外の複数のLLMにレビューさせる
    - prompt
```
あなたはGitHub Actionsと共通ワークフローのスペシャリストです。
以下の2つのファイルをレビューしてください。最優先で、エラーが発生するかどうかだけレビューしてください。エラー以外の改善事項のチェックをするかわりに、エラー発生有無チェックに最大限注力してください。

--- 共通ワークフロー

# GitHub Actions Reusable Workflow for Call Graph Generation
name: Generate Call Graph

# TODO Windowsネイティブでのtestをしていた名残が残っているので、今後整理していく。今はWSL act でtestしており、Windowsネイティブ環境依存問題が解決した
#  ChatGPTにレビューさせるとそこそこ有用そうな提案が得られたので、今後それをやる予定
#  agentに自己チェックさせる手も、セカンドオピニオンとして選択肢に入れておく

on:
  workflow_call:

jobs:
  check-commits:
    runs-on: ubuntu-latest
    outputs:
      should-run: ${{ steps.check.outputs.should-run }}
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 50 # 過去のコミットを取得

      - name: Check for user commits in last 24 hours
        id: check
        run: |
          node .github/scripts/callgraph_enhanced/check-commits.cjs

  generate-callgraph:
    needs: check-commits
    if: needs.check-commits.outputs.should-run == 'true'
    runs-on: ubuntu-latest
    permissions:
      contents: write
      security-events: write
      actions: read

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set Git identity
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

      - name: Remove old CodeQL packages cache
        run: rm -rf ~/.codeql/packages

      - name: Check Node.js version
        run: |
          node .github/scripts/callgraph_enhanced/check-node-version.cjs

      - name: Install CodeQL CLI
        run: |
          wget https://github.com/github/codeql-cli-binaries/releases/download/v2.22.1/codeql-linux64.zip
          unzip codeql-linux64.zip
          sudo mv codeql /opt/codeql
          echo "/opt/codeql" >> $GITHUB_PATH

      - name: Install CodeQL query packs
        run: |
          /opt/codeql/codeql pack install .github/codeql-queries

      - name: Check CodeQL exists
        run: |
          node .github/scripts/callgraph_enhanced/check-codeql-exists.cjs

      - name: Verify CodeQL Configuration
        run: |
          node .github/scripts/callgraph_enhanced/analyze-codeql.cjs verify-config

      - name: Remove existing CodeQL DB (if any)
        run: |
          rm -rf codeql-db

      - name: Perform CodeQL Analysis
        run: |
          node .github/scripts/callgraph_enhanced/analyze-codeql.cjs analyze

      - name: Check CodeQL Analysis Results
        run: |
          node .github/scripts/callgraph_enhanced/analyze-codeql.cjs check-results

      - name: Debug CodeQL execution
        run: |
          node .github/scripts/callgraph_enhanced/analyze-codeql.cjs debug

      - name: Wait for CodeQL results
        run: |
          node -e "setTimeout(()=>{}, 10000)"

      - name: Find and process CodeQL results
        run: |
          node .github/scripts/callgraph_enhanced/find-process-results.cjs

      - name: Generate HTML graph
        run: |
          node .github/scripts/callgraph_enhanced/generate-html-graph.cjs

      - name: Copy files to generated-docs and commit results
        run: |
          node .github/scripts/callgraph_enhanced/copy-commit-results.cjs

--- 呼び出し元
# 呼び出し元ワークフロー: call-callgraph_enhanced.yml
name: Call Call Graph Enhanced

on:
  schedule:
    # 毎日午前5時(JST) = UTC 20:00前日
    - cron: '0 20 * * *'
  workflow_dispatch:

jobs:
  call-callgraph-enhanced:
    # uses: cat2151/github-actions/.github/workflows/callgraph_enhanced.yml
    uses: ./.github/workflows/callgraph_enhanced.yml # ローカルでのテスト用
```

# レビュー結果OKと判断する
- レビュー結果を人力でレビューした形になった

# test
- #4 同様にローカル WSL + act でtestする
- エラー。userのtest設計ミス。
  - scriptの挙動 : src/ がある前提
  - 今回の共通ワークフローのリポジトリ : src/ がない
  - 今回testで実現したいこと
    - 仮のソースでよいので、関数コールグラフを生成させる
  - 対策
    - src/ にダミーを配置する
- test green
  - ただしcommit pushはしてないので、html内容が0件NG、といったケースの検知はできない
  - もしそうなったら別issueとしよう

# test green

# commit用に、yml 呼び出し元 uses をlocal用から本番用に書き換える

# closeとする
- もしhtml内容が0件NG、などになったら、別issueとするつもり

```

### issue-notes/2.md
```md
# issue windowのlogだけでなく、toml actionsのlogを別途、1日単位のfileで出力する #2
[issues #2](https://github.com/cat2151/cat-active-window-logger/issues/2)

# これまでの課題
- tomlでactionsを定義したのはいいが、
- 実際どれくらい何がactionされているか？が
- 可視化されていない

# 対策案
- 可視化したい
- ひとまずlogで可視化しよう

## 出力イメージ
- logs/ と別に、logs_actions/ を用意する、そこに出力する
- 内容ブレインストーミング：
    - イメージ：
        - この時刻に、このactionをしました
    - list：
        - `[[action_information]]`
            - `timestamp = "～"`
            - `actions = ～`
    - 詳細：
        - actions の内容はtomlのactionsのコピーそのものとする
            - もしあとからtoml変更しても、logには変更前のimmutableな情報が残せる
            - 毎回だと冗長だが、それでよい。いつでもtoml変更はありうるので。
            - log rotateしたあと圧縮すれば、冗長さは解決する。

↑あとでさらに整理する

```

### .github/actions-tmp/issue-notes/4.md
```md
# issue GitHub Actions「project概要生成」を共通ワークフロー化する #4
[issues #4](https://github.com/cat2151/github-actions/issues/4)

# prompt
```
あなたはGitHub Actionsと共通ワークフローのスペシャリストです。
このymlファイルを、以下の2つのファイルに分割してください。
1. 共通ワークフロー       cat2151/github-actions/.github/workflows/daily-project-summary.yml
2. 呼び出し元ワークフロー cat2151/github-actions/.github/workflows/call-daily-project-summary.yml
まずplanしてください
```

# 結果、あちこちハルシネーションのあるymlが生成された
- agentの挙動があからさまにハルシネーション
    - インデントが修正できない、「失敗した」という
    - 構文誤りを認識できない
- 人力で修正した

# このagentによるセルフレビューが信頼できないため、別のLLMによるセカンドオピニオンを試す
```
あなたはGitHub Actionsと共通ワークフローのスペシャリストです。
以下の2つのファイルをレビューしてください。最優先で、エラーが発生するかどうかだけレビューてください。エラー以外の改善事項のチェックをするかわりに、エラー発生有無チェックに最大限注力してください。

--- 呼び出し元

name: Call Daily Project Summary

on:
  schedule:
    # 日本時間 07:00 (UTC 22:00 前日)
    - cron: '0 22 * * *'
  workflow_dispatch:

jobs:
  call-daily-project-summary:
    uses: cat2151/github-actions/.github/workflows/daily-project-summary.yml
    secrets:
      GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}

--- 共通ワークフロー
name: Daily Project Summary
on:
  workflow_call:

jobs:
  generate-summary:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      issues: read
      pull-requests: read

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          fetch-depth: 0  # 履歴を取得するため

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: |
          # 一時的なディレクトリで依存関係をインストール
          mkdir -p /tmp/summary-deps
          cd /tmp/summary-deps
          npm init -y
          npm install @google/generative-ai @octokit/rest
          # generated-docsディレクトリを作成
          mkdir -p $GITHUB_WORKSPACE/generated-docs

      - name: Generate project summary
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GITHUB_REPOSITORY: ${{ github.repository }}
          NODE_PATH: /tmp/summary-deps/node_modules
        run: |
          node .github/scripts/generate-project-summary.cjs

      - name: Check for generated summaries
        id: check_summaries
        run: |
          if [ -f "generated-docs/project-overview.md" ] && [ -f "generated-docs/development-status.md" ]; then
            echo "summaries_generated=true" >> $GITHUB_OUTPUT
          else
            echo "summaries_generated=false" >> $GITHUB_OUTPUT
          fi

      - name: Commit and push summaries
        if: steps.check_summaries.outputs.summaries_generated == 'true'
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          # package.jsonの変更のみリセット（generated-docsは保持）
          git restore package.json 2>/dev/null || true
          # サマリーファイルのみを追加
          git add generated-docs/project-overview.md
          git add generated-docs/development-status.md
          git commit -m "Update project summaries (overview & development status)"
          git push

      - name: Summary generation result
        run: |
          if [ "${{ steps.check_summaries.outputs.summaries_generated }}" == "true" ]; then
            echo "✅ Project summaries updated successfully"
            echo "📊 Generated: project-overview.md & development-status.md"
          else
            echo "ℹ️ No summaries generated (likely no user commits in the last 24 hours)"
          fi
```

# 上記promptで、2つのLLMにレビューさせ、合格した

# 細部を、先行する2つのymlを参照に手直しした

# ローカルtestをしてからcommitできるとよい。方法を検討する
- ローカルtestのメリット
    - 素早く修正のサイクルをまわせる
    - ムダにgit historyを汚さない
        - これまでの事例：「実装したつもり」「エラー。修正したつもり」「エラー。修正したつもり」...（以降エラー多数）
- 方法
    - ※検討、WSL + act を環境構築済みである。test可能であると判断する
    - 呼び出し元のURLをコメントアウトし、相対パス記述にする
    - ※備考、テスト成功すると結果がcommit pushされる。それでよしとする
- 結果
    - OK
    - secretsを簡略化できるか試した、できなかった、現状のsecrets記述が今わかっている範囲でベストと判断する
    - OK

# test green

# commit用に、yml 呼び出し元 uses をlocal用から本番用に書き換える

# closeとする

```

### issue-notes/4.md
```md
# issue 次のwindowに切り替わるまでの時間のlog、を入力とし、tomlで指定した条件例えばまずはprocess_nameでgroupingした合計時間logを出力する #4
[issues #4](https://github.com/cat2151/cat-active-window-logger/issues/4)

# これまでの課題
- 例えば何分SNSをしていたかがわからない

# 前提
- [issues #3](https://github.com/cat2151/cat-active-window-logger/issues/3)

# 対策案
- 時間のlog（時刻のlogを加工したもの）が得られた前提で、
- それを例えばprocess_name chrome.exe でgroupingする
- でcrhome.exeの合計時間のlogを出力する
- もちろん、これだけでは、何分SNSしていたかを知るには不足
    - 何が不足か、次の手はどれがいいか、の可視化のための検証である
        - 例えば、より細かいgrouping条件や、ロジックが必要な想定
            - それらを今の段階から想定するよりは、
                - まずデータを取ってからのほうがスムーズである想定
- まずハードコーディングでagentに実装させる
- のち仕様変更してagentに実装させる。issues 3 と同じ手法。

↑あとで整理する

```

### .github/actions-tmp/issue-notes/7.md
```md
# issue issue note生成できるかのtest用 #7
[issues #7](https://github.com/cat2151/github-actions/issues/7)

- 生成できた
- closeとする

```

### issue-notes/7.md
```md
# issue logが日をまたいだのに前日のfilenameのまま追記が続いてしまっている #7
[issues #7](https://github.com/cat2151/cat-active-window-logger/issues/7)

# これまでの課題
- logが日をまたいだのに前日のfilenameのまま追記が続いてしまっている

# プロンプト案
- logが日をまたいだのに前日のfilenameのまま追記が続いてしまっています。
- 以下の挙動にしてください：
    - 日をまたいだのち初回のlog書き込み時は、
    - これまでのlogをcloseし、
    - 新たにその日のfilenameのlogへのappendを開始する
- コードベースのloggerのpyをreadして進めてください。

# 結果
- agentに書かせて、指摘して、修正させた
- close条件は、翌日にlogが期待値どおりの動作になっていること
- 様子見する

```

### .github/actions-tmp/issue-notes/9.md
```md
# issue 関数コールグラフhtmlビジュアライズが0件なので、原因を可視化する #9
[issues #9](https://github.com/cat2151/github-actions/issues/9)

# agentに修正させたり、人力で修正したりした
- agentがハルシネーションし、いろいろ根の深いバグにつながる、エラー隠蔽などを仕込んでいたため、検知が遅れた
- 詳しくはcommit logを参照のこと
- WSL + actの環境を少し変更、act起動時のコマンドライン引数を変更し、generated-docsをmountする（ほかはデフォルト挙動であるcpだけにする）ことで、デバッグ情報をコンテナ外に出力できるようにし、デバッグを効率化した

# test green

# closeとする

```

### issue-notes/9.md
```md
# issue エンドユーザーが使うには向かない。どこまで自分以外のユーザーに使いやすくするか、project方針を整理する #9
[issues #9](https://github.com/cat2151/cat-active-window-logger/issues/9)



```

### issue-notes/5.md
```md
# issue process_nameでgroupingした合計時間logを入力とし、tkinterによるGUIで表示する #5
[issues #5](https://github.com/cat2151/cat-active-window-logger/issues/5)

# これまでの課題
- 例えば何分SNSをしていたかが、GUIですぐにわからない
    - 例、今まさにSNSを、自分で決めた5分を超過してやってしまったら、
        - リマインダーとして、その旨を、GUIで表示する
            - GUIは
                - バルーン的に、フォーカスを奪わない
                - フォーカスを奪わないし、適切な条件で、最背面化し、邪魔にならない
                - これらは 別project 格ゲーボタンチャレンジ で実現済み

# 前提
- [issues #4](https://github.com/cat2151/cat-active-window-logger/issues/4)


↑あとで整理する

```

## 最近の変更（過去7日間）
### コミット履歴:
8b2740a 日次バッチでdeveopment statusを生成させるようにした、つもり
91c6759 #4 mdメンテ

### 変更されたファイル:
.github/workflows/call-daily-project-summary.yml
.github/workflows/issue-note.yml
issue-notes/10.md
issue-notes/4.md
issue-notes/7.md
issue-notes/8.md
issue-notes/9.md
src/logger/log_and_display.py


---
Generated at: 2025-09-20 18:05:02 JST
