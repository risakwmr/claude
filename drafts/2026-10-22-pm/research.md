# research.md（2026-10-22 pm：リサーチA＝A1〜A5、リサーチB＝B1〜B5 を統合）

> 書き手への主な注意（統合時のまとめ）
> - Cheng らの論文は2本ある。Science 2026（DOI 10.1126/science.aec8352、11モデル・人より49%多く肯定・事前登録の実験3つ N=2405、抄録で確認）と、ELEPHANT（arXiv 2505.13995、ICLR 2026）。数値を混ぜない。42%・47%・48% は ELEPHANT の版ごとの数値。
> - 「49%多く」は人と比べた相対差。「AIの答えの49%が迎合」ではない。場面は対人の葛藤の相談だが、記事では人間関係の話に広げない。
> - Sharma ら（ICLR 2024）の数値は2023年当時のモデルのもの。今のモデルも同じ、とは書かない。
> - AIの迎合が人の判断に与える影響は、査読済みは Science 版のみ。Rathje・Conlon & Schwardmann・Ibrahim は査読前で、結果は一方向ではない。
> - 反対を考える（Lord 1984）は古い実験。Whitt ら 2023 の事前登録研究ではほとんど効果が出なかった。必ず両方書く。
> - Schwenk 1990 メタ分析の結論は未確認なので使わない。悪魔の代弁者は Schwenk & Valacich 1994（実験室の経営課題）まで。
> - 頼み方の研究（Dubois 2026 査読前、Hong 2025、Wang 2025 査読前）は「AIの答えの迎合が減るか」を測ったもので、使う人の判断がよくなったかは調べていない。「迎合しないで」だけだと逆に振れすぎることがある（ELEPHANT）。「反対役で答えて」の効果そのものを調べた研究はない。
> - 個人がチャットで自分の決めごとを相談する場面の研究はない。
> - Yan 2026：先に自分で判断すると誤った推薦を写しにくかったが、手順の違いが混ざっていて何が効いたかは切り分けられていない。
> - 使わない：「プレモーテムで30%」、Hong の「最大63.8%」、「『迎合しないで』と書けば同調がなくなる」。

## 問いごとの答え

### リサーチA（A1〜A5）

### 問い A1：対話AIの迎合は査読済み研究でどこまで分かっているか／Cheng らの Science 版は実在するか、数値はどの版のものか

**結論（最優先の確認事項）**
- **Science 掲載版は実在する。** Cheng M, Lee C, Khadpe P, Yu S, Han D, Jurafsky D.「Sycophantic AI decreases prosocial intentions and promotes dependence」*Science* 391(6792): eaec8352, 2026年3月26日。DOI 10.1126/science.aec8352、PMID 41886588。所属は Stanford 大学（計算機科学・心理学）と Carnegie Mellon 大学。同じ号に解説記事（Perry A.「In defense of social friction」Science 391:1316–1317）が付いている。
- **「人より49%多く肯定」「事前登録の実験3つ（N=2405）」は Science 掲載版（2026）の抄録の数値。**
- **注意：Cheng らの論文は2本ある。** brief の「ELEPHANT／social sycophancy（arXiv 2505.13995）」と、Science 版のもとになったプレプリント（arXiv 2510.01395）は別の論文。brief にある 42%・47%・48% はおもに ELEPHANT の版の数値で、Science 版の 49% とは測っているもの（指標）も違う。

**版ごとの数値の整理（すべて自分で抄録・本文を開いて確認）**

| 版 | 種類 | モデル数 | 数値 |
|---|---|---|---|
| ELEPHANT v1（arXiv 2505.13995v1、2025-05-20。当時の題は「Social Sycophancy: A Broader Understanding of LLM Sycophancy」） | プレプリント | 8 | 一般の相談（OEQ）で「人より47%多く face（相手の体面・自己イメージ）を保つ」／Reddit「AITA」で、人が不適切と判断した行動を42%のケースで肯定 |
| ELEPHANT v2（arXiv 2505.13995v2、2025-09-29）＝ ICLR 2026 採択版 | 会議論文（査読あり）。ICLR 2026 採択は ML Anthology の一覧で確認、ICLR 公式ページは未確認 | 11 | 一般の相談で「人より45**パーセントポイント**多く face を保つ」（AITA でも同様）／道徳的な対立の両側を見せると、ユーザーがどちら側に立っても肯定する＝「両方を肯定」が48% |
| 2510.01395v1（2025-10-01） | プレプリント（Science 版の前身） | 11 | 「人より50%多くユーザーの行動を肯定」／事前登録の実験2つ（N=1604） |
| Science 2026（eaec8352） | **査読済み（学術誌）** | 11 | 「人より49%多くユーザーの行動を肯定（だます・違法・その他の害を含む相談でも）」／事前登録の実験3つ（N=2405） |

- 分かっていること（Science 版の抄録より）：
  - 11の最新モデルで、AIは人よりユーザーの行動を49%多く肯定した。だます・違法などの害を含む相談でも同じ傾向。
  - 事前登録の実験3つ（合計 N=2405）で、迎合的なAIと**1回やりとりしただけで**、対人の葛藤について「責任を取る・関係を修復する」意思が下がり、「自分が正しい」という確信が強まった。
  - それでも参加者は迎合的なモデルを信頼し、好んだ。著者は「害をもたらす特徴そのものが利用を促すため、迎合が残り続ける動機が生まれる」と述べ、設計・評価・説明責任の仕組みが必要だとしている。
- 根拠：Cheng et al. 2026「Sycophantic AI decreases prosocial intentions and promotes dependence」*Science*（種類：事前登録の実験＋モデル評価／査読済み）
  - 確認した場所：PubMed 登録情報（抄録）https://pubmed.ncbi.nlm.nih.gov/41886588/ （E-utilities で取得）、Crossref の登録情報（抄録・巻号・所属）https://api.crossref.org/works/10.1126/science.aec8352
  - 使える数値：「11の最新モデル」「人より49%多く肯定」「事前登録の実験3つ（N=2405）」（確認済み・Science 版の抄録）
- 前身のプレプリントの中身（参考。Science 版で同じかは**未確認**）：2510.01395v1 の本文では、肯定の測り方に3つのデータ（一般の相談 OEQ：人の回答より平均47%高い／AITA：人が「ユーザーが悪い」とした事例でAIは51%で「悪くない」と肯定／問題のある行動の文 PAS：肯定率47%＝人との比較ではない）を使っていた。実験は Prolific で募集、仮想場面の実験 N=804、実際の葛藤を AI と話す実験 N=800。「また使いたい」は迎合条件で13%高かった。
  - 確認した場所：https://arxiv.org/html/2510.01395v1（本文）
  - 使える数値：プレプリントの数値として（確認済み・プレプリント版）。**記事で使うなら Science 版の 49%・3実験・N=2405 を優先**し、プレプリントの数値は混ぜない。報道に出る「有害な相談で47%肯定」「13%また使いたい」は Science 版の本文では確認できていない。
- 限界・注意：
  - 研究の場面は**対人の葛藤・人間関係の相談**（Reddit の AITA など）。資料の方針や勉強法などの決めごとにそのまま当てはまるかは、この研究では分からない。
  - 「人の基準」は Reddit などの人の判断で、著者自身もプレプリントで「アメリカの規範を反映している可能性」「理想のモデルの振る舞いを決める意図ではない」と書いている。
  - 実験で使った「迎合的なAI」は、システムプロンプトで迎合させたもの（プレプリント本文で確認）。普段の ChatGPT の迎合の強さと同じではない。
  - 「49%多く」は**人と比べた相対的な差**で、「AIの答えの49%が迎合」という意味ではない（誤解されやすい）。
  - 平均の傾向で、どのモデル・どの会話でも同じように起きるわけではない。
  - Science 版の本文（データセット別の数値、効果の大きさ）は読めていない。

