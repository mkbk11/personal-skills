# Assignment Review — Feedback Contract

The output is a **diagnostic review report**, never a rewritten assignment. Keep the original file and original wording intact. Use Chinese by default, even for English assignments, unless the student requests another feedback language.

## Standard response layout

### 1. 检查范围与依据

- 检查对象：文件名/章节/页码或实际可见部分。
- 作业要求：已提供 / 未提供；若提供，列出所依据的关键要求。
- 检查方式：静态阅读、可核实的计算检查，或明确经授权执行的测试。
- 限制：未看到的附件、无法解析的公式/截图、未运行的代码。

### 2. 总体结论

- **基本符合的地方：** 简要提及已检查且有证据的部分。
- **最需要关注：** 一到三个真正影响正确性/要求的风险。
- **问题统计：** 高 / 中 / 低各多少项（仅计算已列出的问题）。
- 无明显问题时应诚实说明“本次检查范围内未发现明显问题”，并列出未核实范围。

### 3. 作业要求覆盖表（仅有题目/评分标准时）

| 要求编号 | 教师要求（简述） | 作业位置/证据 | 状态 | 自检方向 |
| --- | --- | --- | --- | --- |
| R1 | 要求 X | 第 2 节 | 满足 / 部分满足 / 缺失 / 无法判断 | 用户应该检查什么 |

Do not infer a missing requirement from generic expectations. If instructions are unavailable, replace this table with “未提供作业要求，无法核实覆盖度”。

### 4. 问题清单

| ID | 严重程度 | 类型 | 位置/定位信息 | 发现的问题与原因 | 修改方向（不代写） | 如何自检 |
| --- | --- | --- | --- | --- | --- | --- |
| A01 | 高 | 推导过程 | 第 2 题公式 (3)→(4) | 此步看起来忽略了某个前提条件；需要回查变量范围 | 检查所用定理或变形对参数域的要求 | 代入边界值测试该变换是否始终成立 |
| A02 | 中 | 英语语法 | 第 3 段某句，定位词“...” | 主语与谓语的数可能不一致 | 重新确认主语单复数与动词形式的对应 | 按原句逐项标出主语和谓语 |
| A03 | 低 | 格式 | 表 1 | 表头未标注量纲/单位 | 依据教师格式要求核对表头 | 检查所有数值列是否有单位 |

The example rows are **illustrative only**; never reuse as actual findings without evidence. Do not output a column named “修改后/润色后版本”.

### 5. 优先自改顺序

List at most three concrete student-owned actions, starting with correctness/mandatory requirements, then logic, then language/format.

### 6. 提交前复查

A short checklist of unresolved issues, such as:
- [ ] 所有教师明确要求有对应证据
- [ ] 关键推导有充分理由，结论和展示结果一致
- [ ] 语法/术语/图表/引用格式统一
- [ ] 需要提交的文件完整且可打开

Invite the student to submit **their own revised version** for a second check. Do not offer to rewrite the draft.

## Severity and confidence

- **高：** Key result likely wrong, mandatory deliverable missing, invalid major reasoning step, material code failure, or likely submission blocker.
- **中：** Ambiguity, incomplete justification, reproducibility issue, partial coverage, localized code/grammar problems with meaningful effect.
- **低：** Minor notation, punctuation, consistency, readability or formatting issue that does not usually change the core result.
- **待核实：** The claim depends on absent rubric, unreadable text, unexecuted code, or missing source. Do not elevate uncertainty to a proven error.

Add “确定 / 可能 / 待核实” to an issue when confidence materially affects the user's decision.

## Review modes

| Mode | Shape |
| --- | --- |
| 速查 | At most five high-impact findings; no lengthy preface |
| 全面检查（default） | Requirement matrix + evidence-backed issue table + priority order |
| 仅语法 | Flag location and rule; no rewritten sentence |
| 数学/统计过程 | Trace first unsupported step, assumptions, calculations and inference |
| 代码检查 | Static defects, requirements and test suggestions; no code patch |
| 提交前检查 | Rubric, formatting, file completeness, figures, filename and export |
| 二次复查 | Map previous issue IDs to 已解决 / 部分解决 / 仍存在 / 无法判断 |

## Language discipline

Good feedback:

- “这里的主谓一致需要核对；请先标出句子的真正主语。”
- “第 3 步到第 4 步使用了一个未说明的假设；建议检查成立条件。”
- “这一段的结论大于当前给出的证据范围，请核对是否符合题目要求。”

Not allowed:

- “我已帮你润色整篇文章。”
- “下面是可以直接替换的完整段落 / 正确推导 / 修复后的代码。”
- “我补充了一个例子和引用，让作业更完整。”
- Unrequested edits to the submission file.
