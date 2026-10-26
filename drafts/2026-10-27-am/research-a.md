# research｜2026-10-27-am（担当A：問い A1〜A4。B は別の担当）

調べた日：2026-10-26。数値は、論文の本文・抄録・掲載先の書誌ページで自分で読んだものだけを「確認済み」にした。過去の下書きで確認済みの研究（drafts/2026-10-16-pm の自動化バイアス、drafts/2026-10-07-pm の Bauer ほか 2007）は、その確認内容をそのまま使っている。

全体の注意（書き手向け）
- 研究の対象がばらばら（高校生・大学生・コールセンターの社員・放射線科医・オンライン実験の一般の人）。どの研究も「職種を変えた社会人が、新しい分野の言葉をAIで覚える」場面を直接調べたものではない。本文では毎回「誰を対象にした研究か」を書く。
- どれも平均の傾向で、個人に当てはまるとは限らない。研究からSena個人の状態（うつ・ADHD・今の職場での様子）を推測しない。
- AIの誤りの割合は、モデル・時期・質問の作り方でまったく変わる。数字は「その研究の、その時点の値」として書く。

⸻

## 問いごとの答え

### 問い A1：生成AIで学ぶと、AIを外したあとの理解・成績はどうなるか（Bastani ら PNAS 2025 の数値、社会人の研究、公開記事との重なり）

- 分かっていること：
  - **Bastani ら（PNAS 2025）**：トルコの高校1校で行ったフィールド実験。ふつうのChatGPT風のAI（GPT Base）を練習で使った生徒は、練習問題の成績が上がったが、AIを外した試験では、AIを使わなかった生徒より成績が低かった。答えを直接言わずヒントを出すように作ったAI（GPT Tutor）では、練習中の伸びはもっと大きく、試験での悪影響はほぼ消えた（ただし、試験でプラスになったわけでもない）。
  - 著者の解釈は「生徒がAIを松葉杖のように使った（答えを写した）」。根拠として、GPT Base への一番多いメッセージが「答えは何？」だったこと、初回の最初のやりとりが表面的（問題をそのまま貼る・答えを聞く）だった生徒が GPT Base で67%、GPT Tutor で37%だったことを挙げている。
  - 生徒の自己評価はずれていた：GPT Base の生徒は「成績が下がった・学べなかった」とは感じておらず、GPT Tutor の生徒は試験の成績が上がっていないのに「かなりよくできた」と感じていた。→ 記事の軸（自分では分かったつもりでも、確かめないと分からない）に使える。
  - GPT Base の答えの正しさ：57問をそれぞれ10回「答えは何？」と聞いたところ、正しい答えは平均51%だった（2023年秋の GPT-4）。
  - **社会人・仕事の学びで近い研究**：1つある。
    - Brynjolfsson, Li & Raymond（QJE 2025）：アメリカのソフトウェア会社の顧客サポート担当 5,172人（多くはフィリピン勤務）に、生成AIの返答候補を順に導入した。1時間あたりの解決件数は平均15%増。経験の浅い人ほど伸び、在籍1年超の人では解決件数への効果は見られなかった。AIが止まった時間（障害）でも、AIを使っていた人は成績が高いままで、著者は「AIの助けで仕事を覚えた」証拠としている。→ Bastani とは逆向きの結果。ただし、課題（顧客対応の会話）もAIの形（返答の候補を出す）も違い、「AIを外したあとに力が残るか」を調べる実験として設計されたものではない（障害は偶然起きたもの）。
    - 大学生では、Lehmann, Cornelius & Sting（査読前）が「AIに答えを作らせる使い方では、扱える範囲は広がるが一つ一つの理解は浅くなる。説明を求める使い方では、範囲は広がらないが理解が深まる」と報告している。Bastani と同じ方向。
    - 逆に、授業の作法に沿って作ったAIチューターで大学の物理の学びが対面の能動学習より大きかった、というランダム化比較試験もある（Kestin ら、Scientific Reports 2025、ハーバード大学）。→「AIで学ぶと必ず力が落ちる」ではなく、「AIの作り方と使い方で結果が分かれる」と書くのが安全。
  - **追試の状況**：Bastani らの研究を別の場所・別の対象でくり返した追試は、今回の検索では見つからなかった（SSRN のワーキングペーパー版が2026年4月に改訂されているが、新しい追試ではない）。方向の近い研究（上の大学生の研究）はあるが、同じ設計の追試ではない。

