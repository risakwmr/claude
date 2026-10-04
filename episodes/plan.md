# Human Curriculum — Episode plan (730 episodes, one year)

Whole-show theme: the human skills AI can't do for you, and growing EQ, with cross-functional (xFN) collaboration, work efficiency, behavioral economics, marketing, data, writing, and English speaking.
Posting pace: 2 episodes a day (00:00 and 12:00 JST), 730 episodes = one year. The listener grows together with Sena, day by day.
Format of each line: `NN Title | EQ domain | today's challenge (Japanese note for the writer)`.
From episode 12 on, each episode ends with a **one-day challenge**: something the listener can do at work TODAY (not "this week"). The next episode opens by asking how the challenge went.
Every episode also has a short **Speaking Lab** before the challenge (see the routine prompt). Research ideas with verified sources are in `episodes/ideas.md`.
Each episode's teaser points to the next line in this file. The last episode of each season closes the season and teases the next season's first episode. Only episode 730 ends the show.

## Story arc (keep continuity)
- The 730 episodes are one year of Sena's life (two sessions with Daniel a day in show time is fine; keep time passing naturally, about half a day per episode): from Associate in Tokyo to Program Manager in Seattle. People manager is her next goal after that, teased in the finale.
- She stays an Associate (IC) in Tokyo until she gets the offer for a Program Manager role on a Seattle team (episode 721). She says goodbye and hands off her Tokyo work (722–723), moves to Seattle (725) and starts as a Program Manager (725–730). She never has direct reports in this show.
- Season 1–4 (1–60): everyday IC work in Tokyo. Manager Kato-san, teammate Ryo, PM Mark and director Laura in Seattle. Season 3 focuses on speaking English at work (Sena's speaking is weaker than her listening; it slowly improves over the year).
- Season 5–6 (61–90): as an Associate, Sena leads her first small cross-team project, without a title or authority, and works closely with engineering, product, data and design.
- Season 7–10 (91–150): change and influence; behavioral economics for work and marketing (Sena helps a marketing launch); focus and efficiency.
- Season 11–46 (151–695): data, marketing, writing, presenting, negotiation, thinking, product, execution, global teams, networking, AI, resilience, listening, coaching, customer research, growth, finance, strategy, executive communication, process, motivation, learning, ethics, creativity, facilitation, advanced speaking, remote work, US career strategy, program management, and preparing for people management. Sena takes on bigger cross-team work in Tokyo and builds relationships in Seattle.
- Season 47 (696–710): thinking like a Program Manager; a one-week business trip to Seattle (she still lives and works in Tokyo).
- Season 48 (711–730): the road to the Seattle Program Manager role: her case, sponsor, interviews, the offer, goodbye to Tokyo, the move, the first weeks, and the finale.
- Time passes naturally (seasons change, holidays come). New side characters get new names; never reuse earlier side characters' names for new people.
Daniel stays a senior People Manager in Seattle (team of 8) and Sena's mentor. Daniel's failure stories must not repeat earlier ones.

## Storytelling (from episode 16; follow this together with the routine's script rules)
The show should feel like a story people want to follow, not a lecture. Same format (only SENA and DANIEL lines), but more drama between and around them.
- Cold open (first 4–8 lines, about 20–40 seconds, BEFORE "Welcome back to Human Curriculum"): drop the listener straight into today's moment. Sena (or Daniel) describes the scene vividly in the present tense, with the exact words someone said quoted, and the tension unresolved. Daniel's last cold-open line promises, in one plain sentence, what the listener will be able to do by the end ("By the end of this episode, you'll have three sentences for..."). No exaggeration, no fake numbers. Then the usual "Welcome back" and the recap of last time's challenge. In epNN.visual.json give these lines the section "Cold open" with a keyword board; the "Last time" section starts at the "Welcome back" line.
- Scenes, not summaries: when Sena retells something, she replays it as a small scene: where she was, what she saw (a look, a pause, a message popping up), and the other person's words in quotes. Side characters come alive through these quoted lines.
- Running threads: keep 2–3 small story threads alive across episodes besides the topic (e.g. Ryo's overwork, Kenta slowly finding his voice, Kato-san's packed calendar, Mark's late-night requests, Sena's English speaking practice, her city-walk photos). Each episode moves at least one thread forward a little, and threads pay off later. Note new threads in this file under "Open threads" so later episodes can pick them up.
- Two people, not a Q&A: Sena pushes back sometimes, jokes, gets things wrong and corrects herself; Daniel has moments from his own week (Maple, a hike, a hard day with his team) that connect to the topic. Small, warm, specific.
- Cliffhanger teaser: the "Next time" part ends on a concrete unresolved moment ("And then Kato-san's message said: 'Can we talk tomorrow? Just you and me.'"), not only the next title.
- Short-ready moment (every episode): write 1 funny or very relatable moment that works on its own as a 20–45 second YouTube Short with no context: a clear setup, a turn, and a punchline or a line people will want to send to a friend (e.g. Sena rehearsing a message out loud and getting it wrong three ways, Daniel's dog Maple "reviewing" his slides, Mark's emoji-only reply at 2 a.m.). 3–8 lines, both characters speaking, no research in it, and it must still fit the episode's topic and stay kind (laugh with people, not at them). Then add it to episodes/epNN.short.json as a "scene" Short (create the file if missing): {"shorts": [{"kind": "scene", "lines": [first, last], "hook": "<a 6–12 word line that makes people stop scrolling, e.g. 'When your manager says \"quick question\" at 6 p.m.'>", "title": "<YouTube title, plain words, under 60 characters>"}]}. Line numbers are 1-based and inclusive; check them with python. The other Short kinds (ai, story, culture, lab) are cut automatically, so only add them to the file when you want a better hook.
- Keep honesty rules: research is reported with its limits, and the drama never invents facts about real people or studies.

## Open threads
- (add threads here as they start, with the episode number, and mark them resolved with the episode that pays them off)

## Characters (fixed settings; use details lightly and keep them consistent)
Character map image: `episodes/character_map.png`.
- Sena Sato: Associate (IC), Tokyo. Data analysis; built the monthly report pipeline (2 days by hand → about 1 hour), now launching the regional dashboard. Careful, reads the room, always takes notes; strong analysis, emails sometimes too polite. Denies praise ("no, no"). Speaking weaker than listening. Goal: Program Manager in Seattle, then people manager. Hobby: city walks and photography (gets off at unfamiliar stations, shoots alleys and signs). Quirk: has used the same notebook model for 20 notebooks.
- Daniel Reed: Senior People Manager, Seattle, team of 8. Sena's mentor. Warm, direct, loves research, tells his own failures honestly. Promoted from inside his own team. Grew up in the US, married. Hobby: weekend hiking; walks with his golden retriever Maple (navy bandana). Quirk: navy mug was a gift from an old team; bad cook, hooked on Japanese curry roux.
- Kato-san: Sena's manager (40s). Former analyst; calendar packed with budget, hiring, Seattle calls, escalations. Never asks for help; sometimes nods plans through; knows he struggles to name people's work specifically. Hobby: running around the Imperial Palace (track team in college). Quirk: canned-coffee person; helps his elementary-school daughter with homework.
- Ryo: teammate (late 20s). Presents the monthly report; kind and meticulous; wrote the automatic data-check script; lately overworking and tired. Hobby: board games, building small handy tools. Quirk: morning person; very careful commit messages.
- Kenta: teammate who reviews Sena's analysis (early 30s). Quiet and detailed; notices problems first but often starts to speak and stops. Hobby: shogi (one online game at lunch).
- Mark: product manager, Seattle. Requests Sena's reports; urgent asks arrive in Sena's evening because of the time difference. Hobby: home coffee roasting, watching soccer on weekends. Quirk: replies on Slack instantly, lots of emoji.
- Laura: director, Seattle, over several teams including Sena's; Kato-san's boss. Will matter later for Sena's career (sponsor arc). Hobby: gardening, classical music (played cello when young). Quirk: always ends meetings with "What did we decide?"
- Hannah: data platform team lead, Seattle. Sena asks her team for data changes. Hobby: rock climbing. Quirk: always busy, but can't resist a well-made request.
- Daniel's past (stories already told; don't reuse the names for new people): Priya (ep6), Yuki (ep7), Elena (ep9), Tom (ep10), Mei (ep11), Owen (ep12), Rafael (ep13), Grace (ep14), Theo (ep15).

## Season 1 — Foundations (1–15)
1 Meet Sena and Daniel: What AI Can't Do for You | All four | (published)
2 Interoceptive Awareness: The 30-Second Window | Self-awareness | (published)
3 Ownership: Acting Like It's Yours | Self-management | 頼まれていない「やりかけ」を1つ閉じる
4 Naming Emotions: Beyond "Fine" | Self-awareness | 1日3回、今の感情をできるだけ正確に名前にする
5 Asking for Feedback (and Using It) | Self-management | 「改善できる点を1つ教えて」と聞き、ありがとうだけ言う
6 Making Your 1:1 Count | Relationship management | 1on1に質問1つと近況1つを持っていく
7 Say It Clearly: Low-Context Communication | Social awareness | メッセージを1通、結論→詳細の順に書き直す
8 Making Your Work Visible | Relationship management | 3行の週次アップデートを送る
9 Earning Trust with Peers | Relationship management | 小さな約束を1つ期限どおりに守る
10 Influence Without Authority | Social awareness | 他チームに「何が必要か」を先に聞く
11 Speaking Up When You Disagree | Self-management | 会議で一度「I see it differently」と言う
12 What Changes When You Lead | Self-awareness | マネージャーに一番驚いたことを聞く
13 Giving Feedback with SBI | Relationship management | SBI(状況・行動・影響)で1つ褒める
14 Building Psychological Safety | Social awareness | 自分の小さな失敗を先に話す
15 The Hard Conversation | All four | 伝えたいことを一文で書き、「How are you, really?」と聞く(シーズン1のしめくくり。番組は続く)

## Season 2 — Emotions at Work (16–30)
16 When You Make a Mistake | Self-management | ミスを1つ、事実・影響・次の一手の3文で報告する
17 Stress Is a Signal | Self-awareness | ストレスを感じた瞬間に体のサインを1つメモする
18 Nerves Before You Speak | Self-management | 発表の前に「I'm excited」と言い換えて臨む
19 Anger Without Damage | Self-management | イラッとしたら返信を20分寝かせる
20 Disappointment and Bouncing Back | Self-management | うまくいかなかったことから学びを1つ書き出す
21 Envy as Information | Self-awareness | うらやましいと感じた相手から「欲しいもの」を1つ言葉にする
22 Impostor Feelings | Self-awareness | 自分の成果の証拠を3つ書き出す
23 Saying No Without Burning Bridges | Relationship management | 代わりの案を添えて1つ断る
24 Switching Off After Work | Self-management | 仕事の終わりに明日の最初の一歩を書いてPCを閉じる
25 Perfectionism vs. Good Enough | Self-management | 1つの仕事を「8割で出す」と決めて期限前に出す
26 Self-Compassion at Work | Self-awareness | 失敗した日に友人にかけるのと同じ言葉を自分に書く
27 Reading Emotions on a Video Call | Social awareness | 会議で1人の様子に気づき、あとで一言声をかける
28 Staying Calm When Others Aren't | Relationship management | 相手が感情的なとき、まず相手の言葉を言い換えて返す
29 Gratitude That Isn't Generic | Relationship management | 具体的な感謝のメッセージを1通送る
30 Your Emotional Baseline | All four | 1週間の気分を1日1語で記録して振り返る(シーズン2のしめくくり)

