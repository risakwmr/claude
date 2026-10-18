# research｜2026-10-19-am（問い1・2・5＝担当A、問い3・4＝担当B を合わせたもの）

確認日：2026-10-19。数値はすべて担当者が論文本文・報告書・公的文書で確かめたもの。
注：AI事業者ガイドラインには「従業員は会社のルールを確認すること」という文言はない。「ガイドラインがそう求めている」とは書かない。サービスの設定（学習に使わない設定など）は未確認で、使うなら公開直前に確認日を付ける。

## 担当Aの全体注意
担当：brief.md「リサーチ係への問い」の 1・2・5（3・4 は別担当）
調査日：2026-10-18

## 担当Bの全体注意
担当：brief.md「リサーチ係への問い」の **3・4 のみ**（1・2・5 は別の担当の research.md）。
調べた日：2026-10-18（日本時間）。

## 問い1・2・5（担当A）
### 問い1：会社の方針に反する使い方をした人、会社の情報を外部のAIに入れた人はどのくらいいるか（KPMG × メルボルン大学 2025）

- 分かっていること：
  - 47か国の働く人を対象にした大きな調査で、職場でAIを使う人のおよそ半分が、少なくとも一度は「会社の方針・ガイドラインに反する使い方」や「会社の情報を公開AIツールにアップロード」をしたと答えている。
  - **brief の疑問への答え**：記事で広く引用される「ほぼ半数が方針に反する」「57%が隠して使う」は**47か国全体の値**。**分母は「職場でAIを使っている従業員」**（全回答者ではない）。報告書の本文に "Almost one in two employees who use AI admit to doing so in ways that contravene organizational policies and guidelines" とある。
  - **「48%」には「まれに（Rarely）」が含まれる**。設問は "At your work, how often have you…" の頻度で、答えは「Never／Rarely／Sometimes〜Very often」に分けて報告されている。「アップロードした」48% は、Rarely 14% と Sometimes〜Very often 34% を足した値。「日常的に入れている人が半分」とは読めない。
  - 同じ調査で、「許されているか分からないまま職場でAIツールを使った」が 56%。勤め先に生成AIの方針・ガイダンスがあると答えた人は約4割（34%＋禁止の方針6%）で、19% は「分からない」と答えている。→ 記事の前提（ルールを知らないまま使っている人が多い）に一番近いデータ。
  - 報告書は、「生成AIを禁止している」と答えた人の職場（67%）や、方針がある職場（56%）のほうが、方針がない職場（33%）や方針があるか分からない人（38%）より、こうした行動が多いとも書いている。著者は「禁止だけでは効かない可能性」と解釈しているが、相関であり因果は分からない。
  - **日本の数値あり**（KPMG の日本版スナップショット）：「方針やガイドラインに反する使い方をした」37%、「AIの出力を正確か確かめずに使った」56%、「AIが作った内容を自分のものとして出した」42%。ただし、**日本版には「会社の情報を公開AIに入れた」の値は載っていない**（見つからなかった）。
- 根拠：Gillespie, N., Lockey, S., Ward, T., Macdade, A., & Hassed, G. (2025). *Trust, attitudes and use of artificial intelligence: A global study 2025.* The University of Melbourne and KPMG. DOI 10.26188/28822919（種類：調査報告／**査読なし**。メルボルン大学の研究チームが設計・分析し、KPMG とメルボルン大学が資金を出している）
  - 確認した場所：
    - 報告書本文 PDF：https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2025/05/trust-attitudes-and-use-of-ai-global-report.pdf（p.6, 13, 15, 71, 75, 76, 107 を読んだ）
    - 日本版スナップショット PDF：https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2025/05/trust-attitudes-and-use-of-ai-japan-snapshot.pdf（p.2「Workplace indicators」）
    - KPMG の要約版（The age of Intelligence）PDF：https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2025/trust-attitudes-artificial-intelligence-executive-summary.pdf（p.8, 12）
  - 調査の概要（確認済み）：オンライン調査。2024年11月〜2025年1月中旬。47か国で 48,340人（各国 1,001〜1,098人）。年齢・性別・地域は各国の人口に合わせた調査パネル。そのうち働いている人 32,352人が職場のAIの設問に答えた。
  - 使える数値（いずれも47か国全体）：
    - 「会社の情報（財務・営業・顧客情報など）を公開AIツールにアップロードした」：**48%**（Rarely 14%＋Sometimes〜Very often 34%。p.75–76 Figure 44。設問 "Uploaded company information into a public AI tool"）（確認済み）
    - 「方針・ガイドラインに反する使い方をした」：**44%**（Rarely 13%＋Sometimes〜Very often 31%。設問 "Used AI in ways that contravene policies or guidelines"）（確認済み）
    - 「許されているか分からないまま、職場でAIツールを使った」：**56%**（Rarely 18%＋Sometimes〜Very often 38%。設問 "Used AI tools at work without knowing whether it is allowed"）（確認済み）
    - 「AIを使ったことを言わなかった」：**61%**（Rarely 19%＋Sometimes〜Very often 42%。設問 "Avoided revealing when you've used AI tools in your work"）（確認済み）
    - 「AIが作った内容を自分のものとして出した」：**55%**（Rarely 16%＋Sometimes〜Very often 39%）（確認済み。Figure 44 の値の足し算。報告書の文章は、言わなかった・自分のものとして出したを合わせて「Over half (57%)」と書いている）
    - 生成AIの方針・ガイダンス（本人の回答）：方針あり 34%／禁止の方針あり 6%／なし 41%／分からない 19%（p.71 Figure 41。設問 "Has your organization put in place a policy or provided guidance on the use of generative AI at work?"）（確認済み）
    - 仕事で使うAIの入手方法：無料の公開ツール 70%／会社が用意したツール 42%／有料の公開ツール 18%（p.71 Figure 40。複数回答）（確認済み）
    - 職場でAIを（数か月に1回以上）使っている人：全体 58%、日本 44%（p.73 Figure 43）（確認済み）
    - 日本：「方針やガイドラインに反する使い方をした」**37%**（日本版 p.2）（確認済み）
