# research｜2026-10-16-pm

確認の方法：論文本文（PDF／PMC）・抄録ページを自分で開いて読んだものだけ「確認済み」。孫引き・検索結果の抜粋だけのものは「未確認」。

## 問いごとの答え

### 問い1：文字（メール）のやりとりで、温度感は書き手の思うほど伝わるか
- 分かっていること：伝わりにくく、書き手はそれに気づきにくい。
- 根拠：Kruger J, Epley N, Parker J, Ng Z-W. (2005). Egocentrism over e-mail: Can we communicate as well as we think? *Journal of Personality and Social Psychology*, 89(6), 925–936.（種類：5つの実験・査読済み）
  - 確認した場所：本文PDF（https://web-docs.stern.nyu.edu/pa/kruger_email_ego.pdf）、抄録（https://pubmed.ncbi.nlm.nih.gov/16393025/）
  - 使える数値（確認済み・本文）：
    - Study 2（学生60人・解析は29組）：声で聞いた側は皮肉かどうかの「ほぼ4分の3」を読み取れた。メールで読んだ側は偶然（50%）と区別がつかない水準。メールで送った側は、その差を予想できていなかった
    - Study 3（イリノイ大学の学生154組）：感情や口調（皮肉・真面目・怒り・悲しみ）を「伝えられる」と予想した割合は平均 89.3%（メール）、実際に伝わったのは 62.8%（メール）。対面は予想 89.4%・実際 73.9%、声のみは予想 89.4%・実際 73.3%。友人どうしでも、初対面どうしでも同じ傾向
  - 本文の説明：書き手は自分の頭の中では口調が聞こえているので、読み手には聞こえないことに気づきにくい（egocentrism）
- 限界・注意：アメリカの大学生が英語で、母語どうしでやった実験。皮肉など限られた口調のテスト。仕事のSlackで同じ割合になるとは言えない。2005年で、絵文字やスタンプのある今のチャットとは違う
- 補足（理論論文・実験ではない）：Byron K. (2008). Carrying too heavy a load? The communication and miscommunication of emotion by email. *Academy of Management Review*, 33(2), 309–327. 抄録（https://journals.aom.org/doi/abs/10.5465/amr.2008.31193163）で確認：「受け手は仕事のメールを、書き手の意図より否定的か中立に読み違えることが多い」と著者が論じている（理論の枠組み。データで確かめた数字ではない）。本文では「理論の論文」と明記して使う

### 問い2：AIが入ると、感情の温度や、相手からの見え方は変わるか
- 分かっていること：AIの返信候補を使うと、会話の感情の向きがAIの候補の側に寄る。使うと相手からの評価は上がるが、AIを使っていると思われると下がる。
- 根拠：Hohenstein J, Kizilcec RF, DiFranzo D, Aghajari Z, Mieczkowski H, Levy K, Naaman M, Hancock J, Jung MF. (2023). Artificial intelligence in communication impacts language and social relationships. *Scientific Reports*, 13, 5487.（種類：2つのランダム化実験・査読済み）
  - 確認した場所：本文（https://pmc.ncbi.nlm.nih.gov/articles/PMC10073210/）
  - 使える数値（確認済み・本文）：
    - 実験1：クラウドワーカー438人（219組）が、政策について約7分（平均6.8分）チャット。AIの返信候補（「スマートリプライ」：タップして送る短い返事）を使える条件と使えない条件にランダムに分けた。送ったメッセージの平均14.3%が返信候補で、候補が使える人は1分あたり10.2%多くメッセージを送った
    - 相手が返信候補を多く使うほど、自分は相手を「協力的」「親しみがある」と評価した（因果の推定）。一方、「相手は返信候補を使っていそうだ」と思うほど、相手を協力的でない、親しみが低い、支配的だと評価した（実際の使用量を揃えても。相関）
    - 実験2：291組。ポジティブな候補・ネガティブな候補・Googleの候補・候補なしの4条件。ネガティブな候補があった会話は、ポジティブな候補やGoogleの候補の会話より否定的な内容が多かった（d=0.35、d=0.32）。変化は、候補を見たことではなく「使ったこと」から来ていた
  - 著者の結論：AIは会話を速くし、感情表現をポジティブ寄りにして、使う人の評価も上げうる。ただし、AIを使っていると疑われると評価は下がる。長期の影響（文体が似てくるのではないか）は未検証
- 限界・注意：英語・アメリカのクラウドワーカー・知らない人どうしの短いチャット。文章を丸ごと直してもらう使い方（LLMでの書き直し）ではなく、タップで送る短い返信候補。日本の職場とは別

