# research.md（2026-10-27 am：リサーチA＝A1〜A4、リサーチB＝B1〜B5 を統合）

> 書き手への主な注意（統合時のまとめ）
> - Bastani ら PNAS 2025：トルコの高校1校・約1,000人。答えを出すAIは練習中+48%だが、AIなしの試験で対照より17%低い。ヒント型は差なし（プラスでもない）。社会人の研究ではない。追試なし。公開記事「ChatGPTを使うと考える力が落ちるのか」と重なる可能性が高いので、Bastani は1〜2行に（自己評価のずれ・ヒント型の作りだけ足す）。
> - Brynjolfsson ら QJE 2025（顧客サポート5,172人、生産性+15%、AIが止まっても成績は高いまま）。「経験の浅い人は34%」は使わない。
> - 「知らない分野ほど気づけない」は研究の結論ではない。経験が少ないほど間違った提案に引っぱられやすい結果はある（Dratsch 2023：79.7%→19.8% 対 82.3%→45.5%、放射線科医27人）が、経験者でも起きる。逆の結果もある（Logg 2019、Gaube 2021）。「研究をもとにした考え方」として書く。Si ら 2024 も知識の量を直接調べた研究ではない。
> - 用語の説明の誤りの割合を測った研究はない。分野別の数字（法律 69〜88%、文献 39.6%/28.6%）は2023年のモデル。「あまり書かれていないことほど間違えやすい」（Kandpal 2023）。社内の略語は「AIはそもそも知らず、それらしい説明を作ることがある」と研究から考えられること、として。
> - Chao 1994：新しく入った人が覚える次元の一つに「言葉」。言葉が分からない負担を直接測った研究はない。
> - 地図（概念マップ）：Schroeder 2018（全体 g=0.58、自分で作る0.72、用意された地図を読む0.43）。要約・アウトラインを自分で書くのと比べると差は小さい（0.194）。AIが作った地図の研究はない → 「AIに地図を作らせる」はこの記事の提案。g を「〇%」と言い換えない。
> - 用語の覚え方：思い出す練習（Rowland 2014、g=0.50、答え合わせありで0.73）。答え合わせの欄を置く根拠。分散学習は Cepeda 2006 を1文で。
> - 確かめ方：ラテラル・リーディング（Wineburg & McGrew 2019、Breakstone 2021 は比較群なし）。Si ら 2024（説明が間違っていると正解率0.35、2023年のモデル）。社会人がAIの答えを一次資料で確かめる効果の研究はない。
> - 社内の言葉をAIに入れること：drafts/2026-10-19-am と同じ（AI事業者ガイドライン第1.2版、個情委の注意喚起 2023年6月）。社内用語・社内AIは書かない。
> - 使わない：「〇日で追いつける」、立ち上がり短縮の業界数字、忘却曲線の74%、ラーニングピラミッド、Dell'Acqua、Darvishi、Kestin の「194人」「2倍」、法律の「58%」、Wineburg 2022 の数値。AIの製品名は本文に出さない（研究のモデル名は「当時のモデル」）。

## 問いごとの答え

### リサーチA（A1〜A4）

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

### リサーチB（B1〜B5）

### 問い B1：全体像を先に見ること（先行オーガナイザー、概念マップ・知識マップ）は、新しい分野の理解に効くか

