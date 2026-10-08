# Notes for Claude

## How the owner wants to be told things

- Notify only when the owner has to act. No "checked, nothing changed" messages.
- The owner forgets easily. Every reminder or action item carries everything needed to do it right away:
  the direct link (file, upload page, workflow run, video) and any text to paste (ChatGPT prompt, brief, reply, JSON line).
  For Japanese pronunciation, also send an audio sample of the candidate spellings in Sena's voice.
- Reply in Japanese, casual and warm.

The YouTube representative (`representative/`) follows the same rules in its briefs.

## Where things are

- YouTube episodes, Shorts and their state files: the `episodes` branch (workflow `.github/workflows/episodes.yml` checks it out).
- Thumbnails: `episodes/epNN_thumbnail.png` on the `episodes` branch, made with ChatGPT from `episodes/thumbnail_rules.md`
  (section 12 is the per-episode brief). Upload page: https://github.com/risakwmr/claude/upload/episodes/episodes
- Japanese respellings for the English voices: `episodes/pronunciations.json` on the `episodes` branch.
- note.com drafts: `note-pipeline/` and `drafts/`.
