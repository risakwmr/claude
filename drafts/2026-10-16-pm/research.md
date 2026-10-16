# research｜2026-10-16-pm（問い1・4＝担当A、問い2・3・5＝担当B を合わせたもの）

確認日：2026-10-16。数値はすべて担当者が論文本文・抄録で確かめたもの。

調べた日：2026-10-16

全体の注意（書き手向け）
- ここで使う研究は、ほとんどが**生成AI以前**の「自動化」研究（飛行シミュレーター、工場の監視作業、医療の判断支援システム）。AIエージェントにメール・議事録・送信まで任せる場面に、そのまま当てはまるとは言えない。本文では「こういう場面で調べられてきた」と書き、AIエージェントへの当てはめは推測と分かる書き方にする。
- どれも**平均の傾向**。「誰でも必ずこうなる」「この人はこうなる」とは言えない。
- 研究からSena個人の状態（うつ・ADHD・調子の低い日）を推測しない。問い4の結果を「うつの日は過信しやすい」と書き換えない（下の「使わないほうがよい情報」参照）。

注：Mosier ほか（パイロットの説明責任）は、担当Aは「使わないほうがよい」、担当Bは「相関のみ」として扱った。使う場合は「パイロットの研究で、責任を感じていた人ほど確かめていたという相関」にとどめる。Skitka 2000 は本文未確認なので使わない。

## 問いごとの答え

### 問い1・4（担当A）
### 問い1：自動化バイアス・自動化への過信（complacency）は、研究でどこまで分かっているか。見落とし（omission）と間違った提案に従う（commission）の両方は確認されているか。経験者や訓練で減るのか。Goddard の発行年は？

- 分かっていること：
  - **言葉の整理**：「自動化への過信（complacency）」は、主に複数の作業を同時にしているときに、自動化の監視がおろそかになること。「自動化バイアス（automation bias）」は、判断のときに自動化の提案に引っぱられること。Parasuraman & Manzey（2010）は、この2つを「重なり合う現象の別の現れ方」とまとめ、**注意の向け方**が中心にあるとしている。
  - **2種類の誤りはどちらも確認されている**：自動化の提案が不完全なとき、「知らせてくれなかったものを見落とす（omission）」誤りと、「間違った提案にそのまま従う（commission）」誤りの両方が起きる（Parasuraman & Manzey 2010 の抄録）。40研究を集めた Lyell & Coiera（2017）のレビューでは、omission を調べた研究の81%（25/31）、commission を調べた研究の91%（21/23）で自動化バイアスの証拠が見つかった。
  - **医療での大きさの目安**：Goddard ほか（2012）のレビュー（74研究）の中の小さなメタ分析（医療の4研究）では、判断支援システムの提案が間違っていたとき、システムを使ったグループは使わないグループより、間違った判断をする危険が約1.26倍（95%信頼区間 1.11〜1.44）だった。
  - **経験者でも起きる**：Parasuraman & Manzey（2010）は、過信も自動化バイアスも「初心者でも熟練者でも起きる」とまとめている。Goddard ほか（2012）は「経験の少ない人に多いが、経験のある人にも起きる」と書いている。
  - **訓練・指示で減るか**：研究によって結論が割れている。
    - Parasuraman & Manzey（2010）の抄録：自動化バイアスは「訓練や指示では防げない」、過信は「単純な練習では克服できない」。
    - Lyell & Coiera（2017）：訓練の介入では自動化バイアスの率に有意な減少はなく、成績のフィードバックも効果がなかった。「説明責任を持たせる」介入は、初心者に小さな効果、熟練者には効果なし（Skitka ほかの研究を引用）。
    - 一方 Goddard ほか（2012）は、訓練や「利用者の説明責任を強調すること」を自動化バイアスを減らしうる要因として挙げ、訓練で間違いに気づきやすくなる可能性（特に commission）にも触れている。ただし同じ論文の中で「訓練は効果がなかったとする研究もある」とも書いている。
    - → 本文では「訓練や練習だけでは防ぎきれない、という結論のレビューが多い」くらいにとどめる。「訓練は無意味」とも「訓練すれば防げる」とも書かない。
  - **複数の作業だけでなく、確かめにくい1つの作業でも起きる**：Lyell & Coiera（2017）は、従来「複数作業のときに起きる」と考えられてきたのに反して、**確認するのが難しい（verification complexity が高い）1つの作業**でも自動化バイアスが見つかったとし、頭の負荷（cognitive load）との関係を示唆している。
    - （書き手向けメモ）「AIの出した下書きが正しいか確かめるのが大変なほど、そのまま通しやすい」という話につなげられる。ただし研究は診断タスク中心で、メール・議事録で調べたものではない。

