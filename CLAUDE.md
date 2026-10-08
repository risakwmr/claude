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
- Thumbnails: `episodes/epNN_thumbnail.png` on the `episodes` branch, made with ChatGPT. **Use the template in
  `representative/thumbnail_template.md`** (the look of EP14 and EP18: cream torn-paper panel, big navy serif title,
  coral EPISODE banner, book stack with the authors, pink sticky note, sunny watercolor Sena with handwritten notes).
  The reference thumbnails (EP14, EP18, EP19) are in the source files of the owner's ChatGPT project: prompts say
  "use the reference thumbnails in this project's source files" instead of asking to attach images.
  Not the "v2 magazine" rules in `episodes/thumbnail_rules.md`: the owner doesn't want that look.
  Upload page: https://github.com/risakwmr/claude/upload/episodes/episodes
- Japanese respellings for the English voices: `episodes/pronunciations.json` on the `episodes` branch.
- note.com drafts: `note-pipeline/` and `drafts/`.