- 限界・注意：
  - **調査報告で、査読を受けた論文ではない**。調査に関わった会社（KPMG）はAIのガバナンス支援も仕事にしている。
  - 本人の申告で、行動を観察したものではない。報告書自身が「匿名にしたが、言いにくい行動なので少なめに出ている可能性がある（social desirability bias）」と書いている。
  - 「Rarely（まれに）」も含めた割合。「会社の情報」の中身（どの程度の機密か）は分からない。「方針に反する」も本人の認識。
  - 日本版の 37% が全体版と同じ集計（Rarely 込み・AIを使う従業員が分母）かどうかは、日本版のページに書かれていない。全体版の 44% と同じ設問の国別の値と考えられるが、**分母の明記はない**。日本の「職場でAIを使う」は、日本版では 55%（intentionally use AI at work）、全体版の国別グラフでは 44%（数か月に1回以上）で、定義が違うらしく一致しない。記事で日本の利用率を出すなら、どちらの定義か書く。
  - 調査は2024年末〜2025年初め。会社の方針や社内AIの導入は速く変わっているので、「2024年末〜2025年初めの調査」と時点を書く。
  - 平均の傾向で、読者の職場や本人に当てはまるとは限らない。

### 問い2：「シャドーAI」「BYOAI」の査読済み研究・レビューはあるか。なぜ人は会社のルールを確かめずに使うのか

- 分かっていること：
  - **シャドーAIそのものの査読済み研究は、まだ少ない**。見つかったのは小規模な混合研究1本（Silic ら 2025）と、文献を分析した学会論文1本（Perozzo ら 2025、査読の有無は未確認）。数字の多くは企業・ベンダーの調査で、このテーマの meta-analysis や systematic review は見つからなかった。
  - Silic, Silic & Kind-Trüller（2025、Strategic Change、査読誌）：専門職 140人へのアンケートと経営層 10人へのインタビュー。シャドーAI（会社が認めていないAIツールを使うこと）を「技術だけでなく組織の仕組みの問題（ガバナンスの失敗）」と位置づけた。「方針が形だけあって、現場で効いていない状態（governance drift zone）」がある、と述べている。対策の案は、使ってよいAIツールの一覧（registry）、役割に合わせた研修、社内監査、相談・報告ルート（escalation protocol）など。※確認できたのは抄録（Crossref のデータ）だけで、本文の数値は読んでいない。
  - **「なぜ確かめずに使うのか」を直接、量的に調べた査読済み研究は見つからなかった**。間接的に関係する根拠は次のとおり：
    - **ルールを知らない・分からない**：KPMG 2025（査読なし）で、職場でAIを使う人の 56% が「許されているか分からないまま使った」と答え、19% は会社に方針があるか「分からない」と答えた（問い1）。
    - **使ったと言いにくい（聞きにくさにつながる可能性）**：Reif, Larrick & Soll（2025、PNAS、査読済み）の事前登録した4つの実験（合計 N=4,439）で、仕事でAIを使う人は「能力ややる気を低く見られる」と予想しており、実際にそう評価されていた。研究1では、AIツールを使う場面を想像した人のほうが、AIでないツールの場面の人より、上司や同僚に使ったことを伝えたがらなかった。ただし、これは「伝えるか」の実験で、「ルールを聞くか」を調べたものではない。記事でつなげるなら「聞きにくさの背景の一つかもしれない」程度にとどめる。
    - **仕事量・自分で何とかする**：Microsoft・LinkedIn の Work Trend Index 2024（企業の調査、査読なし）で、AIを使う人の 78% が自分のAIツールを職場に持ち込んでいる（BYOAI）。Microsoft は背景として、仕事量の多さと、会社にAIの方針・計画がないこと（リーダーの 60%）を挙げている。同じ調査で、AIを使う人の 52% が「一番大事な仕事でAIを使っていると認めたがらない」と答えた。
  - BYOAI と「ルール違反」は同じではない。自分のツールを持ち込むことを会社が認めている場合もあるので、「78%が違反」とは書かない。