- 根拠：
  - Parasuraman R, Manzey DH 2010『Complacency and Bias in Human Use of Automation: An Attentional Integration』Human Factors 52(3):381–410（種類：レビュー〔ナラティブ・レビュー＋理論モデル。systematic review ではない〕／査読済み）
    - 確認した場所：https://depositonce.tu-berlin.de/items/0c787d91-6021-480b-a333-009e0d1d0092/full （TU Berlin リポジトリ。出版版。抄録を確認。本文は未読）
    - 使える内容（抄録で確認済み）：
      - 「Automation complacency occurs under conditions of multiple-task load, when manual tasks compete with the automated task for the operator's attention.」（確認済み）
      - 「Automation complacency is found in both naive and expert participants and cannot be overcome with simple practice.」（確認済み）
      - 「Automation bias results in making both omission and commission errors when decision aids are imperfect.」（確認済み）
      - 「Automation bias occurs in both naive and expert participants, cannot be prevented by training or instructions, and can affect decision making in individuals as well as in teams.」（確認済み）
      - 2つは「different manifestations of overlapping automation-induced phenomena」で、注意が中心的な役割を持つ（確認済み）
  - Goddard K, Roudsari A, Wyatt JC 2012『Automation bias: a systematic review of frequency, effect mediators, and mitigators』J Am Med Inform Assoc 19(1):121–127. doi:10.1136/amiajnl-2011-000089（種類：systematic review＋小規模meta-analysis／査読済み）
    - **発行年**：オンライン先行公開 2011年6月16日、掲載号は 2012年1–2月号（Vol.19 No.1）。参考文献では「2012」と書くのが一般的（オンライン公開は2011年、と添えてもよい）（確認済み）
    - 確認した場所：https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751 （PMC 本文）
    - 使える数値：
      - 「Of 13 821 retrieved papers, 74 met the inclusion criteria.」→ 74研究（確認済み）
      - 医療4研究のメタ分析：リスク比 1.26（95%CI 1.11〜1.44）。「when in error the CDSS increased the risk of an incorrect decision being made by 26%」（確認済み）
      - 「AB manifests in errors of commission (following incorrect advice) and omission (failing to act because of not being prompted to do so)」（定義、確認済み）
      - 「Automation bias occurs more often with task inexperienced users but can occur with more experienced users.」（確認済み）
      - 影響する要因：利用者側（認知スタイル、作業経験）、環境（作業負荷、作業の複雑さ、時間の制約）。減らしうる要因：訓練、説明責任の強調、出力に最新の確信度を付ける、「推奨」ではなく「情報」として出す（抄録、確認済み）
  - Lyell D, Coiera E 2017『Automation bias and verification complexity: a systematic review』J Am Med Inform Assoc 24(2):423–431. doi:10.1093/jamia/ocw105（種類：systematic review／査読済み）
    - 確認した場所：https://pmc.ncbi.nlm.nih.gov/articles/PMC7651899 （PMC 本文）
    - 使える数値：
      - 「Of 890 papers identified, 40 met the inclusion criteria; 6 were in health care.」（確認済み）
      - 「81% of studies (n = 25/31) testing for omission errors and 91% (n = 21/23) testing for commission errors」で自動化バイアスの証拠あり（確認済み）
      - 訓練の介入は自動化バイアスの率を有意に下げなかった／フィードバックは効果なし／説明責任の操作は初心者に小さな効果・熟練者に効果なし（本文 Discussion、確認済み）
- 限界・注意：
  - どれも生成AI・AIエージェント以前の研究（飛行、工場の監視、医療の判断支援など）。
  - Goddard ほかのレビュー自身が「自動化バイアスの報告が付随的（後付けの分析が多い）」「結果がばらばらで、メタ分析は小さいものしかできなかった」と限界を書いている。リスク比1.26は医療の4研究だけの値。
  - Lyell & Coiera も「研究ごとに報告の仕方が大きく違う」「対照条件と比べた統計的有意性を示した研究が少ない」「参加者が少なく均質」と限界を書いている。81%・91%は「その誤りを調べた研究のうち、証拠が出た研究の割合」で、「人の81%が見落とす」という意味ではない（誤読に注意）。
  - Parasuraman & Manzey は本文を読んでいない（抄録のみ確認）。抄録に書かれていること以上は書かない。

### 問い4：忙しさ・作業負荷・疲れが大きいとき、自動化に頼りやすくなるのか

- 分かっていること（3つに分けて書く）：
  1. **同時にこなす作業が多い（マルチタスク）とき**：自動化の監視がおろそかになりやすい、という結果は比較的しっかりしている。
     - Parasuraman, Molloy & Singh（1993）：40人が飛行シミュレーターで「手動の追従作業・燃料管理」と「自動化された監視作業」を同時に行う実験。自動化の信頼性がずっと一定（高いまま／低いまま）だと、約20分後から自動化の失敗を見つける率が大きく下がった。一方、監視だけを1つの作業としてやったときは、信頼性に関係なく失敗をよく見つけられた。
     - Parasuraman & Manzey（2010）の抄録も「過信は複数作業の負荷がかかる条件で起きる」とまとめている。
  2. **作業負荷・時間の制約が大きいとき**：レビューは「頼りやすくなる」方向を示しているが、多くは「そう考えられている（posited）」レベル。
     - Goddard ほか（2012）：作業負荷・作業の複雑さ・時間の制約を、自動化バイアスに影響する環境要因として挙げている（「認知の余力を圧迫する」）。本文では「複雑な作業や高い作業負荷は依存を増やすと考えられている（posited）」「時間の圧力が強いと判断支援を使う方向に偏りうる」という書き方。
     - Lyell & Coiera（2017）：Wickens & Dixon のレビューを引いて「高い作業負荷のもとでは自動化への依存が大きくなる」「いったん誤りが起きると、高い作業負荷のもとでは見つかりにくい」と書いている。自動化バイアスは頭の負荷（cognitive load）の大きさと関係しているようだ、というのがこのレビューの結論。
     - AIの提案を使った比較的新しい実験（Swaroop ほか 2024、IUI '24）：論理パズルで、AIの答えを先に見せる条件では、時間の圧力があると「AIが間違っている／最善でないときに同じ答えを選ぶ率（過剰依存率）」が 0.41 → 0.59 に上がった（実験2、316人、p=0.008）。ただし実験1（159人）では有意な差はなかった（p=0.13）。**結果は一貫していない**。
  3. **疲れ・睡眠不足のとき**：「疲れると頼りやすくなる」とは**言えない**。逆の結果もある。
     - Reichenbach, Onnasch & Manzey（2011）：工場の監視作業のシミュレーションで、昼の回と、20時間以上起き続けた夜の回を比べた。睡眠不足の状態の参加者は、むしろ**より慎重で、過信や自動化バイアスが少なかった**。ただし、別の作業（副次作業）の成績が落ちる、自動化が止まって手動に戻ったときに成績が落ちる危険が増える、というコストがあった。著者は「睡眠不足の人は注意の配分を変えて補っている」と解釈している。
     - → 「疲れている日は自動化を信じすぎる」という単純な話にはならない。研究では、疲れていると慎重になって補う人もいる一方、ほかのところに無理が出る、という結果。

- 書き手向けのまとめ（「調子が低い日」の分岐に使えるか）：
  - 使える言い方の例：「同時にいくつも抱えているときや、確認しにくい作業のときほど、自動化の間違いを見落としやすい、という研究があります（飛行や医療など、生成AI以前の研究です）」。
  - 使えない言い方：「うつの日は自動化に頼りすぎる」「疲れているとAIを信じすぎる」。うつ・気分の落ち込みと自動化への頼り方を直接調べた完成した研究は、今回の検索では見つからなかった。睡眠不足の研究はむしろ逆の結果。
  - 「調子が低い日は止まる地点を増やす」は、研究の結論ではなく**Claudeの提案**として書く（RULES 5.5）。根拠に使うなら「負荷が高いと見落としやすい、という研究がある」まで。「調子が低い日＝負荷が高い日」と研究が示したわけではない。

