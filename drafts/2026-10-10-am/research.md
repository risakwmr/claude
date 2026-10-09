# research｜2026-10-10-am

※ どの研究も「平均の傾向」で、個人には当てはまらないことがある。研究から Sena 個人の理解力・特性（ADHD、知能検査の結果など）を推測しない。
※ 「確認済み」＝論文本文・抄録・著者所属機関のページのどれかで自分で読んだ数値。それ以外は「未確認」と書いた。

## 問いごとの答え

### 問い1：Bisra ら (2018) 自己説明のメタ分析

- 分かっていること：
  - 学習中・問題を解いている最中に「自分で説明するよう促された（prompt）」学習者と、促されなかった学習者の学習成果を比べたメタ分析。64の研究報告から69の効果量、全体の効果量は g = .55（ランダム効果モデル）。brief の数値はすべて原文と一致した。
  - 促し方の形式（inducement format）で分けると、「質問の形で促す（interrogative：例「なぜ〜？」と問う）」は g = .559（k = 36）。ただし**形式どうしの比較では、事後検定で有意な差は見つからなかった**（全体の比較は p = .048 だが、どの形式が他より優れているとは言えない）。→「質問形式が一番効く」とは書けない。「質問の形で促した研究でも、効果は全体とほぼ同じ大きさだった」まで。
  - 選択式（multiple choice）の促しは g = .24 で有意でない（k = 2 と少ない）。
  - **自分の理解度や取り組み方を振り返らせる促し（metacognitive：「自分はどこまで分かっているか説明して」型）は g = .19 で有意でなかった（k = 3）**。中身（概念・仕組み）を説明させる促し（conceptualize g = .87、k = 13）より効果が小さかった（事後検定で有意差）。→ AIに質問させるなら「私は分かってる？」より「なぜそうなる？」「これはどういう意味？」の方向が、研究の結果に近い（ただし AI を使った研究ではない）。
  - 比較条件によって効果の大きさが違う：比較群に何も追加の説明がない場合 g = .67、比較群に「教える側が用意した説明」を渡した場合でも g = .35 で自己説明のほうが上。
  - 時間の問題：自己説明のほうが学習時間が長かった研究（g = .72）と同じ時間だった研究（g = .41）で有意差はなかった。ただし多くの研究が時間を報告しておらず、著者は「効果が大きく見積もられている可能性がある」と書いている。
- 対象者：
  - 学校段階で分類されていて、**小学校（k = 10、g = .48）／高校（k = 13、g = .43）／学部生（k = 42、g = .61）／専門職課程（professional program、k = 4、g = .68、95%CI .11〜1.25）**。年齢は元の研究で報告されないことが多く、学校段階で代用したと書かれている。段階どうしで有意差なし。
  - **社会人・職場の学習（研修など）を対象にしたカテゴリはない**。大人で一番近いのは学部生と専門職課程（4研究のみ、信頼区間が広い）。
  - 地域は北米42件・欧州18件・東アジア6件など。
- 根拠：Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. 2018『Inducing Self-Explanation: a Meta-Analysis』Educational Psychology Review 30(3), 703–725（種類：meta-analysis／査読済み）
  - 確認した場所：論文本文（出版版のPDFの写し）https://www.gwern.net/doc/psychology/spaced-repetition/2018-bisra.pdf （抄録・表1・表2・表3・表7・考察を読んだ）。書誌は https://api.crossref.org/works/10.1007/s10648-018-9434-x
  - 使える数値：
    - 「64の研究報告、69の効果量、参加者5,917人」（確認済み）
    - 「全体 g = .55（95%CI .45〜.65）」（確認済み）
    - 「質問の形で促した研究：g = .56（k = 36）。ただし促し方の形式どうしで有意差なし」（確認済み）
    - 「自分の理解度を振り返らせる促し（metacognitive）：g = .19、有意でない（k = 3）」（確認済み）
    - 「学校段階：小学校 .48／高校 .43／学部生 .61／専門職課程 .68（k = 4）」（確認済み）
    - 「教える側の説明を渡した比較群より上回った：g = .35」（確認済み）
- 限界・注意：
  - **学習課題（文章を読む、問題を解く、例題を学ぶ）の研究で、職場の知識・自分の業務の理解を調べたものではない**。AIに促される研究でもない（人や教材が用意した促し）。
  - 「g = .55」は記事では「中くらいの効果」程度の言い換えが無難。著者は効果を「potentially powerful（大きな効果になりうる）」と表現。
  - 時間をかけた分の効果が混ざっている可能性（著者の指摘）。
  - 記事向けの言い換え例：「学習の研究をまとめた分析では、『自分で説明してみて』と促された人は、促されなかった人より平均して学習成果がよかった。ただし対象は学校や大学での学習で、仕事の知識を調べたものではない」。