- 根拠：
  - Silic, M., Silic, D., & Kind-Trüller, K. (2025). From Shadow IT to Shadow AI: Threats, Risks and Opportunities for Organizations. *Strategic Change*. https://doi.org/10.1002/jsc.2682（種類：混合研究（アンケート＋インタビュー）／査読済み）
    - 確認した場所：Crossref の書誌データと抄録 https://api.crossref.org/works/10.1002/jsc.2682（Wiley のページは 403 で開けなかった）
    - 使える数値：「専門職 140人のアンケート、経営層 10人のインタビュー」（確認済み・抄録）。結果の割合は**未確認**（本文を読めていない）
  - Reif, J. A., Larrick, R. P., & Soll, J. B. (2025). Evidence of a social evaluation penalty for using AI. *PNAS*, 122. https://doi.org/10.1073/pnas.2426766122（種類：事前登録した実験4つ／査読済み）
    - 確認した場所：本文（PMC）https://pmc.ncbi.nlm.nih.gov/articles/PMC12088386/
    - 使える数値：「4つの事前登録実験、N = 4,439」（確認済み）。研究1（分析対象 497人）：上司に伝えたい気持ち 4.91 対 5.25（p=0.016）、同僚に 4.85 対 5.17（p=0.026）（確認済み。点数の差は小さいので、記事では数値より「伝えたがらない傾向があった」と書くほうが誤解が少ない）
  - Microsoft & LinkedIn (2024). *2024 Work Trend Index Annual Report: AI at Work Is Here. Now Comes the Hard Part.*（種類：企業の調査／査読なし。調査は Edelman Data & Intelligence）
    - 確認した場所：https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part ／ プレスリリース https://news.microsoft.com/source/?p=19728（2024-05-08）
    - 使える数値：「AIを使う人の 78% が自分のAIツールを職場に持ち込んでいる（BYOAI）」「AIを使う人の 52% が、一番大事な仕事でAIを使っていると認めたがらない」「53% が、大事な仕事でAIを使うと自分が替えのきく人に見えると心配している」（確認済み）。調査：31の国・地域、ナレッジワーカー 31,000人（各市場 1,000人）、2024年2月15日〜3月28日（確認済み）
  - （参考・数値なし）Perozzo, H., Ravarini, A., Strada, E., & Valentini, J. (2025). From Shadows to Syntax: Tracing the Evolution from Shadow IT to Shadow Generative AI in Organizations. ITAIS 2025 Proceedings, 35.（種類：文献ネットワーク分析／学会論文、査読の有無は**未確認**）
    - 確認した場所：https://aisel.aisnet.org/itais2025/35（抄録）。シャドーIT からシャドー生成AIへのつながりを整理したもので、理由を量的に調べたものではない
- 限界・注意：
  - シャドーAIの研究は始まったばかりで、査読済みの量的研究はほぼない。「研究で、人がルールを確かめない理由が分かっている」とは**書けない**。
  - Reif らは米国のオンラインパネル（Prolific など）の実験で、実際の職場ではない。著者も、AIが普及すると変わる可能性があると書いている。
  - Microsoft はAIツールを売る会社で、BYOAI のリスクを強調するのは自社に有利な面がある。
  - 記事では「研究で分かっていること」（KPMG：分からないまま使う人が多い／Reif：使ったと言いにくい）と、「Claudeの提案」（確かめる手順を決めておく）を分けて書く。

### 問い5（任意）：忙しいとき・疲れているときに、ルールの確認や慎重な判断を省きやすくなるか

- 分かっていること：
  - **AIの利用や情報の入力を対象にした研究は見つからなかった**。近い分野の研究が2つある。
  - 医療の現場の観察研究（Dai ら 2015、査読済み）：米国 35病院の介護・医療スタッフ 4,157人以上のデータで、手指衛生のルールを守る割合は、12時間勤務の始めから終わりにかけて平均 8.7 ポイント下がった（回帰による推定）。仕事が立て込んでいるほど下がり方が大きく、勤務の間の休みが長いと次の勤務で守る割合が戻った。「長く働いて疲れると、分かっているルールでも守りにくくなる」ことを、実際の職場の大きなデータで示した研究。
  - サイバーセキュリティ行動の systematic review（Chowdhury ら 2019、査読済み）：時間に追われる（time pressure）とセキュリティ行動にどう影響するかを、21本の研究から整理した。抄録には、時間に追われると認知的な負担やストレスが増え、行動に悪い影響が出うるとあり、研究はまだ少ないとも書かれている。効果の大きさをまとめた meta-analysis ではない。
- 根拠：
  - Dai, H., Milkman, K. L., Hofmann, D. A., & Staats, B. R. (2015). The impact of time at work and time off from work on rule compliance: The case of hand hygiene in health care. *Journal of Applied Psychology*, 100(3), 846–862. https://doi.org/10.1037/a0038067（種類：観察研究（縦断データ）／査読済み）
    - 確認した場所：抄録（Europe PMC、PMID 25365728）https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/a0038067&resultType=core&format=json ／ 米国 AHRQ（公的機関）の要約 https://psnet.ahrq.gov/issue/impact-time-work-and-time-work-rule-compliance-case-hand-hygiene-health-care
    - 使える数値：「35病院・4,157人以上」「12時間勤務の始めから終わりにかけて、平均 8.7 ポイント低下（回帰による推定）」（確認済み・抄録）。「最初の1時間の遵守率は約43%、12時間勤務の最後の1時間は35%」（確認済み・AHRQ の要約）
  - Chowdhury, N. H., Adam, M. T. P., & Skinner, G. (2019). The impact of time pressure on cybersecurity behaviour: a systematic literature review. *Behaviour & Information Technology*, 38(12), 1290–1308. https://doi.org/10.1080/0144929X.2019.1583769（種類：systematic review／査読済み）
    - 確認した場所：抄録（RePEc/IDEAS）https://ideas.repec.org/a/taf/tbitxx/v38y2019i12p1290-1308.html
    - 使える数値：「21本の研究を整理」（確認済み）。効果の大きさの数値はない
- 限界・注意：
  - Dai らは医療現場の手洗いで、オフィスワークやAIへの情報の入力ではない。記事では「別の分野だが」と断ってから「疲れると、分かっているルールでも守りにくくなる傾向が報告されている」程度に使う。
  - 研究が対象にしているのは「時間・疲れ」で、うつ・ADHD・PMDD などの「調子が低い日」を調べたものではない。**研究からSena個人や特定の病気・特性の人について推測しない**。
  - 「調子が低い日は『迷ったら入れない』を初期値にする」は**Claudeの提案**として書き、「研究が示したものではない」と明記する（RULES 5.5）。

