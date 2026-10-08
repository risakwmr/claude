# YouTube representative

One voice for every scheduled run, automation and agent around the channel. You talk to it in a GitHub issue from your phone.

```
                 ┌──────────── listeners (no AI) ────────────┐
 GitHub Actions ─┤ pipeline  runs of every workflow, failures │
 episodes branch ┤ channel   uploaded / scheduled / waiting,  │
                 │           thumbnails, views and likes      │
 YouTube API ────┤ audience  new viewer comments              │
 main branch ────┤ note      note.com draft pipeline          │
                 └─────────────────────┬──────────────────────┘
                                       ▼
            ┌────────── specialist agents (in parallel) ──────────┐
            │ ops       is everything healthy? what needs you?    │
            │ audience  sorts comments, drafts replies            │
            │ growth    what the numbers say, one idea to try     │
            │ pronunciation  Japanese words to check by ear       │
            └─────────────────────┬───────────────────────────────┘
                                  ▼
                  representative: one brief, answers your questions
                                  ▼
                 issue "📮 YouTube representative" (phone notification)
```

## What it does

- **Every morning at 07:30 JST** it checks everything, and **posts only when something needs you** (a failure, a blocker, new comment replies to approve, or Japanese words to check by ear). On quiet days it posts nothing and keeps the brief on the `rep-data` branch. Set the variable `REP_NOTIFY` = `always` for a post every day. When it does post, the brief has what went well, what needs you (with the exact next step), what is scheduled next, what viewers said with reply drafts, and the numbers.
- **Japanese pronunciation**: it reads the scripts of the episodes not made yet and finds Japanese words and names that `episodes/pronunciations.json` has no respelling for (e.g. *gaman*, *kashikomarimashita*). It tells you once when it first finds them, and once more when their episode is next in line, with 3-5 respelling candidates to try in the `voicetest` action.
- **Ask it anything** by commenting in the issue, e.g. 「昨日のShortsどうだった？」「次のエピソードはいつ公開？」「なんで止まってるの？」. It answers from the live state of the channel and the latest reports.
- **Comment replies are never posted on their own.** Each draft has an id like `c3`:
  - `/reply all` posts every draft except the ones flagged for your judgment
  - `/reply c1 c3` posts those drafts
  - `/edit c4 your own text` posts your text instead
  - `/skip c2` drops a draft

Only the repository owner's comments wake it, so nobody else can spend the API budget or post replies.

## Set up (once)

1. Settings → Secrets and variables → Actions → **Secrets**: add `ANTHROPIC_API_KEY` (from console.anthropic.com). The YouTube secrets are the ones the episode workflow already uses.
2. **Variables**: add `REPRESENTATIVE` = `true` to turn on the daily brief.
3. To try it now: Actions → **YouTube representative** → Run workflow → `brief`. The first run creates the issue; pin it if you like.

Replying to comments needs the YouTube refresh token to have the `youtube.force-ssl` scope; it already does if the episode workflow's question comments work.

## Where things are kept

The `rep-data` branch: `briefs/` (every brief), `inbox.json` (reply drafts waiting), `sent_replies.json`, `seen_comments.json`, and the last numbers so the next brief can say what changed.

## Cost

Each brief is five calls to the model (`REP_MODEL`, default `claude-opus-5-5`); each question is one call. YouTube quota: about 2 units per brief, 50 per posted reply.