- 根拠1：Bastani H, Bastani O, Sungu A, Ge H, Kabakcı Ö, Mariman R 2025『Generative AI without guardrails can harm learning: Evidence from high school mathematics』PNAS 122(26): e2422633122（種類：フィールド実験〔クラス単位のランダム化〕／査読済み）
  - 確認した場所：Europe PMC の本文（PMC12232635）https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12232635/fullTextXML 、書誌は https://pubmed.ncbi.nlm.nih.gov/40560616/ （PNAS のページは 403 で開けなかった。Europe PMC の本文で確認）
  - 対象：トルコの大きな高校1校、9〜11年生の約50クラス・約1,000人（優秀クラスは主な分析から除外）。2023–2024年度の秋学期に、90分の練習の回を4回。3群（対照＝教科書とノートのみ／GPT Base／GPT Tutor）にクラス単位で割り付け。
  - 使える数値（すべて本文で確認済み）：
    - 練習中の成績：GPT Base で「48% improvement」、GPT Tutor で「127%」（対照群の平均に対する割合）
    - AIなしの試験：GPT Base は対照群より「17%」低い（係数 −0.054、p<0.05）
    - GPT Tutor の試験：係数 −0.004で、対照群と「statistically indistinguishable」（統計的に差がない）。著者は「we still do not observe a positive effect」とも書いている
    - 約1,000人・約50クラス・90分×4回（確認済み）
    - GPT Base の正答：「correct answer only 51% of the time」（57問×10回、確認済み）
    - 初回の最初のやりとりが表面的だった生徒：GPT Base 67%、GPT Tutor 37%（確認済み）
  - GPT Tutor の作り：ヒントを出し、答えを直接言わないように指示。さらに数学の先生2人が、問題ごとの正しい解き方と、よくある間違いとその直し方をAIに渡していた（本文で確認）。→「答えを言わないAI」だけでなく「正しい答えを持たせたAI」でもあった点に注意。
- 根拠2：Brynjolfsson E, Li D, Raymond L 2025『Generative AI at Work』Quarterly Journal of Economics 140(2): 889–942（種類：自然実験〔導入時期のずれを使った分析〕／査読済み）
  - 確認した場所：書誌と抄録 https://api.crossref.org/works/10.1093/qje/qjae044 、本文（査読前の版 v2）https://arxiv.org/html/2304.11771v2
  - 使える数値：5,172人、平均15%（抄録で確認済み）。「we see no effect for agents with more than a year of tenure」（本文 v2 で確認済み）。障害の時間でも「workers exposed to AI recommendations continue to perform better during outages」（本文 v2 で確認済み。効果の大きさの数字は使わない）
  - 注意：本文は arXiv の版で読んだ。掲載版と細部が違う可能性がある（人数は掲載版 5,172）。
- 根拠3：Lehmann M, Cornelius PB, Sting FJ『AI Meets the Classroom: When Do Large Language Models Harm Learning?』arXiv 2409.09047 v2（2025年3月）（種類：事前登録した実験2本＋フィールド研究／**査読前**）
  - 確認した場所：https://arxiv.org/abs/2409.09047 （抄録）
  - 使える内容：全体の学習成果への効果はなし。答えを作らせる使い方は範囲が広く理解が浅い、説明を求める使い方は理解が深い（抄録で確認済み）。人数・国は抄録になく未確認。
- 根拠4：Kestin G, Miller K, Klales A, Milbourne T, Ponti G 2025『AI tutoring outperforms in-class active learning: an RCT introducing a novel research-based design in an authentic educational setting』Scientific Reports 15: 17458（種類：ランダム化比較試験／査読済み）
  - 確認した場所：Europe PMC の抄録（PMC12179260）
  - 使える内容：大学の物理の授業で、AIチューターのほうが短い時間で有意に多く学べた（抄録で確認済み）。人数（194人とする記事がある）は抄録になく未確認。