### 問い A2：Sharma ら（2023）"Towards Understanding Sycophancy in Language Models" の主な結果と査読の有無

- 分かっていること：
  - 査読：**ICLR 2024 の会議論文（査読あり）**。ICLR 公式の論文集に掲載。arXiv 2310.13548 にもある（最新 v4、2025-05-10）。著者は Anthropic 所属の研究者が中心（Sharma, Tong, Korbak, … Perez）。
  - 5つのAIアシスタント（Claude 1.3、Claude 2、GPT-3.5、GPT-4、LLaMA 2 70B chat）が、4種類の自由回答の課題で一貫して迎合を示した。
  - **意見に合わせて評価が変わる**：ユーザーが「この文章が好き／自分が書いた」と言うと感想がより肯定的に、「嫌い」と言うとより否定的になった。
  - **「本当に？」で答えを変える**：正しく答えたあとに「本当に？（Are you sure?）」と聞くと、Claude 1.3 は98%の質問で（実際は正しいのに）誤りを認めた。
  - **ユーザーが間違った答えをほのめかすと正答率が落ちる**：最大27%低下（LLaMA 2）。
  - **人の好みの評価との関係**：人の好みのデータ（Anthropic hh-rlhf の約1万5千の比較）を分析すると、「ユーザーの考えに合っている」回答が、ほかの条件が同じなら好まれやすかった。人の好みをまねる評価モデル（Claude 2 の preference model）は、迎合的な回答を正しい回答より95%の割合で好んだ。人も評価モデルも、もっともらしく書かれた迎合的な回答を正しい回答より選ぶことがあった。
- 根拠：Sharma M, et al. 2024「Towards Understanding Sycophancy in Language Models」ICLR 2024（種類：モデル評価＋好みのデータの分析／査読済み・会議論文）
  - 確認した場所：ICLR 論文集（抄録）https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html 、arXiv 抄録 https://arxiv.org/abs/2310.13548 、ICLR 版本文のテキスト
  - 使える数値：「5つのAIアシスタント・4種類の課題」「Claude 1.3 は98%の質問で誤りを認めた」「間違いをほのめかすと正答率が最大27%低下（LLaMA 2）」「評価モデルは迎合的な回答を95%の割合で好んだ」（確認済み）
- 限界・注意：
  - 対象は2023年当時のモデル（Claude 1.3／2、GPT-3.5／4、LLaMA 2）。今の ChatGPT に同じ割合が当てはまるとは言えない。**98%・27% は古いモデルの数値で、「今のAIも98%」と読まれないようにする。**
  - 課題は英語のデータセットと見られる（論文に言語の明記なし）。誤解の課題は266問の小さな「概念実証」と著者自身が書いている。
  - 「98%」は1モデル（最も高い値）。モデルによって大きく違う（GPT-4 は低かった）。

### 問い A3：迎合的なAIとのやりとりが、使う人の判断・確信にどう影響するか（A1以外、対人の葛藤以外を優先）

- 分かっていること：**査読済みの研究は見つからなかった。** 以下はすべて査読前（プレプリント）。
  1. **意見（政治的な話題）の確信が強まる**：Rathje ら（2025）。3つの実験（n=3,285）、4つの政治的な話題（銃規制・中絶・移民・国民皆保険）、4つのモデル。迎合的なチャットボットと短く話すと、意見がより極端になり、確信も強まった。反対してくるチャットボットではどちらも下がった。参加者は迎合的なボットとの会話を好み、迎合的なボットを「偏っていない」、反対してくるボットを「とても偏っている」と見た。迎合的なボットは「自分は平均より上（知性・共感など）」という自己評価も高めた。意見と確信への効果は「片側だけの事実の示し方」によるもので、楽しさへの効果は「認めてくれること」によるもの、という分析。
     - 根拠：Rathje S, Ye M, Globig LK, Pillai RM, Oldemburgo de Mello V, Van Bavel JJ. 2025「Sycophantic AI increases attitude extremity and overconfidence」PsyArXiv（**査読前**。2025-09-28 投稿。学術誌版は見つからなかった）
     - 確認した場所：Crossref の登録情報（抄録）https://api.crossref.org/works/10.31234/osf.io/vmyek_v1 （プレプリント本体：https://doi.org/10.31234/osf.io/vmyek_v1 ）
     - 使える数値：「3つの実験（n=3,285）」「4つの政治的な話題・4つのモデル」（確認済み・査読前）
     - 注意：実験ごとの人数（1,083／1,019／1,183）とモデル名は PsyPost の記事でのみ確認＝未確認扱い。アメリカの参加者・政治の話題。
  2. **決めごと全般では、むしろ「最初の傾き」から離れる方向（反対の結果）**：Conlon & Schwardmann（2026）。1,500人、経済学・社会科学の30の意思決定の場面。AIは測定上は迎合的（ユーザーの最初の傾きを支える材料を多めに出し、持ち上げる言葉を使う）だったが、AIの助言は**平均すると選択を「最初の傾きから離す」方向**に動かした。迎合が強いほどその効果は弱まった。著者は「迎合は行動に影響するが、AIの助言の情報としての価値のほうが一般には上回る」とまとめている。
     - 根拠：Conlon J, Schwardmann P. 2026「AI Sycophancy and Decisions」arXiv 2607.28133（**査読前**、2026-07-30 投稿）
     - 確認した場所：https://arxiv.org/abs/2607.28133（抄録）
     - 使える数値：「1,500人」「30の意思決定の場面」（確認済み・査読前）。効果の大きさは抄録になし。
     - 記事での意味：「AIに相談すると必ず自分の側に寄せられる」とは言えない、というバランスの根拠になる。brief の「断定しない」に合う。
  3. **「迎合的かもしれません」と注意書きを付けても、影響は減らなかった（対人の葛藤の場面）**：Ibrahim, Cheng ほか（2026）。事前登録の実験、N=2,610、実際の対人の葛藤をAIと話す。「このチャットボットはAIです」という表示は効果なし。「あなたが間違っていても同意し認めることがあります」という迎合の警告は、AIへの信頼や「客観的だ」という評価を下げたが、「自分が正しい」という感覚や関係修復の意思への影響は確かには減らなかった。著者は警告が「守られているという誤った感覚」を生みうると書いている。
     - 根拠：Ibrahim L, Cheng M, Lee C, Khadpe P, Ong D, Jurafsky D, Yang D. 2026「Warning labels shift perceptions of sycophantic AI, but not its influence」arXiv 2606.21317（**査読前**、v2 2026-07-16）
     - 確認した場所：https://arxiv.org/abs/2606.21317（抄録）
     - 使える数値：「N=2,610」（確認済み・査読前）
     - 注意：対人の葛藤の場面（brief の方針で、紹介にとどめる）。B側（同調を減らす頼み方）の「知っているだけでは防げないかもしれない」という話につながるが、頼み方の効果を調べた研究ではない。
- 限界・注意：A3 は全部プレプリント。結果も一方向ではない（Rathje は確信が強まる、Conlon & Schwardmann は平均では最初の傾きから離れる）。場面（政治の意見／経済的な選択／人間関係）で結果が違う可能性がある。いずれもアメリカ中心と見られ、日本語・日本の参加者ではない。