- 分かっていること：
  - **概念マップ（言葉と言葉を線でつなぎ、つながりに名前をつけた図）で学ぶと、平均すると覚えている量が増える**。メタ分析が2本あり、どちらも同じ方向。
    - Nesbit & Adesope 2006：55の研究（67の効果量、5,818人）。対象は小学4年生〜大学生（大学以上を含む）、分野は理科・心理学・統計・看護など。「概念マップを使うと、知識の保持が高かった」。効果の大きさは「使い方と、何と比べたかによって、小〜大まで幅があった」。ほとんどの組み合わせで研究ごとのばらつきが大きかった。
    - Schroeder ら 2018（Nesbit・Adesope も共著）：142の効果量（11,814人）で、全体 g = 0.58（中くらい）。**自分で作る g = 0.72、用意された地図を読む g = 0.43**。理系・理系以外のどちらでも効果があった。
  - **「読むだけの地図」でも効果はあるが、大きくはない**（Nesbit & Adesope 2006 の表）：
    - 用意された地図を読む vs 文章を読む：g = 0.388（29の比較）
    - 用意された地図を読む vs アウトライン・箇条書きを読む：g = 0.278（10の比較）
    - 大学以上の学生が地図を読む研究：g = 0.363（38の比較。ほぼ全部が大学生）
    - リンクでたどる形式の地図（ハイパーリンク）は、リンク付きのアウトラインなどと比べて差がなかった（g = 0.017、有意でない）。
  - **自分で作る効果の多くは「取り組むこと」から来ている可能性**（著者の解釈）：
    - 自分で地図を作る vs 講義を聞く・クラスで話し合う：g = 0.742。
    - 自分で地図を作る vs 文章やアウトラインを自分で書く：g = 0.194（小さい）。
    - 著者は結論で「効果の多くは、読む・聞くより取り組みが増えることによるもので、概念マップという形そのものの性質によるものではないかもしれない」「要約やアウトラインを書くことより少し効果がある程度で、効果が小さいので本当の効果か疑問が残る」と書いている。
  - **大づかみの考え（中心となる考え）は、細かい点より残りやすい**：同じ内容を文章と地図で比べた6つの研究で、中心となる考え g = 0.596、細かい点 g = 0.204。著者は「概念マップは要約に向いた偏りがあるかもしれない」とも書いている。
  - **前提知識・言葉の力が低い学生ほど、地図を読む効果が出た**：比較的低い学生 g = 0.404（有意）、高い学生 g = −0.133（有意でない）。ただし比べた研究は各5本と少なく、著者は「高い学生に効かないとは結論できない」としている。→ 「新しい分野で、まだ知識が少ないときほど、全体の図が役立つ可能性」の根拠の候補。ただし学生の研究で、数も少ない。
  - **先行オーガナイザー**（学ぶ前に、全体の枠組みを短く示す資料）：135の研究のメタ分析（Luiten ら 1980）で、学習と保持の両方を助けると結論。効果の大きさは抄録になく、本文を読めていないので数値は使わない。1980年の古い研究。
- 根拠：
  - Nesbit, J. C., & Adesope, O. O. 2006『Learning With Concept and Knowledge Maps: A Meta-Analysis』Review of Educational Research 76(3), 413–448（種類：meta-analysis／査読済み）
    - 確認した場所：本文PDF（著者 Nesbit のサイト）https://www.sfu.ca/~jcnesbit/articles/NesbitAdesope2006.pdf（抄録 p.413、表2〜8 p.427–433、結論 p.434–435 を読んだ）
    - 使える数値（確認済み）：「55の研究・67の効果量・5,818人」「小学4年〜大学以上」「地図を読む vs 文章 g=0.388」「地図を読む vs アウトライン・箇条書き g=0.278」「大学以上の学生が地図を読む g=0.363」「自分で作る vs 講義・話し合い g=0.742」「自分で作る vs 文章・アウトラインを書く g=0.194」「中心となる考え g=0.596／細かい点 g=0.204」「前提知識・言葉の力が低い学生 g=0.404、高い学生 g=−0.133（有意でない）」「ハイパーリンクの地図 g=0.017（有意でない）」
  - Schroeder, N. L., Nesbit, J. C., Anguiano, C. J., & Adesope, O. O. 2018『Studying and Constructing Concept Maps: a Meta-Analysis』Educational Psychology Review 30(2), 431–455（2017年オンライン公開）（種類：meta-analysis／査読済み）
    - 確認した場所：抄録（共著者 Adesope の所属するワシントン州立大学の機関リポジトリ）https://rex.libraries.wsu.edu/esploro/outputs/journalArticle/Studying-and-Constructing-Concept-Maps-a/99900601155801842 ／書誌は Crossref（https://doi.org/10.1007/s10648-017-9403-9）
    - 使える数値（確認済み）：「142の効果量・11,814人」「全体 g=0.58」「自分で作る g=0.72／読む g=0.43」
  - Luiten, J., Ames, W., & Ackerson, G. 1980『A Meta-analysis of the Effects of Advance Organizers on Learning and Retention』American Educational Research Journal 17(2), 211–218（種類：meta-analysis／査読済み）
    - 確認した場所：Crossref に登録された抄録 https://api.crossref.org/works/10.3102/00028312017002211
    - 使える数値（確認済み）：「135の研究」。効果の大きさは未確認（使わない）。