### 問い3：AIの下書きに、書き手の文体が寄っていくか（日本語話者の研究は？）
- 分かっていること：寄っていく。日本の人は、アメリカの人より丁寧さ・お詫びの表現が多く、AIの下書きの文体が自分と違うほど、大きく寄った。
- 根拠：Sakai S, Gao A, Shoda Y, Reinecke K. (2026). AI-Generated Email Drafts Shift Culturally Distinctive Communication Styles in Professional Email. arXiv:2609.26403.（種類：事前登録された被験者内実験・**プレプリント（査読前）**・2026年9月22日投稿）
  - 確認した場所：抄録ページ（https://arxiv.org/abs/2609.26403）
  - 使える内容（確認済み・抄録）：日本人とアメリカ人の参加者が、職場のメールを「母語で」、AIなし・直接的な（低コンテクスト）AIの下書きあり・間接的な（高コンテクスト）AIの下書きありの3条件で書いた。日本の参加者はアメリカの参加者より、丁寧さやお詫びの表現（高コンテクストの表現）が有意に多かった。AIの下書きは参加者のメールを下書きの文体の側に動かし、下書きが自分の文化の文体とずれているほど動きが大きかった（日本の参加者は直接的な下書きで最も動いた）
  - 数値（人数・効果の大きさ）は抄録にないため使わない
- 限界・注意：査読前。母語（日本語は日本語、英語は英語）で書いたメールで、英語で書く場面そのものではない。結論は著者の抄録の範囲まで

### 問い4：英語が母語でない書き手の英語メールは、読み手にどう読まれるか。AIで整えた英文は？
- 分かっていること（4a）：母語でない書き手の英語のメールは、直接的で、和らげる言い回しや挨拶が少なく、失礼に読まれうる、という研究がある。
  - 根拠：Economidou-Kogetsidis M. (2011). "Please answer me as soon as possible": Pragmatic failure in non-native speakers' e-mail requests to faculty. *Journal of Pragmatics*, 43(13), 3193–3215.（種類：メールのコーパス分析・査読済み）
  - 確認した場所：抄録（UNIC 研究ポータル https://pure.unic.ac.cy/en/publications/please-answer-me-as-soon-as-possible-pragmatic-failure-in-non-nat/）。本文は未取得（出版社ページは開いていない）
  - 使える内容（確認済み・抄録）：英語が母語でないキプロスのギリシャ系の大学生が、英語で大学の教員に送ったお願いのメールを数学期分調べた。かなり直接的で（特に情報を求めるお願い）、和らげる言い回しがなく、挨拶・結びが抜けていて、呼び方が不適切なものがあった。著者は、このようなメールは失礼・不躾に読まれて「語用論的な失敗」を起こしうる、と論じている（相手に断る余地を与えず、負担をかけることへの配慮が見えないため）
  - 限界：学生→教員のメール。キプロス。日本人の書き手や、今のSlackの文体の研究ではない。数値は使わない
- 分かっていること（4b）：AIで整えた文が、読み手に書き手の英語力を高く見積もらせて、共同作業で摩擦が起きた実験がある。
  - 根拠：Xiao Y, Chen Y, Yamashita N, Chen Y, Liu Z, Gao G. (2024). (Dis)placed Contributions: Uncovering Hidden Hurdles to Collaborative Writing Involving Non-Native Speakers, Native Speakers, and AI-Powered Editing Tools. *Proceedings of the ACM on Human-Computer Interaction*, 8(CSCW2), Article 403.（種類：混合研究法・査読済み）
  - 確認した場所：抄録（https://dl.acm.org/doi/10.1145/3686942）
  - 使える数値（確認済み・抄録）：英語母語話者1人と、英語力が限られた母語でない話者1人の32組が、共同で文章を書いた。AIの編集ツールがあっても、母語でない話者は不利から抜けられなかった。AIの助けは、母語話者が、相手の英語力と、文章に出ている主体的な貢献を「実際より高く」見積もることにつながり、共同作業に意図しない緊張が生まれた
  - 限界：共同執筆の課題の実験で、職場のSlackではない。「英語力が限られた」人が対象。参加者の国の内訳は抄録に書かれていない