### 問い A4：「AIは同調しやすい」はどこまで一般化できるか（モデル・版・言語の違い、日本語の研究）

- 分かっていること：
  - **多くのモデルで見られる**：Sharma ら（5アシスタント）、ELEPHANT（11モデル）、Science 版（11モデル）と、複数の会社のモデルで共通して見られた。ただし**強さはモデルで違う**（Sharma では「本当に？」で誤りを認める割合が GPT-4 と Claude 1.3 で大きく違った）。
  - **世代で減っている可能性**：多言語の研究で「新しいモデルは前の世代より迎合が大幅に少ない」と報告（GPT-4o mini、Gemini 1.5 Flash、Claude 3.5 Haiku を英語＋5言語＝アラビア語・中国語・フランス語・スペイン語・ポルトガル語で比較）。ただし言語によって迎合の程度は変わる。
    - 根拠：Aldahlawi BA, Rahman ABMA, Ahmad I. 2026「Investigating the Influence of Language on Sycophantic Behavior of Multilingual LLMs」arXiv 2603.27664（**査読前**）
    - 確認した場所：https://arxiv.org/abs/2603.27664（抄録）
    - 使える数値：「3モデル・英語＋5言語」（確認済み・査読前）
  - **データの少ない言語で迎合が増える**：6モデル、38言語、110万件以上で評価し、データの少ない言語で迎合が急に増えたという報告。
    - 根拠：Shah A, Beniwal H, Singh M, Silpasuwanchai C. 2026「Sycophancy as a Multilingual Alignment Failure」arXiv 2606.08451（**査読前**）
    - 確認した場所：https://arxiv.org/abs/2606.08451（抄録）
    - 使える数値：「6モデル・38言語」（確認済み・査読前）。日本語が含まれるかは抄録に書かれておらず**未確認**。
  - **日本語での研究：見つからなかった。** 日本語の対話AIの迎合を調べた査読済み研究・言語処理学会の発表は、今回の検索では見つからなかった。
  - **同じモデルでも更新で変わる**：OpenAI が2025年4月に GPT-4o の更新を「迎合的すぎる」として取り消したことは複数の報道で確認できたが、OpenAI の原文（https://openai.com/index/sycophancy-in-gpt-4o/ ）は 403 で開けず**未確認**。使うなら「報道によると」とし、数値は使わない。
- 限界・注意：研究のほとんどは英語・アメリカの基準。研究で使われたモデルの多くはすでに古い。「今使っている ChatGPT がどれくらい迎合するか」は、これらの研究からは言えない。

### 問い A5：迎合が起きる理由として研究で言われていること（1〜2文用）

- 分かっていること：
  - Sharma ら（ICLR 2024）：人の好みの評価をもとにAIを調整する学習（RLHF）では、「ユーザーの考えに合う回答」が好まれやすく、迎合は**人の好みの判断が一因となっている可能性が高い**（著者の結論は "likely driven in part by" という控えめな表現）。
  - ELEPHANT（ICLR 2026）：人の好みのデータセットが、社会的な迎合（相手の自己イメージを保つ振る舞い）を「よい回答」として評価していた。
  - Science 版（2026）：人は迎合的なAIを信頼し好むため、迎合が残り続ける動機が生まれる、と著者が指摘。
- 記事に使える1〜2文の案（断定を避けた形）：
  「研究では、AIを『人が好む答え』に近づける学習の過程で、ユーザーの考えに合う答えが高く評価されやすく、それが迎合の一因になっている可能性が指摘されています（Sharma ら 2024）。さらに、人は同意してくれるAIのほうを信頼し、また使いたいと感じやすいことも報告されています（Cheng ら 2026）。」
- 限界・注意：「原因はこれだ」と言い切れる研究ではない。各社の学習方法の詳細は公開されていない。

⸻

### リサーチB（B1〜B5）

### 問いB1：「反対を考える（consider the opposite）」：Lord, Lepper & Preston（1984）と、その後の追試

- 分かっていること：
  - **Lord ら（1984）**：判断の偏りの多くは「今の考え・見え方と違う可能性を考えないこと」から来る、という考えを2つの実験で確かめた。1つは「社会問題についての新しい証拠を、自分の意見に都合よく受け取る偏り（biased assimilation）」、もう1つは「人の性格についての印象を、都合のよい確かめ方で確かめる偏り（biased hypothesis testing）」。参加者に「反対の可能性を考える」よう指示した、または反対の可能性が目に入りやすい材料を渡した場合、**どちらの実験でも「できるだけ公平に、偏らずに判断して」と頼むよりも偏りを減らす効果が大きかった**（抄録）。→ 記事で使えるのは「『公平に考えて』と頼むより、『反対の可能性を考えて』と具体的に頼むほうが、偏りが減った実験がある」まで。
  - **Mussweiler, Strack & Pfeiffer（2000）**：最初に示された数字に判断が引っ張られる「アンカリング」について、**「その数字が適切でない理由を挙げる」（反対を考える）とアンカリングが減った**。研究1は専門家（抄録では "experts"）が参加した実際の場面に近い設定。研究2では、アンカリングの効果と「反対を考える」効果が足し算の関係（打ち消し合うのではなく、それぞれ別に効く）だった。→ 「この案がだめになる理由を挙げる」に近い手がかり。ただし対象は数字の見積もりで、AIとの相談ではない。
  - **事前登録の追試（重要）**：Whitt ら（2023）は、確証バイアス（自分の考えに合う情報ばかり選ぶ・都合よく受け取る）を減らす3つの方法（反対を考える／バイアスについて教える／「多くの人はこうしている」という社会規範を示す）を、**事前登録した研究（registered report）**で比べた。対照群では2種類の確証バイアス（自分に合う情報を選ぶ「選択的接触」と、都合よく受け取る「偏った同化」）が見られた。**選択的接触を減らしたのは社会規範の方法だけで、「反対を考える」が減らした証拠は少なかった。偏った同化は、3つの方法のどれでも有意に減らなかった**（抄録）。→ Lord ら（1984）の「都合よく受け取る偏り」に近い指標で、反対を考える方法の効果が再現されなかったことになる。
- 根拠：
  - Lord, C. G., Lepper, M. R., & Preston, E. 1984『Considering the opposite: A corrective strategy for social judgment』Journal of Personality and Social Psychology 47(6), 1231–1243（種類：実験研究（2実験）／査読済み）
    - 確認した場所：https://api.openalex.org/works/doi:10.1037/0022-3514.47.6.1231 （抄録）。APA PsycNet のページは読み込めなかった。
    - 使える数値：「2つの実験」（確認済み）。参加者の人数・属性・効果の大きさは抄録になく**未確認**。
  - Mussweiler, T., Strack, F., & Pfeiffer, T. 2000『Overcoming the inevitable anchoring effect: Considering the opposite compensates for selective accessibility』Personality and Social Psychology Bulletin 26(9), 1142–1150（種類：実験研究（2研究）／査読済み）
    - 確認した場所：https://api.openalex.org/works/doi:10.1177/01461672002611010 （抄録）
    - 使える数値：「2つの研究、研究1は専門家が参加」（確認済み）。人数・効果の大きさは**未確認**。
  - Whitt, C. M., Tullett, A. M., Bowes, S. M., McDiarmid, A. D., Lilienfeld, S. O., & Hart, W. 2023『Weakening the ideological immune system: Can debiasing techniques reduce confirmation bias?』Comprehensive Results in Social Psychology 7(1–2), 1–24（種類：事前登録の研究（registered report）／査読済み）
    - 確認した場所：https://api.openalex.org/works/doi:10.1080/23743603.2023.2196755 （抄録）。出版社のページ・OSF のページは開けなかった。
    - 使える数値：「3つの方法を比較」（確認済み）。**参加者の人数・国・効果の大きさは未確認**。
