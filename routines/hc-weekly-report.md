# Human Curriculum 週次レポート（このチャットで回す版）

## 作業場所（このチャットで回すための変更・2026-10-09）
- このチャットの /home/user/claude は note のブランチ（claude/vigilant-gates-tewzrg）で使っているので、切り替えない。episodes ブランチは別の作業ツリーで扱う：
  cd /home/user/claude && git fetch origin episodes && (git worktree add /home/user/episodes-wt origin/episodes 2>/dev/null || true) && cd /home/user/episodes-wt && git checkout -B episodes origin/episodes
- 以下の手順はすべて /home/user/episodes-wt で行う（「準備」の 1〜2 は、この手順で置き換える）。

YouTube番組「Human Curriculum」(チャンネル @learnwhataicant)の週次レポートを作って、ユーザー(リサさん)にこのチャットで届けてください。日本語で、やさしく率直なトーンで。

## 準備
1. 作業ディレクトリに risakwmr/claude がなければ、add_repo ツール(owner: risakwmr, repo: claude, access: push)で追加し、その結果の手順でcloneする。
2. git fetch origin episodes && git checkout -B episodes origin/episodes
3. README.md の「Weekly report」と src/report.py の冒頭の説明を読む。

## 数字を取る
1. レポート用の実行を1回だけ起動する(これ以外の操作は起動しない):
   gh api -X POST repos/risakwmr/claude/actions/workflows/episodes.yml/dispatches -f ref=main -f 'inputs[action]=report'
2. gh api 'repos/risakwmr/claude/actions/runs?per_page=3&event=workflow_dispatch' で完了を待つ(1分おき、最大15分)。失敗したら、失敗したステップ名を調べて報告に含め、手元にある最新の reports/*.json で書く。
3. git pull --rebase origin episodes して、reports/ の最新ファイル(今日の日付)と、その前のファイルを読む。shorts_stats.json、published.json、shorts.json、episodes/episodes.json(タイトル・title_ja)も参考にする。数字の計算は必ず python で行う(暗算しない)。

## レポートの中身(短く、スマホで読みやすく)
- 今週のまとめ:登録者数と総再生数、前回からの増減。
- よく見られた本編 TOP3 と Shorts TOP3(タイトル・再生・いいね・コメント)。
- Shorts の種類別(ai=AIにできないこと / story=ダニエルの話 / culture=日米比較 / lab=Speaking Lab)の1本あたり平均再生。
- analytics.available が true のとき:平均視聴率(何%まで見られているか)、総視聴時間、主な流入元(検索・おすすめ・Shorts・外部など)、上位の国(ターゲットは海外の視聴者なので、日本以外の割合にも触れる)、デバイス、登録者・非登録者の視聴の違い。
- 気づき2〜3個と、来週試すこと1〜2個:冒頭のフック・タイトル・Shorts の種類や時間帯など、具体的に。数字がまだ小さいとき(例:1本あたり再生が数十回未満)は、偶然の差が大きいことを正直に書き、強い結論を出さない。少ない数字を責めたり、不安をあおったりしない。伸びた点はちゃんと喜ぶ。
- analytics.available が false のときは、最後に1行だけ:「視聴時間や流入元も見たい場合は、Googleの許可画面でアナリティクスの閲覧(yt-analytics.readonly)を足して、新しい Refresh token を GitHub の Secret REFRESH_TOKEN に入れてね(トークンはチャットに貼らないでね)」。

## 届け方（このチャットで回すための変更・2026-10-09）
- 通知は出さない。PushNotification・SendUserMessage・SendUserFile は使わない。
- レポート本文をこのチャットに書く。見出しと箇条書きで、全体で30行程度まで。

## してはいけないこと
- 動画のタイトル・説明・公開設定・字幕・プレイリストなど、YouTube 側のものを変えない。report 以外のワークフロー操作を起動しない。
- コミットするのは、ワークフローが保存した reports/ だけ(自分では基本的にコミット不要)。
- Refresh token やシークレットの値を表示・要求しない。