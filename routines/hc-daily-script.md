# Human Curriculum 毎日台本作成（このチャットで回す版）

## 作業場所（このチャットで回すための変更・2026-10-09）
- このチャットの /home/user/claude は note のブランチ（claude/vigilant-gates-tewzrg）で使っているので、切り替えない。episodes ブランチは別の作業ツリーで扱う：
  cd /home/user/claude && git fetch origin episodes && (git worktree add /home/user/episodes-wt origin/episodes 2>/dev/null || true) && cd /home/user/episodes-wt && git checkout -B episodes origin/episodes
- 以下の手順はすべて /home/user/episodes-wt で行う（「準備」の 1〜2 は、この手順で置き換える）。

YouTube番組「Human Curriculum」の台本を、毎日0時と12時(日本時間)のYouTube公開に間に合うよう先に作ってpushしてください。投稿そのものはGitHub側(リポジトリ変数 AUTO_UPLOAD=true のスケジュール実行が、未投稿の回を1話ずつアップロードし、0時・12時に順番に公開=1日2話。スケジュール実行は episodes ブランチを使う)が行うので、このタスクではGitHub Actionsを起動しない(workflow dispatch や gh api -X POST .../dispatches は使わない)。

## 準備
1. 作業ディレクトリに risakwmr/claude がなければ、add_repo ツール(owner: risakwmr, repo: claude, access: push)で追加し、その結果の手順でcloneする。
2. ブランチ episodes を使う(main は使わない・プルリクエストは作らない):
   git fetch origin episodes && git checkout -B episodes origin/episodes
3. README.md、episodes/plan.md(全730話=1年分の企画表、ストーリーの流れ、「Storytelling」の書き方ルール、「Characters」の登場人物設定)、episodes/ideas.md(確認済みの研究ネタ帳)、episodes/episodes.json、published.json、直近の台本2本(番号が最大の2本)とその日本語訳(epNN.ja.txt)と映像の演出ファイル(epNN.visual.json)と Shorts の指定(epNN.short.json)、src/scenes.py と src/make_short.py の冒頭の説明を読み、形式・口調・話の流れ(前回のチャレンジ・次回予告・登場人物の状況)をつかむ。

## 前回の自動投稿の確認(読むだけ)
- gh api 'repos/risakwmr/claude/actions/runs?per_page=5' で workflow「Make and upload episodes」の直近の実行を見る。直近の実行が failure なら、失敗したステップ名を gh api で調べて最後の通知に含める(再実行はしない)。run_status.json に各操作の最後の結果(字幕・プレイリストなどのエラー)が残るので、それも確認する。

## 何話書くか
- 「台本あり・未投稿」= episodes.json にあって published.json に無い回。
- その数が4未満なら、episodes/plan.md の番号順で台本がまだ無い回を最大2話まで作る(1回の実行で2話まで)。4以上なら新しく書かない。
- plan.md の全730話の台本が揃っていれば書かない。

## 企画
- 各回のタイトル・EQ領域・今日のチャレンジは episodes/plan.md の該当行に従う(日本語メモを英語の台本に自然に落とし込む)。
- 番組全体のねらい:AIにできない人間の力とEQ、他部署(xFN)との協業、仕事の効率、行動経済学とマーケティング、英語のスピーキング。1年かけて聞き手がSenaと一緒に毎日少しずつ成長する。聞いた人が「今日の仕事ですぐ試せる」ことを大事にする。主なターゲットは海外の視聴者で、日本人の英語学習者も聞き手に含まれる。
- plan.md の「Story arc」と「Characters」に従って登場人物の状況・役職・趣味・小ネタをそろえる(Senaは第721話のオファーまで東京のAssociate、その後シアトルでProgram Manager。部下は持たない。ピープルマネージャーは次の目標として最終回で予告)。趣味や小ネタは毎回出さず、場面に合うときに軽く使う。季節や行事など、時間の流れも自然に入れる。
- plan.md の「Storytelling」の節(第16話から:コールドオープン、シーン、続いていく話の糸、Shorts 用のハイライトなど)にも必ず従う。このプロンプトと食い違うところは plan.md を優先する。
- 各シーズンの最終話(plan.md の各見出しの範囲の最後の回)はシーズンのしめくくりにして、次のシーズンの最初の回を予告する。730話だけが番組の最終回。
- episodes/bonus/ に下書きがある回はテーマが合えば参考にしてよい(そのまま使わず、今のルールと流れに合わせて書き直す)。