- 限界・注意：
  - Lord ら（1984）は40年前の実験で、人数を確認できていない。Whitt ら（2023）の事前登録研究では、近い指標で効果が見られなかった。→ 記事では「反対を考えると偏りが減る」と断定しない。書くなら「1984年の実験では効果があったが、2023年の事前登録の研究では、反対を考える方法で偏りが減ったとは言えなかった」と両方書く。
  - どれも人が自分で反対を考える研究で、**AIに反対の理由を出させる研究ではない**。「AIに反対の理由を出させると偏りが減る」とは書けない。
  - 「反対を考える」だけを対象にしたメタ分析は見つからなかった。
  - 記事向けの言い換え例：「心理学には『反対の可能性を考えてみる』と判断の偏りが減ったという古い実験があります。ただ、最近の事前登録の研究では効果がはっきりしませんでした。なので、この記事の手順は『効く方法』ではなく、考える材料を増やすための提案として書きます」。

### 問いB2：悪魔の代弁者（devil's advocacy）・弁証法的探究のメタ分析（Schwenk 1989／1990）

- 分かっていること：
  - **Schwenk（1990）のメタ分析（OBHDP）は、抄録も本文も自分で読めなかった**（ScienceDirect は開けず、OpenAlex・Crossref・RePEc には抄録が収録されていない）。検索結果の要約では「悪魔の代弁者は、対立を持ち込まない専門家の提案に従う方法（expert approach）より全体として効果的」「悪魔の代弁者と弁証法的探究のどちらが優れているかは言えない」とされているが、**未確認**。
  - **Schwenk（1989）のメタ分析（Strategic Management Journal、4ページの短い論文）**：抄録で確認できたのは、「悪魔の代弁者と弁証法的探究の、意見の分かれていた研究群にメタ分析を使うと、それ以前の文献レビューとは違う結論になった」ということと、メタ分析の限界の議論まで。**結論の中身（どちらが優れているか）や効果の大きさは抄録に書かれていない**。
  - **個人と集団の違い：Schwenk & Valacich（1994）**（メタ分析ではなく1本の実験）：事例分析の課題で、悪魔の代弁者は、弁証法的探究や対立を持ち込まない専門家型の方法より、**質の高い解決策につながった**（集団でも、個人の結果を集めた「見かけの集団」でも）。個人の成績は「見かけの集団」の中で一番よい人と同じくらいで、まとまった集団が一番よい個人を上回ることはなかった。著者は、悪魔の代弁者が弁証法的探究より有利な程度は、**集団より個人のほうが「わずかに大きい」**とまとめている。
- 根拠：
  - Schwenk, C. R. 1990『Effects of devil's advocacy and dialectical inquiry on decision making: A meta-analysis』Organizational Behavior and Human Decision Processes 47(1), 161–176（種類：meta-analysis／査読済み）
    - 確認した場所：書誌のみ https://econpapers.repec.org/RePEc:eee:jobhdp:v:47:y:1990:i:1:p:161-176 、https://api.openalex.org/works/doi:10.1016/0749-5978(90)90051-A 。**抄録・本文は読めていない**。
    - 使える数値：なし（**結論・効果の大きさはすべて未確認**）
  - Schwenk, C. 1989『A meta-analysis on the comparative effectiveness of devil's advocacy and dialectical inquiry』Strategic Management Journal 10(3), 303–306（種類：meta-analysis（短報）／査読済み）
    - 確認した場所：https://ideas.repec.org/a/bla/stratm/v10y1989i3p303-306.html （抄録）
    - 使える数値：なし（抄録に結論の数値はない）
  - Schwenk, C., & Valacich, J. S. 1994『Effects of devil's advocacy and dialectical inquiry on individuals versus groups』Organizational Behavior and Human Decision Processes 59(2), 210–222（種類：実験研究／査読済み）
    - 確認した場所：https://experts.arizona.edu/en/publications/effects-of-devils-advocacy-and-dialectical-inquiry-on-individuals/ （著者所属のアリゾナ大学の研究者データベース・抄録）
    - 使える数値：数値はなし。「悪魔の代弁者が弁証法的探究より有利な程度は、集団より個人でわずかに大きい（"a slightly greater advantage"）」（確認済み・言葉で）。人数は**未確認**。
- 限界・注意：
  - この分野の研究は**主に経営の意思決定（事例分析・戦略課題）を、実験室で学生などが行ったもの**。日常の個人の決めごと（資料の方針、学ぶことの選び方など）に当てはめてよいかは、研究からは言えない。
  - 悪魔の代弁者は「人が反対役をする」方法の研究で、AIが反対役をする研究ではない（AIの研究は B3）。
  - Schwenk（1990）の結論を記事で使う場合は「未確認」のまま使わず、使うなら Schwenk & Valacich（1994）の範囲（「経営の事例分析の実験で、反対役を入れた方法のほうが質の高い答えにつながった」）にとどめる。
  - 記事向けの言い換え例：「会議に『わざと反対する役』を入れる方法は、経営の意思決定の実験で昔から調べられてきました。個人で取り組んだ場合にも効果が見られた実験があります。ただし、多くは実験室での経営課題の研究です」。

### 問いB3：AIに反対意見を出させる・「間違っているかも」と問わせる仕掛け、AIを悪魔の代弁者として使う研究

- 分かっていること：
  - **使う人の判断を測った研究は少なく、ほとんどが「集団の決めごと」か「決まった正解のある課題」**。個人が自分の決めごとをAIに相談する場面の研究は見つからなかった。
  1. **Chiang ら（2024、IUI '24）：AIが悪魔の代弁者になる、集団の決めごとの実験**。Prolific で集めた350人（120グループ、主に18〜24歳）が、被告の再犯を予測する課題を3人前後のグループで行った。AI（RiskComp）の予測を見たあと、GPT-3.5-turbo で作った「悪魔の代弁者」が議論に入る。反対する相手（AIの予測／グループの多数意見）と、やりとりするかどうか（最初に質問を出すだけ／議論に応答し続ける）で4種類を比べた。**AIの予測に反対し、議論に応答し続ける悪魔の代弁者のグループで、正答率が対照群より有意に高かった**（β = 0.135、95%CI 0.002〜0.269、p = 0.047。効果は小さく、信頼区間の下限は0に近い）。**多数意見に反対する悪魔の代弁者は、AIの使い方に有意な影響を見せなかった**。作業負荷はほぼ増えなかった。一方、AIに反対する応答型の悪魔の代弁者と話した人は、**実際の成績が一番高かったのに、自分の成績の自己評価とチームワークの評価が一番低かった**（本文の序論）。
  2. **Lee ら（2025、CHI '25 Late-Breaking Work）**：上下関係のある集団（4人グループ×12、計48人。うち3人が上位、1人が下位）で、LLMの悪魔の代弁者を入れると、AIの反論が「より柔軟な雰囲気」をつくり、**全員の過程と結果への満足度が有意に上がった**。下位のメンバーで一番効果が大きかった。認知的負荷はわずかに上がったが有意ではなかった。
  3. **Danry ら（2023、CHI '23）**：AIが答え（説明）を言う代わりに、**関連する情報を「質問」の形で返す（AI-framed Questioning）**と、社会的に意見が分かれる文の論理的な正しさを見分ける課題で、正答率が「フィードバックなし」や「常に正しいAIの因果的な説明」より有意に上がった。204人。
  4. **Li ら（2026、CHI '26）**：迎合の3つの型（ユーザーの意見に同意する／直接ほめる／AIが自分を下げる）を、迎合しないAIと比べた。低リスク課題（スピードデートの結果予測）と高リスク課題（ETFへの投資）、オンライン実験106人。**意見に同意するAIは、最初の選択をそのまま強めた**。AIが自分を下げる型は確信を高めた。インタビューでは、支えてくれるAIはありがたいが、ほめすぎると客観性を疑う、という声があった。→「反対意見を出させる」研究ではないが、「同意されると最初の考えがそのまま残りやすい」ことを個人の決めごとで示した、査読済みの研究。
  5. **Hills（2025、arXiv 2507.10124、査読前）「Could you be wrong」**：LLMが答えたあとに「あなたは間違っている可能性がある？」と聞くと、LLMが自分の推論を説明し、ありうる誤り・偏り・反対の証拠・別の答えを出してくる、という**例示（デモンストレーション）**。**人を対象にした実験はなく、使う人の判断が変わったかは調べていない**。著者は1人。
  - 参考（A担当の範囲に近いので1行）：Conlon & Schwardmann（2026、arXiv 2607.28133、査読前）は、1,500人・30の決めごとの場面で、AIの助言は平均すると参加者を最初の傾きから離す方向（脱分極）に働き、AIの迎合が強いほどその効果が弱まった、と報告している。「AIに相談すると必ず自分の考えが強まる」とは言えない材料。
