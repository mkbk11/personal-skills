# Research Idea Lab — Extract, Transfer, Test

An idea is useful only if the **mechanism**, **compatible setting**, **cost**, and **falsifiable prediction** are explicit. Do not manufacture novelty or promise gains.

## 1. Decompose the source mechanism

For each useful contribution, extract:

1. **Triggering failure:** What specific error or limitation motivated it?
2. **Invariance/inductive bias:** Geometry, locality, temporal consistency, uncertainty, sparsity, symmetry, or information bottleneck?
3. **Operational change:** Architecture replacement, plug-in module, feature transformation, loss/regularizer, training curriculum, distillation, sample selection, or inference adaptation?
4. **Required signals:** Labels, spatial coordinates, gradients, neighbors, auxiliary teacher, sequence, test stream?
5. **Causal hypothesis:** What measurable intermediate behavior should change before the final metric improves?
6. **Boundary conditions:** What data regime or architecture invalidates the mechanism?

Separate the generalizable principle from paper-specific hyperparameters or benchmark tricks.

## 2. Explore transfer paths

| Path | Question | Example of a *hypothesis*, not a claim |
| --- | --- | --- |
| Module transplant | Can a module replace or attach to a target backbone? | Geometry gate added to an adapter block |
| Loss / regularization | Can the training signal be transferred without inference cost? | Boundary-aware contrastive objective |
| Feature or data view | Can representations be augmented while preserving semantics? | Tangent-space feature perturbation |
| Sampling / attention | Can compute be allocated only where difficult? | Density/curvature-conditioned token selection |
| Training strategy | Can self-distillation, freezing, or scheduling improve stability? | Teacher-guided adapter warmup |
| Cross-task adaptation | What changes for 2D→3D, dense→few-shot, classification→segmentation? | Apply a local mechanism to episodic support/query features |

Do not propose a mere collage of modules. Explain why the source mechanism addresses a diagnosed weakness in the target model. Verify compatibility of feature shapes, receptive fields, labels, differentiability, data flow, and training/inference budgets.

For point-cloud work, explicitly ask whether coordinates/neighbor topology exist where the module runs; whether point permutation, rigid transforms, point density, voxelization, sparsity, occlusions, or cross-scene statistics break its assumptions; and whether proposed improvements are at boundaries, on planes, or for rare classes.

## 3. Rank proposals

Choose 2–4 **distinct**, not cosmetic, possibilities. For each:

**Idea title:** [specific mechanism] + [target problem]

- **What to borrow:** Named source technique and essential mechanism (with paper location).
- **Target / insertion point:** Model, tensor path, stage, and before/after what operation.
- **Modification:** Exactly what differs from the original method; loss formula or pseudocode when useful.
- **Why it might help:** One explicit prediction about errors, robustness, or efficiency.
- **Conditions:** Needed data, labels, code, memory, and architectural assumptions.
- **Risk / novelty:** Possible prior art, failed assumptions, training instability, compute burden. New idea is not automatically publishable novelty.
- **First experiment:** Controlled comparison against direct target baseline and simple alternative.
- **Success / reject rule:** Minimum meaningful effect relative to run-to-run noise, memory/latency budget, and failure signal.

Optionally rank with low/medium/high **novelty potential**, **feasibility**, **expected impact**, **implementation cost**, **evidence strength**; these are qualitative judgments, not measured scores. Favor low-cost, high-information tests before elaborate combinations.

## 4. Minimum viable research experiment (1–3 days)

1. **Day 0 / Baseline:** Fix code commit, data/split, random seed(s), environment, evaluation, and one measurable hypothesis. Verify baseline metric and memory.
2. **Day 1 / Minimal transplant:** Change exactly one component or objective. Use identical settings, short sanity training, log gradient norms/feature statistics if relevant.
3. **Day 2 / Signal check:** Compare not only headline metric but predicted intermediate behavior (boundary IoU, rare-class recall, robustness to density, latency, etc.). Check at least one alternative or negative control.
4. **Day 3 / Decision:** If signal persists, expand seeds/splits/backbones and factorial ablations. If not, inspect assumptions; stop or revise rather than stacking unrelated tricks.

These are planning windows, not promises that hardware, data, or training time always fit.

## 5. Idea card template

| Field | Fill precisely |
| --- | --- |
| Problem / target | Existing failure mode in a named task/model |
| Source principle | Mechanism extracted from paper |
| Integration | Specific stage, tensor, loss, or sampling hook |
| Hypothesis | Predicted measurable change |
| Fair baseline | Identical protocol; exact comparator |
| Ablations | Remove/replace gate, loss, input signal or module |
| Cost | Trainable parameters, FLOPs, VRAM, latency, labels |
| Stop condition | No signal beyond noise, instability, exceeded cost, violated assumption |
| Next step | One immediately executable experiment |

Clearly mark all such cards **[研究建议：未经实验验证]**. When the user has a known active model/project, tailor targets to that project without assuming its current repository or configuration is accessible.