- 公開記事「ChatGPTを使うと考える力が落ちるのか ― AIに渡す仕事、渡さない仕事 #02」との重なり：
  - 公開記事の本文は今回読めなかった（note のページから記事を特定できなかった）。ただし、公開タイトルは drafts/2026-10-04-am/article.md のタイトル案2と同じで、その下書きは **Bastani ら（48%・17%・ヒント型AI）、Budzyń ら（内視鏡医の観察研究）、Lee ら（知識労働者319人の調査）** の3つを使っている。公開記事でも同じ研究を使っている可能性が高い（**未確認**。まとめ役かSenaが公開記事で確かめる）。
  - 書き手へ：重なっている場合は、Bastani の説明をくり返さず「#02 で紹介した高校生の数学の実験」と1〜2行で触れ、今回は新しく「生徒の自己評価がずれていた」「GPT Tutor には先生が正しい解き方を渡していた」の2点だけ足すと重なりが小さい。社会人の研究として Brynjolfsson ら（QJE 2025）を足せる。
  - 10-04-am の下書きの数値（48%・17%）は原典と合っていた。「ヒント型AIでは悪影響が大きく和らいでいた」も原典どおり（「消えたが、プラスにはならなかった」とまで書くとより正確）。
- 限界・注意：
  - Bastani：高校1校・数学のみ・短期間（4回）・2023年秋の GPT-4。著者自身が「1校での実施」「短期の結果のみ」「他の設計・場面への一般化には追加の研究が必要」と書いている。社会人や職場は調べていない。
  - 「AIで学ぶと17%下がる」と一般化しない。「答えをそのまま出すAIで練習した高校生は、AIなしの試験で対照より17%低かった」と、対象と条件をつけて書く。
  - Brynjolfsson：顧客対応の仕事1社。「新しい分野の言葉を覚える」学びではない。

### 問い A2：その分野の知識が少ない人ほど、AIの誤りに気づきにくい・信じすぎるか（逆の結果も）

- 分かっていること：
  - **知識・経験が少ない人ほど、間違ったAIの提案に引っぱられやすい、という方向の結果が複数ある。ただし、経験者でも起きる。**
    - Dratsch ら（Radiology 2023）：ドイツの放射線科医27人が、AIのふりをした提案つきで乳がん検診の画像50枚を判定した実験。AIの提案が間違っていたとき、正しく判定できた割合は、経験の少ない人で 79.7%→19.8%、中くらいで 81.3%→24.8%、経験の多い人で 82.3%→45.5% に下がった。AIが間違って重い判定を出したときに引っぱられる度合いは、経験の少ない人が有意に大きかった。著者の結論は「経験に関係なく、すべての読影医が自動化バイアスの影響を受けうる」。
    - Nourani ら（HCOMP 2020）：画像を分類するAIを使った実験で、「初心者は、誤りに気づくための知識がないため、過度に頼りやすかった」と抄録に書かれている。分野の知識がある人は、AIの当たり外れを見て信頼を調整していた。
    - Goddard ら（2012、医療の systematic review・drafts/2026-10-16-pm で確認済み）：「作業に不慣れな利用者で多いが、経験のある利用者でも起きる」。Parasuraman & Manzey（2010）：初心者でも熟練者でも起き、訓練や指示では防げない（抄録、確認済み）。
  - **逆の結果（知識が少ない人がむしろ疑う／知識が多い人のほうが外す）もある**：
    - Logg ら（2019）：一般の人は、同じ助言でも「アルゴリズムから」と言われたほうに従った。ところが、ふだん予測をしている専門家はアルゴリズムの助言にあまり頼らず、そのせいで正確さが下がった。→「知識がある人は疑う」が、正しいAIのときは損になることもある。
    - Gaube ら（npj Digital Medicine 2021）：胸部X線の診断で、放射線科医は「AIの助言」と書かれた助言を低く評価したが、専門外の医師はそうしなかった。一方、間違った助言を受けると、出どころの表示に関係なく診断の正確さは有意に下がった（専門家も含めて）。
    - Fernandes ら（Computers in Human Behavior 2026）：生成AIを使って論理問題（LSAT）20問を解いた実験で、成績は基準の集団より約3点上がったが、自分の成績を約4点高く見積もった（研究1・246人、研究2・452人で再現）。「AIに詳しい」と自己申告した人ほど、自己評価が不正確だった。→「AIに詳しい」ことは「AIの間違いに気づける」ことにはならない、という材料。ここでの知識は「AIの知識」で、分野の知識ではない点に注意。
    - Horowitz & Kahn（査読前の版で確認）：安全保障の判断を使った9か国の調査実験で、AIの知識がいちばん少ない人はややAIを避け、少し〜中くらいの知識で自動化バイアスが大きくなり、最も詳しい人で横ばいになる「山なり」の関係を報告。これもAIの知識の話。
  - **生成AIで、分野の知識の量と誤りの見抜き方を直接比べた査読済みの実験は、今回の検索では見つからなかった。** 近いものは、生成AIの誤りにそのまま乗りやすい実験（Spatharioti ら CHI 2025、Kim ら FAccT 2024：drafts/2026-10-16-pm で確認済み）と、知識労働者の自己申告（Lee ら CHI 2025：自分の力に自信がある人ほど批判的に考える、AIへの信頼が高い人ほど考えない）。
  - 書き手向けのまとめ：本文で言えるのは「その分野に慣れていない人ほど、間違ったAIの提案に引っぱられやすい、という実験がある（医療の画像や分類の課題）。ただ、経験者でも起きる」まで。「知らない分野ほどAIの間違いに気づけない」は、研究と矛盾しない言い方だが、生成AIで直接確かめられた結論ではない。「研究をもとにした考え方」として書く。