- 限界・注意：
  - **対象は学校・大学の学生**（Nesbit の「地図を読む」研究はほぼ全部が大学生、多くは実験室で1時間前後）。社会人が仕事で新しい分野に追いつく場面を調べた研究ではない。
  - 地図は研究者・先生が正しく作ったもの。**AIが作った（間違いを含むかもしれない）地図の効果を調べた研究は、今回の検索では見つからなかった**。
  - 測ったのは主に「覚えているか（保持）」。仕事で使えるようになるか、会議の話が分かるようになるかは測っていない。著者も、より高いレベルの学び（問題解決など）への効果は証拠が足りないと書いている。
  - g は「平均の差を標準偏差で割った値」で、「〇%良くなる」という意味ではない。
  - どれも平均の傾向で、個人には当てはまらないことがある。
- 記事での使い方の案：
  - 研究で分かっていること：「全体の図（概念マップ）で学ぶと、平均すると覚えている量が増えるという研究のまとめがあります。用意された図を読むより、自分で作るほうが効果が大きく、とくに大づかみの考えが残りやすいという結果です（学生の研究）」。
  - Claude の提案（研究の結論ではない）：「AIに地図の下書きを作らせ、自分で線を引き直す・つながりを書き直す」。研究で「自分で作る」ほうが効果が大きかったことを参考にした提案で、AIの地図を確かめた研究はない、と添える。

### 問い B2：用語を覚えるとき、思い出す練習（検索練習）や間をあけたくり返し（分散学習）はどこまで裏づけがあるか

- 分かっていること：
  - **学習法の大きなレビュー（Dunlosky ら 2013）で、10の学習法のうち「思い出す練習（practice testing）」と「間をあけた学習（distributed practice）」の2つだけが「有用性が高い」と評価された**。抄録には「年齢や能力の違う学習者に効果がある」とある。
    - 「中くらい」：理由を自分に問う（elaborative interrogation）、自分に説明する（self-explanation）、種類を混ぜて練習する（interleaved practice）。
    - 「低い」：要約、線を引く（ハイライト）、語呂合わせ（keyword mnemonic）、イメージを使う、読み直し。
    - → 用語メモに当てはめると「AIの説明を読み直す・線を引く」より「隠して思い出してから答え合わせする」ほうが裏づけがある、と言える。
    - ※自分に説明する（self-explanation）は drafts/2026-10-10-am（#04）で扱っているので、ここでは触れないか #04 に案内する。
  - **思い出す練習（テスト効果）のメタ分析**（Rowland 2014）：61の研究・159の効果量。もう一度読む（再学習）と比べて、**思い出す練習のほうが平均 g = 0.50（95%CI 0.42〜0.58）よく覚えていた**。
    - **答え合わせ（フィードバック）があると g = 0.73、ないと g = 0.39**。
    - **答え合わせがなく、練習のときに半分以下しか思い出せなかった場合は g = 0.03（効果なし）**。→ 「思い出せなかったら、すぐ正解を見て直す」ことが大事、の根拠。用語メモに「答え合わせ」の欄を作る理由になる。
    - 最後のテストまで1日以上あいた研究のほうが効果が大きかった（1日以上 g = 0.69、1日未満 g = 0.41）。
    - 対になった言葉（例：外国語と訳語）を覚える課題で g = 0.59。用語と意味の組み合わせに近い形式。
    - 159の効果量のうち136は大学生のデータ。大学生以外（23）でも効果に差はなかった。
  - **授業の中での小テスト**（Yang ら 2021）：222の研究・48,478人の学生のメタ分析で、小テストは学業成績を中くらい（g = 0.499）上げた。効果は、比べる学習法、答え合わせの有無、くり返し回数などで変わった。
  - **間をあけた学習**：drafts/2026-10-25-pm と同じ Cepeda ら 2006 を使う（再利用・確認済み）。184の論文・317の実験・839の比較で、覚えておく期間が1か月より長い研究では、まとめて学ぶより分けて学んだほうが平均15%（正答率の差）よかった。データの約85%は18〜35歳。-25-pm で説明しているので、今回は1文で十分。