## Season 3 — Speaking Up in English at Work (31–45)
31 Small Talk Is Not Small | Relationship management | 会議の最初の2分で相手に質問を1つ、続けてフォローアップの質問も1つする
32 Thinking in English, Not Translating | Self-management | 今日の予定を英語で声に出して3回説明する(2分→1分半→1分)
33 Chunks That Buy You Time | Self-management | 会議で使う決まり文句を5つ選び、今日1つ使う
34 Asking Clarifying Questions | Social awareness | 「Just to make sure I understand…」で1回確認する
35 Interrupting Politely | Self-management | 会議で一度「Can I add something?」と入る
36 Listen, Summarize, Then Speak | Social awareness | 相手の話を一言で要約してから自分の意見を言う
37 Retell in 30 Seconds | Self-awareness | 今日の会議の要点を30秒で声に出して要約し、録音する
38 Speaking Before You Feel Ready | Self-management | 英語の会議で最初の1分以内に一言話す(前後の緊張を1〜10で記録)
39 Presenting with a Story | Relationship management | 発表の冒頭を具体的な場面1つで始める
40 Pushing Back on Deadlines | Relationship management | 期限について代案を添えて交渉する
41 Saying "I Don't Know" | Self-awareness | 「I don't know yet, I'll find out by…」と1回言う
42 Running a Short Meeting in English | Relationship management | 目的・決めたいこと・時間を最初に言って会議を始める
43 Learning from Your Own Recording | Self-awareness | 2分の発言を録音して書き起こし、直して録り直す
44 Speaking with Senior Leaders | Self-management | 上の立場の人に話す前に結論を1文で用意して声に出す
45 Finding Your Voice in English | All four | 1か月前の録音と今日の録音を聞き比べる(シーズン3のしめくくり)

## Season 4 — Growing Your Career (46–60)
46 The Career Conversation | Self-awareness | マネージャーに「1年後どうなっていたいか」を話す
47 Mentors and Sponsors | Relationship management | 自分を推薦してくれそうな人を1人書き出す
48 Networking Without Feeling Fake | Relationship management | 他部署の人に15分のコーヒーチャットを頼む
49 Your Strengths, Named | Self-awareness | 周りの3人に「私の強みは?」と聞く
50 Learning Fast | Self-management | 新しいことを学んだら24時間以内に人に説明する
51 Job Crafting | Self-management | 今の仕事の中で好きな部分を1つ増やす工夫をする
52 Building Your Promotion Case | Relationship management | 成果と影響を5行でまとめる
53 Handling Rejection | Self-management | 断られた経験から次に変えることを1つ決める
54 Choosing What Not to Do | Self-awareness | やめることリストに1つ書く
55 Interviewing with Confidence | Self-management | STAR形式で自分の話を1つ準備する
56 Talking About Pay | Self-awareness | 自分の市場価値を調べ、話す内容を一文にする
57 Working with a New Manager | Relationship management | 新しい上司に「どう働くのが好きか」を聞く
58 Reputation Is Built Slowly | Social awareness | 自分が人からどう見られたいかを3語で書く
59 Taking a Stretch Assignment | Self-management | 少し背伸びする仕事に1つ手を挙げる
60 Your Five-Year Story | All four | 5年後の自分を1段落で書き、1人に話す(シーズン4のしめくくり)

## Season 5 — Leading a Project Without the Title (61–75)
61 Your First Project to Lead | Self-awareness | 任されたプロジェクトで不安なことと楽しみなことを1つずつ書く
62 Defining the Problem Before the Plan | Social awareness | 関係者3人に「このプロジェクトで何が変われば成功か」を聞く
63 The Kickoff Meeting | Relationship management | キックオフで目的・範囲・決め方を最初の5分で伝える
64 Scope: What's In and What's Out | Self-management | 「今回やらないこと」を3つ書いて共有する
65 Roles and Who Decides | Relationship management | 誰が決めて誰に相談するかを1枚の表にする
66 Estimating Honestly | Self-awareness | 見積もりに「自信の度合い」を添えて出す
67 A Plan People Can Read | Social awareness | 計画を相手が1分で読める形にまとめ直す
68 Status Updates Without Spin | Relationship management | 赤・黄・緑の状況を理由付きで正直に報告する
69 Spotting Risk Early | Self-management | 心配なことを毎週1つリスクとして書き出す
70 Dependencies on Other Teams | Relationship management | 依存先のチームと期限を一緒に確認する
71 Scope Creep and the Kind No | Relationship management | 追加の依頼に「やるなら何を後ろにするか」を聞く
72 When the Project Slips | Self-management | 遅れを分かった日のうちに代案と一緒に伝える
73 Keeping the Team Motivated Without Authority | Social awareness | プロジェクトのメンバーに貢献を1つずつ伝える
74 Launch Day | All four | リリースの日に関わった人全員に一言お礼を送る
75 The Retrospective | All four | うまくいったこと・変えること・続けることを1つずつ書く(シーズン5のしめくくり)

## Season 6 — Working Across Teams (76–90)
76 Shared Goals, Different Priorities | Social awareness | 相手チームの今期の目標を調べて自分の依頼とつなげる
77 Meetings That Decide Something | Self-management | 会議の招待に「この会議で決めること」を1行書く
78 Writing It Down: Decision Logs | Relationship management | 決まったことと理由を1か所に記録する
79 Translating Between Business and Engineering | Social awareness | 技術の話をビジネスの言葉で1文に言い換える
80 Earning Trust with Engineers | Relationship management | エンジニアに「今いちばん困っていること」を聞く
81 Escalating Well | Self-management | エスカレーションの前に相手と事実をそろえる
82 Conflicting Requests | Relationship management | 2つの依頼がぶつかったら両方の依頼者を同じ場に呼ぶ
83 Consensus vs. Consent | Social awareness | 「全員賛成」ではなく「反対はないか」で決めてみる
84 Async Collaboration Across Time Zones | Self-management | 返事を待たなくても進める書き方で依頼を1つ送る
85 When a Partner Team Misses a Date | Self-management | 責める前に何が起きたかを質問で確かめる
86 Including Quiet Voices | Social awareness | 会議で話していない人に意見を聞く
87 Credit and Ownership Across Teams | Relationship management | 他チームの貢献を報告の中で名前付きで伝える
88 Repairing a Cross-Team Misunderstanding | Relationship management | こじれた相手に短く連絡して話す時間をもらう
89 Show, Don't Describe | Social awareness | 次の他部署との話し合いに画面・サンプルなど実物を持っていく
90 The Connector | All four | 自分がつないだ人と人を3組書き出す(シーズン6のしめくくり)

## Season 7 — Change and Ambiguity (91–105)
91 Why Change Feels Like Loss | Social awareness | 変化で失うものを相手の立場で1つ書く
92 Explaining a Change You Didn't Choose | Relationship management | 理由・変わること・変わらないことを3行で伝える
93 Working in Ambiguity | Self-management | 分からないことを「分かっていること・いないこと」に分ける
94 Delivering Bad News on a Project | Relationship management | 悪い知らせを最初の一文で伝える練習をする
95 Reorganizations | Social awareness | 組織変更で不安そうな同僚に声をかける
96 When Priorities Change Mid-Way | Self-management | 中断した仕事の区切りを1行で残す
97 Pushing Back on Leadership | Relationship management | 優先順位を見せて上に相談する
98 Keeping Spirits Up in Hard Times | Relationship management | 大変な時期にチームの小さな成功を1つ伝える
99 Your Own Resistance to Change | Self-awareness | 自分が抵抗している変化を1つ認める
100 Incidents and Crisis Mode | Self-management | 緊急時の最初の3つの行動を決めておく
101 Communicating Uncertainty | Relationship management | 「まだ決まっていない」ことを正直に伝える
102 When Colleagues Leave | Social awareness | 去る人と残る人の両方に声をかける
103 Blameless Reviews | Self-management | 振り返りを責めずに事実で書く
104 Disagree and Commit | Self-management | 意見を伝えたあと、決まったことを支える言い方を考える
105 Steady in the Storm | All four | 変化の中で自分を保つ習慣を1つ決める(シーズン7のしめくくり)

## Season 8 — Influence and Stakeholders (106–120)
106 Managing Up | Relationship management | 上司の優先事項を3つ書き出して確認する
107 Mapping Your Stakeholders | Social awareness | 関係者を1枚の図にする
108 Pre-Wiring a Decision | Relationship management | 会議の前に1人に個別に相談する
109 Presenting to Executives | Self-management | 説明を「結論・理由・お願い」の3枚にする
110 Executive Presence | Self-awareness | 自分の話し方を録音して1つ直す
111 Negotiation Basics | Social awareness | 相手の本当の関心を1つ質問で探る
112 Building a Coalition | Relationship management | 同じ課題を持つ人を2人見つける
113 Persuasion with Integrity | Self-awareness | 説得の前に自分に不利な事実も1つ書く
114 Handling a Difficult Stakeholder | Self-management | 苦手な相手との会話の前に目的を1文で決める
115 Running a Steering Meeting | Relationship management | 判断してほしいことを会議の最初に示す
116 Asking for Resources | Relationship management | 必要なものと理由と効果を3行で頼む
117 When You Lose the Argument | Self-management | 負けた議論から学びを1つ書く
118 Saying the Uncomfortable Thing to a Senior Person | Self-management | 上の立場の人に懸念を1つ事実で伝える
119 Influence Through Listening | Social awareness | 説得したい相手の話を10分だけ聞く
120 Your Influence Map | All four | 半年で信頼を築いた相手を振り返る(シーズン8のしめくくり)

## Season 9 — Behavioral Economics at Work and in Marketing (121–135)
121 Why People Don't Decide Like Spreadsheets | Social awareness | 今日の自分の選択で「理屈どおりでなかった」ものを1つ書く
122 Anchors in Every Meeting | Self-awareness | 見積もりの話し合いの前に自分の数字を先に書いておく
123 Framing: Same Facts, Different Story | Social awareness | 提案の1文を「得る」言い方と「失う」言い方で書き比べて選ぶ
124 Loss Aversion and Resistance to Change | Social awareness | 変化に反対する人に「何を失うと感じるか」を聞く
125 The Power of Defaults | Relationship management | 自分のテンプレートや招待で、望ましい行動を初期設定にする
126 Too Many Options? | Self-management | 選択肢を3つに絞って1つを推す(本当に絞るべき場面か先に確かめる)
127 Decoys and Honest Pricing | Self-awareness | 3段階の案を作り、真ん中の案が相手の役に立っているか確かめる
128 Mental Accounting and Reference Points | Social awareness | 予算や価格の説明に、比べてほしい基準を1つ書く
129 Ownership and the Endowment Effect | Relationship management | 関係者に試してもらえる小さなパイロットを提案する
130 Sunk Costs | Self-management | 「今日ゼロから始めるならやるか?」を1つの仕事に問う
131 The IKEA Effect: Build It Together | Relationship management | 計画の一部(成功の指標など)を関係者と一緒に決める
132 Social Proof, Used Honestly | Social awareness | 依頼に本当の数字で「多くの人がもうやっている」を1つ添える
133 Peak-End: How People Remember | Relationship management | 会議やデモを一番いい瞬間で終える
134 Test, Don't Guess | Self-management | 2〜3案を小さく試して比べる計画を立てる
135 The Limits and Ethics of Nudges | All four | 使う前に「再現研究での効果」と「相手のためになるか」を確かめる(シーズン9のしめくくり)

