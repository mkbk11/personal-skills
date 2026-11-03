# Personal Skills

[English](README.en.md) · **中文**

一个面向 ChatGPT、Codex 及其他兼容 Agent Skills 的个人工作流工具箱。这里收录可复用的 AI 技能包，覆盖网页设计、学术论文阅读、摄影指导和作业检查。

> **设计目标：自己用得顺手，也让第一次访问仓库的人能看懂、能安装、能贡献。**
>
> 当前仓库包含 4 个 Skill。详细使用教程以中文为主；每个 Skill 的核心执行文件为 `SKILL.md`。

## 技能目录

| Skill | 适用场景 | 主要特点 | 中文指南 |
| --- | --- | --- | --- |
| **Beautiful Web Design** | 网页、React 页面、移动端界面与 UI 改版 | 从需求梳理、视觉方向到交互与验收 | [使用指南](docs/beautiful-web-design.md) |
| **Analyze Research Paper** | 学术论文精读、组会、复现与科研选题 | 拆解 Baseline、方法、实验和可迁移 Idea | [使用指南](docs/analyze-research-paper.md) |
| **Photo Coach** | 摄影学习、照片点评、拍摄规划与后期 | 构图、曝光、镜头选择、修图和练习 | [使用指南](docs/photo-coach.md) |
| **Check Assignment** | 课程作业、数学推导、代码、报告与 PPT 检查 | **只检查、定位问题和提建议，不润色、不代写** | [使用指南](docs/check-assignment.md) |

## 快速开始

### 1. 选择一个 Skill

每个 Skill 都是一个独立目录，至少包含 `SKILL.md`，并可带有 `references/` 等辅助资料。你可以只安装需要的 Skill，不必安装整个仓库。

### 2. 安装

**Codex（个人级安装）**

将所需 Skill 文件夹复制到 `~/.agents/skills/`：

```bash
git clone https://github.com/mkbk11/personal-skills.git
mkdir -p ~/.agents/skills
cp -R personal-skills/analyze-research-paper ~/.agents/skills/
```

Windows PowerShell 示例：

```powershell
git clone https://github.com/mkbk11/personal-skills.git
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item ".\personal-skills\analyze-research-paper" "$HOME\.agents\skills\" -Recurse
```

**ChatGPT**

如果你的账号或工作空间已开放 Skills 功能，可在 Skills 页面选择 **Create → Upload from computer**，上传单个 Skill 文件夹的 ZIP。功能可用性、上传权限和共享方式以账号及工作空间设置为准。

**其他 Agent**

Agent Skills 是开放格式，但各客户端的安装目录、调用方式和支持能力可能不同。请按目标客户端的官方说明安装；不要假设一个命令或路径适用于所有产品。

完整步骤、目录结构和常见问题见 [安装与调用指南](docs/installation.md)。

### 3. 调用

- **ChatGPT（已开放 Skills 功能且安装完成）**：在提示词中使用 `@skill-name` 选择 Skill，或让 ChatGPT 根据任务自动选择。
- **Codex**：使用 `$skill-name` 显式调用；也可以通过 `/skills` 查看可用技能。
- **其他 Agent**：使用该客户端支持的调用方式。

例如：

```text
请使用 analyze-research-paper 深度阅读我上传的论文，
重点分析 Baseline、方法、实验和可迁移的研究思路。
```

## 适合谁使用？

- **学生与研究者**：论文阅读、实验分析、作业检查和学术表达复核。
- **开发者与产品设计者**：网页 UI 设计、前端实现和交互审查。
- **摄影爱好者**：拍摄参数、照片点评、后期思路和练习计划。
- **Skill 作者**：参考目录组织、说明文档和维护流程，创建自己的 Skill。

## 个性化内容说明

本仓库源于维护者的真实使用场景，但不要求其他用户拥有相同背景或设备：

- Research Paper 的示例会涉及计算机视觉和点云研究；其他领域可按论文类型调整。
- Photo Coach 中提到的 Nikon 器材是维护者曾讨论的参考配置，**不代表所有使用者拥有这些器材**；使用前应替换为自己的设备。
- Beautiful Web Design 的项目示例不限制实际技术栈。
- Check Assignment 默认只提供诊断与自查建议，不会直接改写或补全作业。

## 仓库结构

```text
personal-skills/
├── README.md
├── README.en.md
├── AGENTS.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── CHANGELOG.md
├── requirements-dev.txt
├── scripts/
│   └── validate_skills.py
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
├── docs/                         # 面向使用者的中文指南
│   ├── installation.md
│   ├── beautiful-web-design.md
│   ├── analyze-research-paper.md
│   ├── photo-coach.md
│   └── check-assignment.md
├── beautiful-web-design/
├── analyze-research-paper/
├── photo-coach/
└── check-assignment/
```

每个 Skill 目录内包含：

- `SKILL.md`：核心触发条件与执行规则。
- `agents/openai.yaml`：OpenAI 客户端可使用的可选界面元数据。
- `references/`：按需读取的详细指南、检查表或参考资料。

## 设计原则

1. **Portable first**：尽量遵循开放的 Agent Skills 文件结构，避免依赖单一客户端。
2. **Progressive disclosure**：核心规则放在 `SKILL.md`，细节放入 `references/`，按需加载。
3. **Evidence over confidence**：不编造来源、实验结果、设备参数或验证结论。
4. **Clear boundaries**：明确 Skill 能做什么、不能做什么，以及哪些操作需要用户确认。
5. **Maintainable**：修改 Skill 行为时，同步更新对应中文指南和示例。

## 贡献与反馈

欢迎提出问题、建议新 Skill 或提交改进：

- [贡献指南](CONTRIBUTING.md)
- [提交 Bug / 使用问题](https://github.com/mkbk11/personal-skills/issues/new?template=bug_report.md)
- [提出新功能或 Skill](https://github.com/mkbk11/personal-skills/issues/new?template=feature_request.md)
- [安全问题报告](SECURITY.md)

## 许可与使用

**当前仓库尚未添加 LICENSE 文件。** 仓库公开可见不等于已经授予复制、修改、再发布或商业使用的许可。在维护者明确选择并添加许可证之前，请不要默认将内容视为可自由再分发。

---

Agent Skills 格式参考：[Agent Skills Specification](https://agentskills.io/specification)。