- 根拠：
  - Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. 2013『Improving Students' Learning With Effective Learning Techniques: Promising Directions From Cognitive and Educational Psychology』Psychological Science in the Public Interest 14(1), 4–58（種類：narrative review〔学習法ごとの研究を整理して評価したレビュー。meta-analysis ではない〕／査読済み）
    - 確認した場所：抄録（Europe PMC、PMID 26173288）https://doi.org/10.1177/1529100612453266
    - 使える数値（確認済み）：「10の学習法」「高い評価は2つ（思い出す練習・間をあけた学習）」「低い評価は5つ」
  - Rowland, C. A. 2014『The effect of testing versus restudy on retention: A meta-analytic review of the testing effect』Psychological Bulletin 140(6), 1432–1463（種類：meta-analysis／査読済み）
    - 確認した場所：本文PDF（著者がアップロードした版。p.8 方法、p.12 結果、p.13 表1）https://courseware.epfl.ch/assets/courseware/v1/fdde2f0aa590bf3b1324077a6bf1540c/asset-v1%3AEPFL%2BDEMO%2B2020%2Btype%40asset%2Bblock/Rowland2014-meta-analysis.pdf ／書誌：Europe PMC
    - 使える数値（確認済み）：「61の研究・159の効果量」「全体 g=0.50（95%CI 0.42〜0.58）」「答え合わせあり g=0.73／なし g=0.39」「答え合わせなし・練習時に50%以下しか思い出せなかった場合 g=0.03」「最後のテストまで1日以上 g=0.69／1日未満 g=0.41」「対になった言葉 g=0.59」「159のうち136が大学生のデータ」
  - Yang, C., Luo, L., Vadillo, M. A., Yu, R., & Shanks, D. R. 2021『Testing (quizzing) boosts classroom learning: A systematic and meta-analytic review』Psychological Bulletin 147(4), 399–435（種類：systematic review・meta-analysis／査読済み）
    - 確認した場所：抄録（Europe PMC、PMID 33683913）https://doi.org/10.1037/bul0000309
    - 使える数値（確認済み）：「222の研究・48,478人」「g=0.499」
  - （再利用）Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. 2006『Distributed practice in verbal recall tasks』Psychological Bulletin 132(3), 354–380（meta-analysis／査読済み）
    - 確認した場所：drafts/2026-10-25-pm/research.md の B3（本文PDFで確認済み）
    - 使える数値（確認済み・再利用）：「184の論文・317の実験・839の比較」「保持期間1か月超で平均15%」「データの約85%が18〜35歳」
- 限界・注意：
  - 対象は主に大学生・実験室・学校の授業。**職種変更・異動で仕事の用語を覚える社会人を調べた研究は見つからなかった**。
  - 測っているのは「覚えている・思い出せる」こと。用語の意味を会議で使いこなせるか、全体のつながりが分かるかは別の話。
  - Dunlosky は効果量をまとめたメタ分析ではなく、研究を読んで評価したレビュー。「〇%効果がある」とは書けない。
  - g は「〇%良くなる」という意味ではない（Cepeda の15%は正答率の差なので別）。
  - 分散学習は「同じ量をまとめるか分けるか」の比較で、「量を減らしてよい」という研究ではない（-25-pm と同じ注意）。
- 用語メモの作り方の根拠に使えるか：
  - **使える（ただし学生の研究を参考にした提案として）**。「AIの説明を読み直すより、言葉だけ見て意味を思い出し、すぐ答え合わせする」「日をあけてもう一度思い出す」は研究とつながっている。
  - 書き方の例：「思い出す練習と、間をあけた復習は、学習法の研究で一番裏づけがある方法です（主に学生の研究）。用語メモは、読み返すためではなく、隠して思い出すために使います」。
  - ひな形の「自分の言葉で一文」の欄は、self-explanation（#04の領域）に近いので、根拠は #04 に任せ、ここでは研究を出さない。

### 問い B3：AIの説明を確かめる方法として、一次資料に当たる・複数の情報源を照らし合わせる（ラテラル・リーディングなど）の研究はあるか