## 問い3・4（担当B）
### 問い3：生成AIに入力した情報が、学習や出力を通じて外に出る可能性（研究で分かっていること・分かっていないこと）

- 分かっていること：
  1. **大規模言語モデルは、学習に使われた文章の一部をそのまま覚え、条件がそろうと出力してしまうことがある**（研究では「記憶（memorization）」「学習データの抽出（extraction）」と呼ぶ）。GPT-2 で、学習データ中の文章を数百件、一字一句そのまま取り出せた。中には個人を特定できる情報も含まれ、学習データに1回しか出てこない文章でも取り出せた例があった。
  2. **覚えやすさには傾向がある**：モデルが大きいほど、同じ文章が学習データに何度も出てくるほど、プロンプトで与える文脈が長いほど、そのまま出てきやすい（どれも対数で比例する関係）。逆に言えば、1回だけ出てきた文章は、何度も出てくる文章より出てきにくい傾向がある（「出てこない」という意味ではない）。
  3. **一般向けに提供されている対話型AI（ChatGPT、gpt-3.5-turbo）でも、特殊な攻撃をすると学習データが出てきた**。研究者が意図的に工夫した入力（同じ単語をくり返させる等）を使った攻撃で、通常より大幅に高い割合で学習データが出てきた。研究者は公開前に OpenAI に知らせ、対策に協力したと書いている。
     - ただしここで取り出されたのは**公開ウェブ由来の事前学習データ**（研究者が集めたウェブ文章のコーパスと照合して確認）で、**ほかの利用者がチャットに入力した内容が取り出されたわけではない**。
  4. **「覚えている」ことと「チャットで漏れる」ことは同じではない**：個人情報を含む架空の経歴でモデルを追加学習させた実験では、一字一句覚えている度合いが高くても、チャットで取り出せる量が増えるとは限らなかった。項目によって取り出しやすさも違った（2025年、査読済み）。
  5. **利用者側の認識**：実際の ChatGPT の会話の分析と19人へのインタビューで、利用者はプライバシー・便利さ・手軽さを天秤にかけているが、AIの仕組みについての誤った思い込みや画面設計（ダークパターン）のために、リスクを十分に理解できていなかった。人と話しているような会話のスタイルが、より踏み込んだ打ち明け話を促していた（2024年、査読済み）。
  6. **学習以外の経路もある**（研究ではなく事業者の報告）：2023年3月、ChatGPT の不具合で、一部の利用者に他人のチャット履歴のタイトルが見えた事例が報告されている。入力した情報は、学習に使われるかどうかとは別に、サービス側に保存されるため、不具合・設定・アクセス権の問題でも外に出うる。→ ただし公式ページは今回直接読めなかったため、数値は「未確認」（下の「使わないほうがよい情報」参照）。

- 根拠：
  - Carlini, N., Tramèr, F., Wallace, E., et al. 2021『Extracting Training Data from Large Language Models』30th USENIX Security Symposium（種類：個別研究／査読済み・国際会議）
    - 確認した場所：https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting （会議ページ・抄録）、https://arxiv.org/abs/2012.07805 （抄録）
    - 使える内容：GPT-2 から「数百件」の文章を一字一句取り出した。個人情報、IRC の会話、コード、128ビットのUUID を含み、各文章は学習データ中の1文書にしか出てこなかった。大きいモデルほど脆弱（確認済み・抄録）
  - Carlini, N., Ippolito, D., Jagielski, M., Lee, K., Tramèr, F., Zhang, C. 2023『Quantifying Memorization Across Neural Language Models』ICLR 2023（種類：個別研究／査読済み・国際会議）
    - 確認した場所：https://arxiv.org/abs/2202.07646 （抄録）、会議採択は https://iclr.cc/virtual/2023/poster/11469 （検索結果で確認）
    - 使える内容：記憶は ①モデルの大きさ ②学習データ中での重複回数 ③プロンプトの文脈の長さ、の3つに対して対数的に増える。モデルの系統をまたぐと関係はもっと複雑になる。対策なしでは、モデルが大きくなるほど悪化しそうだと著者は述べている（確認済み・抄録）
  - Nasr, M., Rando, J., Carlini, N., et al. 2025『Scalable Extraction of Training Data from Aligned, Production Language Models』ICLR 2025（種類：個別研究／査読済み・国際会議。2023年11月の査読前版は題名が『Scalable Extraction of Training Data from (Production) Language Models』）
    - 確認した場所：https://proceedings.iclr.cc/paper_files/paper/2025/hash/cce0e917b050208170151f77b497fc71-Abstract-Conference.html （ICLR 2025 抄録）、https://arxiv.org/abs/2311.17035 （査読前版の抄録）、https://arxiv.org/html/2311.17035v1 （査読前版の本文）
    - 使える数値：
      - 「ChatGPT を含む商用の対話型AIから、数千件の学習データを取り出した」（確認済み・ICLR 2025 抄録）
      - 「通常の振る舞いのときより150倍高い割合で学習データを出力させた」（確認済み・査読前版の抄録。**査読前版の値**と明記）
      - 「200ドル分の問い合わせで、1万件を超える学習データを一字一句取り出した」（確認済み・査読前版の本文。**査読前版の値**）
      - 「調べた出力の16.9%に、記憶された個人情報が含まれていた」（確認済み・査読前版の本文。**査読前版の値**。母数は研究者が検査した出力で、ChatGPT の普段の回答の16.9%という意味ではない）
    - 照合先：研究者が作った約9TBの公開ウェブ文章コーパス（The Pile、RefinedWeb、RedPajama、Dolma）。＝取り出されたのは公開ウェブ由来の事前学習データ（確認済み・査読前版の本文）
  - Sander, T., Jayaraman, B., Ibrahim, M., Chaudhuri, K., Guo, C. 2025『Rethinking the Role of Verbatim Memorization in LLM Privacy』NeurIPS 2025（種類：個別研究／査読済み・国際会議）
    - 確認した場所：https://neurips.cc/virtual/2025/poster/117464 （抄録）
    - 使える内容：一字一句の記憶が増えても、チャット経由の漏えいが増えるとは限らない。知識をうまく扱えるモデルのほうが、小さくてもチャットで取り出しやすいことがある。項目によって取り出しやすさが違う（確認済み・抄録）
  - Miranda, M., Ruzzetti, E. S., Santilli, A., et al. 2025『Preserving Privacy in Large Language Models: A Survey on Current Threats and Solutions』Transactions on Machine Learning Research（種類：レビュー（サーベイ）／査読済み・学術誌）
    - 確認した場所：https://mlanthology.org/tmlr/2025/miranda2025tmlr-preserving （抄録）
    - 使える内容：大規模言語モデルは機微な情報を記憶し漏らす傾向があり、ネット由来のデータでの学習と、非公開データでの追加学習（ファインチューニング）の両方がプライバシー上の懸念になる。対策として学習データの匿名化、差分プライバシー、学習後の「忘れさせる」技術（マシン・アンラーニング）などが研究されている（確認済み・抄録）。※systematic review / meta-analysis ではない
  - Zhang, Z., Jia, M., Lee, H.-P., et al. 2024『"It's a Fair Game", or Is It? Examining How Users Navigate Disclosure Risks and Benefits When Using LLM-Based Conversational Agents』CHI 2024（種類：質的研究（会話データの分析＋インタビュー）／査読済み・国際会議、DOI 10.1145/3613904.3642385）
    - 確認した場所：https://arxiv.org/abs/2309.11653 （抄録）
    - 使える数値：「半構造化インタビュー19人」（確認済み・抄録）
    - 使える内容：誤った思い込みとダークパターンがリスクの理解を妨げていた。人間らしい対話が、より機微な打ち明けを促していた（確認済み・抄録）

