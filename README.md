# Personal Skills

我的个人 AI Skills 工具箱：把经常使用的**网页开发、论文研究、摄影学习和作业检查**方法整理为可复用的工作流程，适用于支持 Agent Skills 的 ChatGPT、Codex 等环境（具体安装与调用方式取决于所用客户端）。

## 技能目录

| Skill | 一句话介绍 | 中文介绍与使用指南 | 执行规则 |
| --- | --- | --- | --- |
| **Beautiful Web Design** | 设计、实现与优化响应式 Web 界面，兼顾视觉质量、交互和可维护性 | [阅读指南](./docs/beautiful-web-design.md) | [SKILL.md](./beautiful-web-design/SKILL.md) |
| **Analyze Research Paper** | 深度精读论文、分析 Baseline 与实验、挖掘可迁移的科研 Idea | [阅读指南](./docs/analyze-research-paper.md) | [SKILL.md](./analyze-research-paper/SKILL.md) |
| **Photo Coach** | 个性化摄影指导、尼康参数建议、照片点评、后期与摄影陪练 | [阅读指南](./docs/photo-coach.md) | [SKILL.md](./photo-coach/SKILL.md) |
| **Check Assignment** | 按作业要求检查语法、推导、代码和格式；只提建议，不润色、不代写 | [阅读指南](./docs/check-assignment.md) | [SKILL.md](./check-assignment/SKILL.md) |

三份中文指南使用相同的结构：**技能定位 → 适用场景 → 核心能力 → 输入与输出 → 使用步骤 → 使用示例 → 建议与边界 → 参考资料**。

## 快速开始

1. **选择技能**：从上表打开对应的中文指南，确认它能解决什么问题。
2. **准备输入**：Web Design 提供需求或项目代码；Research Paper 提供论文 PDF/链接；Photo Coach 提供照片或拍摄场景；Check Assignment 提供作业要求和已完成的答案。
3. **发起任务**：在已安装 Skill 的环境中，直接说明要使用的 Skill，再描述目标、限制和期望结果。
4. **逐轮改进**：根据第一次输出追问、补充素材或要求调整；不要把演示代码、未复现实验或猜测参数当成已验证结果。

在支持个人 Skills 的 ChatGPT 中，可用 `@beautiful-web-design`、`@analyze-research-paper`、`@photo-coach`、`@check-assignment` 指定已安装的 Skill；在 Codex 等环境里，也可以使用对应的 `$skill-name` 形式（以实际客户端为准）。

需要可直接复制的完整提示词？请进入各自的**中文使用指南**：

- [Web Design：新建页面、现有项目改版与 UI 审查](./docs/beautiful-web-design.md#6-使用示例)
- [Research Paper：论文精读、实验对比、组会与 Idea 迁移](./docs/analyze-research-paper.md#6-使用示例)
- [Photo Coach：照片点评、扫街、夜景人像、修图与选片](./docs/photo-coach.md#6-使用示例)
- [Check Assignment：语法、数学推导、代码与提交前检查](./docs/check-assignment.md#6-使用示例)

## 安装说明

如果 Skill 已安装到当前环境，**无需重复下载**。只有在另一台设备、另一种 Agent 或新的安装环境中使用时，才需要根据该环境的要求安装。

在支持 GitHub Skill 目录安装的 Codex 环境中，可以指定单个目录，例如：

```text
$skill-installer 请安装以下 GitHub 目录中的技能：
https://github.com/mkbk11/personal-skills/tree/main/photo-coach
```

将链接中的 `photo-coach` 换成 `beautiful-web-design`、`analyze-research-paper` 或 `check-assignment`，即可指定其他技能。安装命令是否可用取决于客户端。

也可以下载仓库：

```bash
git clone https://github.com/mkbk11/personal-skills.git
```

按目标 Agent 的文档，将**整个 Skill 文件夹**放到相应的 Skills 目录，并保留其中的 `SKILL.md`、`agents/`、`references/`。注意：仅复制 `docs/` 中的中文指南，不等于安装 Skill。

## 仓库结构

```text
personal-skills/
├── README.md                         # 简洁首页与导航
├── docs/                             # 面向使用者的统一中文指南
│   ├── beautiful-web-design.md
│   ├── analyze-research-paper.md
│   ├── photo-coach.md
│   └── check-assignment.md
├── beautiful-web-design/
│   ├── SKILL.md                       # AI 执行规则
│   ├── agents/
│   └── references/
├── analyze-research-paper/
│   ├── SKILL.md
│   ├── agents/
│   └── references/
├── photo-coach/
│   ├── SKILL.md
│   ├── agents/
│   └── references/
└── check-assignment/
    ├── SKILL.md
    ├── agents/
    └── references/
```

- `docs/*.md`：给人阅读的中文介绍、使用教程和可复制提示词。
- `<skill-name>/SKILL.md`：Agent 根据任务触发后遵循的正式工作流程。
- `references/`：该 Skill 的深入规则、范例和检查清单；`agents/`：显示与调用相关的元信息。

## 反馈与改进

欢迎通过 [GitHub Issues](https://github.com/mkbk11/personal-skills/issues) 提交使用建议。最好附上具体任务、期望效果、实际结果以及需要改进的环节。