- 分かっていること：
  - **プロのファクトチェッカーは「横に読む」**：経験のあるネット利用者45人（博士号を持つ歴史家10人、プロのファクトチェッカー10人、スタンフォード大学の学部生25人）に、実際のウェブサイトを考えながら評価してもらった研究。歴史家と学生は、それらしいロゴやドメイン名など、簡単に作れる見た目にだまされることが多く、サイトの中だけを上から下へ読んで判断していた（縦に読む）。ファクトチェッカーはサイトをざっと見たらすぐ離れ、新しいタブで「このサイトの元はどこか」を調べていた（横に読む＝lateral reading）。そして、ほかの2グループより短い時間で、よりしっかりした結論にたどり着いた。
  - **横に読むことは教えると身につく（学生）**：
    - アメリカの州立大学のオンライン講座（栄養学）で、87人の学生が1時間の教材を4つ受けた。サイトを離れて別の情報源を1つ以上確かめた学生は、**事前テストで87人中3人、事後テストで87人中67人**。13点満点のテストの平均は3.95点 → 7.08点。ただし、横に読んだ67人のうち、サイトの信頼性を正しく疑えたのは36人で、31人は横に読んでも結論が違っていた。比べる群のない前後比較。
    - 高校の授業での研究（Wineburg ら 2022）：教師が数か月にわたって数回の授業を行い、授業を受けたクラスの生徒は、ふつうのクラスの生徒より、ネットの情報の信頼性を判断する力が伸びた（査読前版の抄録の転載で確認。人数などの数値は出版社版で確認できていないので使わない）。
  - **AIの説明を読むと速いが、AIが間違っていると人も間違える**（Si ら 2024）：
    - 80人（クラウドソーシングの Prolific、各条件16人）が、本当か嘘か分からない主張（200件から1人20件）を判定した。条件は、主張だけ／Wikipedia の関連段落を読む／ChatGPT（gpt-3.5-turbo、2023年7〜8月）の説明を読む／「本当である理由と嘘である理由」の両方を読む／段落と説明の両方、の5つ。
    - **ChatGPT の説明が正しいとき、正解率は0.87。説明が間違っているときは0.35に下がった**（説明を信じすぎた）。説明が間違っていた問題でも、Wikipedia の段落を読んだ人の正解率は0.54だった。
    - 説明を読むほうが、段落を読むより判断が有意に速かった。
    - 「本当の理由と嘘の理由の両方」を出させると信じすぎは減ったが、段落を読むより有意に良くはならなかった。段落と説明を両方見せても、段落だけより良くはならなかった。
    - 著者のまとめ：「重要な場面では、AIの説明は、元の資料を読むことの代わりにはならないかもしれない」。
- 根拠：
  - Wineburg, S., & McGrew, S. 2019『Lateral Reading and the Nature of Expertise: Reading Less and Learning More When Evaluating Digital Information』Teachers College Record 121(11), 1–40（種類：熟達者と初心者を比べた質的研究／査読済み）
    - 確認した場所：Crossref に出版社が登録した抄録 https://api.crossref.org/works/10.1177/016146811912101102
    - 使える数値（確認済み）：「45人（歴史家10人・ファクトチェッカー10人・学部生25人）」
  - Breakstone, J., Smith, M., Connors, P., Ortega, T., Kerr, D., & Wineburg, S. 2021『Lateral reading: College students learn to critically evaluate internet sources in an online course』Harvard Kennedy School Misinformation Review 2(1)（種類：個別研究〔前後比較〕／査読済み）
    - 確認した場所：本文PDF（p.1–5）https://misinforeview.hks.harvard.edu/wp-content/uploads/2021/02/breakstone_lateral_reading_online_course_20210223.pdf
    - 使える数値（確認済み）：「87人・1時間の教材4つ」「横に読んだ学生：事前3人 → 事後67人（87人中）」「67人のうち正しく疑えたのは36人」「13点満点で平均3.95点 → 7.08点」
  - Wineburg, S., Breakstone, J., McGrew, S., Smith, M. D., & Ortega, T. 2022『Lateral reading on the open Internet: A district-wide field study in high school government classes』Journal of Educational Psychology 114(5), 893–909（種類：クラス単位の比較研究／査読済み）
    - 確認した場所：書誌は Crossref（https://doi.org/10.1037/edu0000740）。内容は SSRN 掲載版（2021年、査読前）の抄録を転載した SSRC MediaWell のページ https://mediawell.ssrc.org/?p=510382 で読んだ。出版社版の抄録・本文は読めていない。
    - 使える数値：なし（「271人 vs 228人」「1時間の授業6回・3か月」は査読前版の抄録の転載でしか見ていないため未確認扱い）。
  - Si, C., Goyal, N., Wu, T., Zhao, C., Feng, S., Daumé III, H., & Boyd-Graber, J. 2024『Large Language Models Help Humans Verify Truthfulness – Except When They Are Convincingly Wrong』Proceedings of NAACL 2024 (Long Papers), 1459–1474（種類：実験／査読済み・国際会議）
    - 確認した場所：抄録 https://aclanthology.org/2024.naacl-long.81 ／本文（arXiv v2、5.1〜5.2節）https://arxiv.org/html/2310.12558v2
    - 使える数値（確認済み）：「80人（Prolific、5条件・各16人）」「200件の主張、1人20件」「説明が正しいときの正解率0.87／間違っているとき0.35」「説明が間違っていた問題で、段落を読んだ人の正解率0.54」