- サービスの設定（学習に使う・使わない）について：
  - 検索結果の要約では、OpenAI のヘルプ記事「Data controls in ChatGPT」に「個人アカウントでは『Improve the model for everyone（すべての人のためにモデルを改善する）』をオフにすると新しい会話は学習に使われない」「ChatGPT Business / Enterprise / Edu のワークスペースの内容は、初期設定で学習に使わない」とあった。**ただし、OpenAI のページは今回 403 で直接読めなかったため「未確認」**。記事で触れるなら、書き手か Sena が公開直前にヘルプ記事を直接開き、「◯年◯月◯日時点」と明記する。
  - 確認できなかったページ：https://help.openai.com/en/articles/7730893-data-controls-in-chatgpt

- 限界・注意：
  - 抽出研究の多くは、**研究者が意図的に攻撃したとき**に何が起きるかを調べたもの。普通に使っていて自分の入力が他人の画面に出てくる確率を示した研究ではない。「入れたら漏れる」とも「入れても漏れない」とも言えない。
  - 取り出されたのは主に**公開ウェブ由来の事前学習データ**。**ある利用者がチャットに入力した社内情報が、別の利用者への回答として出てきたことを示した査読研究は、今回見つからなかった**。
  - 対象モデル（GPT-2、gpt-3.5-turbo など）は古いものが多く、事業者はその後対策をしている。今のサービスにそのまま当てはまるとは言えない。
  - Nasr らの具体的な数値（150倍、200ドル、1万件、16.9%）は**査読前版（arXiv v1、2023年11月）**のもの。ICLR 2025 版の抄録は「数千件」としか書いておらず、査読版の本文で同じ数値かは確認していない。記事で数値を使うなら「2023年の研究（査読前版）」と書くか、数値を使わず「数千件」（ICLR 2025 抄録）にとどめるのが安全。
  - 研究から読者の会社の状況や、ある情報を入れてよいかを判断することはできない。「どの情報なら入れてよいか」は研究ではなく各社のルール・契約・使うツールの設定で決まる。

- 書き方の提案（不安をあおらないために）：
  - 「AIに入れたものは漏れる」ではなく、「学習に使われた文章が、条件によってはそのまま出てくることが研究で確かめられている。だから、学習に使われるかどうか（＝どのAIか・どの設定か）が判断材料になる」という順で書くと、brief の「②どのAIか」につながる。
  - 学習以外にも「サービスに保存される」こと自体が論点（不具合・アクセス権）なので、「学習オフ＝何を入れても安全」とは書かない。

### 問い4：日本の公的なガイドラインで、利用者・従業員に向けて「入力する情報」について書かれていること