### 問い2：説明の深さの錯覚（Rozenblit & Keil 2002）と Fernbach ら (2013)

- 分かっていること：
  - Rozenblit & Keil（2002）：10/9 pm の research.md（問い6）で抄録を確認済みの範囲を再利用。人は複雑な物事（機械・自然現象など）を実際より深く理解していると思いがちで、説明させるとそれに気づく。**この過信は「物事がどう動くか」の説明の知識で特に強く、事実・手順・出来事の流れ（ナラティブ）の知識ではずっと弱い**。12の研究からなる論文。
  - Fernbach ら（2013）：政治の政策（米国の政策）について、仕組みを詳しく説明させると、理解しているという自己評価が下がり、意見が穏やかになった。2つ目の実験では、この効果は「仕組みを説明させた」ときに出て、「賛成の理由を挙げさせた」ときには出なかった。3つ目の実験では、関連団体への寄付が減った。
  - **追試（重要）**：Crawford & Ruscio（2021、Psychological Science）が事前登録した3つの追試（実験2の追試2本：306人・405人、実験3の追試：343人）を行った。**「説明させると理解の自己評価が下がる」は再現された一方、「意見が穏やかになる」などの主要な効果は再現されなかった**。著者のまとめは「仕組みを説明させると自分の無知に気づきやすくなるが、政治的な意見を穏やかにする可能性は低い」。→ 今回の記事に必要なのは「説明しようとすると、分かったつもりに気づく」部分で、これは追試でも支持された。「意見が変わる」までは書かない。
- **仕事の知識（自分の業務や担当分野）に当てはまるか：研究からは言えない。**
  1. 対象は機械・自然現象（2002）と政策（2013、2021）。仕事の知識・自分の担当分野を対象にした研究は見つからなかった。
  2. 自分の業務の「何をしたか」は手順・出来事の流れの知識に近く、元の研究では錯覚が弱いとされた種類（10/9 pm の注意と同じ）。
  3. 使うなら、仕事の知識のうち「**なぜそうなるか（仕組み・因果）**」の説明に絞るのが元の研究に近い（例：なぜこの施策が効くと思うか、なぜこの数字が動いたか）。その場合も「研究の対象は機械の仕組みや政策で、仕事の知識を調べたものではない」と1文添える。
  - Senaの公開済みの理由（「理解しているつもりのことも『なんで？』と聞かれると意外に答えられない」）に近い現象として紹介するのは可。ただし「研究が Sena の体験を説明している」とは書かない。
- 根拠：
  - Rozenblit, L., & Keil, F. 2002『The misunderstood limits of folk science: An illusion of explanatory depth』Cognitive Science 26(5), 521–562（種類：個別研究（12研究）／査読済み）
    - 確認した場所：https://api.crossref.org/works/10.1207/s15516709cog2605_1 （抄録。10/9 pm で確認済み）
    - 使える数値：「12の研究」（確認済み）。効果の大きさは抄録になく未確認。
  - Fernbach, P. M., Rogers, T., Fox, C. R., & Sloman, S. A. 2013『Political extremism is supported by an illusion of understanding』Psychological Science 24(6), 939–946（種類：実験研究（3実験）／査読済み）
    - 確認した場所：https://api.crossref.org/works/10.1177/0956797612464058 （抄録）、https://www.psychologicalscience.org/journals/psychological-science/0956797612464058/ （学会のページの抄録）
    - 使える数値：「3つの実験」（確認済み）。**各実験の人数は未確認**（ブログの要約では実験1が米国在住198人・Mechanical Turk とあるが、本文は読めなかった）。
  - Crawford, J. T., & Ruscio, J. 2021『Asking people to explain complex policies does not increase political moderation: Three preregistered failures to closely replicate Fernbach, Rogers, Fox, and Sloman's (2013) findings』Psychological Science 32(4), 611–621（種類：事前登録の追試／査読済み）
    - 確認した場所：https://www.psychologicalscience.org/journals/psychological-science/0956797620972367/ （学会のページの抄録）
    - 使える数値：「3つの事前登録の追試、306人・405人・343人」（確認済み）