## Season 10 — Focus, Efficiency and Energy (136–150)
136 Attention Residue | Self-management | 作業を切り替える前に「どこまでやって次は何か」を1行書く
137 Deep Work in a Shallow Day | Self-management | 通知を切って60分集中する
138 Interruptions and Breakpoints | Social awareness | 急ぎでない質問をまとめて、相手の区切りのいい時間に送る
139 Quiet Time for the Team | Relationship management | チームに90分の「声をかけない時間」を提案する
140 Email and Chat, Three Times a Day | Self-management | メールを決めた3回だけ確認する
141 If-Then Plans | Self-management | 今日の「もし〇〇なら△△する」を1つ書く
142 Beating the Planning Fallacy | Self-awareness | 作業を5つ以上に分けて見積もり、前回の実績と比べる
143 Urgent vs. Important | Self-awareness | 上位3つを「重要」か「急ぎなだけ」かに分け、重要なものから始める
144 Meetings That Earn Their Time | Relationship management | 次の定例を立って15分で終える
145 Collaboration Overload | Relationship management | よく来る依頼を1つ、ドキュメントやFAQで済む形にする
146 Breaks That Restore | Self-management | 90分ごとに5分画面から離れる
147 Rest Is Part of the Work | Self-management | 休む時間を予定に先に入れる
148 Values and Meaning at Work | Self-awareness | 自分の仕事が誰の役に立つかを1文で書く
149 When to Get Professional Support | Self-awareness | 相談できる窓口を1つ調べておく
150 A Sustainable Pace | All four | 3か月続けられる働き方を1枚にまとめる(シーズン10のしめくくり)

## Season 11 — Data Without Fear (151–165)
151 Numbers Tell Stories | Social awareness | 今日の会議で出た数字を1つ選び「だから何?」を1文で書く
152 Asking Good Questions of Data | Self-awareness | ダッシュボードを見て「なぜ?」を3回くり返す
153 Averages Hide People | Social awareness | 平均の数字の裏で一番困っている人を1人想像して書く
154 Correlation Is Not Causation | Self-awareness | 社内の「AだからB」を1つ見つけて別の説明を考える
155 One Metric That Matters | Self-management | 今のプロジェクトの指標を1つに絞って共有する
156 Charts People Understand | Social awareness | グラフ1つに「一言で分かる」見出しをつける
157 Leading and Lagging Indicators | Self-awareness | 結果の指標と、先に動く指標を1つずつ書く
158 A/B Testing Basics | Self-management | 小さく比べて試せることを1つ見つける
159 When Data and Gut Disagree | Self-awareness | 直感とデータが食い違う点を1つ書き、確かめ方を決める
160 Explaining Data to Executives | Relationship management | 数字の報告を「結論・根拠1つ・お願い」の3行にする
161 Data Ethics and Privacy | Social awareness | 扱うデータで「本人が知ったらどう思うか」を考える
162 Survey Questions That Work | Social awareness | アンケートの質問を1つ、誘導しない形に直す
163 Working with Analysts | Relationship management | アナリストに分析の目的と使い道を先に伝える
164 Uncertainty in Numbers | Self-management | 見積もりや予測に幅をつけて伝える
165 Your Data Story | All four | 今月の自分の仕事を数字1つと物語1つで話す(シーズン11のしめくくり)

## Season 12 — Marketing Fundamentals (166–180)
166 What Marketing Really Is | Social awareness | 自社の商品を一言で説明し、誰のためかを書く
167 Customer Empathy | Social awareness | お客さんの声(レビューや問い合わせ)を5件読む
168 Jobs to Be Done | Social awareness | お客さんが商品を「何のために使っているか」を1文で書く
169 Segments and Personas | Self-awareness | 一番大事なお客さん像を3行で書く
170 Positioning | Social awareness | 競合と比べた自社の違いを1文にする
171 The Customer Journey | Social awareness | 購入までの道のりで一番つまずく所を1つ見つける
172 The Funnel and Its Leaks | Self-management | ファネルの数字を見て一番漏れている段階を探す
173 Messaging That Lands | Relationship management | メッセージを1つ、お客さんの言葉で書き直す
174 Brand Is a Promise | Relationship management | ブランドの約束を守れていない場面を1つ探す
175 Pricing from the Customer's Side | Social awareness | 価格の見せ方を1つ、お客さんの立場で見直す
176 Launch Planning | Self-management | 発表までにやることを逆算して1枚にする
177 Working with Sales | Relationship management | 営業の人に「お客さんから一番聞かれること」を聞く
178 Measuring Marketing | Self-awareness | 施策の成果を何で測るかを先に決める
179 Marketing Ethics | Self-awareness | 広告や文言に誇張がないか1つ見直す
180 A Marketer's Mindset for Program Managers | All four | 自分のプロジェクトを「お客さんにとっての価値」で説明する(シーズン12のしめくくり)

## Season 13 — Writing at Work (181–195)
181 Writing Is Thinking | Self-management | まとまらない仕事を1つ、5文で書いてみる
182 The One-Page Memo | Self-management | 提案を1ページにまとめる
183 Writing for Busy Readers | Social awareness | 最初の2行だけで分かるメールを1通書く
184 Narratives vs. Slides | Relationship management | スライドの代わりに短い文章で説明してみる
185 Writing a Problem Statement | Self-awareness | 課題を「誰が・何に・なぜ困っているか」で書く
186 Requirements Without Ambiguity | Social awareness | あいまいな言葉(すぐ・たくさん)を数字に直す
187 FAQs That Prevent Meetings | Relationship management | よくある質問を3つ、答えつきで共有する
188 Editing Your Own Writing | Self-management | 送る前に文章を3割短くする
189 Polite and Clear in English | Social awareness | 英語のメールで丁寧さと分かりやすさを両立させる
190 Writing Bad News | Relationship management | 悪い知らせのメールを結論の一文から書く
191 Meeting Notes That Drive Action | Self-management | 会議メモに担当と期限を必ず入れる
192 Written Feedback | Relationship management | 文章でのフィードバックを1つ、具体例つきで書く
193 Docs as Influence | Relationship management | 自分の文書に意見をもらう人を1人増やす
194 AI as a Writing Partner | Self-awareness | AIに下書きを手伝わせ、自分の判断で直した点を書く
195 Your Writing Voice | All four | 1か月前の文章と今の文章を比べる(シーズン13のしめくくり)

## Season 14 — Presenting and Storytelling (196–210)
196 Story Structure at Work | Relationship management | 仕事の話を「状況・困難・変化」で1分で話す
197 Opening Lines That Hook | Self-management | 発表の最初の一文を3通り声に出して比べる
198 The Rule of Three | Self-management | 伝えたいことを3つに絞る
199 Slides That Support You | Social awareness | スライド1枚の文字を半分にする
200 Pace and Pauses | Self-management | 大事な一文の前に2秒の間を入れて話す
201 Handling Questions | Self-management | 想定質問を3つ用意して声に出して答える
202 When You Don't Understand the Question | Self-management | 「Could you rephrase that?」を声に出して練習し、使う
203 Presenting Online | Social awareness | オンライン発表でカメラを見て話す時間を増やす
204 Making Numbers Memorable | Relationship management | 数字を1つ、身近な例えで説明する
205 Persuasive Endings | Relationship management | 発表の最後に具体的なお願いを1つ入れる
206 Impromptu Speaking | Self-management | 急に振られた質問に「結論・理由・例」で答える
207 Nerves on Stage | Self-awareness | 発表前の体のサインに気づき、言い換えて臨む
208 Telling Your Mistakes Well | Relationship management | 自分の失敗談を1分で話す
209 Feedback on Your Talk | Self-awareness | 発表後に1人に「一番伝わった所」を聞く
210 Your Signature Talk | All four | 自分の得意な話を5分版にまとめて録音する(シーズン14のしめくくり)

## Season 15 — Negotiation and Conflict (211–225)
211 Negotiation Is Everyday Work | Social awareness | 今日の仕事の中の「交渉」を1つ見つける
212 Interests, Not Positions | Social awareness | 相手の要望の裏にある理由を1つ質問で探る
213 Your Walk-Away Option | Self-management | 交渉の前に「合意できなかったときの手」を書く
214 Expanding the Pie | Relationship management | お互いに得になる案を1つ考える
215 The First Number | Self-awareness | 交渉で最初に出す数字を準備する
216 Negotiating Across Cultures | Social awareness | 日本とアメリカの交渉の進め方の違いを1つ書く
217 When You Can't Say Yes | Self-management | 断るときに代わりにできることを1つ添える
218 When Emotions Run High | Self-management | 熱くなったら休憩を提案する言い方を準備する
219 Hard Conversations with Peers | Relationship management | 気になっていることを事実から話し始める
220 Mediating Between Two Teams | Social awareness | 2つのチームの言い分を1枚に並べて書く
221 Repairing After Conflict | Relationship management | 衝突のあとに一言連絡する
222 Negotiating for Yourself | Self-awareness | 自分のために交渉したいことを1つ書く
223 Fair Deals Build Trust | Relationship management | 合意内容が両者にとって公平か見直す
224 Learning from a Failed Negotiation | Self-awareness | うまくいかなかった交渉から学びを1つ書く
225 The Calm Negotiator | All four | 交渉で落ち着いていられる自分の準備を1枚にまとめる(シーズン15のしめくくり)

## Season 16 — Thinking Clearly (226–240)
226 Fast and Slow Thinking at Work | Self-awareness | 今日「すぐ決めた」判断を1つ見直す
227 Confirmation Bias | Self-awareness | 自分の意見に反する情報を1つ探す
228 Pre-Mortems | Self-management | 「失敗したとしたら原因は何か」を3つ書く
229 Base Rates | Self-awareness | 予想の前に似た例の実績を調べる
230 Overconfidence | Self-awareness | 予想に自信の度合い(%)をつける
231 Groupthink | Social awareness | 会議で反対の立場をあえて一度言う
232 One-Way and Two-Way Doors | Self-management | 今日の判断を「やり直せるか」で分ける
233 What Would Change My Mind? | Self-awareness | 自分の意見を変える条件を1つ書く
234 Second-Order Effects | Social awareness | 決定の「その次に起きること」を1つ考える
235 Good Decisions, Bad Outcomes | Self-management | 結果ではなく判断の質で振り返る
236 Keeping a Decision Journal | Self-management | 大事な判断を理由と一緒に記録する
237 Disagreement as Data | Social awareness | 反対意見から学べる点を1つ書く
238 Simple Rules for Complex Work | Self-management | 迷いやすい場面のマイルールを1つ作る
239 Checking the Machine | Self-awareness | AIの答えの根拠を1つ自分で確かめる
240 A Clear Thinker | All four | 今月一番いい判断を1つ振り返る(シーズン16のしめくくり)

