---
name: note-related
description: noteの最後に置く関連記事の案内文を作る（note-related-guide を呼ぶ）。「関連記事の案内を作って」「次に読む記事の誘導文」「/note-related」のとき。引数に今回のnoteのタイトル・要約と公開済みnoteの一覧を書けば、それで作る。引数がなければ最新の下書きフォルダで作る。
---

1. `claude/vigilant-gates-tewzrg` ブランチにいることを確かめる（`note-pipeline/PROMPT.md` の0. 準備）。
2. 対象を決める：
   - 引数（$ARGUMENTS）にタイトル・要約・公開済み一覧があれば、それを note-related-guide にそのまま渡す。対応する下書きフォルダがあればそのパスも渡す。なければ `article.md` には入れず、`related.md` を `note-pipeline/related/YYYY-MM-DD-<短い名前>.md` に書かせる。
   - 引数がなければ、`drafts/` のいちばん新しいフォルダを対象にする。
3. Agent（subagent_type: `note-related-guide`）を呼ぶ。
4. コミットしてpushする（例：`note related: 2026-10-09 am — 関連記事の案内`）。
5. 案内（すすめた記事・次に困りそうなこと・つなぐ1行・誘導文と字数）と、`related-map.md` の今回の行を日本語で短く報告する。