- 限界・注意：
  - Fernbach ら（2013）を「説明させると考えが柔らかくなる」の根拠に使わない（追試で再現されず）。
  - 「説明させると自分の理解の評価が下がる」は、理解の**自己評価**の変化で、実際の理解が深まったことを示したものではない。
  - AIに質問させる研究ではない。

### 問い3：AIに「答えさせる」のではなく「質問させる・ヒントを出させる」使い方の研究

- 分かっていること：
  - **研究はまだ少なく、対象はほぼ中高生・大学生。結果もそろっていない。**
  - Blasco & Charisi（2024、査読前）：高校生122人の無作為化実験。ソクラテス式（質問で導く）チャットボットは、関わり・やりとりを有意に増やしたが、**学習の向上は有意でなかった**。「役に立たない」と評価した生徒の割合が高かった。AIの手助けを外すと、内容を保持して新しい場面に応用するのが難しかった。→「質問させれば力がつく」とは言えない材料。
  - Bastani ら（2025、PNAS）：高校の数学の授業で約1,000人。ふつうのChatGPT型（GPT Base）は練習中の成績が48%上がったが、AIを外すとAIを使わなかった生徒より17%低かった。答えをすぐ言わないよう設計した「GPT Tutor」は練習中に127%上がり、AIを外したあとの悪影響を大きく和らげた。**公開済み #02 で主役として使われている**（下の「公開済み記事との重なり」）。今回は1行でつなぐだけにする。
  - 大学生のソクラテス式エージェントの研究（Xi ら 2025、Computers & Education）が検索で出たが、抄録を読めず、人数・無作為化かどうかを確認できなかった。使わない。
- **大人・職場を対象にした研究**：AIに質問させる（ソクラテス式）使い方を、社会人・職場の学びで調べた査読済み研究は**見つからなかった**。→ 記事では「大人や仕事の場面では、まだ研究で分かっていない」と書く。
- 根拠：
  - Blasco, A., & Charisi, V. 2024『The Impact of Large Language Models on Students: A Randomised Study of Socratic vs. Non-Socratic AI and the Role of Step-by-Step Reasoning』SSRN（種類：無作為化実験／**査読前（ワーキングペーパー）**）
    - 確認した場所：https://scale.stanford.edu/ai/repository/impact-large-language-models-students-randomised-study-socratic-vs-non-socratic-ai （スタンフォード大学 SCALE の研究データベースの要約）。SSRN の論文ページ（https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5040921 ）は開けず、**本文・抄録は読めていない**。
    - 数値：「高校生122人」（SCALE の要約で確認。論文本文では未確認のため**未確認**扱い）。年齢は「14〜18歳」（SCALE）と「14〜16歳」（検索結果の要約）で食い違い、未確認。国は未確認。効果の大きさの数値は要約になし。
  - Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. 2025『Generative AI without guardrails can harm learning: Evidence from high school mathematics』PNAS 122(26), e2422633122（種類：現場での無作為化実験／査読済み）
    - 確認した場所：https://api.crossref.org/works/10.1073/pnas.2422633122 （抄録）
    - 使える数値：「約1,000人の高校生」「GPT Base 練習中+48%、AIを外すと−17%」「GPT Tutor 練習中+127%、悪影響を大きく和らげた」（確認済み）
- 限界・注意：
  - Blasco & Charisi は査読前で、書くなら「まだ査読を経ていない研究ですが」と明記。対象は高校生。
  - Bastani らの「GPT Tutor」はヒントを出す設計で、「AIがユーザーに質問する」使い方と同じではない。
  - どちらも子ども・学校の研究で、Sena の読者（働く大人）にそのまま当てはめない。

### 問い4：「自分の考えを先に出してからAIに聞く」順番の研究