- 根拠1：Dratsch T ほか 2023『Automation Bias in Mammography: The Impact of Artificial Intelligence BI-RADS Suggestions on Reader Performance』Radiology 307(4): e222176（種類：前向き実験／査読済み）
  - 確認した場所：Europe PMC の抄録 https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1148/radiol.222176&resultType=core&format=json 、補足に RSNA のプレスリリース https://www.rsna.org/media/press/i/2432
  - 使える数値（抄録で確認済み）：27人、50枚（練習10枚＝全部正しい提案、本番40枚のうち12枚が間違った提案）。正しく判定できた割合：経験の少ない人 79.7%→19.8%、中くらい 81.3%→24.8%、多い人 82.3%→45.5%
  - 注意：画像は2017〜2019年のもので、AIは「AIだと言って見せた提案」（実際は研究者が用意したもの）。生成AIではない。著者の所属はドイツ（ケルン大学など）。
- 根拠2：Nourani M, King JT, Ragan ED 2020『The Role of Domain Expertise in User Trust and the Impact of First Impressions with Intelligent Systems』HCOMP 2020（AAAI）（種類：統制した利用者実験／査読あり国際会議）
  - 確認した場所：https://arxiv.org/abs/2008.09100 （抄録。HCOMP 2020 採録と記載）
  - 使える内容：「novice users suffer from over-reliance due to their lack of proper knowledge to detect errors」（抄録で確認済み）。参加人数は抄録になく未確認。
- 根拠3：Logg JM, Minson JA, Moore DA 2019『Algorithm appreciation: People prefer algorithmic to human judgment』Organizational Behavior and Human Decision Processes 151: 90–103（種類：実験6本／査読済み）
  - 確認した場所：https://ideas.repec.org/a/eee/jobhdp/v151y2019icp90-103.html （抄録）
  - 使える内容：「experienced professionals, who make forecasts on a regular basis, relied less on algorithmic advice than lay people did, which hurt their accuracy」（抄録で確認済み）。生成AI以前。
- 根拠4：Gaube S ほか 2021『Do as AI say: susceptibility in deployment of clinical decision-aids』npj Digital Medicine 4: 31（種類：実験／査読済み）
  - 確認した場所：Europe PMC の抄録（PMC7896064）
  - 使える内容：放射線科医は「AI」と表示された助言を低く評価、専門外の医師はそうでない。間違った助言で、表示に関係なく正確さが有意に低下（抄録で確認済み）。人数は未確認。
- 根拠5：Fernandes D ほか 2026『AI makes you smarter but none the wiser: The disconnect between performance and metacognition』Computers in Human Behavior 175: 108779（オンライン公開 2025年10月）（種類：実験2本／査読済み）
  - 確認した場所：https://research.aalto.fi/en/publications/ai-makes-you-smarter-but-none-the-wiser-the-disconnect-between-pe/ （アールト大学の研究ページの抄録）
  - 使える数値：研究1 246人・研究2 452人、成績は基準の集団より3点上、自己評価は4点高すぎた（抄録で確認済み）。AIリテラシーが高いほど自己評価が不正確（抄録で確認済み）。
- 根拠6：Lee H-P ほか 2025『The Impact of Generative AI on Critical Thinking』CHI '25（種類：調査〔自己申告〕／査読済み）
  - 確認した場所：https://www.microsoft.com/en-us/research/?p=1135061 （抄録）
  - 使える数値：319人、936の例。「higher confidence in GenAI is associated with less critical thinking」「higher self-confidence is associated with more critical thinking」（確認済み）
  - 注意：公開記事 #02 で使われている可能性が高い（A1 の項を参照）。自己申告・一時点。