- 分かっていること：
  1. **個人情報保護委員会「生成AIサービスの利用に関する注意喚起等」（2023年6月2日）**：
     - 事業者向け（個人情報取扱事業者）：個人情報を含むプロンプトを入力するときは、利用目的の達成に必要な範囲内かを十分に確認すること。本人の同意なく個人データを入力し、それが応答の出力以外の目的で扱われると、個人情報保護法に違反する可能性がある。そのため、提供事業者がその個人データを機械学習に使わないこと等を十分に確認すること。
     - 一般の利用者向け：入力された個人情報が機械学習に使われ、他の情報と統計的に結びついたうえで、正確または不正確な内容で出力されるリスクがある。サービス提供事業者の**利用規約やプライバシーポリシー等を十分に確認し、入力する情報の内容等を踏まえて**利用を判断すること。
     - ※対象は「個人情報」。会社の機密情報一般については書いていない。
  2. **総務省・経済産業省「AI事業者ガイドライン（第1.2版）」（2026年3月31日）本編・第5部「AI利用者に関する事項」**（40ページ）：
     - U-4）i.「AIシステム・サービスへ個人情報を不適切に入力することがないよう注意を払う」
     - U-5）i.「AI提供者によるセキュリティ上の留意点を遵守する」「AIシステム・サービスに機密情報等を不適切に入力することがないよう注意を払う」
     - U-7）ii.「AI提供者が定めたサービス規約を遵守する」
  3. **同ガイドライン 別添（付属資料）第1.2版・別添5「AI利用者向け」**の解説（170〜173ページ）：
     - 個人情報（U-4）：個人情報保護委員会の注意喚起等も参照のうえ、個人情報保護法に従うべき。具体例として「入力する個人データが提供者において学習データとして利用されることが予定されている場合には、同意を得られていない個人データを含むプロンプトを入力しないよう留意する」「AIに過度に感情移入すること等により、特に秘匿性の高い情報（自己の情報のみならず他者の情報を含む）をむやみにAIに与えないようにする」。社内に「プライバシー保護組織」や組織ごとの責任者を置き、「新規事業又は新規技術の開発・利用する組織が悩みを抱え込まずに、自由に相談できる体制及び環境が形成されることが重要」とも書かれている。
     - 機密情報（U-5）：「入力する機密情報が生成AIサービスの提供者においてAIの学習データとして利用されることが予定されている場合には、機密情報を含むプロンプトを入力しないよう留意する」「AIに過度に感情移入すること等により、機密情報をむやみにAIに与えないようにする」。セキュリティ上の疑問を感じた場合は提供者に報告することが期待される。
  4. **ガイドラインの性格と対象**：
     - 本編「はじめに」で、罰則のない「非拘束的なソフトロー」と明記（本編2ページ）。
     - 「AI利用者」は「事業活動において、AIシステム又はAIサービスを利用する事業者」で、想定しているのは**事業者（又は各者内の部門）**（本編5ページ）。**従業員個人に直接向けた文書ではなく、会社（組織）が取り組むことを書いたもの**。事業活動以外でAIを使う人（業務外利用者）は対象外。
     - 別添の冒頭で、各事業者が自社の「AIポリシー／AI規定等の状況に合った独自のチェックリスト・ワークシートを作成・更新」することが重要と書いている（別添3ページ）。
  5. 補足（本編の脚注で存在のみ確認）：政府職員向けには、デジタル庁「行政の進化と革新のための生成AIの調達・利活用に係るガイドライン」（2025年5月27日）がある（AI事業者ガイドライン本編3ページ脚注3）。民間企業の従業員向けではないので、今回の記事には使わなくてよい。

- 「会社のルールを確認する」の裏づけとして使えるか：
  - **使える（ただし言い方に注意）**。公的文書は「入力する情報に注意を払う」「提供者の規約・プライバシーポリシーを確認する」「学習に使われる予定なら、機密情報・同意のない個人データを入れない」と書いており、さらに AI事業者ガイドラインは**会社（事業者）が自社のAIポリシー・規定・チェックリストを作ること、相談できる体制をつくること**を想定している。
  - したがって「どの情報を入れてよいかは、国のガイドラインが一律に決めているのではなく、ガイドラインを参考に各社がルールを作る形になっている。だから個人で判断せず、まず会社のルールを確認する」という説明は、ガイドラインの構造と矛盾しない。
  - ただし、ガイドラインに「従業員は会社のルールを確認すること」という文言そのものはない（確認した範囲で）。「ガイドラインが従業員に会社のルールの確認を求めている」とは書かないほうがよい。
  - 法律の判断（どの入力が違法か）には踏み込まない。個人情報保護委員会の文書も「違反することとなる可能性がある」という書き方で、個別の判断は示していない。

- 根拠：
  - 個人情報保護委員会 2023『生成AIサービスの利用に関する注意喚起等』（令和5年6月2日）（種類：公的機関の文書）
    - 確認した場所：https://www.ppc.go.jp/news/careful_information/230602_AI_utilize_alert/ （掲載ページ）、https://www.ppc.go.jp/files/pdf/230602_alert_generative_AI_service.pdf （別添1本文・全3ページを読んだ）
    - 使える数値：日付「令和5年6月2日」（確認済み）
  - 総務省・経済産業省 2026『AI事業者ガイドライン（第1.2版）』本編（令和8年3月31日）（種類：公的機関のガイドライン／非拘束的なソフトロー）
    - 確認した場所：https://www.soumu.go.jp/main_content/001064279.pdf （本文。表紙、目次、2〜5ページ、17〜20ページ、40〜41ページを読んだ）
    - 使える数値：日付「令和8年3月31日」（確認済み）
  - 総務省・経済産業省 2026『AI事業者ガイドライン（第1.2版）別添（付属資料）』（令和8年3月31日）（種類：同上）
    - 確認した場所：https://www.soumu.go.jp/main_content/001064286.pdf （本文。目次、2〜4ページ、170〜176ページを読んだ）

- 限界・注意：
  - 第1.2版は2026年3月31日公表。第1.0版（2024年4月）、第1.1版（2025年3月28日）もあり、ネット上の解説記事は古い版を引用していることが多い。記事では「第1.2版（2026年3月）」と版を明記する。
  - 経済産業省のページ（meti.go.jp）は今回 403 で開けなかったため、総務省掲載の PDF で確認した。
  - 個人情報保護委員会の注意喚起は2023年のもので、それ以降に生成AIに特化した新しい注意喚起は今回の検索では見つからなかった（2026年の個人情報保護法改正については解説記事でしか見ておらず、未確認）。
  - 外資系企業で働く読者の場合、会社のルールは本社の方針や海外の法令にも基づくことが多く、日本のガイドラインはあくまで参考の一つ。

