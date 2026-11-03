# 安装与调用指南

> Agent Skills 的文件格式可以跨客户端复用，但**安装位置、导入方式、自动触发和显式调用语法由具体客户端决定**。请先确认目标产品支持 Agent Skills。

[返回仓库首页](../README.md)

## 1. 下载仓库

```bash
git clone https://github.com/mkbk11/personal-skills.git
```

Windows PowerShell：

```powershell
git clone https://github.com/mkbk11/personal-skills.git
```

仓库中的每个 Skill 都可以单独安装。不要只复制 `docs/` 中文说明；真正供 Agent 加载的是 Skill 文件夹中的 `SKILL.md` 及其引用资源。

## 2. Codex

Codex 支持个人级和项目级 Skill 目录。

| 范围 | 目录 | 适用场景 |
| --- | --- | --- |
| 个人级 | `~/.agents/skills/<skill-name>/` | 在自己的不同项目中复用 |
| 项目级 | `<project>/.agents/skills/<skill-name>/` | 与某个项目或团队共享 |

macOS / Linux 示例：

```bash
mkdir -p ~/.agents/skills
cp -R personal-skills/analyze-research-paper ~/.agents/skills/
```

Windows PowerShell 示例：

```powershell
New-Item -ItemType Directory -Force "$HOME\\.agents\\skills" | Out-Null
Copy-Item ".\\personal-skills\\analyze-research-paper" "$HOME\\.agents\\skills\\" -Recurse
```

安装后可使用 `$analyze-research-paper`、`$photo-coach` 等形式显式调用，也可输入 `/skills` 查看可用 Skill。若新 Skill 未出现，重新加载或重启 Codex。

## 3. ChatGPT

如果你的 ChatGPT 账号或工作空间已开放 Skills 功能：

1. 打开侧边栏中的 **Skills** 页面。
2. 选择 **Create → Upload from computer**。
3. 将单个 Skill 文件夹打包为 ZIP 后上传。
4. 等待平台完成扫描；如出现审核提示，先阅读相关提示再使用。
5. 在支持 Skills 的对话中，可通过 `@skill-name` 选择已安装的 Skill，或让 ChatGPT 根据任务自动调用。

ZIP 内建议保留单一顶层目录，例如：

```text
photo-coach.zip
└── photo-coach/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        ├── gear-profile.md
        ├── critique-and-editing.md
        └── shooting-playbooks.md
```

**注意：** ChatGPT Skills 的可用计划、工作空间权限、上传和共享能力可能变化。若你的界面没有 Skills 入口，请查看 [OpenAI Skills in ChatGPT 帮助文档](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)，不要假设普通聊天中的 GitHub 链接会自动安装 Skill。

## 4. Claude Code、GitHub Copilot 与其他客户端

Agent Skills 标准不规定所有客户端统一使用哪个目录。以下是常见目录示例，具体以目标客户端当前文档为准：

| 客户端 | 个人级示例 | 项目级示例 |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| GitHub Copilot | `~/.copilot/skills/` | `.github/skills/` |
| Codex | `~/.agents/skills/` | `.agents/skills/` |

将整个 Skill 文件夹放入对应目录，不要只复制 `SKILL.md`，否则其中的 `references/` 可能无法读取。

参考文档：

- [Agent Skills Specification](https://agentskills.io/specification)
- [OpenAI：Build Skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI：Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [VS Code：Use Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)

## 5. `SKILL.md` 与 `agents/openai.yaml` 有什么区别？

- `SKILL.md` 是 Agent Skills 的核心文件，包含必需的 `name`、`description` 和执行说明。
- `references/` 存放按需读取的补充规则、清单和示例。
- `agents/openai.yaml` 是面向 OpenAI 客户端的可选界面元数据，不是基础 Agent Skills 格式的必需文件。
- Skill 只提供工作流程和指令，不会自动赋予 Agent 浏览器、网络、文件或外部服务权限。

## 6. 安装与安全建议

- 只从你信任的来源安装 Skill；安装前阅读 `SKILL.md` 和引用文件。
- 不要把 API Key、密码、访问令牌或个人隐私写进 Skill。
- 第三方 Skill 可能包含影响 Agent 行为的指令；不要在未审查时授予高权限工具。
- 更新仓库后，按客户端规则同步 Skill 文件夹；必要时重新加载客户端。
- 如果你只想尝试某个 Skill，先安装单个目录，不必一次导入全部四个。
