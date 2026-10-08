---
name: note-themes
description: 有料note向けのテーマを15個探して note-pipeline/theme-bank.md に追加する（note-theme-researcher を呼ぶ）。「有料noteのテーマを出して」「テーマの在庫を増やして」「/note-themes」のとき。
---

1. `claude/vigilant-gates-tewzrg` ブランチにいることを確かめる（`note-pipeline/PROMPT.md` の0. 準備）。
2. Agent（subagent_type: `note-theme-researcher`）を呼び、`note-pipeline/theme-bank.md` に15個追加させる。引数（$ARGUMENTS）があれば、テーマの方向性の指定として渡す。
3. コミットしてpushする（例：`note themes: 2026-10-09 — 15 paid-note themes`）。
4. SendUserFile で `note-pipeline/theme-bank.md` を送り（status: normal、display: render）、追加したテーマ名15個と、検索されている根拠を確かめられた数を日本語で短く報告する。