- 限界・注意：
  - ラテラル・リーディングの研究は、**ウェブサイトの信頼性の判断**（政治・社会の話題）を学生で調べたもの。AIの説明を確かめる場面、仕事の専門用語を確かめる場面ではない。
  - Breakstone 2021 は比べる群がない前後比較。横に読むようになっても、半分近くは結論を誤った。「横に読めば正しく判断できる」とは書かない。
  - Si ら 2024 はクラウドワーカーが短い主張を判定した実験で、使ったのは2023年の gpt-3.5-turbo。今のAIの間違いの頻度にそのまま当てはまらない。「AIの説明は35%しか当たらない」という意味ではない（**AIが間違えたときに、人が正しく判定できた割合**）。
  - **「AIの答えを別の資料で確かめると、仕事の理解の誤りが減る」ことを社会人で直接調べた研究は見つからなかった**。
- 記事での使い方の案：
  - 研究で分かっていること：「AIの説明を読むと速く判断できるが、説明が間違っていると、読んだ人も一緒に間違えやすい。元の資料を読んだ人のほうが、その場面では正解が多かった、という実験があります（2023年のAI、クラウドワーカー80人）」「プロのファクトチェッカーは、気になる情報があるとすぐ別の情報源を見に行く（横に読む）。これは学生でも教えると身につく」。
  - Claude の提案：「確かめる場所を3か所（一次資料・人・自分の言い直し）に決めておく」は、これらの研究を参考にした提案で、効果を確かめた研究はない、と書く。
  - 補足（A2 との関係）：Si ら 2024 は「知識が少ない人ほど気づきにくい」ことを直接調べたものではない。A2 の担当の結果とそろえて使う。

### 問い B4：社内の資料・社内の言葉をAIに入れてよいか（drafts/2026-10-19-am にそろえる。古くなっていないかの確認のみ）

- 確認結果：**古くなっていない（2026-10-26 時点）**。drafts/2026-10-19-am/research.md の問い4の内容をそのまま使ってよい。
  - **AI事業者ガイドライン**：総務省のページで、掲載されている最新版は**第1.2版（令和8年3月31日）**。それより前は第1.1版（2025年3月28日）、第1.01版（2024年11月22日）、第1.0版（2024年4月19日）。第1.3版などの新しい版は見当たらなかった。
    - 確認した場所：https://www.soumu.go.jp/main_sosiki/kenkyu/ai_network/02ryutsu20_04000019.html （経済産業省のページは 403 で開けなかった）
  - **個人情報保護委員会**：「注意情報」の一覧で、生成AIについての注意喚起は**2023年6月2日「生成AIサービスの利用に関する注意喚起等について」が唯一**。その後のAI関連は2025年2月3日の「DeepSeekに関する情報提供」のみ（一覧では2026年10月7日の別件の注意喚起まで載っており、新しい生成AIの注意喚起はなかった）。注意喚起のページも掲載が続いている。
    - 確認した場所：https://www.ppc.go.jp/news/careful_information/ ／ https://www.ppc.go.jp/news/careful_information/230602_AI_utilize_alert/
- 注意：
  - 2026年4月に個人情報保護法の改正案が閣議決定されたという解説記事（法律事務所など）があるが、今回は一次資料を確認していない（未確認）。この記事では触れなくてよい。触れるなら公開前に個人情報保護委員会のページで確かめる。
  - -19-am の書き方の注意（「ガイドラインが従業員に会社のルールの確認を求めている」とは書かない／ガイドラインは事業者向けで、具体的な線引きは各社に任されている）はそのまま有効。
  - この記事の方針（社内の言葉・略語はAIに入れず人に聞く）は、ガイドラインの「機密情報を不適切に入力しないよう注意」と矛盾しない。ただし「入れてはいけない」と法的に断定はしない。

### 問い B5：使わないほうがよい情報（検索で出てきた、出典のはっきりしない数字）

→ 下の「使わないほうがよい情報」にまとめた。結論：**「〇日で業界に追いつける」を示す研究は見つからなかった**。「AIで学習時間・立ち上がり時間が〇%短縮」という数字は、出てきたものがすべて、販売会社のブログ・自社調査・自己申告のアンケート・原典不明の孫引きだった。

## 分かっていないこと

