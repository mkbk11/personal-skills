# Personal Skills

个人维护的 AI / Codex / ChatGPT Skills 集合，将常用的开发方法、科研分析流程和实践经验沉淀为可复用的技能。

## 技能列表

| 技能 | 用途 | 适用场景 |
| --- | --- | --- |
| [beautiful-web-design](./beautiful-web-design/SKILL.md) | 设计、构建和优化美观、易用的响应式 Web 界面 | 落地页、仪表盘、Web 应用、React 组件、已有页面改版 |
| [analyze-research-paper](./analyze-research-paper/SKILL.md) | 深度解读论文、审视实验结果、提炼可迁移研究 Idea | 论文精读、导师组会、模型复现、Baseline 分析、科研创新探索 |

## Beautiful Web Design

`beautiful-web-design` 为前端界面开发提供从需求理解到交付检查的指导，关注视觉质量、真实交互和代码可维护性。

- **视觉设计**：建立适合产品的配色、字体、间距和组件状态，保持清晰的信息层级。
- **响应式布局**：从移动端出发，兼顾平板与桌面端的阅读和操作体验。
- **组件实现**：优先复用现有组件和依赖，遵循项目约定；适用于 React 等前端项目。
- **交互与可访问性**：关注加载、空数据、错误与成功状态，以及键盘操作和可访问名称。
- **现有页面改版**：保留必要功能，控制修改范围，并检查重要用户流程。
- **验证与交付**：在工具可用时检查实际渲染结果，说明已验证内容和已知限制。

技能提供工作指导；具体实现和验证取决于项目代码、需求及可用工具。

## Analyze Research Paper

`analyze-research-paper` 是面向科研学习与论文研究的深度阅读助手，不止总结 Abstract，更强调**读懂方法、判断证据、提炼可迁移的技术思路**。默认中文输出，保留必要的英文术语。

- **背景与任务**：梳理研究问题、应用场景、已有方法的不足和论文动机。
- **Baseline 与创新点**：辨别直接 Baseline、相关工作、Backbone 和真正新增的技术机制。
- **顶层设计与方法**：从整体框架到模块数据流、关键公式、损失函数、训练与推理过程逐层解释。
- **实验与可信度**：分析主结果、不同 Backbone、消融、计算效率和鲁棒性；检查指标口径与比较条件是否公平。
- **复现与工程实现**：整理代码、数据集、配置、依赖、关键参数及潜在复现难点。
- **科研启发与 Idea**：提炼能迁移到其他模型/任务的机制，明确插入位置、技术风险、对照实验与最小可行验证路线。

支持**速读、深读（默认）、导师组会 / Reviewer、复现 / Code、Idea / 迁移、多篇对比**等模式。对计算机视觉、点云分割、Few-shot 学习等论文，可进一步核查数据划分、mAP/mIoU、采样、预训练、训练预算和消融细节。

> 分析时区分「论文事实」「核算结果」「推断」「研究建议」。如果论文未报告某项实验，明确标注“未报告”，不臆造指标或实验结论。

详细规范见 [SKILL.md](./analyze-research-paper/SKILL.md)，以及 [论文分析模板](./analyze-research-paper/references/analysis-template.md)、[实验审查清单](./analyze-research-paper/references/experiment-audit.md)、[科研 Idea 指南](./analyze-research-paper/references/research-idea-lab.md)。

## 安装

### 在支持 Skill Installer 的 Codex 环境中

安装所需技能（把目录链接替换成对应技能的 GitHub 链接）：

```text
$skill-installer 请安装以下 GitHub 目录中的技能：
https://github.com/mkbk11/personal-skills/tree/main/analyze-research-paper
```

同理可以安装 [beautiful-web-design](https://github.com/mkbk11/personal-skills/tree/main/beautiful-web-design)。

### 手动安装

下载或克隆仓库：

```bash
git clone https://github.com/mkbk11/personal-skills.git
```

将所需的**整个技能文件夹**（例如 `analyze-research-paper`）复制到相应的 Skills 目录。常见 Codex Agent Skills 目录如下：

| 使用范围 | 目标目录示例 |
| --- | --- |
| 当前项目 | `<项目根目录>/.agents/skills/<skill-name>/` |
| 当前用户的项目 | `~/.agents/skills/<skill-name>/` |

请保留 `SKILL.md`、`agents/` 和 `references/` 的结构；具体安装方式以使用环境为准。更多说明见 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills)。

## 使用示例

### 论文深度精读

```text
使用 $analyze-research-paper 深度分析我上传的这篇论文。
请重点解释：研究背景、任务、Baseline、核心思想、方法细节、
与 Baseline / 其他 Backbone 的对比、消融结果、局限性，
以及可以迁移到点云分割模型中的 2–4 个科研 Idea。
```

### 论文复现与 Idea 探索

```text
使用 $analyze-research-paper 的复现与 Idea 模式。
结合我正在研究的 Point Transformer / Few-shot Point Cloud Segmentation，
找出这篇论文中值得移植的技术，说明模块插入位置、必要修改、
潜在风险，并设计 1–3 天可验证的最小实验。
严格区分论文已验证结论与未验证假设。
```

### 创建新页面

```text
使用 $beautiful-web-design 为个人知识管理产品制作中文落地页。
使用 React 和 TypeScript，包含产品介绍、功能展示和注册入口，
兼顾手机与桌面端。
```

### 优化已有界面

```text
使用 $beautiful-web-design 优化当前仪表盘的视觉层级和移动端布局。
保留现有数据查询、筛选和导出功能，遵循现有组件与样式约定。
```

## 仓库结构

```text
personal-skills/
├── README.md
├── beautiful-web-design/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── references/
│       └── design-guidelines.md
└── analyze-research-paper/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        ├── analysis-template.md
        ├── experiment-audit.md
        └── research-idea-lab.md
```

## 反馈

如有使用问题或改进建议，欢迎通过 [Issues](https://github.com/mkbk11/personal-skills/issues) 反馈。描述具体场景、预期效果和实际表现，有助于不断完善技能。