- 根拠7（再利用）：Goddard ほか 2012、Parasuraman & Manzey 2010、Spatharioti ほか 2025、Kim ほか 2024 は drafts/2026-10-16-pm/research.md の確認内容のまま使える。
- 根拠8（補助・査読前の版）：Horowitz MC, Kahn L『Bending the Automation Bias Curve』arXiv 2306.16507（2023）
  - 確認した場所：https://arxiv.org/abs/2306.16507 （抄録）。雑誌（International Studies Quarterly 2024 とされる）への掲載は確認できていない。人数は使わない。
- 限界・注意：
  - 上の実験の多くは生成AI以前、または研究者が用意した「AIのふりをした提案」。分野の言葉の説明をAIに聞く場面とは違う。
  - Dratsch の数字は「間違った提案だけを集めた12枚」での値。「AIを使うと正答率が2割になる」と書かない。
  - 「知識が少ない人ほど」の比較は、多くが「経験年数」や「専門か専門外か」で分けたもの。

### 問い A3：生成AIは、専門用語・業界の言葉の説明でどのくらい間違えるか（言えること・言えないこと）

- 分かっていること：
  - **分野をまたいだ「誤りの割合」をまとめたメタ分析は、今回の検索では見つからなかった。** 研究ごとに「誤り（ハルシネーション）」の定義や測り方が違い、まとめた数字を出しにくい。
  - 分野別の研究はあるが、**「専門用語の説明」そのものの誤りの割合を測った研究は見つからなかった**。見つかったのは、判例・文献のような「確かめられる具体的な事実」を聞いた研究。
    - 法律：Dahl ら（Journal of Legal Analysis 2024）：アメリカの連邦裁判所の判例について確かめられる質問をすると、誤りは ChatGPT 3.5 で69%、Llama 2 で88%（2023年のモデル）。下級の裁判所ほど、また目立たない（知られていない）判例ほど誤りが多かった。
    - 文献：Chelli ら（JMIR 2024）：systematic review 11本の文献集めをAIにさせると、存在しない文献を作った割合は GPT-3.5 で39.6%、GPT-4 で28.6%、Bard で91.4%（471文献）。
  - **「あまり書かれていないことほど間違えやすい」は、研究で比較的しっかりしている**：Kandpal ら（ICML 2023）は、事実を聞く質問の正答率が、学習した文章の中でその話題に触れた文書の数とともに上がることを示し、因果の証拠もあるとした。検索で関連資料を渡すと（retrieval augmentation）、この依存が小さくなった。Dahl らの「目立たない判例ほど誤る」も同じ方向。
  - **社内の略語・社内だけの言葉について**：AIが学習した文章に含まれていない言葉は、AIが知りようがない、という整理は上の研究と合う。ただし「AIは知らないと言ってくれる」とは限らない。Kalai ら（OpenAI、査読前・2025）は、学習と評価の仕組みが「分からない」と言うより推測することを評価しているため、もっともらしい誤りが出ると論じている（数字は使わない）。→「社内の言葉は、AIはそもそも知らない。しかも、知らないと言わずに、それらしい説明を作ることがある」と書くと、研究と矛盾しない。研究で社内用語そのものを調べたわけではないので、「研究から考えられること」として書く。
  - 言えること／言えないことの範囲（書き手向け）：
    - 言える：「AIの誤りは、分野・質問の具体さ・モデルで大きく違う」「あまり知られていない・新しい・狭い分野の事実ほど間違えやすい、という研究がある」「資料を渡して答えさせると、この弱さが小さくなる」。
    - 言えない：「AIの用語説明は○%間違える」（そういう研究はない）。上の数字を今のAIにそのまま当てはめること（2023年前後のモデル）。

- 根拠1：Dahl M, Magesh V, Suzgun M, Ho DE 2024『Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models』Journal of Legal Analysis 16: 64–93（種類：評価研究／査読済み）
  - 確認した場所：スタンフォード大学ロースクールの論文ページ https://law.stanford.edu/publications/large-legal-fictions-profiling-legal-hallucinations-in-large-language-models （抄録）、本文は arXiv 版 https://arxiv.org/html/2401.01301v1
  - 使える数値：「between 69% of the time with ChatGPT 3.5 and 88% with Llama 2」（確認済み）。「Hallucination rates are higher for lower levels of the federal judiciary」「case prominence is negatively correlated with hallucination」（arXiv 本文で確認済み）
  - 注意：掲載版の抄録は「少なくとも58%」と書いているという情報があるが、自分では読めていない（未確認）。数字を使うなら「2023年のモデルで69〜88%（論文の初期の版）」とし、版で数字が違うことを添える。