## Season 17 — Product Thinking (241–255)
241 What Product Managers Do | Social awareness | プロダクトマネージャーに仕事で一番大事なことを聞く
242 Program, Product, Project | Self-awareness | 3つの役割の違いを自分の言葉で書く
243 User Interviews | Social awareness | ユーザー1人に「最近困ったこと」を聞く
244 Discovery Before Delivery | Self-management | 作る前に確かめたい仮説を1つ書く
245 Value vs. Effort | Self-management | やりたいことを価値と手間で並べてみる
246 The Smallest Useful Thing | Self-management | 計画を「最初に出せる一番小さい形」に削る
247 Roadmaps and What Waits | Relationship management | ロードマップで後回しにしたものと理由を書く
248 Working with Designers | Relationship management | デザイナーに「何を一番大事にしたか」を聞く
249 Scoping with Engineers | Relationship management | エンジニアと一緒に削れる範囲を探す
250 Saying No to Feature Requests | Self-management | 要望を断るときに理由と代案を伝える
251 Measuring Product Success | Self-awareness | 機能の成功を測る指標を1つ決める
252 Launch and Learn | Self-management | リリース後に確かめることを3つ決める
253 Products for Everyone | Social awareness | 自社サービスを使いにくい人を1人想像して改善点を書く
254 The Customer in the Room | Relationship management | 会議でお客さんの声を1つ紹介する
255 Thinking Like a Customer | All four | お客さんとして自社サービスを使ってみる(シーズン17のしめくくり)

## Season 18 — Execution and Delivery (256–270)
256 Agile Without the Buzzwords | Self-awareness | チームの「小さく作って確かめる」流れを1つ見つける
257 Standups That Help | Relationship management | 朝会で「困っていること」を必ず聞く
258 Limit Work in Progress | Self-management | 同時に進める仕事を3つまでに減らす
259 Goals You Can Measure | Self-management | 目標を1つ、測れる成果に書き直す
260 Milestones and Checkpoints | Self-management | 次の確認ポイントを日付つきで決める
261 Risks, Assumptions, Issues, Dependencies | Self-management | リスク・前提・課題・依存を1つずつ書く
262 Release Planning Together | Relationship management | リリースの流れを関係者と一緒に確認する
263 Quality Is Everyone's Job | Social awareness | テスト担当の人に一番の心配を聞く
264 Unblocking Others | Relationship management | 誰かの止まっている仕事を1つ動かす
265 Launch Day Communication | Self-management | リリース当日の連絡ルールを決める
266 Incident Timelines | Self-management | 問題の振り返りを事実の時系列で書く
267 Many Projects at Once | Self-management | 担当中の仕事を一覧にして状態を色分けする
268 Automate the Boring Parts | Self-awareness | 毎週の手作業を1つ自動化できないか考える
269 Finishing Strong | Self-management | やりかけの仕事を1つ完了させる
270 A Reliable Deliverer | All four | 今月期限どおりに届けたものを振り返る(シーズン18のしめくくり)

## Season 19 — Culture and Global Teams (271–285)
271 Cultural Intelligence | Social awareness | 違う文化の同僚の行動を1つ、相手の文化から考える
272 Feedback Across Cultures | Social awareness | 相手に合わせてフィードバックの言い方を1つ変える
273 Time Zones and Fairness | Relationship management | 会議の時間を交代制にする提案をする
274 Including Non-Native Speakers | Social awareness | 会議で話すスピードと確認の仕方を1つ変える
275 First Impressions and Bias | Self-awareness | 自分の第一印象を1つ疑ってみる
276 Belonging at Work | Relationship management | 新しく来た人を雑談に誘う
277 Different Working Styles | Social awareness | 同僚1人に「どう働くのが好きか」を聞く
278 Being the Bridge Between Tokyo and Seattle | Relationship management | 2つの拠点の間で誤解を1つ解く
279 Small Talk the American Way | Social awareness | アメリカの同僚の雑談のパターンを1つメモする
280 Your Accent, Your Voice | Self-awareness | 自分の英語で話すことに誇りを持てる点を1つ書く
281 Speaking Up from the Minority | Self-management | 少数派の意見を一度言葉にする
282 Small Acts of Allyship | Relationship management | 誰かの意見を名前付きで引用する
283 Differences as Strength | Social awareness | チームの多様さが役立った場面を1つ伝える
284 Global Email Etiquette | Social awareness | 海外の相手とのメールのマナーを1つ確認する
285 A Global Teammate | All four | 文化を越えて学んだことを1人に話す(シーズン19のしめくくり)

## Season 20 — Networking and Visibility (286–300)
286 Networking as Relationship Building | Relationship management | 社内の知らない人に1人連絡する
287 The 15-Minute Coffee Chat | Relationship management | 15分の会話の質問を3つ準備する
288 Your 30-Second Introduction | Self-management | 自分の仕事と目標を30秒で声に出して話す
289 Your Internal Profile | Self-awareness | 社内プロフィールに最近の成果を1つ加える
290 Following Up | Relationship management | 会った人に24時間以内に一言お礼を送る
291 Giving Before Asking | Relationship management | 誰かの役に立つ情報を1つ共有する
292 The Strength of Weak Ties | Social awareness | 最近話していない知り合いに連絡する
293 Finding a Sponsor in Seattle | Relationship management | シアトルで自分を推してくれそうな人を書き出す
294 Visible Without Bragging | Self-management | 成果を事実と数字で1行にして共有する
295 One Line at the All-Hands | Self-management | 全体会議で一言話す準備をする
296 Internal Communities | Relationship management | 社内の勉強会やコミュニティに1つ参加する
297 Teaching to Connect | Relationship management | 後輩に自分の学びを1つ伝える
298 Reliable Across Time Zones | Social awareness | 時差のある相手にとって頼れる工夫を1つする
299 Networking for Introverts | Self-awareness | 自分に合った人とのつながり方を1つ決める
300 Your Network Map | All four | この3か月で新しくつながった人を書き出す(シーズン20のしめくくり)

