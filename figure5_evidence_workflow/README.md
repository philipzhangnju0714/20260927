# 新 Figure 5：带实证数据的研究流程图

## 文件
- `figure5_evidence_workflow.html`：源文件。所有数字都在文件末尾 `DATA` 对象里，逐项抄自正文 Table 1–8
- `output/figure5_evidence_workflow.png`：2880 px 宽，排成 17 cm 整页宽时约 430 dpi
- `output/figure5_evidence_workflow.pdf`：矢量版，投稿时二选一
- `render.js`：重新渲染用，命令为 `npm install playwright && node render.js`
- `fonts/`：TeX Gyre Pagella，Palatino 的开源替代字体；`assets/`：裁自 Figure 4 的两张界面截图

## 放置位置与图号
- 放在 §3.4 Data Analysis 末尾，作为新的 Figure 5
- 原 Figure 5（SEM 路径图）改为 Figure 6，原 Figure 6（ANN 拓扑图）改为 Figure 7，也可以移到补充材料作 Figure S1
- 图里第 4 步的标注写的是 "Figure 6"，指的就是改号后的 SEM 图。若图号另有安排，请改 HTML 里对应的 `ehead` 文字

## 图注（英文，可直接用）
**Figure 5.** Research process and principal empirical evidence. Each row pairs a research stage (left) with the evidence it produced (right). (1) GeoDrama interfaces used during the on-site walk (details in Figure 4) and the six perceived stimulus attributes. (2) On-site procedure, screening of 607 completed responses to 548 valid cases, and sample profile. (3) Observed ranges of measurement-quality indices against conventional criteria; shaded bands mark the acceptable region and dashed ticks the criterion. (4) Standardised structural estimates: filled circles denote significant paths (p ≤ .001) with area proportional to |β|; hollow circles denote non-significant paths; the lower strip compares the three specifications of the HPM–PA link. (5) Predictor ranks from SEM (standardised β) and ANN (mean normalised importance across ten folds); the only reversal (red) involves two paths that were non-significant in SEM. HC = historical contextualization; PC = place contextualization; NC = narrative coherence; NV = narrative vividness; PP = perceived personalisation; PIQ = perceived interaction quality; HPM = historical place meaning; PA = place affect; LHEI = local heritage exploration intention.

## 正文需要补的一句（§3.4 末尾）
> Figure 5 summarises the research process and links each stage to the principal empirical evidence it produced.

## 回复审稿人第 3 条（可直接用）
> We thank the reviewer for this suggestion. We have added a new Figure 5 at the end of Section 3.4, which integrates the research process with the empirical evidence obtained at each stage. Each methodological stage is paired with its outputs: images of the GeoDrama platform in use; the participant screening (607 completed responses, 548 retained) and the sample profile; the measurement-quality indices plotted against their criteria; the standardised structural estimates together with the comparison of alternative specifications; and the agreement between SEM and ANN predictor rankings (12 of 14 rank positions). All values are taken directly from Tables 1–8; no new analyses were conducted. Figures were renumbered accordingly.

## 改动方法
- 改数字：只改 `DATA`，图会自动重画
- 改文字：直接改 HTML 中 `.proc` 内的英文
- 改配色：改 `:root` 里的变量。`--cog` 为认知路径（蓝），`--aff` 为情感路径（橙），`--acc` 为强调色（深红）