- 職種を変えた社会人が、新しい分野の言葉や全体像をAIで学んだとき、AIを使わない場面での理解がどうなるか（高校生・大学生・顧客サポートの研究しかない）。
- Bastani らの研究の、別の場所・別の対象での追試（見つからなかった）。
- 生成AIで、その分野の知識の量によって誤りの見抜き方がどう違うか（直接比べた査読済みの実験は見つからなかった）。
- 生成AIが一般的な専門用語・業界の言葉を説明するときの誤りの割合（測った研究は見つからなかった）。分野をまたいでまとめた数字もない。
- AIが社内の略語を聞かれたとき、どのくらいの割合で「知らない」と言わずにそれらしい説明を作るか（研究は見つからなかった）。
- 「言葉が分からない」ことが新しく入った人の負担・成果にどのくらい影響するか（効果の大きさ）。
- 「地図・つながり・確認の質問をAIに作らせ、正しさは自分で確かめる」という手順の効果（研究で確かめられていない。Claudeの提案として書く）。

- **AIが作った全体の図（地図）で学ぶ効果**：概念マップの研究は人が作った正しい地図が前提。AIが作った、間違いを含むかもしれない地図の効果を調べた研究は見つからなかった。
- **社会人が職種変更・異動で、新しい分野の言葉や全体像に追いつく方法を比べた研究**：見つからなかった（概念マップ・思い出す練習・分散学習の研究は、ほぼ学生）。
- **「何日で業界に追いつけるか」**：研究は見つからなかった。
- **AIの説明を一次資料で確かめると、仕事での誤解が減るか**：社会人で直接調べた研究は見つからなかった。近いのは Si ら 2024（短い主張の真偽判定、クラウドワーカー、2023年のモデル）。
- **社内の言葉・略語を、AIに聞いた場合と人に聞いた場合で比べた研究**：見つからなかった。
- 先行オーガナイザーのメタ分析（Luiten 1980）の効果の大きさ：本文を読めず未確認。

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

- **「AIを使うと新入社員の立ち上がりが半分に（49日 vs 91日）」**（開発者向けの調査会社 DX のブログ）：販売会社の自社データで査読なし。開発者が「10回目のプルリクエスト」に達するまでの日数という特殊な指標で、AIを毎日使う人と使わない人を比べただけの観察（もともと速い人がAIを多く使っている可能性がある）。職種変更の理解の速さとは別物。原文は開いておらず、検索結果の要約で見ただけ。
- **「AIを使ったオンボーディングで立ち上がり時間が25〜40%短縮」（Brandon Hall Group や Deloitte の調査とされる）**：販売会社のページでの孫引きしか見つからず、原典を確認できなかった（未確認）。
- **「生成AIで週10時間以上の業務時間を短縮（42%、日本29%）」（UiPath の調査）**：販売会社の調査で、本人の申告。学習・キャッチアップの時間ではなく業務時間の話（検索結果の要約で見ただけで未確認）。
- **「生成AI研修の受講者の98.5%が業務時間を削減」「生成AIで作業時間が3〜4割短縮」**などの国内の企業調査：研修会社・IT企業の自社アンケートで、回答者が限られ、自己申告。学習の速さとは別（未確認）。
- **「人は1日で74%忘れる」などのエビングハウスの忘却曲線の数字**：用語メモの話でよく出るが、元の実験は意味のない文字の並びを本人1人で覚えたもので、数字は媒体によって違う。今回原典を確認していない（未確認）。仕事の言葉に当てはまる数字ではない。
- **「人に教えると90%覚えている」（ラーニングピラミッド）**：学習法の話でよく出るが、元になった研究データが示されていないと以前から指摘されている図。今回も原典は見つからなかった。使わない。
- **Hattie『Visible Learning』の先行オーガナイザー・概念マップの効果量（d = 0.21 など）**：読者のメモなどの孫引きでしか見ておらず、未確認。複数のメタ分析をさらにまとめた数字で、条件の違いが見えなくなる。
- **Nesbit & Adesope 2006 の全体の値（g = 0.604）だけを出すこと**：アフリカの研究（効果がとても大きい、g = 1.446）を含んだ値で、著者自身が以降の分析はアメリカ・カナダに絞っている。使うなら「読む」「作る」の値を分けて、比べた相手と一緒に書く。
- **「概念マップで成績が58%上がる」「思い出す練習で50%覚えられる」のような言い換え**：g = 0.58、g = 0.50 は標準偏差の単位で、パーセントではない。
- **Si ら 2024 を「AIの説明の65%は間違い」「AIを使うと正解率35%」と書くこと**：0.35 は「AIの説明が間違っていた問題」での人の正解率。AIの説明全体の正しさとは別。
- **Wineburg ら 2022 の「271人 vs 228人」「6回・3か月」**：査読前版の抄録の転載で見ただけで、出版社版で確認していない（未確認）。
- **2026年の個人情報保護法改正案の内容**：解説記事でしか見ておらず未確認。
- **「AIは社内の略語を知らないので必ず間違える」と言い切ること**：研究ではなく推論。A3 の担当の整理とそろえ、「AIが知りようがないことがある」程度にする。

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