- 根拠2：Chelli M ほか 2024『Hallucination Rates and Reference Accuracy of ChatGPT and Bard for Systematic Reviews: Comparative Analysis』J Med Internet Res 26: e53164（種類：比較研究／査読済み）
  - 確認した場所：Europe PMC の抄録（PMID 38776130）
  - 使える数値：GPT-3.5 39.6%（55/139）、GPT-4 28.6%（34/119）、Bard 91.4%（95/104）、11本のレビュー・471文献（抄録で確認済み）
- 根拠3：Kandpal N, Deng H, Roberts A, Wallace E, Raffel C 2023『Large Language Models Struggle to Learn Long-Tail Knowledge』ICML 2023（種類：評価研究／査読あり国際会議）
  - 確認した場所：https://arxiv.org/abs/2211.08411 （抄録。ICML 2023 の最終版と記載）
  - 使える内容：正答率は関連する学習文書の数とともに上がる、検索で資料を渡すと依存が下がる（抄録で確認済み）。数値は抄録になく使わない。
- 根拠4（補助・査読前）：Kalai AT, Nachum O, Vempala SS, Zhang E 2025『Why Language Models Hallucinate』arXiv 2509.04664
  - 確認した場所：https://arxiv.org/abs/2509.04664 （抄録）
  - 使える内容：学習と評価が「分からない」と言うより推測を評価するため誤りが出る、という主張（抄録で確認済み）。企業の研究者による査読前の論文。数字は抄録になく使わない。
- 限界・注意：
  - 法律・医学文献の研究は「具体的な事実（判例・文献）を聞いた」もので、「この言葉はどういう意味？」という一般的な用語の説明とは難しさが違う。一般的な用語の説明は、これらの数字より誤りが少ない可能性があるが、測った研究は見つからなかった。
  - モデルの改善が速く、数字はすぐ古くなる。

### 問い A4：職種変更・異動の直後に「言葉が分からない」こと自体は、どう扱われているか

- 分かっていること：
  - 組織社会化（新しく入った人が組織に慣れていく過程）の研究では、**「言葉」は新しく覚える中身の一つとして扱われている**。Chao ら（Journal of Applied Psychology 1994）は、正社員の専門職594人のデータで、覚える中身として6つの次元（仕事の熟達、組織内の力関係、**言葉**、人、組織の目標・価値観、歴史）を因子分析で確かめた。さらに「同じ仕事のまま」「社内で仕事を変えた」「仕事も組織も変えた」の3群で回答の傾向がはっきり違った。→「職種を変えると、言葉を含めて覚え直すものがある」の根拠として使える。
  - 「言葉」の次元の質問項目（業界の専門用語・社内の略語など）の中身は、原典を読めておらず**未確認**。「職種の専門用語と、組織の略語・言い回し」のような説明は二次情報でよく見るが、本文で使う場合は「言葉（その仕事・その組織で使われる言葉）」くらいにとどめる。
  - Bauer ら（2007、70サンプルのメタ分析）は drafts/2026-10-07-pm で使用済み（要旨で確認済み：役割の明確さ・自信・受け入れられ感が、受け入れの仕組みや情報を取りに行く行動と、満足・成果・定着をつなぐ）。使うなら出典をそろえて1行で。
  - 「言葉が分からないこと」を負担（ストレス）として直接測った研究は、今回の検索では見つからなかった。

- 根拠1：Chao GT, O'Leary-Kelly AM, Wolf S, Klein HJ, Gardner PD 1994『Organizational socialization: Its content and consequences』Journal of Applied Psychology 79(5): 730–743（種類：調査研究〔因子分析〕／査読済み）
  - 確認した場所：論文の抄録を載せている索引ページ https://synapsesocial.com/papers/W2016105036 （APA PsycNet は読み込めなかった）。巻号ページは複数の文献リストで一致。
  - 使える数値：「594 full-time professionals」、6次元（「performance proficiency, politics, language, people, organizational goals/values, and history」）（抄録で確認済み）
  - 注意：1994年の研究で、アメリカの専門職が対象。古いので「古典的な研究」として書く。抄録は索引サイト経由で読んだもので、出版社のページでは確認できていない。