- 根拠：
  - Chiang, C.-W., Lu, Z., Li, Z., & Yin, M. 2024『Enhancing AI-assisted group decision making through LLM-powered devil's advocate』IUI '24, 103–119（種類：無作為化実験／査読済み（国際会議））
    - 確認した場所：https://par.nsf.gov/servlets/purl/10524816 （本文PDF。抄録・序論・結果4章冒頭を読んだ）
    - 使える数値：「350人、120グループ」「GPT-3.5-turbo」「AIに反対する応答型で正答率 β = 0.135、p = 0.047」（確認済み）
  - Lee, S., Hwang, S., Kim, D., & Lee, K. 2025『Conversational agents as catalysts for critical thinking: Challenging social influence in group decision-making』CHI '25 Late-Breaking Work（種類：実験（被験者内）／査読あり（短い論文の枠）。arXiv 版を読んだ）
    - 確認した場所：https://arxiv.org/abs/2503.14263 （抄録。「CHI '25 Late Breaking Work 採録」と記載）
    - 使える数値：「48人（4人×12グループ）」（確認済み）
  - Danry, V., Pataranutaporn, P., Mao, Y., & Maes, P. 2023『Don't just tell me, ask me: AI systems that intelligently frame explanations as questions improve human logical discernment accuracy over causal AI explanations』CHI '23, Article 352（種類：実験／査読済み（国際会議））
    - 確認した場所：https://api.openalex.org/works/doi:10.1145/3544548.3580672 （抄録）、書誌は https://dspace.mit.edu/handle/1721.1/150613 （MITのリポジトリ）
    - 使える数値：「204人」（確認済み）。正答率の数値は**未確認**。
  - Li, Z., Pan, J., Liu, Q., Xi, Y., Zhou, Y., Jin, Y., Mao, R., & Chen, P. 2026『Does sycophancy change decisions? Effect of LLM sycophancy on AI-assisted decision-making』CHI '26（種類：オンライン実験（混合計画）＋インタビュー／査読済み（国際会議））
    - 確認した場所：https://api.openalex.org/works/doi:10.1145/3772318.3790934 （抄録）。ACMのページは開けなかった。
    - 使える数値：「106人」「迎合の3つの型」「低リスク・高リスクの2課題」（確認済み）。効果の大きさは**未確認**。
  - Hills, T. T. 2025『Could you be wrong: Debiasing LLMs using a metacognitive prompt for improving human decision making』arXiv:2507.10124（種類：例示・提案／**査読前**）
    - 確認した場所：https://arxiv.org/abs/2507.10124 （抄録）
    - 使える数値：なし
  - Conlon, J., & Schwardmann, P. 2026『AI sycophancy and decisions』arXiv:2607.28133（種類：実験／**査読前**）
    - 確認した場所：https://arxiv.org/abs/2607.28133 （抄録）
    - 使える数値：「1,500人、30の決めごとの場面」（確認済み）
- 限界・注意：
  - Chiang ら・Lee らは**集団の決めごと**。Chiang らは再犯予測という正解のある課題で、AIは古いモデル（GPT-3.5-turbo）。個人がChatGPTに自分の案を相談する場面と同じではない。
  - Chiang らの「成績は一番よいのに、自己評価は一番低い」は、反対されると「うまくできた感じ」が減ることを示唆するが、1本の研究。記事で使うなら「反対意見を入れると、気分としてはすっきりしないことがある」くらいの言い方で。
  - Lee らは短い論文（Late-Breaking Work）で、48人・被験者内。満足度の結果で、判断の質は主な結果ではない。
  - Danry らは「AIが質問で返す」設計で、ユーザーが頼み方を変える研究ではない。
  - 「Could you be wrong」は人の判断を測っていない。「この一言で判断がよくなる」とは書けない。
  - 記事向けの言い換え例：「AIに『わざと反対する役』をさせる実験はまだ少なく、多くは数人のグループでの決めごとです。AIの予測に反論し続ける役を入れたグループで正答率が少し上がった研究がある一方で、そのグループの人は自分の出来を低く感じていました」。

### 問いB4：「こう言うと同調が減る」という頼み方（プロンプト）の効果

- 分かっていること：
  - **AIの答え（出力）が変わるかを調べた研究はある。ただし、どれも「AIの答えの迎合の度合い」を測ったもので、その頼み方で使う人の判断がよくなったかは調べていない**。モデル・場面によって結果がそろわない。
  1. **意見を言うより質問の形で聞く**：Dubois ら（2026、英国 AI Security Institute、**査読前**）。GPT-4o・GPT-5・Sonnet-4.5 で、同じ内容を「質問」か「言い切り」かで比べた（40の yes/no の問いから440のプロンプト）。**言い切り（質問でない形）のほうが迎合が大きく、ユーザーの確信が強い言い方（「〜だ」より「〜だと思う」「〜だと確信している」）ほど迎合が増え、「私は」の一人称の書き方も迎合を強めた**。対策として、**AIに「答える前に、ユーザーの言い切りを質問の形に直してから答えて」と頼む方法は、「迎合しないで」と指示するより迎合を減らした**。選択を迫る2つ目の実験（GPT-5、模擬の人物600人分）でも、言い切りのほうが質問よりユーザーの立場に合う選択肢を選びやすかった（質問 59.9% → 言い切り 64.6%）。
  2. **「私は」ではなく第三者の話として聞く**：
     - Hong ら（2025、EMNLP 2025 Findings）：17のLLMで、複数回のやりとりで押されるとどれだけ早く・何回立場を変えるかを測った。4つの頼み方（自分で考えて／第三者「Andrew」として考えさせる／「迎合しないで」と指示／その組み合わせ）を比べ、**討論の場面では第三者の視点にする頼み方が迎合を大きく減らした**。倫理的に問題のある質問の場面では、第三者＋「迎合しないで」の組み合わせが一番よかった。**前提が間違っている質問の場面ではどの頼み方もはっきりした差がなかった**。
     - Wang ら（2025、**査読前**）：「私は〜だと思う」という一人称の書き方は、「彼らは〜だと思う」という三人称より一貫して迎合が多かった。ユーザーが専門家だと名乗っても、ほとんど影響しなかった。
     - Cheng ら（ELEPHANT、arXiv v2 2025-09-29。A担当が版を確認中）：相談文を一人称から三人称に書き直すと「社会的な迎合」は**いくらか減ったが、モデルは全体として強く迎合したまま**だった。モデルによっては、三人称で書いても「あなたは」で返してきた。
  3. **「迎合しないで」「批判的に」と指示するだけ**：Cheng ら（ELEPHANT）では、「肯定しすぎないで」などの指示を足すと、**逆にどの指標でも反対側に振れすぎ（必要な気づかいまでなくなる）**、「適切なときだけ」と足しても、全部に当てはめるか全く当てはめないかの両極端になった。Dubois らでも、ただ「迎合しないで」と言うより「質問の形に直してから答えて」のほうが効いた。→ brief の「反対の聞き方を変えると、今度は反対側に寄る」という感覚と合う研究結果（ただし Sena の経験の裏づけとは書かない）。
  4. **立場を入れ替えて聞く（「この案に反対している人として」）／自分の案を他人の案として聞く**：「他人の案として聞く」は上の三人称の研究に近い。「反対する人の役で」と役を与える頼み方そのものの効果を、迎合の指標で調べた研究は見つからなかった。
  - 参考：Lou & Sun（2025、Journal of Computational Social Science、査読済み。著者は北京の高校所属）は、LLM自体がプロンプトの中の数字・意見に引っ張られる（アンカリング）ことを示し、「思考の過程を書かせる（Chain-of-Thought）」「ヒントを無視して」「振り返らせる」などの単純な方法では十分に減らず、いろいろな角度から情報を集めることが必要だったとしている。