- 根拠：
  - Parasuraman R, Molloy R, Singh IL 1993『Performance consequences of automation-induced "complacency"』International Journal of Aviation Psychology 3(1)（種類：実験研究／査読済み）
    - 確認した場所：https://ntrs.nasa.gov/citations/19930055574 （NASA技術報告サーバーの抄録）
    - 使える数値：40人、30分×4セッション、約20分後から検出率が低下、単一作業では信頼性に関係なく検出が効率的（抄録で確認済み）。検出率の具体的な%は抄録になく、未確認。
    - 注意：ページ番号は確認できなかった。別の文献リストでは巻数が「2」になっているものもあるが、NASA記録の「3(1)」を採用（一般的にも 3(1):1–23 として引用される。ページは未確認）。
  - Goddard ほか 2012（上記）：作業負荷・時間の制約に関する記述は PMC 本文で確認済み。
  - Lyell & Coiera 2017（上記）：Wickens & Dixon を引いた記述、「once errors are made, they are less likely to be detected under conditions of high workload」は PMC 本文で確認済み。
  - Swaroop S, Buçinca Z, Gajos KZ, Doshi-Velez F 2024『Accuracy-Time Tradeoffs in AI-Assisted Decision Making under Time Pressure』Proceedings of IUI '24, doi:10.1145/3640543.3645206（種類：実験研究／査読あり国際会議。arXiv 2306.07458 に査読前版あり）
    - 確認した場所：https://arxiv.org/html/2306.07458v3 （本文。IUI '24 掲載と明記）
    - 使える数値：実験2（316人、米国の英語話者、Prolific）でAIを先に見せる条件の過剰依存率 0.41→0.59（p=0.008）／実験1（159人）では有意差なし（p=0.13）（確認済み）
    - 注意：AIは本物の機械学習モデルや生成AIではなく、正答率70%に設定された「台本どおりの提案」。課題は論理パズルで、著者自身が「現実的でない可能性」「専門家に当てはまるかは不明」と書いている。「過剰依存」には「間違い」だけでなく「最善でない答え」に従った場合も含む。
  - Reichenbach J, Onnasch L, Manzey D 2011『Human Performance Consequences of Automated Decision Aids in States of Sleep Loss』Human Factors（doi:10.1177/0018720811418222）（種類：実験研究／査読済み）
    - 確認した場所：https://depositonce.tu-berlin.de/items/45819fed-e956-462f-b00b-c781886ca29c （TU Berlin リポジトリの抄録）
    - 使える内容：20時間以上起きていた夜の回では、参加者はより慎重で、過信・自動化バイアスが少なかった。一方で副次作業の成績低下と、手動に戻ったときの成績低下の危険の増加があった（抄録で確認済み）。参加人数・巻号ページは未確認。

- 限界・注意：
  - 「負荷が高いと頼りやすい」は、レビューでは「そう考えられている」「支持されている」の言い方が多く、効果の大きさをまとめた数値は見つからなかった。
  - 研究の「負荷」は実験で作った同時作業・時間制限で、仕事の忙しさ・体調・気分の落ち込みとは別物。
  - 疲れ（睡眠不足）は逆の結果があり、方向がはっきりしない。

---

### 問い2・3・5（担当B）
### 問い2：生成AI（LLM）やAIエージェントの出力を、人はどの程度確認しているか。過信（overreliance）の査読済み研究・レビューはあるか

- 分かっていること：
  - 生成AIへの過信は、2023年以降に査読済みの実験研究がまとまって出てきている。共通する結果は「AIが正しいときは助かるが、AIが間違えたときに、人はその間違いにそのまま乗りやすい」。
  - LLM検索を使った人は、ふつうの検索より約半分の時間で終わり、満足度も高かった。一方、LLMが間違えやすい問題では正答率が大きく下がり、間違った情報を見た人も「信頼できた」と答える度合いはほとんど変わらなかった（＝間違いに気づいていない）。多くの人は質問を1回しかせず、確認の再検索をしていなかった。
  - AIの答えがあると、自分でネット検索する人の割合が大きく下がる（AIなし約93% → AIあり約19%）。
  - 説明を付けると、正しい答えにも間違った答えにも頼りやすくなる（説明は「確認」の代わりにならない）。出典を示すことは、間違った答えへの依存を下げた。
  - 過信しやすい人の行動として「コピー＆ペーストが多い」「最初に課題をよく読まない」「疑問を感じても確かめずに受け入れる」が観察された（小規模・査読前段階の採録）。
  - 人とAIを組み合わせると、人だけよりは良いが、「人かAIのうち良いほう」より平均で悪くなる、というmeta-analysisがある。特にAIのほうが得意な課題・判断の課題で損が出やすい。これは「人が最後に見れば安全」とは限らないことの根拠になる。
  - 生成AIへの過信をまとめたものは、Microsoftの研究者による文献レビュー（約50本・2024年）がある。ただし企業の技術報告で、査読は経ていない。生成AIに絞った査読済みの systematic review／meta-analysis は、今回の検索では見つからなかった。

- 根拠1：Spatharioti, Rothschild, Goldstein & Hofman 2025『Effects of LLM-based Search on Decision Making: Speed, Accuracy, and Overreliance』CHI '25（種類：ランダム化オンライン実験2本／査読済み・国際会議）
  - 確認した場所：https://dangoldstein.com/papers/spatharioti_rothschild_goldstein_hofman_LLM_Search_CHI25.pdf（本文）、https://www.microsoft.com/en-us/research/?p=1134789（抄録）
  - 対象：実験1は米国のMTurk参加者90人（2023年春、GPT-3.5）、実験2は120人（GPT-3）。SUV 2台のどちらが条件に合うかを調べる課題。
  - 使える数値：
    - 「LLM検索の所要時間は1課題あたり平均1.6分、従来の検索は3.4分（約50%短縮）」（確認済み）
    - 「LLMが間違えやすい課題での正答率：従来の検索93%、LLM検索47%」（確認済み）
    - 「LLM検索の51人のうち30人は質問を1回だけ送り、そのうち23人は間違った回答を受け取って、そのまま間違った選択をした」（確認済み）
    - 「信頼性の評価は両条件でほぼ同じ（差は有意でない）」（確認済み）
    - 実験2：「確信度の低い部分を色で示さない条件の正答率26%、色で示した条件は58%（高・低両方を表示）と53%（低いところだけ表示）」（確認済み → 問い3でも使える）
  - 限界・注意：2023年のモデル（GPT-3.5/GPT-3）で、商品比較という1種類の課題。「難しい課題」はLLMが間違えるように研究者が選んだもの。人数も少なめ。今のAIエージェントの精度とは違う。