- 分かっていること：直接「チャットAIに『私はこう思ったんだけど、どう思う？』と聞く／最初から聞く」を比べた研究は見つからなかった。ただし**判断や学習の場面で「先に自分で決める・解いてからAIを見る」順番を調べた研究**はある。結果は「AIへの引っ張られ（過度な依存）が減る」方向だが、代わりに満足度が下がる・AIが正しいときにも同意しにくくなる、という両面がある。
  1. **先に自分の判断を記録してからAIの提案を見る（医療画像）**：Fogliato ら（2022）。獣医の放射線科医19人がX線画像の所見を判断。先に自分の暫定の判断を記録してからAIの提案を見た条件では、**AIの提案が正しいかどうかに関係なく、AIに同意しにくくなった**。AIの提案を「役に立たない」と感じやすく、AIと意見が違うときに同僚の意見を求めることも減った。作業時間は増えなかった。→「先に自分で考える」と引っ張られにくい。ただし、AIが正しいときにも採用しにくくなる、という代償つき。
  2. **AIの答えを見る前に考えさせる仕掛け（cognitive forcing）**：Buçinca ら（2021）。米国在住の大人199人（Mechanical Turk）が、食事の写真から炭水化物の多い食材を見つけて置き換える課題。AIは75%正しい設定。仕掛けは3種類（自分から押したときだけAIを表示／**先に自分で決めてからAIを見る（update）**／30秒待つ）。3つをまとめると、AIが間違っていたときに、ただ説明を見せる条件より AIに従ってしまう割合が減った（炭水化物の多い食材を見つける判断で約48% vs 約64%）。**ただし仕掛けを使った人ほどその設計を好まなかった**。効果は「考えることが好き（認知欲求が高い）」人で大きかった。「先に自分で決める」条件だけの結果は報告されていない（3条件の間に有意差なし）。それでも、AIを使わなかった人より、AIが間違えた問題での成績は低かった。
  3. **先に自分で解いてからAIの説明を見る（数学の学習）**：Kumar ら（2023、査読前）。1,200人の事前登録の実験。LLMの説明は、正解だけを見るより学習にプラスで、**先に自分で問題に取り組んだ人で効果が一番大きかった**。説明を見ると「たくさん学んだ」と感じ、テストを簡単に感じる傾向もあった（実際の成績とのずれに注意）。
  4. （参考・査読前で小規模）Kosmyna ら（2025）：小論文をLLMで書く群・検索で書く群・何も使わない群（計54人、4回目は18人）。4回目に「何も使わない → LLM」に切り替えた人は、記憶の想起が高かったと報告。脳波（EEG）中心の研究で、人数が少なく査読前。**記事の根拠には使わないほうが安全**（下の「使わないほうがよい情報」）。
- 根拠：
  - Fogliato, R., Chappidi, S., Lungren, M., Fisher, P., Wilson, D., Fitzke, M., Parkinson, M., Horvitz, E., Inkpen, K., & Nushi, B. 2022『Who Goes First? Influences of Human-AI Workflow on Decision Making in Clinical Imaging』FAccT '22（種類：ユーザー実験／査読済み（国際会議））
    - 確認した場所：https://arxiv.org/abs/2205.09696v1 （抄録。「FAccT 2022 採録」と記載）。著者名の一部は検索結果の書誌から（著者所属の Microsoft Research のページ https://www.microsoft.com/en-us/research/uploads/prod/2022/06/3531146.3533193.pdf にあり）。
    - 使える数値：「獣医の放射線科医19人」（確認済み）。効果の大きさは抄録になく未確認。
  - Buçinca, Z., Malaya, M. B., & Gajos, K. Z. 2021『To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making』Proceedings of the ACM on Human-Computer Interaction 5(CSCW1), Article 188（種類：オンライン実験／査読済み）
    - 確認した場所：https://www.eecs.harvard.edu/~kgajos/papers/2021/bucinca2021trust.shtml （著者所属機関のページ・抄録）、https://ar5iv.labs.arxiv.org/html/2102.09692 （arXiv版の本文）
    - 使える数値：「199人」（確認済み・著者ページ）。「AIの正答率75%の設定」「AIが間違ったときの過度な依存 約48% vs 約64%」（arXiv版本文で確認。出版版と同じかは未照合。使うなら「約半分 vs 約3分の2」程度の丸め方が無難）
  - Kumar, H., Rothschild, D. M., Goldstein, D. G., & Hofman, J. M. 2023『Math Education with Large Language Models: Peril or Promise?』SSRN（種類：事前登録の実験／**査読前**）
    - 確認した場所：https://www.microsoft.com/en-us/research/publication/math-education-with-large-language-models-peril-or-promise/ （著者所属の Microsoft Research のページ・抄録）
    - 使える数値：「1,200人」（確認済み）。参加者が大人かどうか・募集方法はページに書かれておらず未確認。
- 限界・注意：
  - どれも「チャットAIとの会話で、自分の考えを先に書く」ことを調べたものではない。判断課題（画像・食事）や数学の学習。
  - Fogliato は19人の獣医放射線科医、Buçinca は1つの簡単な課題で AI は作られたもの（正答率固定）。一般化は限られる。
  - 「先に自分で考えると引っ張られにくい」はあるが、「判断の質が上がる」とまでは言えない（AIが正しいときに同意しにくくなる、仕掛けがあってもAIなしより成績が低い場面がある）。
  - 記事向けの言い換え例：「先に自分の考えを書いてからAIの意見を見ると、AIの意見に引っ張られにくくなる、という実験はあります。ただし対象は画像診断や簡単な判断課題で、AIが正しいときにも採用しにくくなる面がありました」。
  - 「私はこう思ったんだけど、どう思う？」の使い分けや効果は、研究の結論として書かず Claude の提案として書く。

