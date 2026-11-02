# Deep Reading Report — Suggested Output Contract

Adapt this outline to the paper. Do **not** force unrelated sections or fill absent cells with guesses. Write in natural, explanatory Chinese; retain exact names of algorithms, datasets, backbones, losses, and metrics in English.

## A. Two-level summary

1. **论文名 / 年份 / 发表状态 / 官方来源** — include DOI, arXiv version, code, and supplementary material only when verified.
2. **一句话** — In order to solve [specific bottleneck], the work introduces [mechanism] into [pipeline], leading to [measured result in stated protocol].
3. **三句话** — Problem; why previous methods fail; conceptual difference and evidence.
4. **阅读价值判断** — Useful for theory, generalizable module, engineering technique, experimental design, or benchmark insight? Label judgment as [分析/推断].

## B. Background, task, and novelty

| Question | What to explain |
| --- | --- |
| What is the task? | Input/output, supervision, training/inference assumptions, applicable setting |
| Why is it difficult? | Concrete bottleneck and failure mode, not generic motivation |
| What was standard? | Closest papers and the paper's direct baseline; distinguish both |
| What is new? | New architectural step, loss, sampler, objective, theory, evaluation, or combination |
| What is inherited? | Existing encoder/backbone/data/training recipe reused unchanged |

Express the gap as **prior method → missing capability → paper's proposed mechanism**. Disambiguate author claims from independent novelty assessment.

## C. Method: top down, then bottom up

1. Explain the central intuition with a simple analogy or 3–5 step mechanism.
2. Trace **input → preprocessing/encoding → key module(s) → fusion/decoder → loss/prediction** as applicable. A compact diagram is helpful only when dependencies become clearer.
3. For each claimed innovation, give:
   - **Location** in architecture or training schedule
   - **Inputs/outputs** (shape, resolution, coordinate space if specified)
   - **Mechanism** (operation, mathematical form, attention/selection policy)
   - **Why it may work** (inductive bias / assumption)
   - **Cost and fragility** (runtime, parameters, memory, dependence on labels/density)
   - **Ablation link** where reported
4. Explain major equations by variable roles, objective, and what changes under optimization. Preserve original notation where practical.
5. Separate **training-only** modules from **inference-time** modifications. If known, indicate actual code entry points; otherwise give conceptual integration points without invented filenames.

## D. Experiments: report, not just praise

### Data and protocol

List dataset version, split, input size/sampling, classes/episodes, labels, evaluation metric, backbone/pretraining, optimizer, schedule, batch, augmentation, seed/repetition, GPU, and availability **only to the extent reported**.

### Main comparison — same or controlled conditions

| Method | Backbone | Dataset / split | Metric ↑/↓ | Value | Δ vs direct baseline | Source / fairness note |
| --- | --- | --- | --- | --- | --- | --- |
| Baseline | … | … | … | … | — | Table X |
| Proposed | … | … | … | … | … points / units | Table X |

Use a *separate table* for other-backbone or cross-method results. Where conditions differ, explicitly label **非严格受控比较**, and avoid causal claims.

### Ablation and efficiency

| Variant / removed component | Metric | Δ vs full | Parameters / FLOPs / latency | Interpretation |
| --- | --- | --- | --- | --- |
| No X | … | … | … | Contribution of X *under the specific ablation* |

Assess whether the design's components interact (combination effect vs independent additive effect), and whether there are variance/error bars, generalization, robustness, qualitative failure analyses, and comparable compute.

When quoting mAP/mIoU/Accuracy as percentages, use **percentage points (pp)** for subtraction, not "percent improvement". For parameters and FLOPs, use absolute difference and correctly computed relative change when useful.

## E. Critical evaluation

- **Well supported:** Which comparison directly demonstrates which contribution?
- **Weakly supported:** What lacks a controlled test, robust estimate, or counterexample?
- **Confounds:** Changes in backbone, resolution, pretraining data, augmentation, schedule, dataset split, label budgets, post-processing, or compute.
- **Failure modes:** Sparse/dense inputs, distribution shift, novel categories, noise, occlusion, hardware constraints, overfitting, out-of-domain evaluation as relevant.
- **Reproducibility:** What source code, configurations, checkpoints, data, and seeds can actually be verified?
- **Review verdict:** Separate significance, novelty, technical strength, clarity, and transfer potential; explain disagreements rather than invent scoring criteria.

## F. Advisor synthesis

1. **Can learn:** One transferable research habit, one theoretical/architectural insight, one experiment-design lesson.
2. **Can reuse:** A concrete component or objective with an insertion point and compatibility conditions.
3. **Should not copy blindly:** Task-specific trick or unfair comparison risk.
4. **Two to four ranked ideas:** Use `research-idea-lab.md`, including minimal experiment and failure criterion.
5. **Next steps:** Read official code section, replicate paper baseline, run one minimal controlled ablation, escalate only if signal persists.
6. **Three research-group questions:** One about mechanism, one about experimental evidence, one about transfer/failure.

## Missing evidence and source labeling

Maintain a short "证据与缺口" box when necessary:

- **已核实**: source location, table/figure/appendix reference.
- **作者声称，未独立验证**: claims without reproducible evidence.
- **论文未报告**: absent information, including other-backbone tests.
- **推断/建议**: explanations or hypotheses not evaluated by authors.

Do not confuse "not mentioned in inspected sections" with "the full work definitively never reports it" when supplement or full text is unavailable.