- 根拠2：Kim, Liao, Vorvoreanu, Ballard & Vaughan 2024『"I'm Not Sure, But...": Examining the Impact of Large Language Models' Uncertainty Expression on User Reliance and Trust』FAccT '24（種類：事前登録したランダム化実験／査読済み・国際会議）
  - 確認した場所：https://facctconference.org/static/papers24/facct24-56.pdf（本文）、https://arxiv.org/abs/2405.00623（抄録）
  - 対象：米国のMTurk参加者404人（2023年9月）。医療に関する「はい／いいえ」の質問8問。AIの回答はCopilot in Bing（2023年7月）の実際の回答をもとにし、半分が正しく半分が間違い。
  - 使える数値：
    - 「AIの回答を見られる条件では、自分でネット検索した人は19.1%。AIなしの条件では92.9%」（確認済み）
    - 「正答率：AIなし74.2%、AIあり（不確かさの表示なし）63.9%」（確認済み。この実験ではAIの正答率が50%に設定されていたため、という著者の注記付き）
  - 限界・注意：AIの正答率を半分に設定した人工的な条件。医療の質問で、仕事のメールとは場面が違う。

- 根拠3：Kim, Vaughan, Liao, Lombrozo & Russakovsky 2025『Fostering Appropriate Reliance on Large Language Models: The Role of Explanations, Sources, and Inconsistencies』CHI '25（種類：事前登録した実験＋think-aloud／査読済み・国際会議）
  - 確認した場所：https://arxiv.org/abs/2502.08554（抄録）
  - 対象：308人の実験（客観的な正解がある質問にLLMアプリを使って答える）。
  - 使える内容：「説明があると、正しい回答にも間違った回答にも頼りやすくなる」「出典を示すと、間違った回答への依存が下がる」「説明の中の矛盾に気づくと、間違った回答への依存が下がる」（抄録で確認済み。効果の大きさの数値は未確認）
  - 限界・注意：抄録のみ確認。数値は本文で未確認。

- 根拠4：Liu, Zhou, Shen, Liu, Wu & Chen 2026『Behavioral Indicators of Overreliance During Interaction with Conversational Language Models』（arXiv 2602.11567。CHI 2026に条件付き採録と記載）
  - 確認した場所：https://arxiv.org/abs/2602.11567（抄録）
  - 対象：77人。3つの現実的な課題で、LLMにもっともらしい誤情報を混ぜ、気づいて直せたかで過信を測った。
  - 使える内容：「過信が多い人は、コピー＆ペーストが多い・最初の理解を飛ばす・LLMに何度も戻る・情報の探し方が粗い」「迷いを感じながらも誤情報を受け入れた人がいた」（抄録で確認済み）
  - 限界・注意：人数が少ない。抄録の時点で「条件付き採録」なので、査読済みとして扱うなら最終版を確認する。行動の特徴は相関で、原因とは言えない。

- 根拠5：Vaccaro, Almaatouq & Malone 2024『When combinations of humans and AI are useful: A systematic review and meta-analysis』Nature Human Behaviour 8(12), 2293–2303（種類：事前登録した systematic review・meta-analysis／査読済み）
  - 確認した場所：https://pmc.ncbi.nlm.nih.gov/articles/PMC11659167/（本文）、MITの紹介 https://mitsloan.mit.edu/node/48565
  - 対象：2020年1月〜2023年6月に発表された106の実験（370の効果量）。
  - 使える数値：
    - 「人＋AIは、人かAIのうち良いほうより平均で劣る：Hedges' g = −0.23（95%CI −0.39〜−0.07）」（確認済み）
    - 「人＋AIは、人だけよりは良い：g = 0.64（95%CI 0.53〜0.74）」（確認済み）
    - 「判断の課題では損：g = −0.27。何かを作る課題では有意でない得：g = 0.19」（確認済み）
    - 「人のほうがAIより得意な課題では、組み合わせで得（g = 0.46）。AIのほうが得意な課題では損（g = −0.54）」（確認済み）
  - 限界・注意：生成AIだけの研究ではない（多くは分類・予測の判断支援）。実験室の課題が中心で、研究ごとのばらつきが大きい。著者は出版バイアスの可能性も挙げている。AIエージェントに送信まで任せる場面に、そのまま当てはまるとは言えない。

- 根拠6（査読なし・補助）：Passi, Dhanorkar & Vorvoreanu 2024『Appropriate reliance on GenAI: Research synthesis』Microsoft 技術報告 MSR-TR-2024-7（種類：文献レビュー、約50本／査読なし・企業の報告）
  - 確認した場所：https://microsoft.com/en-us/research/uploads/prodnew/2024/03/GenAI_AppropriateReliance_Published2024-3-21.pdf（本文 1〜3ページ）
  - 使える内容：「生成AIは大量の文章（メールの下書きなど）を速く出すため、確認の負担が増える。人は文章の流暢さ・長さ・速さを正確さの目印にしてしまいがち」（本文で確認済み）
  - 限界・注意：査読を経ていない。著者はMicrosoftの研究者で、自社製品の文脈もある。

- 2010年ごろの自動化研究との違い（整理）：
  - 共通点：「間違ったAIの提案に乗る」「自分で確かめなくなる」という型は、生成AIの実験でも繰り返し観察されている（根拠1・2・4）。
  - 違い：①古い研究の多くは操縦室・医療の警報など「決まった出力」が対象だが、生成AIは毎回違う文章を作り、流暢なので間違いが見えにくい（根拠6）。②確認する量が多い（長い下書き・要約）。③AIエージェントは「提案」で止まらず「実行（送信）」まで進むため、人が確認しないと間違いがそのまま外に出る。AIエージェントの実行結果を人がどの程度確認しているかを測った査読済み研究は、今回の検索では見つからなかった。
  - 本文で書くときは「生成AIでも似た傾向が実験で見られている」までにとどめ、「AIエージェントでも同じことが起きる」とは断定しない。