## 分かっていないこと
- 「どんな理由で、人は会社のAIルールを確かめずに使うのか」を、査読済みの量的研究で直接調べたものは見つからなかった（ルールを知らない、確認が面倒、聞きにくい、などの割合）。
- 「会社の情報を公開AIに入れた」日本の割合（KPMG の日本版にはない）。日本の他の調査（総務省の白書や民間調査など）は今回は調べていない。
- 公開AIに会社の情報を入れたことで、実際にどのくらい情報が漏れたり問題になったりしたか（KPMG は行動の割合だけで、その結果は調べていない）。
- 疲れ・時間に追われることと「AIに何を入れるか」の判断の関係（直接の研究なし）。
- 会社に「方針がある」と「守られる」の関係は、KPMG では相関しか分からない（禁止している職場ほど違反の申告が多いが、原因と結果は分からない）。

- 普通に使っている利用者が仕事の情報を入力したとき、それが別の利用者への回答に出てくる**確率**。研究は「攻撃したら何が出るか」が中心で、日常の使い方でのリスクの大きさは分かっていない。
- 利用者がチャットに入力した内容（社内資料など）が、学習を経て別の利用者に出てきたことを示した**査読研究**（今回の検索では見つからなかった）。
- 最新のモデル・最新のサービスで、上記の抽出攻撃がどこまで通用するか（対象は GPT-2、gpt-3.5-turbo など）。
- 「学習に使わない」設定や法人向けプランで、実際にどの程度リスクが下がるかを第三者が検証した研究（見つからなかった。事業者の説明はあるが研究ではない）。
- 日本の公的文書で、**従業員個人に向けて**「入力してよい情報／いけない情報」を具体的に列挙したもの（見つからなかった。公的文書は事業者向けで、具体的な線引きは各社に委ねている）。

## 使わないほうがよい情報
- 「57%の従業員がAIの使用を隠している」：メルボルン大学のニュースリリースや多くの記事で出ている数字だが、**報告書の「57%」は「言わなかった」と「自分のものとして出した」を合わせた non-transparent use の値**。要約版では「61% avoid revealing」とも書かれていて、媒体によって数字が違う。使うなら報告書の Figure 44 の個別の値（言わなかった 61%）と設問文を添える。単に「57%が隠す」とは書かない。
- 「従業員の40%しか、職場に方針があると言っていない」：方針あり 34%＋禁止 6% を足した値。要約版は「34%」と書いていて混乱しやすい。使うなら「方針（禁止を含む）があると答えたのは約4割、19%は分からない」と書く。
- 「48%の従業員が会社の機密データを ChatGPT に入れている」のような言い換え：設問は「公開AIツール」で ChatGPT に限らない。「機密」かどうかも聞いていない。Rarely 込みの値。ニュース記事で広まっている言い方で、誤解されやすい。
- ベンダー・セキュリティ企業の「シャドーAI」調査の数値（ManageEngine「93%が承認なしに情報を入力」、UpGuard「81%」、BlackFog「49%」、1Password「37%が方針を守らない」、CybSafe「38%が機密を共有」など）：**孫引きで、原典を読んでいない（未確認）**。サンプルや設問がそれぞれ違い、自社製品の販売につながる調査が多い。
- Deel のブログが引用している「Computers & Security の 433人の研究（方針が明確だと抜け道を使う意図が減り、方針が多すぎると増える）」：原典を見つけられなかった（**未確認**）。
- Haag & Eckhardt 2015（PACIS）「Justifying Shadow IT Usage」：研究の計画（research-in-progress）で、結果は出ていない。根拠には使えない。
- 「意志の力は使うと減る（ego depletion）」や「判事は昼食前に厳しくなる（Danziger ら 2011）」：「疲れると判断が雑になる」話でよく引用されるが、ego depletion は大規模な追試で効果がほぼ見られなかった（Hagger ら 2016 の多施設の追試など）。判事の研究には事件の順番などによる別の説明が出されている。どちらも議論が続いているので使わない（今回は原典を読み直していない）。
- 「日本で職場でAIを使う人は55%」と「44%」：KPMG の日本版と全体版で定義が違うらしく値が違う。使うならどちらの定義か書くか、使わない。