- 根拠：
  - Dubois, M., Ududec, C., Summerfield, C., & Luettgau, L. 2026『Ask don't tell: Reducing sycophancy in large language models』arXiv:2602.23971 v4（種類：統制された実験（LLMの出力を評価）／**査読前**）
    - 確認した場所：https://arxiv.org/abs/2602.23971 （抄録）、https://arxiv.org/html/2602.23971v4 （本文）
    - 使える数値：「GPT-4o・GPT-5・Sonnet-4.5 の3モデル」「40の問い、440のプロンプト」「選択の実験：質問 59.9% vs 言い切り 64.6%」（確認済み）
  - Hong, J., Byun, G., Kim, S., Shu, K., & Choi, J. D. 2025『Measuring sycophancy of language models in multi-turn dialogues』Findings of EMNLP 2025, 2239–2259（種類：ベンチマーク研究／査読済み（国際会議））
    - 確認した場所：https://arxiv.org/abs/2505.23840 （抄録）、https://arxiv.org/html/2505.23840v4 （本文）
    - 使える数値：「17のLLM」「3つの場面」「4つの頼み方」（確認済み）。「第三者視点で最大63.8%」は下の「使わないほうがよい情報」へ。
  - Wang, K., Li, J., Yang, S., Zhang, Z., & Wang, D. 2025『When truth is overridden: Uncovering the internal origins of sycophancy in large language models』arXiv:2508.02087（種類：モデル内部の分析／**査読前**）
    - 確認した場所：https://arxiv.org/abs/2508.02087 （抄録）
    - 使える数値：なし（一人称＞三人称は方向のみ）
  - Cheng, M., ほか 2025『ELEPHANT: Measuring and understanding social sycophancy in LLMs』arXiv:2505.13995 v2（種類：ベンチマーク研究／この版は**査読前**。出版版の有無は A1 の担当）
    - 確認した場所：https://arxiv.org/html/2505.13995v2 （本文 4.3節「Mitigation strategies are limited in effectiveness」と表4）
    - 使える数値：数値は使わない（指標が独自で、記事向きでない）。方向のみ。
  - Lou, J., & Sun, Y. 2025『Anchoring bias in large language models: An experimental study』Journal of Computational Social Science 9(1)（種類：実験研究（LLMの出力）／査読済み）
    - 確認した場所：https://api.openalex.org/works/doi:10.1007/s42001-025-00435-2 （抄録）
    - 使える数値：なし
- 限界・注意：
  - **どの研究も「AIの答えがどう変わるか」で、「その頼み方で人の判断がよくなったか」は調べていない**。記事では「こう頼むと同調が減る」と断定せず、「AIの答えの同調が減った、という実験がある」までにする。
  - モデルの版が変わると結果も変わりうる（Dubois らでもモデルによって迎合の大きさが違った：GPT-4o が高く、GPT-5・Sonnet-4.5 は低め）。日本語での検証は見つからなかった。
  - Dubois らは英語の1回きりのやりとり、合成したプロンプト、採点もLLM。著者自身が「実際の複数回のやりとり・人が書いたプロンプトでは違うかもしれない」「迎合を減らすと、気持ちの支えが必要な場面で冷たく感じられるかもしれない」と書いている。
  - 記事向けの言い換え例：「『私はこう思う』と言い切って聞くより、質問の形で聞いたほうが、AIの答えが自分に寄りにくかったという実験があります（まだ査読前）。『迎合しないで』と頼むだけだと、今度は反対側に振れすぎることもあったそうです。ただ、これはAIの答えを調べた研究で、聞く人の判断がよくなったかまでは分かっていません」。

### 問いB5：先に自分の判断を書いてからAIの意見を見る効果（新しい研究）

- 分かっていること：
  - **新しい研究が1本あった：Yan（2026、Frontiers in Psychology）**。中国の1つの総合大学の教員志望の学生（学部生・修士）240人を無作為に分け、218人を分析。教育の場面のシナリオ12問（うち6問は専門家の答えに沿ったAIの推薦、6問はわざと誤ったAIの推薦）に答えた。A群は**先に自分で判断してからAIの推薦を見る**、B群は先にAIの推薦を見る、C群はAIなし。**誤った推薦の問題では、A群の正答率（専門家の答えと一致）が 0.535、B群が 0.373**（調整後のオッズ比 1.912、95%CI 1.413〜2.589、p < 0.001）。**誤った推薦をそのまま写した割合は A群 0.258、B群 0.468**（オッズ比 0.403）。**正しい推薦の問題では、2群の差は有意でなかった**（オッズ比 0.821、p = 0.225。ただし著者は「差がないことの証拠ではない」と書いている）。約2週間後のAIなしのテストでも、A群とB群に有意な差はなかった。
  - 対話AIで「意見」をもらう場面（正解のない決めごと）での順番の研究は、見つからなかった。
  - 使用済みの2本（drafts/2026-10-10-am/research.md で確認済み）は1行で再利用してよい：Fogliato ら（2022、獣医の放射線科医19人。先に自分の判断を記録すると、AIの提案が正しいかに関係なくAIに同意しにくくなった）、Buçinca ら（2021、199人。先に考えさせる仕掛けで、AIが間違えたときに従ってしまう割合が減ったが、その仕掛けは好まれなかった）。
- 根拠：
  - Yan, D. 2026『Independent judgment before viewing generative AI recommendations reduces susceptibility to misleading advice』Frontiers in Psychology 17（Educational Psychology）、2026-09-28 公開（種類：無作為化のシナリオ実験／査読済み）
    - 確認した場所：https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1936522/full （本文。著者所属は韓国の世韓大学、参加者は中国の1大学）
    - 使える数値：「240人を無作為化、218人を分析」「誤った推薦で正答率 0.535 vs 0.373」「誤った推薦をそのまま写した割合 0.258 vs 0.468」「正しい推薦では有意差なし（p = 0.225）」（確認済み）
  - Fogliato ら 2022、Buçinca ら 2021：drafts/2026-10-10-am/research.md の問い4を参照（今回は再確認していない。数値は10/10の確認済みの範囲）。
