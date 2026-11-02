# Empirical Paper Evidence & Reproducibility Audit

Use this checklist when analyzing benchmarks, methodology, results, or reproduction. Evaluate relevance, not every item mechanically.

## 1. Identify the comparison type

- **Direct baseline:** Original architecture reimplemented under identical setup.
- **Prior work / SOTA:** Historical reported numbers, often with different data and training.
- **Different backbone:** Tests plug-and-play generality only if other settings remain controlled.
- **Ablation:** Isolates a component or parameter; interactions need factorial comparisons.
- **Oracle / upper bound:** Not a deployable baseline.
- **Efficiency comparison:** Match precision, batch, input size, implementation, hardware, warmup, and throughput definition.

For every table row, locate source table and footnotes. Record whether numbers come from authors' reproductions or other papers. Treat missing variance and missing replication as uncertainty rather than evidence of no variance.

## 2. Numerical honesty

- Confirm whether metrics are fractions, percentages, points, or losses, and whether higher is better.
- `89.5 - 88.9 = +0.6 percentage points`; relative gain is `0.6 / 88.9 ≈ 0.67%`, **not** `+0.6%` relative.
- Distinguish mAP@0.5 from mAP@[.5:.95], class mIoU from instance mIoU, OA from mAcc, single-view from multi-view, and val from test.
- Parameters, checkpoint storage MB, FLOPs, MACs, measured latency, throughput, and peak VRAM are different quantities. Never infer one directly from another without assumptions.
- Check whether comparisons control data augmentation, optimizer, epoch count, seeds, pretraining, test-time augmentation, input scale, and labels.
- Check statistical variation (repeat runs, confidence intervals, significant tests). A small difference without variance estimates may be inconclusive.

## 3. Mechanism attribution

For each contribution, find:

1. An explicit no-component ablation.
2. A controlled replacement or fair alternative (stronger than only comparing against no module).
3. Complexity impact and train/test-time behavior.
4. Failure cases / negative conditions.
5. Whether gains can be explained by extra parameters, longer training, auxiliary data, or changed preprocessing.

Distinguish **evidence supporting a claim** from **proof of causation**. If no component isolation exists, say the paper does not isolate the effect.

## 4. Vision and point-cloud-specific checks

- **2D detection/segmentation:** Resolution, NMS and confidence threshold, IoU matching, class averaging, augmentations, pretraining, FPN/neck, detector variant (n/s/m/l), FPS/latency hardware.
- **3D point clouds:** Raw points vs voxel/sparse tensors, voxel size, number of sampled points, coordinate normalization, neighbor radius/kNN, scene blocks, pooling, sparse convolution or attention scaling, color/normals, data augmentations.
- **S3DIS / ScanNet / ScanNet200:** Precise dataset and split (e.g. S3DIS Area 5 vs six-fold), class set and ignore labels, validation vs official benchmark, evaluation interpolation, multi-vote and preprocessing. Do not compare these protocols naively.
- **Few-shot point-cloud segmentation:** N-way/K-shot query/support sampling, base/novel split, transductive vs inductive assumption, repeated episode averages, backbone pretraining exposure, label budgets, class balancing.
- **Domain adaptation / distillation:** Teacher access at train/test, pseudo-label quality, unlabeled target access, test-time updates, leakage possibility, storage/runtime of teacher features.
- **LoRA / adapters / TTT:** Frozen vs trainable parameter count, where adaptation occurs, episodic reset, inference batch assumptions, potential data leakage and compute overhead.

These are audit prompts, **not** assertions about any focal paper.

## 5. Reproduction readiness

| Gate | Required evidence |
| --- | --- |
| Data | Dataset edition, URL/license, splits, download/preprocess scripts |
| Environment | Framework, versions, compiled extensions, GPU, seed |
| Model | Config, exact backbone, initialization/pretraining, checkpoints |
| Training | Objective, optimizer, schedule, batch, accumulation, precision, augmentations |
| Evaluation | Script, postprocessing, class mapping, TTA, metric implementation |
| Acceptance | Target metric with tolerance, cost estimate, logged diagnostics, failure cutoff |

If resources or exact values are absent, propose how to discover them; do not invent settings. Separate **reproduce the paper** from **extend the model** and do not claim a replication was run.