## Season 21 — Working with AI, Staying Human (301–315)
301 What AI Is Good At (and Isn't) | Self-awareness | 今日の仕事でAIに任せることと任せないことを分ける
302 Prompting Is Communicating | Social awareness | AIへの指示を、人に頼むときと同じくらい具体的に書く
303 Checking AI's Work | Self-management | AIの出力の事実を1つ原典で確かめる
304 AI and Confidential Information | Self-awareness | AIに入れてはいけない情報を確認する
305 Human Judgment in the Loop | Self-management | AIの提案を採用する前に自分の判断を1行書く
306 AI Meeting Notes, Human Follow-Up | Self-management | AIの議事録に抜けていた大事なことを1つ足す
307 Being Open About AI Use | Relationship management | AIを使ったことをチームに正直に伝える
308 AI in Marketing | Social awareness | AIが作った文言を、お客さんの立場で読み直す
309 Bias in AI | Self-awareness | AIの答えに偏りがないか1つ確かめる
310 Learning Faster with AI | Self-management | AIに自分の説明の弱点を聞いて直す
311 Speaking Practice with AI | Self-management | AIと英語で5分会話して、詰まった表現を3つメモする
312 What Stays Human | Self-awareness | 自分にしかできない仕事を3つ書く
313 Team Rules for AI | Relationship management | AIの使い方のルールをチームで1つ決める
314 AI Anxiety | Self-management | AIへの不安を名前にして、できることを1つ決める
315 Human + AI | All four | AIと働いてよかったことと気をつけることを書く(シーズン21のしめくくり)

## Season 22 — Resilience for the Long Run (316–330)
316 Bouncing Back | Self-management | 最近のつまずきから学びを1つ書く
317 Energy and Evenings | Self-awareness | 寝る前のスクリーン時間を15分減らす
318 Walking Meetings | Self-management | 会議の1つを歩きながら参加する
319 Stress in the Body | Self-awareness | ストレスを感じたときの体のサインを1つメモする
320 Boundaries Without Guilt | Self-management | 返信しない時間を相手に伝える
321 Social Support | Relationship management | 最近話していない友人に連絡する
322 Three Good Things | Self-awareness | 今日よかったことを3つ書く
323 Loneliness at Work | Social awareness | 1人で働いていそうな人に声をかける
324 Early Signs of Burnout | Self-awareness | 自分の疲れのサインを1つ書く
325 Shutdown Rituals | Self-management | 仕事の終わりに切り替える小さな習慣を作る
326 Self-Compassion, Revisited | Self-awareness | 失敗した日に自分にかける言葉を書く
327 Purpose When Work Is Hard | Self-awareness | 大変な仕事が誰の役に立つかを書く
328 Real Rest | Self-management | 次の休みに仕事を持ち込まない計画を立てる
329 Asking for Help Early | Relationship management | 困っていることを1つ早めに相談する
330 Sustainable Ambition | All four | 続けられる目標とペースを1枚にまとめる(シーズン22のしめくくり)

## Season 23 — Deep Listening and Empathy (331–345)
331 Listening to Understand, Not to Reply | Social awareness | 今日の会話で1回、自分の意見を言う前に相手の話を最後まで聞き切る
332 The Three Levels of Listening | Self-awareness | 会議中に、自分の注意が「自分・相手・場」のどこに向いているかを3回チェックする
333 Silence as an Invitation | Self-management | 相手が話し終えたあと、3秒待ってから口を開く
334 Questions That Open People Up | Social awareness | 「What」や「How」で始まる開かれた質問を、会議で2つする
335 Hearing the Feeling Behind the Words | Social awareness | 同僚の発言から、言葉の裏にある気持ちを1つ推測してメモする
336 Empathy Is Not Agreement | Relationship management | 意見が違う相手に「That makes sense from your side」と一度言ってから、自分の考えを話す
337 Cognitive and Emotional Empathy | Self-awareness | 今日話した人の「考え」と「気持ち」を、それぞれ1行ずつ書き分ける
338 Empathy Fatigue | Self-management | 人の相談に乗ったあと、5分だけ一人の時間をとって気持ちを切り替える
339 Listening on a Bad Connection | Social awareness | オンライン会議で聞き取れなかった部分を、推測せずに英語で確認する
340 Reflecting Back Without Parroting | Relationship management | 相手の話を自分の言葉で1文にまとめて「Is that right?」と確かめる
341 Listening to Someone Who Is Upset | Relationship management | 困っている同僚の話を、解決策を出さずに5分聞く
342 Your Listening Blind Spots | Self-awareness | 自分がつい話をさえぎってしまう相手や話題を1つ見つけて書き出す
343 Curious About the Other Side | Social awareness | 他チームの人に「今一番大変なことは何?」と聞いてみる
344 Listening in a Group | Social awareness | 会議でまだ発言していない人の意見を拾い、名前を出して返す
345 A Listener People Seek Out | All four | 今日いちばんよく聞けた会話を1つ選び、何が良かったかを書く(シーズン23のしめくくり)

## Season 24 — Peer Coaching Conversations (346–360)
346 Coaching Is Not Advising | Self-awareness | 相談されたら、アドバイスの前に質問を1つする
347 And What Else? | Relationship management | 同僚との会話で「And what else?」を一度使ってみる
348 Helping a Peer Find the Real Problem | Social awareness | 相談に来た人に「本当の課題は何だと思う?」と聞く
349 Goals, Reality, Options, Way Forward | Self-management | 自分の悩みを1つ、GROWの4つの質問で整理する
350 Holding Back Your Answer | Self-management | 答えを言いたくなったら、口に出す前に「What have you tried?」と聞く
351 Coaching Up and Sideways | Relationship management | 先輩か同じ立場の同僚に、考えを深める質問を1つ投げる
352 Powerful Questions in English | Self-management | コーチングの質問を英語で5つ、声に出して練習する
353 Asking Permission to Coach | Relationship management | 「Can I ask you a few questions about that?」と一言断ってから質問する
354 Spotting Strengths in Others | Social awareness | 同僚の強みを1つ見つけて、具体的に本人に伝える
355 Peer Feedback Circles | Relationship management | 同僚2人と、お互いの仕事に一言ずつフィードバックし合う15分をつくる
356 When Coaching Isn't Enough | Self-awareness | 自分の手に負えない相談のとき、つなぐべき人を1人思い浮かべてメモする
357 Coaching Yourself | Self-management | 今日の迷いごとに自分で3つ質問し、答えを書く
358 Commitments That Stick | Relationship management | 会話の最後に「What's your next step?」と聞き、相手の言葉で決めてもらう
359 Being Coached Well | Self-awareness | メンターとの会話で、答えではなく質問をもらうようにお願いしてみる
360 A Peer Who Helps Others Think | All four | 今日だれかの考えを助けた場面を1つ振り返り、効いた質問を書き残す(シーズン24のしめくくり)

## Season 25 — Customer Research and UX (361–375)
361 Research Before Opinions | Self-awareness | 「お客さんはこう思っているはず」と思い込んでいることを1つ書き出す
362 Writing a Research Question | Self-management | 調べたいことを「誰が・何を・なぜ」が入った1文の問いにする
363 Recruiting the Right Participants | Social awareness | 話を聞くべきユーザー像を、3つの条件で書く
364 Asking About the Past, Not the Future | Social awareness | ユーザーへの質問を「最後に〜したときは?」の形に3つ書き直す
365 Observing Real Behavior | Social awareness | 誰かが社内ツールを使う様子を、5分だけ黙って観察する
366 Usability Testing on a Budget | Relationship management | 同僚1人に画面や資料を使ってもらい、迷った箇所をメモする
367 Note-Taking Without Bias | Self-management | 会議メモで「事実」と「自分の解釈」を分けて書く
368 Finding Patterns in Feedback | Self-awareness | 集まった意見をグループ分けして、3つのテーマに名前をつける
369 Support Tickets as Research | Social awareness | 問い合わせの記録を10件読み、繰り返し出てくる不満を1つ見つける
370 Journey Maps That Reveal Pain | Social awareness | ユーザーの1日の流れを書き、一番つらい瞬間に印をつける
371 Accessibility Is UX | Social awareness | 自分の資料を色や文字の大きさの点で見直し、1か所直す
372 Friction Hunting | Self-management | チームの手続きで、ユーザーが何回クリックするか実際に数えてみる
373 Sharing Insights People Remember | Relationship management | ユーザーの声を1つそのまま引用して、チームのチャットで共有する
374 Research with Engineers in the Room | Relationship management | エンジニアを次のユーザーインタビューに誘う
375 The User's Advocate | All four | ユーザーの立場から、今の企画に質問を1つ投げる(シーズン25のしめくくり)

## Season 26 — Growth Marketing and Experiments (376–390)
376 What Growth Really Means | Self-awareness | 自分のチームの「成長」が何を指すのかを1文で書く
377 Loops, Not Just Funnels | Social awareness | 使った人が次の利用者を連れてくる流れが自社にあるか、図にして考える
378 Writing a Testable Hypothesis | Self-management | アイデアを1つ「もし〜なら、〜が増える。なぜなら〜」の形で書く
379 Picking Experiments with ICE | Self-management | 試したいアイデアを3つ、効果・自信・手軽さで点数をつけて比べる
380 Activation: The First Win | Social awareness | 新しいユーザーが最初に「便利だ」と感じる瞬間を1つ言葉にする
381 Retention Beats Acquisition | Social awareness | 一度使ってやめた人の理由を1つ調べるか、同僚に聞く
382 Onboarding That Helps | Relationship management | 新しく来た人向けの案内を、1か所わかりやすく直す
383 Copy Tests and Small Words | Self-management | メールの件名を2案書いて、同僚にどちらを開きたいか聞く
384 Sample Size and Patience | Self-management | 実験結果を見る前に「何日・何人分待つか」を先に決めて書く
385 When the Test Fails | Self-awareness | うまくいかなかった試みから分かったことを1つ、チームに共有する
386 Cohorts Over Totals | Social awareness | 数字を1つ、始めた時期ごとのグループに分けて見てみる
387 Growth with Product and Engineering | Relationship management | 実験のアイデアをエンジニアに見せて、手間を一緒に見積もる
388 Referral and Word of Mouth | Social awareness | 自分が人にすすめたサービスを1つ思い出し、すすめた理由を書く
389 Growth Without Dark Patterns | Self-awareness | 自社の画面に、ユーザーをだますように見える箇所がないか1つ確認する
390 An Experiment Culture | All four | 小さな実験を1つ決めて、仮説と測り方をチームに共有する(シーズン26のしめくくり)

## Season 27 — Consumer Psychology (391–405)
391 Scarcity and Urgency, Honestly | Social awareness | 「残りわずか」などの表現を1つ見つけ、本当かどうか考える
392 The Reciprocity Effect in Marketing | Social awareness | 無料サンプルやお試しを1つ見つけ、なぜ人が動くのかを書く
393 Commitment and Consistency | Self-management | 会議の決定事項を、担当者自身の言葉でチャットに書いてもらう
394 The Fresh Start Effect | Self-management | 来週の月曜を区切りにして始めることを1つ決める
395 The Goal-Gradient Effect | Social awareness | 進行中のタスクに「あと何%」を見える形で書き足す
396 Present Bias and Procrastination | Self-awareness | 後回しにしている仕事を1つ、最初の5分だけ今やる
397 The Pain of Paying | Social awareness | お金を払うときに「痛い」と感じた場面を1つ思い出し、理由を書く
398 The Power of Free | Social awareness | 「無料」と書かれた広告を1つ見て、隠れたコストを書き出す
399 Charm Prices and Round Numbers | Social awareness | 「980円」と「1,000円」で受ける印象の違いを同僚と話してみる
400 Processing Fluency: Easy Feels True | Self-management | 資料の一番大事な一文を、もっと短く読みやすく書き直す
401 Mere Exposure and Familiarity | Relationship management | 来週出す提案の要点を、今日のチャットで一言だけ先に触れておく
402 Habits and Cues in Products | Social awareness | 毎日開くアプリを1つ選び、きっかけ・行動・ごほうびを書き出す
403 Identity: "People Like Us" | Social awareness | 自社のメッセージを、誰のためのものかが伝わる一文に直す
404 Hedonic Adaptation and Delight | Relationship management | いつも手伝ってくれる人に、いつもと違う形でお礼を伝える
405 Persuasion You Can Be Proud Of | All four | 今日の説得で使った心理の仕組みを1つ書き、相手のためになっていたか見直す(シーズン27のしめくくり)

## Season 28 — Business and Finance Basics for Program Managers (406–420)
406 How Your Company Makes Money | Self-awareness | 自社の売上の柱を3つ、人に説明できるように書く
407 Reading a P&L Without Fear | Self-management | 損益計算書(P&L)の上から3行を、自分の言葉で説明してみる
408 Revenue, Cost and Margin | Social awareness | 自分のチームの仕事が売上・コスト・利益のどれに効くかを1行で書く
409 Fixed and Variable Costs | Social awareness | 担当している仕事のコストを「固定」と「変動」に分けてみる
410 Budgets Are Promises | Self-management | 自分のプロジェクトの予算(お金と時間)の残りを確認する
411 The Cost of People's Time | Self-awareness | 今日の会議1つのコストを「人数×時間」で計算してみる
412 Writing a Business Case | Self-management | 提案したいことを「課題・案・費用・効果」の4行で書く
413 ROI and Payback Period | Social awareness | 小さな改善案を1つ選び、何か月で元が取れるかざっくり計算する
414 Opportunity Cost | Self-awareness | 今の仕事を選んだことで、あきらめているものを1つ書き出す
415 Headcount Requests and Trade-Offs | Relationship management | 人を増やす以外の解決策を3つ書き出す
416 Unit Economics in Plain Words | Social awareness | ユーザー1人あたりの売上とコストを、詳しい同僚に聞いて確かめる
417 Forecasts and Ranges | Self-management | 次の見積もりを1つの数字ではなく「最低〜最高」の幅で出す
418 Talking Money with Finance Partners | Relationship management | 財務の担当者に、自分の仕事に関係する数字を1つ質問する
419 When the Budget Gets Cut | Self-management | 予算が半分になったら何を残すかを3行で書く
420 Thinking Like an Owner of the Numbers | All four | 自分の仕事を1つ、お金の言葉で説明して声に出す(シーズン28のしめくくり)

## Season 29 — Strategy Basics (421–435)
421 What Strategy Is and Isn't | Self-awareness | チームの「戦略」「目標」「計画」を1行ずつ書き分ける
422 Diagnosis, Policy, Action | Self-management | 今の課題を「診断・方針・行動」の3行でまとめる
423 Strategy Is Choosing | Self-management | チームでやめてもよいことを1つ、理由と一緒に提案する
424 Where to Play, How to Win | Social awareness | 自社が勝てる場所を1つと、その理由を書く
425 Knowing Your Competitors | Social awareness | 競合のサービスを10分さわって、違いを3つメモする
426 Moats and Advantages | Social awareness | 自社がまねされにくい強みを1つ、同僚と話してみる
427 Trends You Can't Ignore | Self-awareness | 業界ニュースを1本読み、自分の仕事への影響を1行書く
428 Scenarios, Not Predictions | Self-management | 来年の状況を「よい・ふつう・悪い」の3パターンで書く
429 From Company Strategy to Team Goals | Social awareness | 会社の目標と今日の自分のタスクを、1本の線でつなげて書く
430 OKRs That Actually Guide | Self-management | 自分の目標を1つ、測れる成果の形に書き直す
431 Strategy in One Page | Self-management | チームの方針を1ページにまとめ、同僚に読んでもらう
432 Asking Strategic Questions | Relationship management | 次の会議で「これは会社の何に効きますか?」と一度聞く
433 When Strategy Changes | Self-management | 方針が変わったとき、自分の仕事で変えることと変えないことを書く
434 Strategy and Culture | Social awareness | チームでよく言われる言葉を1つ選び、それが行動にどう出ているか考える
435 A Strategic Teammate | All four | 今日の仕事で「なぜ」を一段上までさかのぼって考えた場面を書く(シーズン29のしめくくり)

## Season 30 — Executive Communication (436–450)
436 How Executives Read | Social awareness | 上の人に送るメッセージを、最初の2行で結論が分かる形にする
437 Bottom Line Up Front | Self-management | 今日のメール1通を、結論→理由→お願いの順に書き直す
438 The Ask in One Sentence | Self-management | 上司に頼みたいことを1文にして、声に出して練習する
439 Three Levels of Detail | Social awareness | 同じ報告を10秒版・1分版・5分版で用意する
440 The Elevator Update | Self-management | エレベーターで聞かれた想定で、今の仕事の状況を英語で30秒話す
441 Options with a Recommendation | Relationship management | 判断をお願いするとき、選択肢2つと自分のおすすめを添える
442 Status Reports Leaders Read | Self-management | 週次報告を「赤・黄・緑」と一言の理由で書き直す
443 Handling Executive Pushback | Self-management | 鋭い質問を1つ想定して、英語の答えを声に出して準備する
444 When a Leader Goes Off Track | Relationship management | 会議が脱線したら「To make sure we decide this today…」と一度言ってみる
445 Skip-Level Conversations | Relationship management | 上司の上司に聞いてみたい質問を1つ用意する
446 Writing an Executive Summary | Self-management | 長い資料の冒頭に、5行の要約をつける
447 Asking for a Decision | Relationship management | 「What I need from you is…」で始まるお願いを1つ送る
448 Admitting Risk to Leadership | Self-awareness | 上司にまだ伝えていない心配ごとを1つ、早めに伝える
449 Short Answers to Hard Questions | Self-management | よく聞かれる質問に20語以内の英語の答えを作り、声に出す
450 Trusted by Leaders | All four | 上の人とのやりとりを1つ振り返り、次に変えることを1つ決める(シーズン30のしめくくり)

## Season 31 — Process Improvement and Root Causes (451–465)
451 Seeing Work as a Process | Social awareness | 自分の仕事を1つ、始まりから終わりまで5ステップで書く
452 Mapping the Value Stream | Social awareness | 依頼から完了までの各ステップにかかる時間を、ざっくり書き込む
453 Waiting Is the Hidden Waste | Self-awareness | 今日、だれかの返事を待っていた時間を合計してみる
454 The Five Whys | Self-management | 最近起きた小さな問題に「なぜ」を5回くり返す
455 Fishbone Diagrams | Social awareness | 1つの問題の原因を「人・方法・道具・情報」に分けて書く
456 Fix the System, Not the Person | Relationship management | 誰かのミスを、仕組みの問題として言い直してみる
457 Small Improvements Every Day | Self-management | 毎日やっている作業を1つ、1分でも短くする工夫をする
458 Standard Work and Checklists | Self-management | よくやる手順を1つ、チェックリストにする
459 Bottlenecks | Social awareness | チームの仕事が一番たまっている場所を1つ見つける
460 Handoffs That Don't Drop | Relationship management | 次の人に仕事を渡すとき、必要な情報を3行で添える
461 Measuring Before and After | Self-management | 改善したい作業の今の所要時間を測って記録する
462 Error-Proofing | Self-management | 自分がよくするミスを1つ選び、起きにくくする仕組みを入れる
463 Process Change People Accept | Relationship management | 手順を変える前に、それを使う人に一言意見を聞く
464 When Process Becomes Bureaucracy | Self-awareness | 目的が分からなくなった手順を1つ見つけ、なぜあるのかを確かめる
465 A Continuous Improver | All four | 今日改善したことを1つ、前後の違いとともにチームに共有する(シーズン31のしめくくり)

## Season 32 — Organizations and Change (466–480)
466 How Organizations Really Work | Social awareness | 組織図に書かれていない「実際の相談ルート」を1つ書き出す
467 Formal and Informal Power | Social awareness | 肩書きはなくても周りが頼りにしている人を1人見つける
468 Why Org Charts Change | Self-awareness | 今の組織がなぜこの形なのか、上司に1つ質問する
469 Teams Shape What They Build | Social awareness | チームの分かれ方が成果物にどう表れているか、例を1つ見つける
470 Silos and Bridges | Relationship management | ふだん話さない部署の人に、質問のメッセージを1つ送る
471 The Change Curve | Self-awareness | 今起きている変化への自分の気持ちが、どの段階にあるかを書く
472 Early Adopters and Skeptics | Social awareness | 新しいやり方への反応で、関係者を「賛成・様子見・反対」に分ける
473 Listening to Resistance | Relationship management | 変化に反対している人に何が心配かを聞き、最後まで聞く
474 Making Change Small | Self-management | 大きな変更を、来週試せる小さな一歩に分ける
475 Change Champions | Relationship management | 新しいやり方を一緒に広めてくれそうな人に声をかける
476 Communicating Change Again and Again | Relationship management | 同じ変更のお知らせを、別の言い方でもう一度伝える
477 New Leader, New Direction | Self-management | 新しいリーダーの方針を、自分の言葉で1文にまとめる
478 Culture Eats Plans | Social awareness | チームで「本当に評価される行動」を1つ書き出す
479 Making Change Stick | Self-management | 最近始めた新しいやり方が続いているか、1つ確認する
480 Steady Through Change | All four | この1か月の変化の中で、自分が保てたものを1つ書く(シーズン32のしめくくり)

## Season 33 — Motivation Science (481–495)
481 What Really Motivates People | Self-awareness | 仕事で一番やる気が出た瞬間を1つ思い出し、理由を書く
482 Autonomy, Competence, Relatedness | Self-awareness | 今日の仕事で、自分で選べること・うまくなれること・人とつながれることを1つずつ書く
483 Intrinsic and Extrinsic Rewards | Social awareness | 同僚に「この仕事のどこが好き?」と聞いてみる
484 The Progress Principle | Self-management | 帰る前に、今日進んだことを1つ書き出す
485 Small Wins for the Team | Relationship management | チームの小さな前進を1つ見つけて、チャットでたたえる
486 Seeing Who Your Work Helps | Self-awareness | 自分の仕事が誰の役に立っているかを1文で書く
487 Goal Setting That Energizes | Self-management | 今日の目標を「少し難しいけど届く」レベルで1つ決める
488 Linking Tasks to What Others Care About | Relationship management | 協力をお願いするとき、相手にとっての意味を1つ添える
489 Interest Grows When You Dig In | Self-management | 今の仕事で気になる「なぜ?」を1つ、15分だけ調べてみる
490 The Overjustification Trap | Self-awareness | ごほうびのためだけにやっている作業を1つ見つけ、その中の面白さを探す
491 Motivation Dips | Self-management | やる気が出ない仕事に、終わったあとの小さなごほうびを1つ決める
492 Recognition That Motivates | Relationship management | 同僚の結果ではなく努力の過程を、具体的にほめる
493 Mastery and Deliberate Practice | Self-management | 苦手なスキルを1つ選び、15分だけ集中して練習する
494 Motivation Across Cultures | Social awareness | 東京とシアトルの同僚に、何が仕事の励みになるかを1人ずつ聞く
495 Your Own Motivation Map | All four | やる気が上がることと下がることを3つずつ書いて見比べる(シーズン33のしめくくり)

## Season 34 — Learning How to Learn and Habits (496–510)
496 How Memory Really Works | Self-awareness | 今日学んだことを、夜に何も見ずに3つ思い出して書く
497 Retrieval Practice | Self-management | 昨日の会議の要点をメモを見ずに書き出し、あとで見比べる
498 Spacing Your Learning | Self-management | 覚えたい英語フレーズ3つを、明日・3日後・1週間後に見直す予定に入れる
499 Mixing Up Practice | Self-management | 英語の練習で、聞く・話す・書くを10分ずつ混ぜてやってみる
500 Explain It Simply to Learn It | Self-management | 最近学んだ言葉を1つ、新人に話すつもりで声に出して説明する
501 Learning from Experts on Your Team | Relationship management | 詳しい同僚に「どうやって覚えたの?」と聞く
502 Tiny Habits | Self-management | 毎日している行動の後に、30秒でできる新しい習慣を1つつなげる
503 Designing Your Environment | Self-management | 気が散るタブやアプリを1つ閉じて、作業の場を整える
504 Breaking a Bad Habit | Self-awareness | やめたい習慣のきっかけを1つ見つけてメモする
505 Identity-Based Habits | Self-awareness | 「私は〜する人だ」という一文を書き、それに合う行動を1つする
506 Learning Plateaus | Self-management | 伸び悩んでいるスキルを1つ選び、練習方法を1つ変えてみる
507 Notes You'll Actually Use | Self-management | 今日のメモに、明日の自分への一言を書き足す
508 Asking the Question Everyone Has | Relationship management | 会議で分からなかった言葉を1つ、その場で質問する
509 Sleep and Learning | Self-management | 今夜はいつもより30分早く画面を閉じる
510 A Lifelong Learner | All four | この数か月で一番伸びたスキルと、その理由を3行で書く(シーズン34のしめくくり)

## Season 35 — Emotion Regulation, Advanced (511–525)
511 The Process Model of Emotion | Self-awareness | 気持ちが動いた場面を1つ、「状況・注目・解釈・反応」に分けて書く
512 Choosing the Situation | Self-management | 苦手な場面に入る前に、自分で変えられる条件を1つ変える
513 Shifting Attention | Self-management | イライラしたとき、目の前の具体的な作業1つに注意を移す
514 Cognitive Reappraisal | Self-management | 嫌だった出来事を、別の見方で1文書き直す
515 Suppression Has a Cost | Self-awareness | 今日がまんした気持ちを1つ、ノートか信頼できる人に出す
516 Emotional Granularity | Self-awareness | 「ストレス」を、もっと細かい2つの言葉に言い換える
517 Self-Distancing | Self-management | 迷ったとき、自分を名前で呼んで「友だちなら何と言う?」と問いかける
518 Co-Regulation: Steadying Others | Relationship management | 緊張している同僚の前で、自分がゆっくり話すことを意識する
519 Triggers and Old Stories | Self-awareness | 強く反応してしまう言葉を1つ見つけ、その背景を考える
520 Recovering After You Snap | Relationship management | きつく言ってしまった相手に、短いおわびと次の一歩を伝える
521 Emotions in Writing | Social awareness | 送る前のメッセージを、相手の気持ちになって一度読み直す
522 Holding Two Feelings at Once | Self-awareness | 今の仕事について「うれしい」と「不安」を両方書く
523 Regulating in Real Time on Calls | Self-management | オンライン会議でカッとなったら、ミュートのまま深く3回息をする
524 Mood and Decisions | Self-awareness | 大事な判断の前に、今の気分を1語で書いてから決める
525 Calm Is a Skill | All four | 今日感情をうまく扱えた場面を1つ選び、使った方法を書く(シーズン35のしめくくり)

## Season 36 — Trust and Ethics at Work (526–540)
526 The Trust Equation | Self-awareness | 信頼の4要素(信頼性・確実さ・親しみ・自分本位でないこと)で自分を採点する
527 Competence Trust and Character Trust | Social awareness | 信頼している同僚を1人選び、何を信頼しているのかを書く
528 Keeping Confidences | Self-management | 聞いた話を人に伝える前に「話していい内容か」を確かめる
529 Rebuilding Broken Trust | Relationship management | 約束を守れなかった相手に、事実を認めて次の約束を1つする
530 Speaking Up About Something Wrong | Self-management | 気になっていることを1つ、「I'm concerned about…」で上司に伝える
531 Gray Areas | Self-awareness | 判断に迷う場面で「1年後に説明できるか」を考えてメモする
532 Conflicts of Interest | Self-awareness | 自分の判断に影響しそうな関係や利害を1つ書き出す
533 Honest Numbers | Self-management | 報告する数字が都合よく見せすぎていないか、1つ確認する
534 Fairness in Small Decisions | Social awareness | 仕事の割り振りが特定の人に偏っていないか見てみる
535 Giving Credit Generously | Relationship management | 自分の成果に関わった人の名前を出して、感謝を伝える
536 Transparency vs. Oversharing | Self-management | 共有しようとしている情報を「必要な人・必要な量」に絞る
537 Consistency Builds Trust | Self-management | 進み具合を毎日同じ時間・同じ形で伝えると決めて、今日から始める
538 Saying No to Shortcuts | Self-management | 期限のために省こうとしている確認を1つ、省かずにやる
539 Psychological Contracts | Social awareness | チームで「言わなくても守っている約束」を1つ書き出す
540 Someone People Can Count On | All four | 今日の行動で信頼を積んだ瞬間を1つ書く(シーズン36のしめくくり)

## Season 37 — Creativity and Innovation (541–555)
541 Creativity Is a Work Skill | Self-awareness | 今日の仕事で「いつもと違うやり方」を1つ試す
542 Divergent and Convergent Thinking | Self-management | 課題に対して案を10個出してから、1つに絞る
543 Better Brainstorming | Relationship management | ブレストの前に、各自が一人で案を書く時間を5分とる
544 Constraints Spark Ideas | Self-management | 「予算ゼロならどうする?」と考えて、案を1つ出す
545 Borrowing Ideas from Other Fields | Social awareness | 別の業界のやり方を1つ見つけ、自分の仕事に当てはめてみる
546 Incubation: Step Away | Self-management | 行き詰まった問題から10分離れ、散歩のあとにもう一度見る
547 Reframing the Question | Self-management | 課題を「How might we…?」の形で3通りに言い換える
548 Prototypes Over Plans | Self-management | アイデアを1つ、紙か簡単な画面で形にして見せる
549 Building on Others' Ideas | Relationship management | 会議で人のアイデアに「Yes, and…」で一つ足す
550 Killing Ideas Kindly | Relationship management | 採用しないアイデアに、良かった点を1つ伝えてから理由を話す
551 Innovation Inside Big Companies | Social awareness | 社内で新しいことを始めた人に、どう進めたかを聞く
552 Room for Wild Ideas | Social awareness | 会議で「変なアイデアでも歓迎です」と一言そえて意見を募る
553 Creative Confidence | Self-awareness | 「自分は創造的ではない」と思った場面を1つ思い出し、言い換える
554 From Idea to Pilot | Self-management | 温めているアイデアを、2週間で試せる小さな計画にする
555 A Creative Program Manager | All four | 今日出したアイデアを1つ誰かに話して、反応を聞く(シーズン37のしめくくり)

## Season 38 — Facilitation and Better Meetings (556–570)
556 The Facilitator's Job | Self-awareness | 次の会議では、話す人ではなく場を進める人になると決めて臨む
557 Purpose, Outcome, Agenda | Self-management | 会議の招待に「目的・ほしい結果・議題」を3行で書く
558 Opening a Meeting Well | Relationship management | 会議の最初の1分で、ゴールと時間配分を英語で伝える
559 Timeboxing Out Loud | Self-management | 議題ごとに時間を決め、「We have five minutes left on this」と声に出す
560 Parking Lot for Side Topics | Relationship management | 脱線した話題を「パーキングロット」に書き、後で扱うと伝える
561 Making Space for Everyone | Social awareness | 話し合いの前に、全員が書き込める共有ドキュメントで意見を集める
562 Handling Dominant Voices | Relationship management | 話し続ける人がいたら「Let's hear from others too」と一度言ってみる
563 Reading the Room Online | Social awareness | オンライン会議で反応の少ない人に、チャットで一言聞く
564 Decision Methods in Meetings | Self-management | 会議の前に「誰が・どの方法で決めるか」を書いておく
565 Workshops That Produce Something | Self-management | 30分のミニワークショップの流れを3ステップで設計する
566 Visual Facilitation | Social awareness | 会議中、話の流れをオンラインのホワイトボードに書いて見せる
567 Closing with Clear Actions | Relationship management | 会議の最後に「誰が・何を・いつまでに」を読み上げて確認する
568 Fewer, Shorter Meetings | Self-management | 定例会議を1つ選び、短くするかなくせないか提案する
569 Facilitating When You're Junior | Self-awareness | 先輩が多い会議の進行役として、最初の一言を声に出して練習する
570 A Meeting People Thank You For | All four | 今日の会議を1つ振り返り、参加者に良かった点と改善点を一言ずつ聞く(シーズン38のしめくくり)

## Season 39 — Advanced Speaking: Discussion and Debate in English (571–585)
571 Joining a Fast Discussion | Self-management | 会議で最初の5分以内に、英語で一言発言する
572 Agreeing and Building | Relationship management | 「Building on that…」で、人の意見に自分の考えを足して話す
573 Disagreeing Without Sounding Rude | Relationship management | 「I see your point, but…」以外の反対の言い方を3つ声に出して練習する
574 Holding the Floor | Self-management | 話の途中でさえぎられたら「Let me just finish this point」と言う
575 Making a Point in Three Parts | Self-management | 意見を「結論・理由・例」の順に、英語で30秒で声に出して言う
576 Asking Follow-Up Questions in Real Time | Social awareness | 会議で人の発言に、英語で追加の質問を1つする
577 Signposting Your Ideas | Self-management | 「There are two things…」と最初に数を言ってから話す
578 Hedging and Being Direct | Social awareness | 同じ意見を、やわらかい言い方とはっきりした言い方の両方で声に出す
579 Steelmanning the Other Side | Social awareness | 反対意見を、相手が納得するくらい強い形で英語で言い直す
580 Thinking on Your Feet | Self-management | ランダムなお題で1分間、英語で話す練習を1回する
581 Conceding Gracefully | Relationship management | 相手が正しいと思ったら「Fair point, I agree」とはっきり言う
582 Summarizing a Debate | Relationship management | 議論の最後に、双方の意見を英語で2文にまとめて伝える
583 Numbers in Live Discussion | Self-management | 自分の仕事の数字を3つ、英語で声に出して言う練習をする
584 Shadowing Real Discussions | Self-management | 英語の会議録画やポッドキャストを1分選び、少し遅れて声に出してついていく
585 Holding Your Own in Debate | All four | 今日英語で意見を言えた場面を1つ書き、次に使いたい表現を1つ選ぶ(シーズン39のしめくくり)

## Season 40 — Speaking on Calls: Accents, Speed and Repair Strategies (586–600)
586 Why Calls Are Harder | Self-awareness | 通話や会議で聞き取りにくいと感じる場面を3つ書く
587 Understanding Different Accents | Social awareness | ふだん聞かない英語のアクセントの音声を5分聞く
588 When People Speak Too Fast | Relationship management | 「Could you slow down a little?」を一度実際に使う
589 Repair Phrases That Save You | Self-management | 聞き返しの表現を3つ声に出して練習し、今日の会議で1つ使う
590 Confirming Before You Act | Self-management | 会議で「Just to confirm, you mean…?」と1回確認する
591 Fixing Your Own Mistakes Mid-Sentence | Self-management | 言い間違えたときの「Sorry, let me rephrase」を声に出して練習し、実際に使う
592 Slowing Down Your Own Speech | Self-management | 自分の英語を録音し、少しゆっくり話した版と聞き比べる
593 Word Stress and Clarity | Self-management | 仕事でよく使う英単語5つの強く読む位置を調べ、声に出す
594 Phone Calls Without Video | Social awareness | 顔が見えない通話で、相づちを声ではっきり返すことを意識する
595 Audio Setup and Background Noise | Self-management | 次の会議の前にマイクと音声を確認し、聞きやすい環境を整える
596 Talking Over Each Other | Relationship management | 発言がかぶったら「Go ahead」とゆずり、そのあと自分の番をとる
597 Spelling and Numbers on Calls | Self-management | 自分の名前とメールアドレスを、英語でゆっくりつづって声に出す
598 Ending a Call Clearly | Relationship management | 通話の最後に、決まったことを英語で1文にまとめて言う
599 Helping Others Understand You | Social awareness | 通話中の大事な言葉や数字を、チャットにも書いて補う
600 Calm and Clear on Any Call | All four | 今日の通話を1つ振り返り、うまくいった聞き返しと次の課題を1つずつ書く(シーズン40のしめくくり)

## Season 41 — Remote and Async Excellence (601–615)
601 Async by Default | Self-management | 会議を開く代わりに、文書とコメントで決められないか1つ試す
602 Writing for the Reader Who Wasn't There | Self-management | 会議に出られなかった人向けに、3行の要約を送る
603 Messages That Need No Follow-Up | Self-management | 依頼メッセージに、背景・期限・判断基準をすべて入れて送る
604 Short Videos Instead of Meetings | Relationship management | 説明が必要なことを、3分の画面録画で送ってみる
605 Handing Work Across Time Zones | Relationship management | 終業前に、シアトルの同僚あての引き継ぎメモを書く
606 Response-Time Agreements | Relationship management | チャットとメールの返信の目安を、チームに提案する
607 Status Without Asking | Self-management | 進み具合を、聞かれる前に決まった場所に書いておく
608 Remote Relationships | Relationship management | オンラインの同僚と、仕事以外の話をする5分のチャットをする
609 Focus Time in a Distributed Team | Self-management | カレンダーに集中時間をブロックし、チームに見えるようにする
610 Documentation Others Can Find | Self-management | よく聞かれることを1つ、探しやすい場所に書いて残す
611 Emoji, Reactions and Tone | Social awareness | チャットのリアクションや絵文字の受け取り方が、人によってどう違うか同僚に聞く
612 Hybrid Meetings That Are Fair | Social awareness | 会議室とオンラインが混ざる会議で、オンライン側に先に発言をふる
613 Avoiding Always-On | Self-awareness | 通知を切る時間を今日1時間決めて、守る
614 Onboarding Someone Remotely | Relationship management | 新しく来た人に、聞きやすい人と資料のリストを送る
615 A Great Remote Teammate | All four | 今日の非同期のやりとりを1つ見直し、もっと伝わる形に書き直す(シーズン41のしめくくり)

## Season 42 — Career Strategy in a US Company (616–630)
616 How US Companies Evaluate Performance | Social awareness | 自社の評価基準を読み、自分に一番関係する項目を1つ選ぶ
617 Levels and Leveling Guides | Self-awareness | 1つ上のレベルに期待されることを読み、今の自分との差を1つ書く
618 Writing Your Self-Review | Self-management | 今期の成果を1つ、「何をして・どんな影響があったか」の形で書く
619 Impact, Not Activity | Self-awareness | 今週やったことを1つ、作業ではなく成果の言葉で書き直す
620 Brag Documents | Self-management | 自分の成果を記録するドキュメントを作り、今日の分を1行書く
621 Peer Feedback in Review Season | Relationship management | 一緒に働いた人に、具体的で役に立つフィードバックを1つ書く
622 Calibration Explained | Social awareness | 評価がどう決まるのか、上司に1つ質問する
623 Self-Promotion Without Embarrassment | Self-management | 自分の成果を「I led…」で始まる英語の1文にして声に出す
624 Direct Feedback, American Style | Social awareness | もらったフィードバックから遠回しな表現を1つ見つけ、意味を確かめる
625 Owning Your Career Plan | Self-management | 1年後になりたい姿と、そのために必要な経験を3つ書く
626 Lateral Moves and Internal Transfers | Self-awareness | 社内で興味のある仕事を1つ調べ、求められるスキルを書き出す
627 Getting Promoted Is a Team Sport | Relationship management | 自分の成長を見てくれている人を3人書き出し、1人に近況を伝える
628 When the Review Disappoints | Self-management | 期待より低い評価を想定して、聞きたい質問を3つ準備する
629 Unwritten Rules of US Offices | Social awareness | シアトルの同僚に「最初に知っておきたかったこと」を1つ聞く
630 Steering Your Own Career | All four | 次の評価までにやることを3つ決め、上司に共有する(シーズン42のしめくくり)

## Season 43 — Influence at Scale for Programs (631–645)
631 From Persuading One to Moving Many | Self-awareness | 動かしたい人を「1人」ではなく「グループ」で書き出す
632 Narratives That Travel | Social awareness | プログラムの目的を、他の人がそのまま転送できる1段落にする
633 Influence Through Rhythm | Self-management | 関係者が予想できる決まったリズムで情報を出す計画を立てる
634 Finding the Key Influencers | Social awareness | 周りが意見を聞きにいく人を3人見つけて書き出す
635 Bringing Skeptics Inside | Relationship management | 一番慎重な人に、計画の一部をレビューしてほしいと頼む
636 Shared Language Across Teams | Social awareness | チームによって意味が違う言葉を1つ見つけ、定義を書く
637 Making It Easy to Say Yes | Relationship management | 相手がすぐ判断できるよう、選択肢と期限をそえてお願いを送る
638 Using Data to Move Groups | Self-management | 関係者全員が見る指標を1つ選び、毎週同じ形で見せると決める
639 Influencing Through Other Leaders | Relationship management | 話を広めてくれる人に、そのまま使える要点を3つ渡す
640 Town Halls and Big Audiences | Self-management | 大人数に向けて伝えたい一言を決め、英語で声に出す
641 Handling Organized Resistance | Relationship management | 反対しているグループの共通の心配ごとを1つ見つけ、答えを用意する
642 Favors Across Teams | Relationship management | 最近助けてもらったチームに、こちらから役立つ情報を1つ送る
643 Influence Without Overreach | Self-awareness | 自分が強く押しすぎていないか、信頼できる同僚に聞く
644 Measuring Your Influence | Self-awareness | この1か月の自分の提案が、どれだけ採用されたかを振り返る
645 Moving a Whole Organization | All four | 今のプログラムで多くの人の行動を変えるための次の一手を1つ書く(シーズン43のしめくくり)

## Season 44 — The Program Manager's Toolkit (646–660)
646 Program Governance Made Simple | Self-management | 自分の仕事で「誰が何を決めるか」を1枚の表にする
647 RACI Without the Bureaucracy | Relationship management | 1つの作業について、実行・責任・相談・報告の担当を関係者と確かめる
648 Dependency Maps | Social awareness | 自分の仕事が待っている他チームの作業を、矢印で図にする
649 Critical Path Thinking | Self-management | 計画の中で、遅れると全体が遅れる作業を1つ見つける
650 Integrated Program Plans | Self-management | 複数チームの予定を1つのタイムラインに並べてみる
651 Workstreams and Leads | Relationship management | 大きな仕事を3つの流れに分け、それぞれの担当候補を書く
652 Program Dashboards | Self-management | 進み具合が一目で分かる指標を3つ選んで並べる
653 Change Requests and Control | Self-management | 途中で来た変更依頼に、時間・人・品質への影響を書いてから返事をする
654 Capacity Planning | Social awareness | チームの来月の空き時間を、ざっくり「人数×日」で数える
655 Program Cadence | Self-management | 毎日・毎週・毎月の確認の場を、1枚に整理する
656 Escalation Paths | Relationship management | 困ったときに誰にどの順で相談するかを書き、上司と確認する
657 Running a Planning Session | Relationship management | 次の計画会議で、各チームに「一番の心配ごと」を一つずつ聞く
658 Program Closure and Handover | Self-management | 終わった仕事を1つ選び、学びと引き継ぎ先を書いて正式に閉じる
659 Tools Serve People | Self-awareness | 管理ツールで誰も見ていない項目を1つ見つけ、減らす
660 A Program Manager's Toolbox | All four | このシーズンで学んだ道具から、明日も使うものを3つ選ぶ(シーズン44のしめくくり)

## Season 45 — Preparing for People Management as an IC (661–675)
661 Studying Great Managers | Social awareness | 尊敬する上司の行動を1つ選び、なぜ効いているのかを書く
662 What Managers Actually Do All Day | Social awareness | 上司に「一番時間を使っていることは何ですか?」と聞く
663 Managing Yourself First | Self-management | 自分の1週間の時間の使い方を見直し、1つ改善する
664 Onboarding a New Teammate | Relationship management | 新しく入った人に、最初の1週間で役立つことを1つ教える
665 Mentoring Someone Junior | Relationship management | 後輩に15分の時間をとり、困っていることを聞く
666 Delegation Practice as an IC | Self-management | 誰かに任せられる仕事を1つ選び、目的と期待を伝えて頼む
667 Feedback That Helps Peers Grow | Relationship management | 同僚に伝えにくいことを1つ準備し、声に出して練習してから伝える
668 A 1:1 from the Other Side | Social awareness | 後輩との会話で、相手が話す時間を7割にしてみる
669 Noticing Team Health | Social awareness | チームの雰囲気を1〜5で点数をつけ、その理由を1つ書く
670 Fairness and Favoritism | Self-awareness | 自分がつい頼みがちな人と、声をかけていない人を書き出す
671 Leading a Team Ritual | Relationship management | チームのふり返りや朝会の進行を、一度自分から引き受ける
672 Interviewing Candidates | Social awareness | 面接官として聞きたい質問を、過去の行動を聞く形で3つ書く
673 The Manager's Emotional Load | Self-awareness | 上司が抱えている重さを想像し、一言ねぎらいを伝える
674 Lessons from a Manager's First Year | Relationship management | 上司かメンターに「マネージャー1年目で一番大変だったこと」を聞く
675 Ready to Lead People | All four | 将来マネージャーになったら大切にしたいことを3つ書く(シーズン45のしめくくり)

## Season 46 — Personal Brand and Sharing What You Learn (676–695)
676 What a Personal Brand Really Is | Self-awareness | 同僚3人に、自分を一言で表すと何かを聞く
677 Knowing What You Stand For | Self-awareness | 仕事で大切にしている価値を3つ書き、一番大事な1つを選ぶ
678 Your Expertise in One Line | Self-management | 「I help teams…」で始まる1文を作って声に出す
679 Writing Short Posts at Work | Self-management | 学んだことを1つ、5行の社内投稿にまとめて出す
680 Turning Lessons into Stories | Self-management | 最近の失敗か成功を、始まり・山場・学びの3文で書く
681 Starting a Simple Newsletter | Self-management | 書いてみたいテーマを5つ書き、最初の1本のタイトルを決める
682 Writing in English for a Wider Audience | Self-management | 日本語で書いたメモを1つ、短い英語の投稿に書き直す
683 Lightning Talks | Self-management | 5分で話せるテーマを1つ選び、話の骨組みを3つの点で書く
684 Speaking at a Meetup | Self-awareness | 社外の勉強会やミートアップを1つ調べ、登壇の条件を確認する
685 Rehearsing a Talk Out Loud | Self-management | 5分の話を一度通しで声に出し、時間を測る
686 Teaching a Lunch-and-Learn | Relationship management | 自分が教えられることを1つ選び、社内勉強会の案をチームに出す
687 Teaching Makes You Learn | Self-awareness | 人に説明してうまく言えなかった部分を1つ書き出し、調べ直す
688 Making Simple Visuals | Self-management | 説明したい考えを、箱と矢印だけの図1枚にかく
689 Handling Public Feedback | Self-management | 投稿や発表へのコメントを1つ選び、感謝と一言の返事を書く
690 Sharing Without Oversharing | Self-awareness | 発信する前に、社外秘や個人の情報が入っていないか確認する
691 Consistency Over Virality | Self-management | 発信の頻度を決めて、次の予定をカレンダーに入れる
692 Lifting Others Up | Relationship management | 同僚の良い発信を1つ見つけ、具体的な感想と一緒に紹介する
693 Starting a Learning Circle | Relationship management | 同じテーマに興味のある人に声をかけ、小さな集まりを提案する
694 Your Brand Across Tokyo and Seattle | Social awareness | シアトルの人が自分の名前を聞いて思い浮かべてほしいことを1文で書く
695 A Voice Worth Following | All four | この1か月で発信したことを振り返り、次に届けたいテーマを1つ決める(シーズン46のしめくくり)

## Season 47 — Thinking Like a Program Manager (696–710)
696 From Projects to Programs | Self-awareness | 自分の仕事を「プロジェクト」と「プログラム」の視点で書き分ける
697 Systems Thinking | Social awareness | 1つの問題に関わるチームと流れを図にする
698 A Roadmap People Believe | Relationship management | ロードマップに「なぜこの順番か」を1行ずつ添える
699 Prioritizing When Everything Matters | Self-management | 優先順位の基準を3つ決めて共有する
700 Metrics That Matter | Social awareness | 成功を測る指標を1つ選び、関係者と合意する
701 Program-Level Risk | Self-management | 複数のプロジェクトにまたがるリスクを1つ見つける
702 A Week in Seattle | Self-awareness | 出張先で会った人に「このチームで成功するには?」と聞く
703 Trust Across Cultures, Face to Face | Relationship management | シアトルの相手と仕事以外の話を1つする
704 Change Management for Programs | Relationship management | 変化を受け入れてもらうために関係者ごとの伝え方を書く
705 Trade-Offs Out Loud | Relationship management | 「これを選ぶと何をあきらめるか」を言葉にして伝える
706 Writing a Program Charter | Self-management | 目的・範囲・成功の基準を1ページにまとめる
707 Communicating Strategy | Social awareness | 戦略を同僚が自分の言葉で言い直せるか確かめる
708 Running a Program Review | Relationship management | 定例レビューで判断が必要な点だけを先に出す
709 A Program Communication Plan | Self-management | 誰に何をいつ伝えるかを1枚の表にする
710 Seeing the Whole Board | All four | 全体を見て判断できたことを1つ振り返る(シーズン47のしめくくり)

## Season 48 — The Road to Seattle (711–730)
711 Judgment Is a Human Skill | Self-awareness | AIの答えを使う前に自分の判断を1行書く
712 Deciding Under Uncertainty | Self-management | 決める前に「何が分かれば決められるか」を書く
713 Ethics in Everyday Work | Self-awareness | 迷った場面で「誰に見られても平気か」を考える
714 Building Your Case for a US Role | Relationship management | 成果と影響を数字つきで5つまとめる
715 Telling Your Sponsor What You Want | Self-management | マネージャーとスポンサーに「シアトルでProgram Managerを目指したい」と伝える
716 Preparing for the Interview Loop | Self-management | STARの話を数字つきで1つ書いて声に出す
717 Interview Day Nerves | Self-management | 面接や発表の前に自分を名前で呼んで励まし、最初の一文を声に出す
718 Humility | Self-awareness | 自分が間違っていたことを1つ認める
719 Curiosity | Social awareness | 意見の違う人に「どうしてそう思うの?」と聞く
720 Waiting for the Answer | Self-management | 結果を待つ間の不安を名前にして、今できることを1つする
721 The Offer | All four | うれしさも不安も言葉にして、支えてくれた人に伝える
722 Saying Goodbye to Your Tokyo Team | Relationship management | お世話になった人に具体的な感謝を伝える
723 Handing Off Tokyo | Relationship management | 引き継ぎ資料を作り、後任と一緒に確認する
724 Building Relationships Before You Arrive | Relationship management | 新しいチームの人に自己紹介のメッセージを送る
725 First Week in Seattle | Self-awareness | 新しい場所で驚いたことを3つ書く
726 Culture Shock in the First Month | Self-management | 戸惑ったことを1つ、相手の文化から考え直す
727 Your First Program Review in Seattle | Self-management | 最初のレビューで伝える結論を1文で用意して声に出す
728 Your First 90 Days as a Program Manager | Self-management | 最初の90日でやること(関係づくり3つ・小さな成果1つ・学ぶこと1つ)を書く
729 Looking Back with Daniel | All four | 1年で一番変わった習慣を1つ書く
730 The Human Curriculum: Next, People Manager | All four | 次の目標(ピープルマネージャー)への最初の一歩を1つ決める(番組の最終回)