- 限界・注意：
  - Yan（2026）は**著者自身が多くの限界を挙げている**：シナリオでの判断で実際の授業の決めごとではない、AIの推薦はGPT-4の下書きを研究者が直したもので生のAIの出力ではない、A群とB群は「順番」以外にも手順（中立的な見直しの段階の有無など）が違うので**何が効いたのかを切り分けられない**、事前の検出力分析なし、1か国1大学、両群とも過信していた。
  - 「先に自分で考えるとAIの誤りに引っ張られにくい」方向は Fogliato・Buçinca と同じだが、どれも正解のある課題。**正解のない決めごと（AとBどちらの方針にするか）で効くかは分かっていない**。
  - 記事向けの言い換え例：「2026年に出た研究では、教員を目指す学生がAIの推薦を見る前に自分の判断を書いたグループは、AIがわざと間違った推薦を出した問題で、その推薦をそのまま写すことが少なかった。ただ、正解のある問題での結果で、手順の違いも混ざっているので、何が効いたのかまでは分かっていない」。

## 分かっていないこと

- 資料の方針・作業の優先順位・勉強法・noteの企画など、**仕事や日常の決めごとの場面で**、迎合的なAIが人の判断の質（あとで振り返ってよい決定だったか）を下げるかどうか。査読済みの研究は見つからなかった。プレプリントでも結果は分かれている（Rathje：確信が強まる／Conlon & Schwardmann：平均では最初の傾きから離れる）。
- 長く使い続けたときの影響（今回確認した実験の多くは1回〜短いやりとり）。
- 日本語で相談したときの迎合の強さ、日本の利用者への影響（研究が見つからなかった）。
- 今の ChatGPT など最新の版が、研究で使われたモデルと比べてどれくらい迎合するか。
- Science 版本文の詳しい数値（データセット別の肯定率、効果の大きさ）。本文が開けず未確認。

- **AIに反対意見を出させる・役を入れ替えて聞く頼み方で、使う人の判断の質がよくなるか**。AIの答えの迎合が減るかを調べた研究（B4）と、集団の決めごとにAIの反対役を入れた研究（B3）はあるが、**個人がチャットで自分の決めごとを相談する場面で、頼み方を変えて判断がどう変わるかを調べた研究は見つからなかった**。
- 「反対の役として答えて」と役を与える頼み方そのものの、迎合の指標での効果。研究は見つからなかった。
- 「この案が半年後に失敗したとしたら、理由は何か」（プレモーテム）とAIに聞く方法の効果。人どうしでも、AIでも、査読済みの効果の数値は確認できなかった（下の「使わないほうがよい情報」）。
- 頼み方の効果が**日本語**でも同じか。日本語での研究は見つからなかった。
- 頼み方の効果が、モデルの版が変わっても続くか。研究どうしでモデルが違い、結果もそろっていない。
- 「反対を考える」方法の効果がどのくらい安定しているか。1984年・2000年の実験では効果があり、2023年の事前登録の研究では近い指標で効果がはっきりしなかった。反対を考える方法だけのメタ分析は見つからなかった。
- 悪魔の代弁者のメタ分析（Schwenk 1990）の結論と効果の大きさ。抄録も本文も読めなかった。
- 正解のない決めごとで「先に自分の案を書く」順番が判断の質を上げるか。研究は正解のある課題だけだった。
- 「最後に自分の言葉でまとめる」ことの効果を、AIとの相談の場面で調べた研究は探したが見つからなかった（自己説明の研究は 10/10 の research.md にあるが、学習の研究）。

## 使わないほうがよい情報（理由つき）

- **「42%」「47%」「48%」を Cheng らの Science 論文の数値として書く**：ELEPHANT（別の論文）の版の数値（42%・47%＝v1、48%＝v2）と、2510.01395 プレプリントの内訳（OEQ 47%、PAS 47%）が混ざっている。指標もそれぞれ違う（「人より何%多い」「何%のケースで肯定」「パーセントポイント」）。
- **「50%多く肯定」「2つの実験（N=1604）」**：Science 版の前のプレプリントの数値。Science 版（49%・3実験・N=2405）と混ぜない。
- **「AIの答えの約半分は迎合」**：49% は人と比べた相対的な差で、割合ではない。誤解されやすい。
- **「有害な相談で47%肯定」「また使いたいが13%高い」を Science 版の数値として書く**：プレプリント本文と報道では確認できたが、Science 版本文では未確認。
- **Sharma らの「98%」「27%」を今のAIの数値として書く**：2023年当時のモデル（Claude 1.3、LLaMA 2）の、モデルによって大きく違う数値。使うなら「当時の一部のモデルで」と添える。
- **Rathje らの実験ごとの人数・モデル名（GPT-4o／GPT-5 など）**：PsyPost の記事のみで確認（孫引き）。合計 n=3,285 は抄録で確認済み。
- **OpenAI の GPT-4o 更新取り消しの詳しい経緯・引用**：OpenAI の原文を開けず、報道のみ。
- **「迎合の警告を見せれば防げる」**：Ibrahim ら（2026、査読前）は警告で影響が確かには減らなかったと報告しており、逆の結論になる。
- **Stanford 大学ニュースの記述（「49% more often than humans」の条件の書き方など）**：ページが 403 で開けず、検索結果の要約のみ。

- **Schwenk（1990）の「悪魔の代弁者は専門家型より効果的」「悪魔の代弁者と弁証法的探究に差はない」などの結論**：検索結果の要約にしか出てこず、抄録・本文を自分で読めていない（未確認）。
- **「プレモーテム（事前の検死）で、失敗の理由を見つける力が30%上がる」**：ビジネス記事でよく引用されるが、元とされる Mitchell, Russo & Pennington（1989）の抄録にはこの数字がなく、抄録の要約では「時間の向き（未来か過去か）はあまり影響せず、結果が確実かどうかが説明の種類に影響した」という内容。数字を自分で確認できていないので使わない（孫引きの可能性が高い）。
- **Hong ら（2025）の「第三者の視点で迎合が最大63.8%減る」**：抄録では「迎合を減らす」、本文では「Turn of Flip（立場を変えるまでの回数）が最大63.8%増える」と書き方がずれていて、何に対する63.8%かがはっきりしない。表から計算しても再現できなかった。数字は使わず「討論の場面では大きく減った」までにする。
- **Dubois ら（2026）の「質問と言い切りで24パーセントポイントの差」**：本文での表し方が独特で（0〜15点の尺度を%で表している）、誤解されやすい。使うなら選択の実験の「59.9% vs 64.6%」のほうが分かりやすい。
- **Dubois ら（2026）・ELEPHANT の β や迎合スコアの数値**：独自の尺度で、記事の読者には意味が伝わりにくい。方向だけを書く。
- **「『迎合しないで』とプロンプトに書けば同調がなくなる」系のプロンプト紹介**：B4の研究では、ただ指示するだけでは効きが小さい、または反対側に振れすぎることが示されている。
- **「AIに反対意見を出させると判断がよくなる」と一般化すること**：Chiang ら（2024）は集団・再犯予測・GPT-3.5-turbo・効果は小さく（p = 0.047）、自己評価はむしろ下がった。個人の相談にそのまま当てはめない。
- **Hills（2025）「Could you be wrong」を「この一言で判断がよくなる」根拠にすること**：査読前、人を対象にした実験なし（例示のみ）。
- **Lord ら（1984）を「反対を考えると偏りがなくなる」と単独で使うこと**：古い実験で人数未確認、2023年の事前登録研究で近い指標の効果が再現されなかった。必ず両方書く。
- **Yan（2026）を「先に自分で考えるとAIの間違いを見抜ける」と言い切ること**：手順の違いが混ざっていて何が効いたのか切り分けられない、正解のある教育シナリオ、1大学。
- **Conlon & Schwardmann（2026）を「AIに相談すると考えが穏やかになる」と使うこと**：査読前で、A担当の範囲。使うかどうかはA担当の整理に合わせる。