### 問い3：過信を減らすために効果が確かめられている工夫はあるか（確認の手順、説明責任、不確かさの表示など）

- 分かっていること：
  - 効果が実験で確かめられたもの（ただし条件つき）：
    1. **先に自分で考えてからAIを見る／AIの答えを見るのを遅らせる／自分で押したときだけ見る**（認知的強制関数：cognitive forcing functions）。シンプルな説明つきAIより、間違ったAIの提案への依存が減った。ただし参加者からの評価は低く、考えることが好きな人ほど効果が大きかった。
    2. **AIの不確かさを示す**。一人称の言い方（「確かではありませんが…」）で正答率が上がった。確信度の低い部分の色分けで、LLMが間違える課題の正答率が26%→53〜58%に上がった。
    3. **出典を示す**。間違った回答への依存が下がった（抄録で確認）。
  - 注意が必要なもの：
    - **説明を付ける**：説明があると、正しい答えにも間違った答えにも頼りやすくなる（LLMの実験）。説明可能なAIのmeta-analysisでも、「AIの予測だけ」と比べて説明が成績を上げる効果は見られなかった。
    - **確認の手間とのバランス**：説明を読む手間が大きいと使われず過信が増え、自分でやる手間が大きいときや、正しくやる報酬が大きいときは過信が減る（費用と利益で決まる）。
    - **対策の多くは「頼る量を全体に減らす」だけ**：GPT-4oを使った実験では、3つの対策（注意書き・不確かさの色分け・答えを直接言わない）はいずれも過信を減らしたが、正しいときは頼り間違っているときは頼らない「適切な頼り方」は全体としてはあまり改善しなかった。正しいアドバイスへの依存まで減ることがある。
    - **対策が逆効果になることがある**：Microsoftの研究者による生成AIのレビューは「対策は状況によって逆に過信を増やすことがあるので、使う場面で効果を確かめる必要がある」と書いている。
  - 説明責任（accountability）：古い自動化研究（パイロット）で、「自分が自動化の使い方に責任を持つ」と感じていた人ほど、自動化の出力を他の手がかりで確かめ、間違いが少なかったという報告がある。ただし、この関連は本人の感じ方との相関で、確認できたのは学会発表の抄録のみ。Skitka, Mosier & Burdick 2000（International Journal of Human-Computer Studies）の本文・抄録は今回読めなかった。
  - **「確認の手順を決めておく（チェックリスト）」が生成AI・AIエージェントの過信を減らすかを直接確かめた査読済み研究は、今回の検索では見つからなかった。** 認知的強制関数の考え方のもとになった医療の意思決定研究では、チェックリストは例として挙げられているが（Buçinca 2021 本文）、AIの確認での効果は確かめられていない。記事のチェックリストは「研究をヒントにしたClaudeの提案」と書く必要がある。

- 根拠1：Buçinca, Malaya & Gajos 2021『To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making』Proc. ACM Hum.-Comput. Interact. 5 (CSCW1), Article 188（種類：ランダム化実験／査読済み）
  - 確認した場所：https://kgajos.seas.harvard.edu/papers/bucinca21trust.pdf（本文）、https://arxiv.org/abs/2102.09692（抄録）
  - 対象：米国在住の成人、Amazon MTurk。260人を集め、除外後の分析対象は199人。料理の写真から一番炭水化物が多い食材を選び、置き換える課題。AIは研究用に作ったもので正答率75%。
  - 3つの工夫：①「AIの提案を見る」ボタンを押したときだけ表示（on demand）②まず自分で決めてから、AIの提案を見て変更できる（update）③AIの提案を30秒待たせる（wait）。
  - 使える数値：
    - 「AIが間違えたとき、どの食材を減らすかでAIに従ってしまった割合：シンプルな説明つきAI 64%、認知的強制関数 48%（効果量 d = 0.36）」（確認済み）
    - 「全体の判断での過信は30%と26%で、有意な差なし」（確認済み。効果が出たのは一部の指標だけ、と書く必要がある）
    - 「過信を最も減らした工夫ほど、参加者の主観的な評価が最も低かった」（抄録で確認済み）
  - 限界・注意：生成AI以前、研究用の模擬AI、栄養という身近な課題。工夫が効いたのは「考えることが好き」な人に偏っていた。AIがない条件のほうが、AIが間違えた問題では成績が良かった。

- 根拠2：Kim ほか 2024（FAccT '24、問い2の根拠2と同じ）
  - 使える数値：
    - 「AIの答えに同意した割合：不確かさの表示なし80.9%、一人称の表示（『確かではありませんが…』）74.8%」（確認済み）
    - 「正答率：不確かさの表示なし63.9%、一人称の表示72.8%、一般的な言い方（『はっきりしませんが…』）67.9%（後者は有意差なし）」（確認済み）
    - 「一人称の表示は、システムを使い続けたい気持ち（trust intention）を下げた」（確認済み）
  - 限界・注意：言い方によって効果が違う（一般的な言い方は弱く有意でない）。著者は「使う前に利用者でテストすべき」と書いている。過信は「減ったが、なくなってはいない」。

- 根拠3：Spatharioti ほか 2025（CHI '25、問い2の根拠1と同じ）実験2
  - 使える数値：「LLMが間違える課題での正答率：色分けなし26%、低確信の部分を赤で示す53%、高確信を緑・低確信を赤で示す58%」（確認済み）。色分けを見た人は追加の質問で確かめる人が増えた（本文で確認）。
  - 限界・注意：GPT-3の確率をそのまま色にした仕組みで、色の正しさは研究者が設計した条件。120人・1種類の課題。

