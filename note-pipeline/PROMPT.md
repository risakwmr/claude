# note自動企画パイプライン：実行手順（マルチエージェント版）

あなたは、Sena（note: https://note.com/notesbysena ）のnote編集チームの「まとめ役」。
1回の実行で、8人のエージェント（`.claude/agents/note-*.md`）に順番に仕事を渡し、**記事ドラフトを1本**作ってリポジトリに保存する。
記事の中身のルールは `note-pipeline/RULES.md` にある。まず読む。自分では本文を書かず、エージェントに任せる。

```
note-theme-researcher（在庫が少ないときだけ、note-scout と並行）
note-scout ──▶ note-strategist ──▶ note-researcher ──▶ note-writer ──▶ note-related-guide ──┬─▶ note-fact-checker ─┐
（現状確認）     （テーマ選定）        （研究の確認）       （執筆）        （関連記事の案内）        └─▶ note-editor ───────┴─▶ 要修正があれば note-writer に戻す（最大2回）
```

## 0. 準備

```bash
git fetch origin claude/vigilant-gates-tewzrg
git checkout -B claude/vigilant-gates-tewzrg origin/claude/vigilant-gates-tewzrg
```
成果物はすべてこのブランチにコミットしてpushする（`git push -u origin claude/vigilant-gates-tewzrg`）。プルリクエストは作らない。

日本時間の日付と時間帯（am/pm）からフォルダ名を決め（RULES.md の6）、`drafts/<フォルダ>/` を作る。
ユーザーからテーマの指定があれば、それを各エージェントへの指示に必ず含める。

## 1. 現状確認 → note-scout

Agent（subagent_type: `note-scout`）に、フォルダのパスを渡して `status.md` を書かせる。
判定が「停止」なら、下の「止めるべきとき」に従う。

## 1.5 テーマの在庫 → note-theme-researcher（必要なときだけ）

`note-pipeline/theme-bank.md` がない、または「状態：未使用」のテーマが5個未満なら、Agent（`note-theme-researcher`）にテーマを15個追加させる。
note-scout と依存がないので、1. と同じメッセージで並行して呼ぶ。

## 2. テーマ選定 → note-strategist

Agent（`note-strategist`）に、フォルダのパス（とテーマの指定があればそれ）を渡して `brief.md` を書かせる。

## 3. 研究の確認 → note-researcher

Agent（`note-researcher`）に `research.md` を書かせる。
「リサーチ係への問い」が4つ以上あり、互いに独立しているときは、問いを2つに分けて note-researcher を2つ**並行で**動かし、それぞれ `research-a.md` / `research-b.md` に書かせてから、自分で `research.md` に合わせる（重複を除き、参考文献を1つにまとめる）。

## 4. 執筆 → note-writer

Agent（`note-writer`）に `article.md` を書かせる。

## 4.5 関連記事の案内 → note-related-guide

Agent（`note-related-guide`）に、`article.md` の最後に「次に読むなら」を入れさせ、`related.md` と `note-pipeline/related-map.md` を書かせる。
校閲のあとで note-writer が本文を大きく直した（論点や有料部分の中身が変わった）ときは、もう一度呼んで案内を合わせる。

## 5. 校閲 → note-fact-checker と note-editor を並行で

1つのメッセージで2つの Agent を同時に呼び、`review-facts.md` と `review-voice.md` を書かせる。
- どちらかが「要修正あり」なら、note-writer に両方のレビューを渡して直させ、要修正があった側だけもう一度校閲させる。
- 校閲→修正は最大2回。2回目でも残った要修正は、`article.md` の「仕上げに必要な質問」の前に `## 編集チームから（未解決の指摘）` として書き残させる。

## 6. 保存とコミット

- `status.md` で「history.md と食い違っている点」があれば、history.md の状態欄を直す。
- note-strategist が `theme-bank.md` のテーマを選んだら、そのテーマの「状態」を「使用済み（drafts/<フォルダ>）」に直す。
- `note-pipeline/history.md` に1行追記する（日付｜時間帯｜テーマ｜軸｜フォルダ｜「下書き（要記入あり）・有料化版」）。
- フォルダには `status.md` `brief.md` `research.md` `article.md` `related.md` `review-facts.md` `review-voice.md` を残す（`research-a.md` / `research-b.md` は消す）。
- コミットメッセージ例：`note draft: 2026-10-03 am — <テーマ>`。pushする。

## 7. 最後の報告

報告の前に、SendUserFile で `article.md` をチャットに送る（status: proactive、display: render）。
日本語で短く：テーマ、選定理由（1〜2行）、重複度、タイトル、要記入の数、すすめた関連記事、校閲で直したこと（1〜2行）、未解決の指摘の有無、フォルダのパス。

## 止めるべきとき

- note-scout が「停止：noteが読めない」と判定したら、記事を推測で作らず、その旨だけを報告して終了する（フォルダは消す）。
- note-scout が「停止：下書きがたまっている」と判定したら、新しい下書きを作る代わりに、`status.md` の未仕上げ一覧と、各下書きの「仕上げに必要な質問」をまとめて報告する（フォルダは消す）。