## 台本のルール
- 登場人物:SENA(Sena Sato、東京のAssociate・IC、1年後にアメリカでProgram Manager、その後ピープルマネージャーを目指す。慎重で空気を読む、メモを取る。英語はリスニングよりスピーキングが苦手で、練習中。1年かけて少しずつ上達する)と DANIEL(Daniel Reed、シアトルのシニアPeople Manager、8人のチーム、温かく率直、研究好き、自分の失敗談を正直に話す)。2人はメンタリング中。
- 英語。1行1発言で「SENA: 」「DANIEL: 」で始める。ト書き・記号・見出し・空行は入れない。同じ話者の行を2行続けない。2,000〜2,400語(約14〜15分、wc -w で確認)。「1:1」は台本内では「one-on-one」と書く(音声読み上げのため)。
- 話すスピードはネイティブの自然な速さ(コードの標準設定)。新しい回の episodes.json に voice_rate や turn_gap は付けない(これはEP1〜15の字幕タイミングを合わせるためだけのもの)。
- 流れ:(第16話からは先頭にコールドオープン)→ 前回のチャレンジの振り返り(前の回の台本のチャレンジと予告に合わせ、「やってみてどうだったか」を具体的に)→ Senaの今日の具体的な場面 → 研究 → なぜAIにはできないか → Danielの失敗談(過去の回と同じ話にしない)→ 日本とアメリカの職場文化の違い → その回のEQスキル(領域名を明示)→ Speaking Lab → 今日のチャレンジ → 次回予告(plan.md の次の回)。
- 「今日のチャレンジ」:その日のうちに仕事で試せる、1つの具体的な行動。「this week」ではなく「today」と言う。Danielが「Today's challenge」と言って紹介し、Senaが自分ならどうやるかを一言で言う。
- Speaking Lab(毎回、チャレンジの直前、合計150〜250語。Versantの出題形式に近い練習で、セリフだけで進める):
  1. Repeat:Danielが「Speaking Lab」と言って始め、その回のテーマに関係する仕事で使える英文を3つ(各8〜14語)言う。Danielの行は引用符で囲んだその英文だけにし、次のSenaの行はまったく同じ英文(引用符なし)にする(映像で自動的に大きく表示され、聞き手が声に出す無音の時間が入るため。概要欄の「今日の英語フレーズ」にも自動で載る)。Danielが聞き手に「Pause and say it out loud.」のように声に出すよう促す。
  2. Retell:DanielがSenaに今日の要点を約30秒でまとめてもらう。Senaが自分の言葉で60〜80語で言い直す(言いよどみを直しながらでもよい)。
  3. Your turn:Danielが「Listeners, your turn. In forty seconds, answer this. <質問>? Pause the audio and speak.」の形で、聞き手向けに40秒で答える意見の質問を1つ出す。この質問は動画の公開後にコメント欄へ自動で投稿されるので、「In forty seconds, answer this.」のあとに「?」で終わる質問文を置く形を必ず守る。
- 研究は最低2つ。まず episodes/ideas.md から合うものを選び、それ以外も WebSearch で探してよい。どちらも WebFetch で実際に原典または信頼できる要約ページを開いて、数字・年・著者を確認したものだけを使う。確認できない数字・出版社名などは使わない。過去の回(episodes.json の sources を確認)と同じ研究を主役にしない。ideas.md の注意書き(小規模、再現性に問題など)は台本でもそう言う。医学的な断定はしない。強いストレスには専門家への相談を勧める一言を入れてよい。使った ideas.md の行には「(used in epNN)」を付け足す。新しく確認した良い研究は ideas.md に同じ形式で追記してよい。
- 実在の人物のセリフを作らない。Sena と Daniel は架空の人物。過去の回に出た脇役の名前(plan.md の Characters と過去の台本を grep して確認)を別人に使い回さない。新しくDanielの失敗談に人を出したら、plan.md の「Daniel's past」の行に名前と回を足す。
- ビザや移住の手続きについて具体的な助言はしない。
- 2話書くときは、サブエージェントで並行して書いてよい(各自に上のルール、plan.md の該当行と Story arc と Storytelling と Characters、前の回のチャレンジ・予告を渡す。2話目の担当には1話目のチャレンジと予告の内容も渡す)。終わったら2話の間で名前や設定の食い違いがないか確認する。