- 根拠4：Bo, Wan & Anderson 2025『To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models』CHI '25（種類：ランダム化オンライン実験／査読済み・国際会議）
  - 確認した場所：https://arxiv.org/abs/2412.15584（抄録）、https://arxiv.org/html/2412.15584（本文の一部）
  - 対象：米国のProlific参加者400人。LSATの論理問題と、画像から数を見積もる課題。GPT-4oの助言。工夫は「頼りすぎに注意する注意書き」「不確かさの色分け」「答えを直接言わない」の3つ。
  - 使える内容：「工夫は過信を減らしたが、適切な頼り方はおおむね改善しなかった」「間違った頼り方をしたあとに自信が上がる場面があった」（抄録で確認済み）。本文では、色分けと「答えを直接言わない」は全体の依存を下げることで過信を減らしていた、とある。
  - 限界・注意：条件ごとの細かい数値は、本文の表から私が計算し直す必要があるため「確認済み」にはしない。課題が仕事の場面と違う。

- 根拠5：Kim ほか 2025（CHI '25、問い2の根拠3と同じ）：説明は依存を増やし、出典と矛盾は間違いへの依存を下げる（抄録で確認済み）。

- 根拠6：Vasconcelos, Jörke, Grunde-McLaughlin, Gerstenberg, Bernstein & Krishna 2023『Explanations Can Reduce Overreliance on AI Systems During Decision-Making』Proc. ACM Hum.-Comput. Interact. 7 (CSCW1)（種類：実験5本、計731人／査読済み）
  - 確認した場所：https://arxiv.org/abs/2212.06823（抄録）
  - 使える内容：「過信は固定した偏りではなく、確認する手間と得の兼ね合いで変わる。説明が分かりにくいと過信が増え、課題が難しいときや報酬が大きいときは過信が減る」（抄録で確認済み）
  - 限界・注意：迷路の課題、研究用の模擬AI。効果の大きさは未確認。

- 根拠7：Schemmer, Hemmer, Nitsche, Kühl & Vössing 2022『A Meta-Analysis of the Utility of Explainable Artificial Intelligence in Human-AI Decision-Making』AIES '22（種類：meta-analysis／査読済み・国際会議）
  - 確認した場所：https://arxiv.org/abs/2205.05126v2（抄録）
  - 使える内容：「説明可能なAIは成績にプラスだが、AIの予測だけを示す場合と比べると、説明の効果は見られなかった」（抄録で確認済み）
  - 限界・注意：含まれる研究の数は抄録になく、二次情報で「9本の論文・44研究」とされるが未確認。生成AI以前。著者名の並びは論文ページで最終確認を。

- 根拠8（説明責任）：Mosier, Skitka, Heers, Burdick & Rosekind『Automation Bias: Decision Making and Performance in High-Tech Cockpits』（Second Automation Technology and Human Performance Conference, 1996発表。NASA NTRS掲載）
  - 確認した場所：https://ntrs.nasa.gov/citations/20020043179（抄録）
  - 使える内容：「自分の成績と自動化との関わり方に責任を持つと感じていたパイロットは、自動化の出力を他の手がかりで確かめることが多く、間違いが少なかった」（抄録で確認済み）
  - 限界・注意：学会発表で、相関。人数・効果の大きさは未確認。生成AIとは別の時代・場面。

- 根拠9（査読なし・補助）：Passi ほか 2024（Microsoft MSR-TR-2024-7、問い2の根拠6と同じ）
  - 使える内容：「確認向けの説明、一人称の不確かさ、AI自身による見直しが過信を減らすという研究がある。これらは確認の手間を下げることで効く。ただし対策は逆効果になって過信を増やすことがあるので、状況ごとに効果を確かめる必要がある」（本文の要約部分で確認済み）

### 問い5（任意）：AIエージェントが実際の事務作業（メール・予定・書類）でどのくらい間違えるか

- 分かっていること：
  - 実際の職場でのAIエージェントの間違いの割合を測った、出典のはっきりした査読済み研究は見つからなかった。あるのは、作られた仮想の環境での「ベンチマーク」（テスト）で、多くが査読前（arXiv）。
  - 数字の変化がとても速い。同じテスト（WorkBench）で、2024年3月の最高成績は43%、2026年6月の更新版では89%〜98%（論文の版によって数字が違う）。「AIエージェントは○%間違える」という1つの数字は、すぐに古くなる。
  - 一方で、2026年9月のメール・予定のテスト（EmailBench）では、最も良い設定でも合格は33.5%。ツールの呼び出し自体は99.7%エラーなく動いていたのに、課題としては完了していなかった。「ちゃんと動いた」ことと「正しくできた」ことは別、という点は記事の論点に合う。
  - テストの種類によって成績は大きく違うため、数字をまたいで比べないほうがよい。

- 根拠1：Styles, Miller, Cerda-Mardini, Guha, Sanchez & Vidgen 2024『WorkBench: a Benchmark Dataset for Agents in a Realistic Workplace Setting』（arXiv 2405.00823／査読前と扱う。arXivページに掲載先の記載なし）
  - 確認した場所：https://arxiv.org/abs/2405.00823（抄録）
  - 内容：予定・メール・顧客管理などを模した5つのデータベース、26のツール、690の課題。
  - 使える数値：「課題の成功率は3%（Llama2-70B）〜43%（GPT-4）」（確認済み・2024年時点）。間違いの例として「メールが間違った人に送られる」が挙がっている（抄録で確認済み）。

- 根拠2：Styles & Miller 2026『WorkBench Revisited: Workplace Agents Two Years On』（arXiv 2606.13715／査読前）
  - 確認した場所：https://arxiv.org/abs/2606.13715（v2の抄録）、https://arxiv.org/abs/2606.13715v1（v1の抄録）
  - 使える数値：
    - 「2024年3月の最高成績GPT-4は課題の43%を完了し、26%の課題で、間違った人にメールするなど意図しない有害な行動をとった」（確認済み。v1・v2で同じ）
    - 最新モデルの数字は版で違う：v1（2026-06-10）「Claude Opus 4.8が89%を完了、有害な行動2.5%」、v2（2026-07-01）「Claude Fable 5が98%を完了、有害な行動1.9%」（どちらも抄録で確認済み。使うなら版と日付を必ず書く）
  - 限界・注意：査読前。著者は元のテストの作者。仮想環境で、実際の職場の受信箱とは違う。版で数字が変わっているので、本文で使うなら「2024年の43%・26%」だけにしておくほうが安全。