- 根拠2（再利用）：Bauer TN, Bodner T, Erdogan B, Truxillo DM, Tucker JS 2007『Newcomer adjustment during organizational socialization: A meta-analytic review of antecedents, outcomes, and methods』Journal of Applied Psychology 92(3): 707–721（種類：meta-analysis／査読済み）
  - 確認した場所：drafts/2026-10-07-pm で要旨を確認済み（「70 unique samples of newcomers」）。今回は開き直していない。
- 限界・注意：どちらも生成AI以前で、「AIで追いつく」ことは調べていない。

⸻

## 分かっていないこと

- 職種を変えた社会人が、新しい分野の言葉や全体像をAIで学んだとき、AIを使わない場面での理解がどうなるか（高校生・大学生・顧客サポートの研究しかない）。
- Bastani らの研究の、別の場所・別の対象での追試（見つからなかった）。
- 生成AIで、その分野の知識の量によって誤りの見抜き方がどう違うか（直接比べた査読済みの実験は見つからなかった）。
- 生成AIが一般的な専門用語・業界の言葉を説明するときの誤りの割合（測った研究は見つからなかった）。分野をまたいでまとめた数字もない。
- AIが社内の略語を聞かれたとき、どのくらいの割合で「知らない」と言わずにそれらしい説明を作るか（研究は見つからなかった）。
- 「言葉が分からない」ことが新しく入った人の負担・成果にどのくらい影響するか（効果の大きさ）。
- 「地図・つながり・確認の質問をAIに作らせ、正しさは自分で確かめる」という手順の効果（研究で確かめられていない。Claudeの提案として書く）。

## 使わないほうがよい情報（理由つき）

- 「AIで勉強すると成績が17%下がる」：Bastani の数字だが、条件（高校生・数学・答えをそのまま出すAI・4回の練習）を外すと誤解を招く。
- 「ヒント型AIなら成績が上がる」：Bastani の GPT Tutor は試験で対照と差がなかった（プラスではない）。また先生が正しい解き方を渡していたので、「答えを言わない」だけの効果とは言えない。
- 「生徒の17%」「1,000人中…」のような人数の言い換え：17%は対照群の平均点に対する差で、人の割合ではない。
- Dell'Acqua ら（2023、BCGのコンサルタント758人、「AIの得意な範囲の外の課題では正答が19ポイント下がった」）：有名だが、HBS・SSRN のページが開けず原典を確認できなかった。ワーキングペーパー（査読前）でもある。使うなら別途確認が必要。
- Darvishi ら（2024、Computers & Education、1,625人の大学生。AIの手助けを外すとピアフィードバックの質が下がり、チェックリストがあると保たれた）：A1 にも B にも合いそうだが、抄録を自分で読めなかった（二次情報のみ）。未確認。
- Kestin ら 2025 の「194人」「2倍学べた」：194人は二次情報、「2倍」は査読前の版の言い方で掲載版では使われていない。
- Dahl ら 2024 の「58%」：掲載版の抄録の数字とされるが未確認。69〜88%は初期の版の数字なので、使うなら版を添える。
- Dratsch の「正答率が2割になる」型の一般化：間違った提案だけを集めた12枚の値。
- Horowitz & Kahn の人数（約9,000人とする抄録の読み取りと、別の論文が書く702人で食い違い）：未確認なので使わない。雑誌掲載も未確認。
- Chao ら 1994 の「言葉」の次元の中身（「略語・スラング・専門用語」など）：二次情報のみ。
- Kalai ら 2025 の数字や「珍しい事実ほど誤る割合は○%」：抄録に数字がなく、査読前。
- SimpleQA（OpenAI 2024）の正答率：抄録に数字がなく未確認。テストもGPT-4が間違えるように集めた問題で、一般の誤りの割合ではない。
- 「AIの誤りは○%」と1つの数字で言う情報全般（ブログ・まとめ記事に多い）：モデル・時期・質問で大きく違い、出典もはっきりしないことが多い。
- Brynjolfsson らの「経験の浅い人は34%伸びた」：二次情報の数字で、本文 v2 では確認できなかった（本文では「在籍1か月未満で1時間あたり0.7件の改善」という書き方）。

## 参考文献（記事末尾にそのまま使える形）

- Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *Proceedings of the National Academy of Sciences, 122*(26), e2422633122. https://doi.org/10.1073/pnas.2422633122
- Bauer, T. N., Bodner, T., Erdogan, B., Truxillo, D. M., & Tucker, J. S. (2007). Newcomer adjustment during organizational socialization: A meta-analytic review of antecedents, outcomes, and methods. *Journal of Applied Psychology, 92*(3), 707–721.
- Brynjolfsson, E., Li, D., & Raymond, L. (2025). Generative AI at work. *The Quarterly Journal of Economics, 140*(2), 889–942. https://doi.org/10.1093/qje/qjae044
- Chao, G. T., O'Leary-Kelly, A. M., Wolf, S., Klein, H. J., & Gardner, P. D. (1994). Organizational socialization: Its content and consequences. *Journal of Applied Psychology, 79*(5), 730–743. https://doi.org/10.1037/0021-9010.79.5.730
- Chelli, M., Descamps, J., Lavoué, V., Trojani, C., Azar, M., Deckert, M., Raynier, J.-L., Clowez, G., Boileau, P., & Ruetsch-Chelli, C. (2024). Hallucination rates and reference accuracy of ChatGPT and Bard for systematic reviews: Comparative analysis. *Journal of Medical Internet Research, 26*, e53164.（著者名は抄録ページで最終確認を）
- Dahl, M., Magesh, V., Suzgun, M., & Ho, D. E. (2024). Large legal fictions: Profiling legal hallucinations in large language models. *Journal of Legal Analysis, 16*(1), 64–93.
- Dratsch, T., Chen, X., Rezazade Mehrizi, M., Kloeckner, R., Mähringer-Kunz, A., Püsken, M., Baeßler, B., Sauer, S., Maintz, D., & Pinto dos Santos, D. (2023). Automation bias in mammography: The impact of artificial intelligence BI-RADS suggestions on reader performance. *Radiology, 307*(4), e222176. https://doi.org/10.1148/radiol.222176
- Fernandes, D., Villa, S., Nicholls, S., Haavisto, O., Buschek, D., Schmidt, A., Kosch, T., Shen, C., & Welsch, R. (2026). AI makes you smarter but none the wiser: The disconnect between performance and metacognition. *Computers in Human Behavior, 175*, 108779. https://doi.org/10.1016/j.chb.2025.108779
- Gaube, S., Suresh, H., Raue, M., Merritt, A., Berkowitz, S. J., Lermer, E., Coughlin, J. F., Guttag, J. V., Colak, E., & Ghassemi, M. (2021). Do as AI say: Susceptibility in deployment of clinical decision-aids. *npj Digital Medicine, 4*, 31. https://doi.org/10.1038/s41746-021-00385-9
- Goddard, K., Roudsari, A., & Wyatt, J. C. (2012). Automation bias: A systematic review of frequency, effect mediators, and mitigators. *Journal of the American Medical Informatics Association, 19*(1), 121–127. https://doi.org/10.1136/amiajnl-2011-000089
- Kalai, A. T., Nachum, O., Vempala, S. S., & Zhang, E. (2025). Why language models hallucinate. arXiv:2509.04664（査読前）
- Kandpal, N., Deng, H., Roberts, A., Wallace, E., & Raffel, C. (2023). Large language models struggle to learn long-tail knowledge. *Proceedings of the 40th International Conference on Machine Learning (ICML)*. https://arxiv.org/abs/2211.08411
- Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). AI tutoring outperforms in-class active learning: An RCT introducing a novel research-based design in an authentic educational setting. *Scientific Reports, 15*, 17458. https://doi.org/10.1038/s41598-025-97652-6
- Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The impact of generative AI on critical thinking: Self-reported reductions in cognitive effort and confidence effects from a survey of knowledge workers. *CHI '25*. https://doi.org/10.1145/3706598.3713778
- Lehmann, M., Cornelius, P. B., & Sting, F. J. (2025). AI meets the classroom: When do large language models harm learning? arXiv:2409.09047（査読前）
- Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm appreciation: People prefer algorithmic to human judgment. *Organizational Behavior and Human Decision Processes, 151*, 90–103.
- Nourani, M., King, J. T., & Ragan, E. D. (2020). The role of domain expertise in user trust and the impact of first impressions with intelligent systems. *Proceedings of the AAAI Conference on Human Computation and Crowdsourcing (HCOMP), 8*. https://doi.org/10.1609/hcomp.v8i1.7469
- Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors, 52*(3), 381–410. https://doi.org/10.1177/0018720810376055
