# Human Curriculum

An English audiobook about the skills AI can't do for you, turned into YouTube videos automatically.
Sena (Associate, Tokyo) learns from her mentor Daniel (People Manager, Seattle).

## What happens

1. `episodes/epNN.txt` holds the script, one line per turn: `SENA: ...` or `DANIEL: ...`
2. Each line is voiced (Sena: female US English voice, Daniel: male US English voice)
3. A 1080p video is drawn in the show's paper-and-brush style: both character cards, the speaker's card lifts and shows sound bars, subtitles at the bottom
4. A thumbnail is drawn (or your own `episodes/epNN_thumbnail.png` is used as-is)
5. The video is uploaded to YouTube as **scheduled** (goes public by itself at 00:00 or 12:00 JST) with its thumbnail

## Character art

Put your illustrations in `assets/characters/`:
- `sena.png`, `daniel.png` (square works best; the face should be in the upper half)
- optional `sena_talk.png`, `daniel_talk.png` (mouth open) — the card switches to it while speaking

## Run it from your phone

GitHub (browser) → this repository → **Actions** → **Make and upload episodes** → **Run workflow**

- `episode`: `1`, `1,2`, or `next`
- `action`: `make` = make the video only (download it from the run page under **Artifacts**); `upload` = also upload to YouTube; `reschedule` = give already uploaded private episodes publish times, one per slot in the order listed (e.g. `1,2,3`); `thumbnail` = replace the thumbnails of uploaded episodes
- `visibility` (for upload): `schedule` = next free 00:00 / 12:00 JST slot, `public` = right away, `private`

Rendering a 15-minute episode takes about 10 minutes.

## Daily automatic posting

Settings → Secrets and variables → Actions → **Variables** → New variable: `AUTO_UPLOAD` = `true`.
Twice a day (at 21:00 and 09:00 Japan time) a run checks the queue. Episodes go public one at a time, in order, at 00:00 and 12:00 JST; when the next free slot is the coming one, the next unpublished episode is made and uploaded with that publish time, otherwise the run waits. If GitHub starts a run too late for its slot, that episode goes public as soon as it is uploaded.
`published.json` keeps track of what has been uploaded.

## Add an episode

1. Add `episodes/ep02.txt`
2. Add its entry to `episodes/episodes.json` (title, short_title, summary, practice, sources, tags)

## Secrets (Settings → Secrets and variables → Actions)

`CLIENT_ID`, `CLIENT_SECRET`, `REFRESH_TOKEN` (the refresh token must be created while signed in to the channel you want to post to).

## Change the voices

Add repository variables `SENA_VOICE` / `DANIEL_VOICE` with any Microsoft Edge neural voice name (default: `en-US-AvaNeural` / `en-US-AndrewNeural`).

## Notes

- Videos from unverified Google Cloud apps can be locked to private until Google's audit (this channel is not affected as of Oct 2026).
- Custom thumbnails need a phone-verified channel (youtube.com/verify).
- Fonts: Inter and Lora (SIL Open Font License), TeX Gyre Chorus (GUST Font License). See `assets/fonts/`.

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
- The description starts with the full-episode link, but links in Shorts can't be clicked. To make one clickable, set **Related video** to the full episode in YouTube Studio (the YouTube API can't set it); the representative sends the Studio link for each new Short. `shorts.json` keeps track of uploaded Shorts.
- By hand: **Run workflow** → `action`: `short_make` (build only, download from **Artifacts**) or `short` (build and upload); `episode`: a number like `14`, or `next`; `short_kind`: one kind or `all`.
- Stats: every scheduled run saves views and likes of each Short to `shorts_stats.json` (summed up by kind in the run summary); run `action`: `stats` to get them now. Retention ("viewed vs swiped away") is only in YouTube Studio.