- 根拠3：Singh, Uniyal, Devlin, Xie, Thadawasin, Dutt, Lai & Kang 2026『EmailBench: A Benchmark for Evaluating LLM Agents on Enterprise Email and Productivity Tasks』（arXiv 2609.31906、2026-09-25投稿／査読前）
  - 確認した場所：https://arxiv.org/abs/2609.31906（抄録）、https://arxiv.org/html/2609.31906（本文の一部）
  - 対象：仮想の1人分のメールボックス（Enronのメールを参考にした合成データ。メール65通・予定15件など）。16種類・206の場面。8つのモデル設定を各1回実行。
  - 使える数値：
    - 「最も良い設定でも場面の合格は33.5%。ツール呼び出しの99.7%はAPIのエラーなく完了していた」（抄録で確認済み）
    - 本文の表（3設定のみ）：「メールを書く課題の合格 53〜73%、予定を書き込む課題 8〜17%」（本文で読んだが、設定ごとの対応は本文の表で再確認してから使う）
  - 限界・注意：査読前・投稿から1か月未満。合成データ、1人のユーザー、英語のみ、各1回の実行、自動採点。モデル名と実際のモデルの対応は著者も「検証していない」と書いている。間違った人に送るなどの有害な行動の例は報告されていない。

- 根拠4（参考）：Xu ほか『TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks』（arXiv 2412.14161、v3は2025-09-10／ページ上の記載は「Preprint」）
  - 確認した場所：https://arxiv.org/abs/2412.14161（抄録）
  - 使える数値：「小さなソフトウェア会社を模した環境で、最も良いエージェントが自律的に完了できたのは課題の30%」（確認済み・v3時点）
  - 限界・注意：事務作業だけでなくプログラミングを含む。時点が古い（2025年）。

- 時点の注意：上の数値はすべて「その時点・そのテスト・そのモデル」のもの。Senaが使っているツールの精度を示すものではない。本文で使うなら「2024年のテストでは〜、2026年には大きく改善した。ただしテストによっては〜」と、変化の速さそのものを伝えるほうが安全。

⸻

## 分かっていないこと
- 生成AI・AIエージェントにメール読み取り→議事録→下書き→送信までを任せる場面で、自動化バイアスがどのくらい起きるか（問い1・4の範囲では、直接調べた研究は見つからなかった。問い2の担当分も参照）。
- うつ・気分の落ち込み・体調の波があるときに、自動化に頼りやすくなるか。今回の検索では、臨床的なうつと自動化バイアスを直接調べた完成した研究は見つからなかった（2025年の国際会議 ICIS で「うつとAIの助言への依存」のモデルを提案する発表はあるようだが、結果は未確認で、研究計画の段階に見える）。
- 作業負荷が自動化バイアスをどのくらい増やすか（効果の大きさ）。レビューは方向を示すが、まとまった数値は見つからなかった。
- 経験者・訓練の効果は研究で結論が割れており、「どんな訓練なら効くか」ははっきりしない。
- AIエージェントが「送信」まで実行する場面で、人が送信前にどのくらい確認しているか（実際の職場での行動データ）。査読済み研究は見つからなかった。
- 「確認チェックリストを決めておく」「送信前に必ず止める」といった手順そのものが、生成AI・AIエージェントの過信を減らすか。直接確かめた研究は見つからなかった（医療・航空のチェックリスト研究はあるが、AIの確認とは別の場面）。
- 「誰に届くか（社内／社外）」「取り消せるか」「判断を含むか」で確認の地点を分ける方法の効果。研究では確かめられていない（Claudeの提案として書く）。
- 過信を減らす工夫の、実際の仕事での長期的な効果。ほとんどの研究はオンラインの短い実験（1回20分程度）で、慣れたあとどうなるかは分かっていない。
- 実際の職場でAIエージェントが間違ったメールを送る頻度。仮想環境のテストの数字しかない。
- 「説明責任を持たせる」工夫を生成AIで試した研究。今回は見つからなかった（古い自動化研究のみ）。

## 使わないほうがよい情報
- 「Goddard ほか 2011」と「2012」の混在：オンライン公開は2011年6月、掲載号は2012年。本文と参考文献で年をそろえる（2012 推奨）。
- 「自動化バイアスの頻度は6〜11%」：Goddard ほかの本文にある数字だが、医療の一部の前向き研究で「間違った助言のあとの判断」の割合として出てきたもので、文脈が狭い。一般的な「起きる頻度」として使うと誤解されやすい。
- Lyell & Coiera の「81%・91%」を「人の8〜9割が見落とす」と書くこと：研究の数の割合であって、人の割合ではない。
- 「疲れているとAIを信じすぎる」「調子が悪い日は過信しやすい」：睡眠不足の研究（Reichenbach ほか 2011）はむしろ逆の結果。気分・うつについては直接の研究が見つからない。
- Merritt（2011, Human Factors）「気分（楽しい／悲しい）を誘導すると自動化への信頼が変わる」：検索結果の要約では「楽しい気分で信頼が上がった」とあるが、自分で読めたのは抄録の冒頭だけで結果は未確認。また誘導した一時的な気分で、うつとは別物。Sena の状態と結びつく誤解を招きやすいので使わない。
- Mosier ほか（パイロットの自動化バイアス、1996年会議／1998年 IJAP とされる）：NASA の会議抄録で「自分に説明責任があると感じていたパイロットほど、自動化を他の手がかりと照らし合わせ、誤りが少なかった（後付けの分析）」は確認したが、雑誌版の書誌・人数は未確認。使うなら「後付けの分析」と書き、問い3の担当と重複しないよう調整。
- Wickens & Dixon（2007）：Lyell & Coiera が引用している内容だけを確認。原著は読んでいないので、原著の数値は使わない（「Lyell & Coiera のレビューによれば」と書く）。
- Skitka, Mosier & Burdick（1999, International Journal of Human-Computer Studies 51(5):991–1006。学生80人の飛行シミュレーター実験）：内容は二次的なまとめでしか見ておらず、未確認。
- 「人とAIの組み合わせは〜より悪い」を「AIと一緒に働くと成績が落ちる」と言い換えること：誤解されやすい。meta-analysisの結果は「人だけよりは良いが、良いほう単独より平均で劣る」。課題の種類で逆にもなる。
- WorkBench Revisited の最新モデルの数字（89%／98%、有害な行動2.5%／1.9%）：版によってモデル名と数字が違い、査読前。使うなら版と日付を併記。基本は使わないほうがよい。
- EmailBench の課題別の数字を「AIは予定を8割間違える」のように一般化すること：1つの合成メールボックス、各課題12件前後と少ない。
- Bo ほか 2025 の条件ごとの「過信○%」：論文の指標から計算し直した値で、論文がそのまま書いている数字ではないため未確認扱い。
- Skitka, Mosier & Burdick 2000 の具体的な結果（「説明責任を課すと誤りが減る」）：抄録・本文を読めていない。検索結果の要約では「実験で課した説明責任には有意な効果がなく、本人が責任を感じていた人だけに差があった」とする記述もあり、未確認。使うならNASAの学会抄録の範囲（相関）で。
- Schemmer ほか 2022 の「44研究・9論文」：二次情報のみで未確認。
- 「Klingbeil ほか 2024（Computers in Human Behavior）」：引用情報は見つかったが、人数・効果の大きさを読めていないため未確認。
- 「AIエージェントの成功率24%（APEX-Agents）」：ニュース記事・ブログでしか見ておらず、元の論文を確認していない。
- Dell'Acqua ほか 2023（BCGのコンサルタント実験）：Microsoftのレビューで引用されているが、今回は原典を確認しておらず、ワーキングペーパー（査読前）。使うなら別途確認が必要。
- Vorvoreanu の講演（Microsoft Research Forum 2024）：内容は根拠9の報告と同じ方向だが、講演で研究ではない。