- **「サムスンの社員がChatGPTに社内のソースコードを入力して漏えいした」（2023年）**：報道で広く知られているが、今回は一次資料（会社の発表や報道の原文）を確認していない＝未確認。また「学習を通じて外に出た」と誤解されやすい（報道の多くは、外部サービスに社外秘を入れたこと自体を問題にしている）。使うなら報道元を確認し、「漏えいした」ではなく「社内で問題になり、利用を制限した」程度の言い方にする。
- **ChatGPT の不具合（2023年3月）で「ChatGPT Plus の有料会員の1.2%の支払い情報が見えた可能性」**：検索結果の要約に出てきた数値。OpenAI の公式ページ（https://openai.com/index/march-20-chatgpt-outage/ ）が 403 で直接読めなかったため未確認。使うなら書き手が公式ページを直接確認する。
- **OpenAI の「学習に使わない設定」「法人向けは初期設定で学習に使わない」の具体的な内容**：検索結果の要約のみで未確認。サービスの設定は頻繁に変わるので、記事に書くなら公開直前に直接確認し、時点を書く。特定サービス名を出さず「多くのサービスには学習に使うかどうかの設定や、法人向けプランがある。どうなっているかは会社が用意した説明やサービスのページで確認する」と一般化するほうが古くなりにくい。
- **Nasr らの「16.9%に個人情報」**：数値自体は査読前版で確認済みだが、「ChatGPT の回答の17%に個人情報が含まれる」と誤読されやすい（実際は、特殊な攻撃で取り出した出力のうち研究者が調べたものの割合）。この記事の目的（入れる前の判断）には不要で、不安をあおりやすいので使わないほうがよい。
- **「150倍」「200ドルで1万件」**：確認済みだが査読前版の値で、文脈なしだと怖さだけが残る。使うなら「研究者が意図的に攻撃した場合」「2023年の査読前版」「公開ウェブ由来のデータ」を必ず添える。基本は数値なしで「数千件（ICLR 2025）」程度でよい。
- **AI事業者ガイドラインの解説記事に出てくる「従業員が自己判断で機密情報を入力してしまうリスク」という一文**：コンサル会社等の解説記事の表現で、ガイドライン本文の文言ではない。ガイドラインの引用として使わない。
- **第1.0版・第1.1版の内容を引用した解説記事**：古い版の可能性がある。引用は第1.2版の本文から。

## 参考文献（記事末尾にそのまま使える形）
- Carlini, N., Ippolito, D., Jagielski, M., Lee, K., Tramèr, F., & Zhang, C. (2023). Quantifying Memorization Across Neural Language Models. *International Conference on Learning Representations (ICLR 2023)*. https://arxiv.org/abs/2202.07646
- Carlini, N., Tramèr, F., Wallace, E., Jagielski, M., Herbert-Voss, A., Lee, K., Roberts, A., Brown, T., Song, D., Erlingsson, Ú., Oprea, A., & Raffel, C. (2021). Extracting Training Data from Large Language Models. *30th USENIX Security Symposium*. https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting
- Chowdhury, N. H., Adam, M. T. P., & Skinner, G. (2019). The impact of time pressure on cybersecurity behaviour: a systematic literature review. *Behaviour & Information Technology*, 38(12), 1290–1308. https://doi.org/10.1080/0144929X.2019.1583769
- Dai, H., Milkman, K. L., Hofmann, D. A., & Staats, B. R. (2015). The impact of time at work and time off from work on rule compliance: The case of hand hygiene in health care. *Journal of Applied Psychology*, 100(3), 846–862. https://doi.org/10.1037/a0038067
- Gillespie, N., Lockey, S., Ward, T., Macdade, A., & Hassed, G. (2025). *Trust, attitudes and use of artificial intelligence: A global study 2025.* The University of Melbourne and KPMG. https://doi.org/10.26188/28822919 （調査報告・査読なし）
- KPMG & The University of Melbourne (2025). *Trust, attitudes and use of artificial intelligence: A global study 2025 — Japan insights.* https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2025/05/trust-attitudes-and-use-of-ai-japan-snapshot.pdf （調査報告・査読なし）
- Microsoft & LinkedIn (2024). *2024 Work Trend Index Annual Report: AI at Work Is Here. Now Comes the Hard Part.* https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part （企業の調査・査読なし）
- Miranda, M., Ruzzetti, E. S., Santilli, A., Zanzotto, F. M., Bratières, S., & Rodolà, E. (2025). Preserving Privacy in Large Language Models: A Survey on Current Threats and Solutions. *Transactions on Machine Learning Research*. https://mlanthology.org/tmlr/2025/miranda2025tmlr-preserving
- Nasr, M., Rando, J., Carlini, N., Hayase, J., Jagielski, M., Cooper, A. F., Ippolito, D., Choquette-Choo, C. A., Tramèr, F., & Lee, K. (2025). Scalable Extraction of Training Data from Aligned, Production Language Models. *ICLR 2025*. https://proceedings.iclr.cc/paper_files/paper/2025/hash/cce0e917b050208170151f77b497fc71-Abstract-Conference.html （査読前版：https://arxiv.org/abs/2311.17035 ）
- Reif, J. A., Larrick, R. P., & Soll, J. B. (2025). Evidence of a social evaluation penalty for using AI. *Proceedings of the National Academy of Sciences*, 122. https://doi.org/10.1073/pnas.2426766122
- Sander, T., Jayaraman, B., Ibrahim, M., Chaudhuri, K., & Guo, C. (2025). Rethinking the Role of Verbatim Memorization in LLM Privacy. *NeurIPS 2025*. https://neurips.cc/virtual/2025/poster/117464
- Silic, M., Silic, D., & Kind-Trüller, K. (2025). From Shadow IT to Shadow AI: Threats, Risks and Opportunities for Organizations. *Strategic Change*. https://doi.org/10.1002/jsc.2682
- Zhang, Z., Jia, M., Lee, H.-P., Yao, B., Das, S., Lerner, A., Wang, D., & Li, T. (2024). "It's a Fair Game", or Is It? Examining How Users Navigate Disclosure Risks and Benefits When Using LLM-Based Conversational Agents. *CHI 2024*. https://doi.org/10.1145/3613904.3642385
- 個人情報保護委員会（2023年6月2日）「生成AIサービスの利用に関する注意喚起等」 https://www.ppc.go.jp/news/careful_information/230602_AI_utilize_alert/
- 総務省・経済産業省（2026年3月31日）「AI事業者ガイドライン（第1.2版）」本編 https://www.soumu.go.jp/main_content/001064279.pdf ／別添（付属資料） https://www.soumu.go.jp/main_content/001064286.pdf