- 補足（書き手の感覚）：Kadoma K, Aubin Le Quéré M, Fu XJ, Munsch C, Metaxa D, Naaman M. (2024). The Role of Inclusion, Control, and Ownership in Workplace AI-Mediated Communication. *CHI '24*, Article 1016.（種類：オンライン実験・査読済み）
  - 確認した場所：抄録（https://arxiv.org/abs/2309.11599）
  - 使える内容（確認済み・抄録）：「昇進のお願い」の文を（仮想の場面で）AIの自動補完を使って書く実験。AIの提案の文体（控えめ／自信あり）は「その場に含まれている感覚」に影響しなかった。ただ、その感覚が高い人ほど、自分の文章への主体感・自分のものという感覚が高かった。AIの提案をたくさん受け入れると、コントロールや主体感が下がりやすかったが、「含まれている感覚」が高いと、その下がりが弱まった
  - 限界：仮想の場面。人数は抄録にないため使わない

## 分かっていないこと
- 日本人が英語のSlack・メールを「AIに直してもらう」ときに、相手からどう読まれるかを直接調べた研究は、今回見つからなかった
- 英語で書くとき、AIの書き直しが温度感をどう動かすか（LLMで文を丸ごと直す使い方）を測った研究は、今回の範囲では、Sakai ほか（母語のメール・プレプリント）と Hohenstein ほか（短い返信候補）が近いだけ
- 「温度感を先に決めてからAIに頼む」「自分の過去の文を渡して特徴を残す」といった頼み方で、温度感が残るかを調べた研究は、見つからなかった。本文の手順は提案で、効果は確かめられていない
- 英語の職場チャットでの丁寧さの「ちょうどいい水準」は、会社・国・相手との距離で変わり、研究で決まった基準はない

## 使わないほうがよい情報（理由つき）
- Li W, Lai Y, Soni S, Saha K. (2025). Emails by LLMs（WebSci '25）の「AIのメールはより丁寧・形式的・長い」：検索結果の抄録の抜粋だけで、本文・抄録ページを開けなかった（未確認）
- Jakesch ほか (2019) の「AI作成と思われると信頼が下がる」：Hohenstein ほか (2023) の本文での引用で確認しただけ（孫引き）
- 78%／56%（メールの皮肉の予想と実際）：APA Monitor・Scientific American・AMA の記事に出るが、論文本文の数値（Study 2 は「偶然と区別がつかない水準」、Study 3 は 89.3%→62.8%）と書き方が違うため、記事では本文の数字だけを使う
- 「AIは丁寧すぎ・元気すぎになる」の断定：Hohenstein ほかは「返信候補」でポジティブ寄りだっただけ。文章を丸ごと直すLLMで同じとは言えない
- Playful AI in Professional Email（arXiv 2607.11749）：検索結果の抄録のみ。使わない

## 参考文献（記事末尾にそのまま使える形）
- Kruger J, Epley N, Parker J, Ng Z-W. (2005). Egocentrism over e-mail: Can we communicate as well as we think? *Journal of Personality and Social Psychology*, 89(6), 925–936. https://doi.org/10.1037/0022-3514.89.6.925
- Byron K. (2008). Carrying too heavy a load? The communication and miscommunication of emotion by email. *Academy of Management Review*, 33(2), 309–327. https://doi.org/10.5465/amr.2008.31193163
- Hohenstein J, Kizilcec RF, DiFranzo D, et al. (2023). Artificial intelligence in communication impacts language and social relationships. *Scientific Reports*, 13, 5487. https://doi.org/10.1038/s41598-023-30938-9
- Sakai S, Gao A, Shoda Y, Reinecke K. (2026). AI-Generated Email Drafts Shift Culturally Distinctive Communication Styles in Professional Email. arXiv:2609.26403（プレプリント）. https://arxiv.org/abs/2609.26403
- Economidou-Kogetsidis M. (2011). "Please answer me as soon as possible": Pragmatic failure in non-native speakers' e-mail requests to faculty. *Journal of Pragmatics*, 43(13), 3193–3215. https://doi.org/10.1016/j.pragma.2011.06.006
- Xiao Y, Chen Y, Yamashita N, Chen Y, Liu Z, Gao G. (2024). (Dis)placed Contributions: Uncovering Hidden Hurdles to Collaborative Writing Involving Non-Native Speakers, Native Speakers, and AI-Powered Editing Tools. *Proceedings of the ACM on Human-Computer Interaction*, 8(CSCW2), Article 403. https://doi.org/10.1145/3686942
- Kadoma K, Aubin Le Quéré M, Fu XJ, Munsch C, Metaxa D, Naaman M. (2024). The Role of Inclusion, Control, and Ownership in Workplace AI-Mediated Communication. *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24)*, Article 1016. https://doi.org/10.1145/3613904.3642650