### 問い5：使わないほうがよい情報の確認
→ 下の「使わないほうがよい情報」にまとめた。

## 分かっていないこと

- AIに「質問させる」使い方が、**大人・職場の学びや仕事の理解**にどう影響するか。査読済みの研究は見つからなかった。
- AIに質問させると「説明の深さの錯覚（分かったつもり）」に気づきやすくなるか。AIを使ったこの種の研究は見つからなかった。
- 説明の深さの錯覚が、仕事の知識・自分の担当分野にも起きるか。研究は見つからなかった。
- 「自分の考えを先に書いてからチャットAIに意見を求める」順番そのものの効果（判断の質、考えの独自性）。近い研究（判断課題・数学の学習）はあるが、チャットでの相談の研究は見つからなかった。
- どんな質問をAIにさせると効果があるか（質問の数・順番・深さ）。研究で分かっていない。テンプレートは Claude の提案として書く。
- ADHD など特性のある人で、自己説明やAIに質問させる使い方の効果が違うか。今回は調べておらず、記事でも結びつけない。

## 使わないほうがよい情報（理由つき）

- **「この質問プロンプトで理解度が〇倍」「ソクラテス式で成績〇%アップ」などの数字**：出典が特定できる研究で確認できなかった。プロンプト紹介ブログ・SNSで出回りやすい。
- **「質問形式で促すのが一番効果がある（Bisra ら）」**：形式どうしの比較で有意差なし。g = .56 は「質問形式の研究でも効果があった」まで。
- **Bisra らの g = .55 を「仕事でも効く」「大人の学び直しに効く」として使うこと**：社会人・職場のカテゴリはない。専門職課程は4研究のみ。
- **Fernbach ら (2013) の「説明させると意見が穏やかになる」**：事前登録の追試で再現されなかった（Crawford & Ruscio 2021）。
- **Fernbach ら (2013) の各実験の人数（「198人」など）**：ブログの要約のみで、本文未確認。
- **説明の深さの錯覚の「最初の実験は16人のイェール大学生」など、Wikipedia やブログにある細部**：本文で確認していない（10/9 pm と同じ）。
- **Kosmyna ら (2025)「Your Brain on ChatGPT」（MIT メディアラボ）の「ChatGPTで脳の活動が落ちる」「認知的負債」**：査読前、54人（4回目は18人）、脳波の解釈が中心で、報道で大きく一般化された。「AIを使うと馬鹿になる」系の見出しの元になりやすい。brief の「煽り記事を使わない」に該当しやすいので使わない。
- **Blasco & Charisi の年齢・国の細部**：要約どうしで食い違う（14〜18歳／14〜16歳）。書くなら「高校生122人（査読前）」まで。
- **Xi ら (2025, Computers & Education) の大学生向けソクラテス式エージェントの結果**：抄録を読めず、人数・設計を確認できていない。
- **Kao (2025, Research Square) の「ChatGPT の学習モードで批判的思考が伸びた」**：査読前・10年生（高校生）・90人。特定製品の機能名が入り、変わりやすい。
- **特定のAI製品の機能・料金（「学習モード」「Study Mode」など）**：変わりやすい。記事に入れない。
- **AIとの対話でメンタルの状態がよくなる／悪くなると断定する記述**：今回の調査範囲外。断定しない。

## 参考文献（記事末尾にそのまま使える形）

- Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2018). Inducing self-explanation: A meta-analysis. *Educational Psychology Review, 30*(3), 703–725. https://doi.org/10.1007/s10648-018-9434-x
- Rozenblit, L., & Keil, F. (2002). The misunderstood limits of folk science: An illusion of explanatory depth. *Cognitive Science, 26*(5), 521–562. https://doi.org/10.1207/s15516709cog2605_1
- Fernbach, P. M., Rogers, T., Fox, C. R., & Sloman, S. A. (2013). Political extremism is supported by an illusion of understanding. *Psychological Science, 24*(6), 939–946. https://doi.org/10.1177/0956797612464058
- Crawford, J. T., & Ruscio, J. (2021). Asking people to explain complex policies does not increase political moderation: Three preregistered failures to closely replicate Fernbach, Rogers, Fox, and Sloman's (2013) findings. *Psychological Science, 32*(4), 611–621. https://doi.org/10.1177/0956797620972367
- Blasco, A., & Charisi, V. (2024). The impact of large language models on students: A randomised study of Socratic vs. non-Socratic AI and the role of step-by-step reasoning. SSRN（査読前）. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5040921
- Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *Proceedings of the National Academy of Sciences, 122*(26), e2422633122. https://doi.org/10.1073/pnas.2422633122
- Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), Article 188. https://doi.org/10.1145/3449287
- Fogliato, R., Chappidi, S., Lungren, M., Fisher, P., Wilson, D., Fitzke, M., Parkinson, M., Horvitz, E., Inkpen, K., & Nushi, B. (2022). Who goes first? Influences of human-AI workflow on decision making in clinical imaging. *FAccT '22*. https://doi.org/10.1145/3531146.3533193
- Kumar, H., Rothschild, D. M., Goldstein, D. G., & Hofman, J. M. (2023). Math education with large language models: Peril or promise? SSRN（査読前）. https://doi.org/10.2139/ssrn.4641653

（本文で使った文献だけを残す。Bastani らは #02 につなぐ1行で触れた場合だけ載せる。Fernbach を載せるなら Crawford & Ruscio とセットで。Fogliato の DOI は Microsoft Research の PDF のファイル名（3531146.3533193）から組み立てたもので、DOI のページそのものは開いていない。）

## 公開済み記事との重なり

公開済み「ChatGPTを使うと考える力が落ちるのか ― AIに渡す仕事、渡さない仕事 #02」（2026-10-04、無料、本文は scratchpad の published/11-chatgpt-thinking.md で全文を確認）。

- **#02 で使われた研究（3本）**：
  1. Budzyń ら (2025) Lancet Gastroenterology & Hepatology（内視鏡医の deskilling の観察研究）
  2. Bastani ら (2025) PNAS（高校数学、GPT Base／GPT Tutor）
  3. Lee ら (2025) CHI '25（知識労働者319人、936場面の自己申告調査）
- **今回の research.md との重なり**：
  - **Bastani ら (2025) が重なる**。#02 の主役の1本で、「ヒント型のAIのほうが学びが残った」まで書かれている。→ 今回は主役にしない。使うなら「前回 #02 で紹介した高校生の研究では…」と1行でつなぐだけ（参考文献にも載せるかは writer の判断）。
  - Budzyń ら・Lee ら は今回使っていない。
  - 今回の主な研究（Bisra ら 2018、Rozenblit & Keil 2002、Crawford & Ruscio 2021／Fernbach ら 2013、Blasco & Charisi 2024、Buçinca ら 2021、Fogliato ら 2022、Kumar ら 2023）は #02 と重ならない。
- **研究以外の中身の重なり（writer・editor への注意）**：
  - #02 の「04｜渡しながら、力を残すための3つの工夫」で、すでに「1. 先に自分で30秒考えてから渡す」「『私はこう思ったんだけど、どう思う？』とよく記入します」「2. 『答え』ではなく『ヒント』や『チェック』を頼む」「私の下書きの弱いところを3つ指摘して」「私の考えに抜けがないか見て」が書かれている。英語は「最初の数文は自分で書いてから添削」「この表現は自然？と聞く」も既出。
  - → brief の切り口②（2つの頼み方の使い分け）と無料部分04（「AIを開く前に自分の答えを一行書く」）は、**#02 の工夫1と近い**。#02 の続きとして「前回は『先に考えてから渡す』を書いた。今回はその先、AIに質問させる側に回してもらう」とつなぎ、同じ言い回し（「30秒」「弱いところを3つ指摘して」「抜けがないか見て」）を繰り返さない。
  - 問い4の研究（Fogliato・Buçinca・Kumar）は、#02 の工夫1「先に自分で考えてから渡す」を後から裏づける形になる。#02 では工夫1は「研究の結論ではなく私の提案」と書かれていたので、今回「近い研究がある」と補うのは自然。ただし「#02 の提案が研究で証明された」とは書かない（対象・課題が違う）。
  - #02 の「研究で分かっていないこと」に「オフィスワークで長期的にスキルがどう変わるか」が既出。今回の「分かっていないこと」は「大人・職場で質問させる使い方の効果」に絞ると重ならない。
- 「AIに心の話をするとき」（2026-10-03）の研究（チャットボットによるメンタルヘルス支援）は今回使っていない。
