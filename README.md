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

## Secrets (Settings → Secrets and variables → Actions)

`CLIENT_ID`, `CLIENT_SECRET`, `REFRESH_TOKEN` (the refresh token must be created while signed in to the channel you want to post to).

## Change the voices

Add repository variables `SENA_VOICE` / `DANIEL_VOICE` with any Microsoft Edge neural voice name (default: `en-US-AvaNeural` / `en-US-AndrewNeural`).

## Notes

- Videos from unverified Google Cloud apps stay private until Google's audit; switch them to public in YouTube Studio.
- Custom thumbnails need a phone-verified channel (youtube.com/verify).
- Fonts: Inter and Lora (SIL Open Font License), TeX Gyre Chorus (GUST Font License). See `assets/fonts/`.