- Breakstone, J., Smith, M., Connors, P., Ortega, T., Kerr, D., & Wineburg, S. (2021). Lateral reading: College students learn to critically evaluate internet sources in an online course. *Harvard Kennedy School (HKS) Misinformation Review, 2*(1). https://doi.org/10.37016/mr-2020-56
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. https://doi.org/10.1037/0033-2909.132.3.354
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques: Promising directions from cognitive and educational psychology. *Psychological Science in the Public Interest, 14*(1), 4–58. https://doi.org/10.1177/1529100612453266
- Luiten, J., Ames, W., & Ackerson, G. (1980). A meta-analysis of the effects of advance organizers on learning and retention. *American Educational Research Journal, 17*(2), 211–218. https://doi.org/10.3102/00028312017002211
- Nesbit, J. C., & Adesope, O. O. (2006). Learning with concept and knowledge maps: A meta-analysis. *Review of Educational Research, 76*(3), 413–448. https://doi.org/10.3102/00346543076003413
- Rowland, C. A. (2014). The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. *Psychological Bulletin, 140*(6), 1432–1463. https://doi.org/10.1037/a0037559
- Schroeder, N. L., Nesbit, J. C., Anguiano, C. J., & Adesope, O. O. (2018). Studying and constructing concept maps: A meta-analysis. *Educational Psychology Review, 30*(2), 431–455. https://doi.org/10.1007/s10648-017-9403-9
- Si, C., Goyal, N., Wu, T., Zhao, C., Feng, S., Daumé III, H., & Boyd-Graber, J. (2024). Large language models help humans verify truthfulness – except when they are convincingly wrong. In *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2024), Volume 1: Long Papers* (pp. 1459–1474). https://doi.org/10.18653/v1/2024.naacl-long.81
- Wineburg, S., & McGrew, S. (2019). Lateral reading and the nature of expertise: Reading less and learning more when evaluating digital information. *Teachers College Record, 121*(11), 1–40. https://doi.org/10.1177/016146811912101102
- （数値を使わず触れる場合）Wineburg, S., Breakstone, J., McGrew, S., Smith, M. D., & Ortega, T. (2022). Lateral reading on the open Internet: A district-wide field study in high school government classes. *Journal of Educational Psychology, 114*(5), 893–909. https://doi.org/10.1037/edu0000740
- Yang, C., Luo, L., Vadillo, M. A., Yu, R., & Shanks, D. R. (2021). Testing (quizzing) boosts classroom learning: A systematic and meta-analytic review. *Psychological Bulletin, 147*(4), 399–435. https://doi.org/10.1037/bul0000309
- 個人情報保護委員会（2023年6月2日）「生成AIサービスの利用に関する注意喚起等について」 https://www.ppc.go.jp/news/careful_information/230602_AI_utilize_alert/
- 総務省・経済産業省（2026年3月31日）「AI事業者ガイドライン（第1.2版）」本編 https://www.soumu.go.jp/main_content/001064279.pdf ／別添（付属資料） https://www.soumu.go.jp/main_content/001064286.pdf

⸻

### まとめ（数）

- 記事で使える研究：11本（＋公的文書2つ）。
  - meta-analysis 6本：Nesbit & Adesope 2006・Schroeder 2018・Luiten 1980（数値は研究数のみ）・Rowland 2014・Yang 2021・Cepeda 2006（-25-pm から再利用）
  - レビュー 1本：Dunlosky 2013
  - 個別研究 4本：Wineburg & McGrew 2019・Breakstone 2021・Si 2024・Wineburg 2022（数値は使わない）
  - 公的文書 2つ：AI事業者ガイドライン第1.2版・個人情報保護委員会の注意喚起（-19-am から再利用。最新であることを今回確認）
- 確認済みの数値：38個（数え方：1つの文の中で組になるもの、例「55の研究・67の効果量・5,818人」は1つと数えた。公的文書の日付は含めない）。
  - B1：14（Nesbit 10・Schroeder 3・Luiten 1）
  - B2：15（Dunlosky 3・Rowland 7・Yang 2・Cepeda 3〔再利用〕）
  - B3：9（Wineburg & McGrew 1・Breakstone 4・Si 4）
- 査読前の情報で数値を使わなかったもの：Wineburg ら 2022 の SSRN 版（2021年）の抄録の数値。