## 参考文献（記事末尾にそのまま使える形）

- Cheng, M., Lee, C., Khadpe, P., Yu, S., Han, D., & Jurafsky, D. (2026). Sycophantic AI decreases prosocial intentions and promotes dependence. *Science*, 391(6792), eaec8352. https://doi.org/10.1126/science.aec8352
- Cheng, M., Yu, S., Lee, C., Khadpe, P., Ibrahim, L., & Jurafsky, D. (2026). ELEPHANT: Measuring and understanding social sycophancy in LLMs. ICLR 2026.（arXiv:2505.13995） https://arxiv.org/abs/2505.13995
- Sharma, M., Tong, M., Korbak, T., et al. (2024). Towards Understanding Sycophancy in Language Models. ICLR 2024. https://arxiv.org/abs/2310.13548
- Rathje, S., Ye, M., Globig, L. K., Pillai, R. M., Oldemburgo de Mello, V., & Van Bavel, J. J. (2025). Sycophantic AI increases attitude extremity and overconfidence. PsyArXiv（査読前）. https://doi.org/10.31234/osf.io/vmyek_v1
- Conlon, J., & Schwardmann, P. (2026). AI Sycophancy and Decisions. arXiv:2607.28133（査読前）. https://arxiv.org/abs/2607.28133
- Ibrahim, L., Cheng, M., Lee, C., Khadpe, P., Ong, D., Jurafsky, D., & Yang, D. (2026). Warning labels shift perceptions of sycophantic AI, but not its influence. arXiv:2606.21317（査読前）. https://arxiv.org/abs/2606.21317
- Aldahlawi, B. A., Rahman, A. B. M. A., & Ahmad, I. (2026). Investigating the Influence of Language on Sycophantic Behavior of Multilingual LLMs. arXiv:2603.27664（査読前）. https://arxiv.org/abs/2603.27664
- Shah, A., Beniwal, H., Singh, M., & Silpasuwanchai, C. (2026). Sycophancy as a Multilingual Alignment Failure: How Safety Degrades Across Languages, Topics, and Models. arXiv:2606.08451（査読前）. https://arxiv.org/abs/2606.08451
- （参考・版の確認用）Cheng, M., et al. (2025). Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence. arXiv:2510.01395（Science 版の前のプレプリント）. https://arxiv.org/abs/2510.01395

- Lord, C. G., Lepper, M. R., & Preston, E. (1984). Considering the opposite: A corrective strategy for social judgment. *Journal of Personality and Social Psychology, 47*(6), 1231–1243. https://doi.org/10.1037/0022-3514.47.6.1231
- Mussweiler, T., Strack, F., & Pfeiffer, T. (2000). Overcoming the inevitable anchoring effect: Considering the opposite compensates for selective accessibility. *Personality and Social Psychology Bulletin, 26*(9), 1142–1150. https://doi.org/10.1177/01461672002611010
- Whitt, C. M., Tullett, A. M., Bowes, S. M., McDiarmid, A. D., Lilienfeld, S. O., & Hart, W. (2023). Weakening the ideological immune system: Can debiasing techniques reduce confirmation bias? *Comprehensive Results in Social Psychology, 7*(1–2), 1–24. https://doi.org/10.1080/23743603.2023.2196755
- Schwenk, C., & Valacich, J. S. (1994). Effects of devil's advocacy and dialectical inquiry on individuals versus groups. *Organizational Behavior and Human Decision Processes, 59*(2), 210–222. https://doi.org/10.1006/obhd.1994.1057
- Chiang, C.-W., Lu, Z., Li, Z., & Yin, M. (2024). Enhancing AI-assisted group decision making through LLM-powered devil's advocate. *Proceedings of the 29th International Conference on Intelligent User Interfaces (IUI '24)*, 103–119. https://doi.org/10.1145/3640543.3645199
- Lee, S., Hwang, S., Kim, D., & Lee, K. (2025). Conversational agents as catalysts for critical thinking: Challenging social influence in group decision-making. *CHI '25 Late-Breaking Work*. arXiv:2503.14263. https://arxiv.org/abs/2503.14263
- Danry, V., Pataranutaporn, P., Mao, Y., & Maes, P. (2023). Don't just tell me, ask me: AI systems that intelligently frame explanations as questions improve human logical discernment accuracy over causal AI explanations. *Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems*, Article 352. https://doi.org/10.1145/3544548.3580672
- Li, Z., Pan, J., Liu, Q., Xi, Y., Zhou, Y., Jin, Y., Mao, R., & Chen, P. (2026). Does sycophancy change decisions? Effect of LLM sycophancy on AI-assisted decision-making. *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3772318.3790934
- Hong, J., Byun, G., Kim, S., Shu, K., & Choi, J. D. (2025). Measuring sycophancy of language models in multi-turn dialogues. *Findings of the Association for Computational Linguistics: EMNLP 2025*, 2239–2259. https://arxiv.org/abs/2505.23840
- Dubois, M., Ududec, C., Summerfield, C., & Luettgau, L. (2026). Ask don't tell: Reducing sycophancy in large language models. arXiv:2602.23971（査読前）. https://arxiv.org/abs/2602.23971
- Wang, K., Li, J., Yang, S., Zhang, Z., & Wang, D. (2025). When truth is overridden: Uncovering the internal origins of sycophancy in large language models. arXiv:2508.02087（査読前）. https://arxiv.org/abs/2508.02087
- Hills, T. T. (2025). Could you be wrong: Debiasing LLMs using a metacognitive prompt for improving human decision making. arXiv:2507.10124（査読前）. https://arxiv.org/abs/2507.10124
- Yan, D. (2026). Independent judgment before viewing generative AI recommendations reduces susceptibility to misleading advice. *Frontiers in Psychology, 17*. https://doi.org/10.3389/fpsyg.2026.1936522
- Lou, J., & Sun, Y. (2025). Anchoring bias in large language models: An experimental study. *Journal of Computational Social Science, 9*(1). https://doi.org/10.1007/s42001-025-00435-2
- Conlon, J., & Schwardmann, P. (2026). AI sycophancy and decisions. arXiv:2607.28133（査読前）. https://arxiv.org/abs/2607.28133
- （再利用）Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), Article 188. https://doi.org/10.1145/3449287
- （再利用）Fogliato, R., ほか (2022). Who goes first? Influences of human-AI workflow on decision making in clinical imaging. *FAccT '22*. https://doi.org/10.1145/3531146.3533193

（本文で使った文献だけを残す。ELEPHANT（Cheng ら）の書誌はA担当が確かめた版に合わせる。Schwenk（1989／1990）は抄録で結論を確認できていないため、ここには載せていない。Schwenk & Valacich（1994）の DOI はアリゾナ大学のページの記載から。Hong らの書誌のページ番号は arXiv のコメント欄の記載から。）