## 日本語字幕(必ず作る)
- 各回の台本と一緒に、日本語訳 episodes/epNN.ja.txt(100話以降は epNNN.ja.txt)を作る。英語台本と同じ行数・同じ順番・同じ話者で、各行を「SENA: 」「DANIEL: 」+自然な日本語訳にする(1行に1発言、空行なし)。これがYouTubeの日本語字幕(CC)として自動でアップされる(英語字幕は台本から自動で作られる)。
- 訳し方:直訳ではなく、自然で読みやすい日本語。Senaはていねい語(〜です・〜ます)、Danielは温かいくだけた話し方(〜だね・〜だよ)。人名はカタカナ(セナ、ダニエル、加藤さん、リョウさん、ケンタさん、マークさん、ローラさん、ハンナさん)。研究者名はカタカナ、論文誌名は英語のまま『』で囲む。Speaking Lab の繰り返し文は意味を訳す(「」で囲んでよい)。
- 確認:英語と日本語の行数と話者の並びが一致すること(python で比較)。

## 映像の演出と Shorts(必ず作る)
- 各回の episodes/epNN.visual.json(100話以降は epNNN.visual.json)を作る。形式は src/scenes.py の冒頭の説明と、直近の回の visual.json に合わせる。
- 1話あたり25〜40個の cue。台本の流れに合わせて section を付ける(Cold open / Last time / Today / Research / Why AI can't / Daniel's story / Japan & US / EQ skill / Speaking Lab / Today's challenge / Next time。シーズン最終話は振り返りも)。section はYouTubeのチャプターにもなる。
- board は話の内容に合わせて切り替える:大事な言葉・数字は keyword、研究は study(who・stat・text・note に注意書き)、日米比較は compare、手順や要点は list、Danielの失敗談は story、聞き手への40秒の質問は question、チャレンジは challenge、冒頭と最後は cover。文字は短く(keyword は2〜8語)、台本に出てきた事実だけを書く。Speaking Lab の繰り返し文は自動で出るので cue を書かない。
- sena / daniel のポーズ(上半身のイラスト)を場面の気持ちに合わせて変える(使える名前は src/scenes.py の SENA_POSES / DANIEL_POSES)。同じポーズばかりにしない。
- icon / icons はフリーのイラスト(Fluent Emoji 3D)。名前は assets/icons/INDEX.txt にあるものだけを使う(大文字小文字は自由)。
- plan.md の Storytelling にある Shorts 用ハイライトを episodes/epNN.short.json に書く(形式は plan.md と src/make_short.py の説明どおり。行番号は python で確認)。
- 確認:python で全 cue の line が台本の行数以内、ポーズのファイル assets/characters/full/sena_<名前>.png・daniel_<名前>.png が存在、icon 名が INDEX.txt にあることを確かめる。

## episodes.json に追加する項目
number, script(epNN.txt。100話以降は epNNN.txt), title, short_title(30文字程度まで), summary(英語3〜4文。最後の文は「Today's challenge: ...」), practice(今日のチャレンジ。英語), sources(「著者 (年), タイトル, 掲載誌」の形。先頭3つがサムネの本の背表紙に出るので、主な研究を先に並べる), tags(10個程度。EQ, emotional intelligence, career, leadership, program manager, audiobook, English learning, English speaking を含める)。
英語の表示用(必ず付ける。海外の視聴者が見るYouTubeのタイトルと概要欄になる。既存の回の書き方に合わせる):
- yt_title:YouTubeの英語タイトル。番組名や回番号は付けない(自動で「| English Podcast EPNN」が付く)。視聴者の悩みや知りたいことを平易な言葉で、検索されやすく、60文字程度まで。
- hook:英語の概要欄の最初の2行。1行目はその回の場面を使った共感できる状況や問いかけ、2行目はこの回で何ができるようになるか。改行(\n)で区切る。
- points:「In this episode」に並ぶ3〜4個の英語の要点(研究・ダニエルの話・日米比較など、台本に出てきた事実だけ)。
日本語の表示用(必ず付ける。YouTubeの表示言語が日本語の人には、タイトルと概要がこの日本語で表示される):
- title_ja:自然な日本語タイトル(直訳でなくてよい)。
- hook_ja:日本語の概要欄の最初の2行(「もっと見る」を押す前に見えるのはここだけなので一番大事)。1行目は、その回の場面を使った共感の問いかけ(例:「「何か問題あった？」…会議で10秒、誰も話さない。そんな沈黙、あなたのチームにもありませんか？」)。2行目は、この回で何ができるようになるか+「英語で学ぼう🎧（日本語字幕あり）」のような一言。2行は改行(\n)で区切る。毎回言い回しを変え、同じ型のコピペにしない。
- points_ja:「この回でわかること」3〜4個のリスト(各40文字程度まで。思わず聞きたくなる言い方で。台本に出てきた事実だけ)。
- summary_ja:日本語の概要3〜4文(場面・紹介する研究・ダニエルの話・日米比較を簡潔に)。
- practice_ja:今日のチャレンジの日本語(1〜2文)。
- 概要欄の英語フレーズ、目次、次回予告、全話プレイリストへのリンクは自動で入る。
サムネ用の予備(src/thumbnail.py、README参照):thumb_accent(サブタイトル中のコーラル斜体にする1語)、thumb_notes(手書きメモ3〜4個、各20文字程度までの英語)、thumb_cup(カップの手書き、3〜4語の英語で今日のチャレンジを表す)、thumb_pose(assets/characters/poses/ から場面に合うもの)。タイトルに「: 」が無い場合は thumb_sub も付ける。番号順に並べて保存。
サムネの本命は、ユーザーが ChatGPT で作る画像 episodes/epNN_thumbnail.png(あればそれがそのまま使われる)。無い回は上の予備設定で自動作成される。100話以降のファイル名の付け方は src/ のコードと README を確認して合わせる。

## 確認とpush
1. python3 -m py_compile src/*.py。依存が足りなければ pip install --break-system-packages -r requirements.txt。
2. 新しく書いた各回で python3 src/fetch_icons.py NN を実行してイラストを取得し、python3 src/make_episode.py NN --fake-tts --lines 6 --out /tmp/check を実行して読み込みと描画を確認(1話に数分かかるので、Bashのtimeoutは長めにする)。続けて python3 src/make_episode.py NN --fake-tts --audio-only --out /tmp/checkja を実行し、出力に ja_srt と chapters のパスが出ることを確認。
3. 全行が「SENA: 」か「DANIEL: 」で始まること、語数、Speaking Lab と「Today's challenge」が入っていること、日本語訳の行数・話者が英語と一致すること、visual.json と short.json の確認、episodes.json が正しいJSONで yt_title・hook・points・title_ja・hook_ja・points_ja・summary_ja・practice_ja があることを確認。google のライブラリが無くても動くよう、google 系モジュールをダミーにして src/upload.py を import し、speaking_phrases(ep) が3つのフレーズ(英語と日本語の両方が空でない)を返すこと、episode_question(ep) が「?」で終わる質問を返すことも確かめる。
4. assets/icons/ の新しいpngはコミットしない(GitHub側で毎回取得する)。それ以外をコミットして git push -u origin episodes(コミットメッセージは英語で簡潔に)。push前に git pull --rebase origin episodes で最新にする。

## 通知（このチャットで回すための変更・2026-10-09）
- 通知は出さない。PushNotification・SendUserMessage・SendUserFile は使わない。
- 新しい台本を書いた、または前回の自動投稿が失敗していた場合は、このチャットに日本語で短く報告する：書いた回の番号とタイトル、今日のチャレンジ、使った研究、次に公開される予定の回、失敗があればそのステップ名。
- 新しい台本を書いたときは、続けてこのチャットに、各回の ChatGPT 用サムネ画像プロンプト（英語）をコードブロックで書く（形式は下の元の指示のとおり）。
- サムネ画像プロンプトの保存（2026-10-10 本人）：書いた各回のプロンプトを、
  1. episodes ブランチの episodes/thumbnail_prompts.md の末尾に「## EPNN｜<title>」＋コードブロックで追記し、台本と同じコミットに入れる。
  2. Googleドライブの「Claudeの記憶（セナ）/06_Human Curriculum台本」フォルダ（id: 1hhBZAGfXAnRbJfzMEZUjCUxEWRzL-PGC）に、Google Drive の create_file（contentMimeType: text/markdown）で「EPNN｜サムネ画像のプロンプト」という新しいドキュメントとして置く（既存ドキュメントは編集できないので回ごとに1つ。本文はチャットに出すのと同じ一言＋コードブロック）。作ったら、チャットの報告にリンクを1行添える。
- 何も書かず、失敗も無かった場合は、このチャットに「台本は足りているので今回は書きませんでした」と1行だけ書く。

（以下は元の「通知」の節。届け方だけ上の変更に従い、プロンプトの形式は従う）
## 通知
- 新しい台本を書いた、または前回の自動投稿が失敗していた場合は、PushNotification で日本語で短く報告:書いた回の番号とタイトル、今日のチャレンジ、使った研究、次に公開される予定の回、失敗があればそのステップ名。
- 新しい台本を書いたときは、各回について ChatGPT 用のサムネ画像プロンプト(英語)を、通知とは別に SendUserMessage でコードブロックにして送る。必ず次の形式に従う(EP番号・タイトル・場面・小物の文字だけ回ごとに変える。場面は机・ノートPC・コーヒーカップ・ノート・座った姿・ビデオ通話を避け、体の動き+環境+視覚的なたとえで、直近の回と違う向き・カメラアングルにする。既存の episodes/epNN_thumbnail.png を数枚見て、同じポーズ・構図を繰り返さない):
16:9 YouTube thumbnail, soft watercolor anime illustration, warm natural light, editorial collage style on cream textured paper with torn edges and coral and blue brush strokes.
Character (keep identical in every episode): Sena, a young Japanese woman, long wavy light-brown hair, sunglasses perched on her head, small gold hoop earrings, oversized soft pink knit sweater, cream wide-leg trousers.(Danielが出る回は追加:Daniel, late 30s, curly brown hair, light blue shirt with rolled sleeves, company lanyard, navy mug, a golden retriever with a navy bandana.)
Scene: <その回の場面とSenaの動きのあるポーズ・カメラアングル>.
IMPORTANT: DO NOT default to a desk, laptop, coffee cup, notebook, or seated office scene.
The protagonist must be physically active or visually interacting with the environment.
Prioritize strong physical storytelling: walking, running, climbing stairs, opening a door, crossing a bridge, looking through a window, carrying objects, reaching, turning, balancing, following a route, standing in a large environment, interacting with oversized conceptual objects, talking while walking, or moving through a public space.
The Mac/laptop should NOT be the main visual focus. A laptop may appear only as a secondary environmental detail when necessary.
Avoid repetitive:
- sitting at a desk
- typing on a laptop
- writing in a notebook
- holding a coffee cup
- video-call composition
- pointing at text
Every episode should communicate the concept through BODY MOVEMENT + ENVIRONMENT + VISUAL METAPHOR.
The viewer should understand what the character is DOING, not simply what she is LOOKING AT.
Make the pose dynamic, natural, and editorial rather than static, posed, or like a corporate illustration.
Use a substantially different body orientation and camera angle from recent episodes.
Text, left side, large navy serif: "<メインタイトル>". Below in navy serif with "<強調語>" in coral italic: "<サブタイトル>". Top left small: "The Human Curriculum". Coral label: "EPISODE NN".
Small details: handwritten notes <2〜3個>; a pink sticky note "<今日のチャレンジを3〜4語で>"; three stacked books with spines <研究者名3つ>.
  プロンプトの前に一言「ChatGPTで作ってこのチャットに送ってね(できた回の前の画像を添付すると絵柄がそろいます)」と日本語で添える。
- 何も書かず、失敗も無かった場合は通知しない。