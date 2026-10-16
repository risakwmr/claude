# research-a｜2026-10-16-pm（担当：問い1・問い4）

担当範囲：brief.md「リサーチ係への問い」の 1 と 4。問い 2・3・5 は別担当（research-b 等）なので、ここでは扱わない。
調べた日：2026-10-16

全体の注意（書き手向け）
- ここで使う研究は、ほとんどが**生成AI以前**の「自動化」研究（飛行シミュレーター、工場の監視作業、医療の判断支援システム）。AIエージェントにメール・議事録・送信まで任せる場面に、そのまま当てはまるとは言えない。本文では「こういう場面で調べられてきた」と書き、AIエージェントへの当てはめは推測と分かる書き方にする。
- どれも**平均の傾向**。「誰でも必ずこうなる」「この人はこうなる」とは言えない。
- 研究からSena個人の状態（うつ・ADHD・調子の低い日）を推測しない。問い4の結果を「うつの日は過信しやすい」と書き換えない（下の「使わないほうがよい情報」参照）。

---

## 問いごとの答え

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

## 分かっていないこと
- 生成AI・AIエージェントにメール読み取り→議事録→下書き→送信までを任せる場面で、自動化バイアスがどのくらい起きるか（問い1・4の範囲では、直接調べた研究は見つからなかった。問い2の担当分も参照）。
- うつ・気分の落ち込み・体調の波があるときに、自動化に頼りやすくなるか。今回の検索では、臨床的なうつと自動化バイアスを直接調べた完成した研究は見つからなかった（2025年の国際会議 ICIS で「うつとAIの助言への依存」のモデルを提案する発表はあるようだが、結果は未確認で、研究計画の段階に見える）。
- 作業負荷が自動化バイアスをどのくらい増やすか（効果の大きさ）。レビューは方向を示すが、まとまった数値は見つからなかった。
- 経験者・訓練の効果は研究で結論が割れており、「どんな訓練なら効くか」ははっきりしない。

## 使わないほうがよい情報
- 「Goddard ほか 2011」と「2012」の混在：オンライン公開は2011年6月、掲載号は2012年。本文と参考文献で年をそろえる（2012 推奨）。
- 「自動化バイアスの頻度は6〜11%」：Goddard ほかの本文にある数字だが、医療の一部の前向き研究で「間違った助言のあとの判断」の割合として出てきたもので、文脈が狭い。一般的な「起きる頻度」として使うと誤解されやすい。
- Lyell & Coiera の「81%・91%」を「人の8〜9割が見落とす」と書くこと：研究の数の割合であって、人の割合ではない。
- 「疲れているとAIを信じすぎる」「調子が悪い日は過信しやすい」：睡眠不足の研究（Reichenbach ほか 2011）はむしろ逆の結果。気分・うつについては直接の研究が見つからない。
- Merritt（2011, Human Factors）「気分（楽しい／悲しい）を誘導すると自動化への信頼が変わる」：検索結果の要約では「楽しい気分で信頼が上がった」とあるが、自分で読めたのは抄録の冒頭だけで結果は未確認。また誘導した一時的な気分で、うつとは別物。Sena の状態と結びつく誤解を招きやすいので使わない。
- Mosier ほか（パイロットの自動化バイアス、1996年会議／1998年 IJAP とされる）：NASA の会議抄録で「自分に説明責任があると感じていたパイロットほど、自動化を他の手がかりと照らし合わせ、誤りが少なかった（後付けの分析）」は確認したが、雑誌版の書誌・人数は未確認。使うなら「後付けの分析」と書き、問い3の担当と重複しないよう調整。
- Wickens & Dixon（2007）：Lyell & Coiera が引用している内容だけを確認。原著は読んでいないので、原著の数値は使わない（「Lyell & Coiera のレビューによれば」と書く）。
- Skitka, Mosier & Burdick（1999, International Journal of Human-Computer Studies 51(5):991–1006。学生80人の飛行シミュレーター実験）：内容は二次的なまとめでしか見ておらず、未確認。

## 参考文献（記事末尾にそのまま使える形）
- Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors*, 52(3), 381–410. https://doi.org/10.1177/0018720810376055
- Goddard, K., Roudsari, A., & Wyatt, J. C. (2012). Automation bias: A systematic review of frequency, effect mediators, and mitigators. *Journal of the American Medical Informatics Association*, 19(1), 121–127.（オンライン公開 2011年） https://doi.org/10.1136/amiajnl-2011-000089
- Lyell, D., & Coiera, E. (2017). Automation bias and verification complexity: A systematic review. *Journal of the American Medical Informatics Association*, 24(2), 423–431. https://doi.org/10.1093/jamia/ocw105
- Parasuraman, R., Molloy, R., & Singh, I. L. (1993). Performance consequences of automation-induced "complacency." *The International Journal of Aviation Psychology*, 3(1).
- Reichenbach, J., Onnasch, L., & Manzey, D. (2011). Human performance consequences of automated decision aids in states of sleep loss. *Human Factors*. https://doi.org/10.1177/0018720811418222
- Swaroop, S., Buçinca, Z., Gajos, K. Z., & Doshi-Velez, F. (2024). Accuracy-time tradeoffs in AI-assisted decision making under time pressure. *Proceedings of the 29th International Conference on Intelligent User Interfaces (IUI '24)*. https://doi.org/10.1145/3640543.3645206
