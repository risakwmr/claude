# Human Curriculum

An English audiobook about the skills AI can't do for you, turned into YouTube videos automatically.
Sena (Associate, Tokyo) learns from her mentor Daniel (People Manager, Seattle).

## What happens

1. `episodes/epNN.txt` holds the script, one line per turn: `SENA: ...` or `DANIEL: ...`
2. Each line is voiced (Sena: female US English voice, Daniel: male US English voice)
3. A 1080p video is drawn in the show's paper-and-brush style: both character cards, the speaker's card lifts and shows sound bars, subtitles at the bottom
4. A thumbnail is drawn (or your own `episodes/epNN_thumbnail.png` is used as-is)
5. The video is uploaded to YouTube as **private** with its thumbnail

## Character art

Put your illustrations in `assets/characters/`:
- `sena.png`, `daniel.png` (square works best; the face should be in the upper half)
- optional `sena_talk.png`, `daniel_talk.png` (mouth open) — the card switches to it while speaking

## Run it from your phone

GitHub (browser) → this repository → **Actions** → **Make and upload episodes** → **Run workflow**

- `episode`: `1`, `1,2`, or `next`
- `upload`: off = make the video only (download it from the run page under **Artifacts**); on = also upload to YouTube

Rendering a 15-minute episode takes about 10 minutes.

## Daily automatic posting

Settings → Secrets and variables → Actions → **Variables** → New variable: `AUTO_UPLOAD` = `true`.
Every day at 09:00 Japan time, the next two unpublished episodes are made and uploaded.
`published.json` keeps track of what has been uploaded.

## Add an episode

1. Add `episodes/ep02.txt`
2. Add its entry to `episodes/episodes.json` (title, short_title, summary, practice, sources, tags)
3. Optional thumbnail fields: `thumb_title`, `thumb_sub`, `thumb_accent` (coral italic word), `thumb_notes` (3–4 handwritten keywords), `thumb_cup`, `thumb_note`, `thumb_character`. The book spines show the first three `sources`.

## Secrets (Settings → Secrets and variables → Actions)

`CLIENT_ID`, `CLIENT_SECRET`, `REFRESH_TOKEN` (the refresh token must be created while signed in to the channel you want to post to).

## Change the voices

Add repository variables `SENA_VOICE` / `DANIEL_VOICE` with any Microsoft Edge neural voice name (default: `en-US-AvaNeural` / `en-US-AndrewNeural`).

## Notes

- Videos from unverified Google Cloud apps stay private until Google's audit; switch them to public in YouTube Studio.
- Custom thumbnails need a phone-verified channel (youtube.com/verify).
- Fonts: Inter and Lora (SIL Open Font License), TeX Gyre Chorus (GUST Font License). See `assets/fonts/`.

## Visual layout (from episode 14)

If `episodes/epNN.visual.json` exists, the video uses the visual layout: full-body poses for Sena and Daniel
(`assets/characters/full/`, the art may be mirrored), a center board with big keywords, research cards,
Japan/US comparisons, lists and today's challenge, free illustrations (Fluent Emoji 3D by Microsoft, MIT License,
names in `assets/icons/INDEX.txt`, downloaded by `src/fetch_icons.py`), section names that also become YouTube
chapters, and a short silent "your turn" countdown after each Speaking Lab repeat. The cue format is described at the
top of `src/scenes.py`.

## Shorts

Every episode also becomes up to four vertical YouTube Shorts (1080×1920): a big hook line at the top, the center board, Sena and Daniel, and large captions, ending on a "Full episode on the channel" card.

| Kind | What it is |
| --- | --- |
| `ai` | "Why can't AI do this?" (every episode) |
| `story` | Daniel's failure story |
| `culture` | Japan vs the US |
| `lab` | Speaking Lab: the phrases, with a silent "your turn" countdown (episode 12 on) |

- What goes in: `episodes/epNN.short.json` (per kind: line range, hook, title, optional board; the format is at the top of `src/make_short.py`). A kind missing from that file is cut automatically when the episode has that part, so new episodes get their Shorts with no extra work.
- When: the twice-daily runs queue one Short per slot. Shorts go public at **08:00, 18:00 and 22:00 JST** (US evening / India and Southeast Asia afternoon / US morning and Europe afternoon). The order mixes kinds and episodes, and a Short only goes up once its episode is public, so the link works. Change the times with the repository variable `SHORT_SLOTS_JST` (e.g. `8,18`), or stop automatic Shorts with `AUTO_SHORTS` = `false`.
- The description starts with the full-episode link, and once a Short is public a comment with the same link is added (you can pin it in YouTube Studio). `shorts.json` keeps track of uploaded Shorts.
- By hand: **Run workflow** → `action`: `short_make` (build only, download from **Artifacts**) or `short` (build and upload); `episode`: a number like `14`, or `next`; `short_kind`: one kind or `all`.
- Stats: every scheduled run saves views and likes of each Short to `shorts_stats.json` (summed up by kind in the run summary); run `action`: `stats` to get them now. Retention ("viewed vs swiped away") is only in YouTube Studio.