## 参考文献（記事末尾にそのまま使える形）
- Bo, J. Y., Wan, S., & Anderson, A. (2025). To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models. *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3706598.3714097
- Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), Article 188. https://doi.org/10.1145/3449287
- Goddard, K., Roudsari, A., & Wyatt, J. C. (2012). Automation bias: A systematic review of frequency, effect mediators, and mitigators. *Journal of the American Medical Informatics Association*, 19(1), 121–127.（オンライン公開 2011年） https://doi.org/10.1136/amiajnl-2011-000089
- Kim, S. S. Y., Liao, Q. V., Vorvoreanu, M., Ballard, S., & Vaughan, J. W. (2024). "I'm Not Sure, But...": Examining the Impact of Large Language Models' Uncertainty Expression on User Reliance and Trust. *FAccT '24*. https://doi.org/10.1145/3630106.3658941
- Kim, S. S. Y., Vaughan, J. W., Liao, Q. V., Lombrozo, T., & Russakovsky, O. (2025). Fostering Appropriate Reliance on Large Language Models: The Role of Explanations, Sources, and Inconsistencies. *CHI '25*. https://arxiv.org/abs/2502.08554
- Liu, C., Zhou, Q., Shen, X., Liu, X. B., Wu, T., & Chen, X. A. (2026). Behavioral Indicators of Overreliance During Interaction with Conversational Language Models. arXiv:2602.11567（CHI 2026 条件付き採録と記載）
- Lyell, D., & Coiera, E. (2017). Automation bias and verification complexity: A systematic review. *Journal of the American Medical Informatics Association*, 24(2), 423–431. https://doi.org/10.1093/jamia/ocw105
- Mosier, K. L., Skitka, L. J., Heers, S., Burdick, M., & Rosekind, M. R. (1996/1997). Automation Bias: Decision Making and Performance in High-Tech Cockpits. Second Automation Technology and Human Performance Conference. NASA NTRS 20020043179. https://ntrs.nasa.gov/citations/20020043179
- Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors*, 52(3), 381–410. https://doi.org/10.1177/0018720810376055
- Parasuraman, R., Molloy, R., & Singh, I. L. (1993). Performance consequences of automation-induced "complacency." *The International Journal of Aviation Psychology*, 3(1).
- Passi, S., Dhanorkar, S., & Vorvoreanu, M. (2024). Appropriate reliance on GenAI: Research synthesis. Microsoft Technical Report MSR-TR-2024-7（査読なし）
- Reichenbach, J., Onnasch, L., & Manzey, D. (2011). Human performance consequences of automated decision aids in states of sleep loss. *Human Factors*. https://doi.org/10.1177/0018720811418222
- Schemmer, M., Hemmer, P., Nitsche, M., Kühl, N., & Vössing, M. (2022). A Meta-Analysis of the Utility of Explainable Artificial Intelligence in Human-AI Decision-Making. *AIES '22*. https://doi.org/10.1145/3514094.3534128
- Singh, M., et al. (2026). EmailBench: A Benchmark for Evaluating LLM Agents on Enterprise Email and Productivity Tasks. arXiv:2609.31906（査読前）
- Spatharioti, S. E., Rothschild, D., Goldstein, D. G., & Hofman, J. M. (2025). Effects of LLM-based Search on Decision Making: Speed, Accuracy, and Overreliance. *CHI '25*. https://doi.org/10.1145/3706598.3714082
- Styles, O., & Miller, S. (2026). WorkBench Revisited: Workplace Agents Two Years On. arXiv:2606.13715（査読前）
- Styles, O., Miller, S., Cerda-Mardini, P., Guha, T., Sanchez, V., & Vidgen, B. (2024). WorkBench: a Benchmark Dataset for Agents in a Realistic Workplace Setting. arXiv:2405.00823
- Swaroop, S., Buçinca, Z., Gajos, K. Z., & Doshi-Velez, F. (2024). Accuracy-time tradeoffs in AI-assisted decision making under time pressure. *Proceedings of the 29th International Conference on Intelligent User Interfaces (IUI '24)*. https://doi.org/10.1145/3640543.3645206
- Vaccaro, M., Almaatouq, A., & Malone, T. (2024). When combinations of humans and AI are useful: A systematic review and meta-analysis. *Nature Human Behaviour, 8*(12), 2293–2303. https://doi.org/10.1038/s41562-024-02024-1
- Vasconcelos, H., Jörke, M., Grunde-McLaughlin, M., Gerstenberg, T., Bernstein, M. S., & Krishna, R. (2023). Explanations Can Reduce Overreliance on AI Systems During Decision-Making. *Proceedings of the ACM on Human-Computer Interaction, 7*(CSCW1). https://doi.org/10.1145/3579605
- Xu, F. F., et al. (2024/2025). TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks. arXiv:2412.14161（査読前）
