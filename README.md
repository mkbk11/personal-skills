# Personal Skills

个人维护的 Codex 技能集合，将常用的设计方法和工作流程整理为可复用的技能。

## 技能列表

| 技能 | 用途 | 适用场景 |
| --- | --- | --- |
| [beautiful-web-design](./beautiful-web-design/SKILL.md) | 设计、构建和优化美观、易用的响应式 Web 界面 | 落地页、仪表盘、Web 应用、React 组件、已有页面改版 |

## Beautiful Web Design

`beautiful-web-design` 为前端界面开发提供从需求理解到交付检查的指导，关注视觉质量、真实交互和代码可维护性。

- **视觉设计**：建立适合产品的配色、字体、间距和组件状态，保持清晰的信息层级。
- **响应式布局**：从移动端出发，兼顾平板与桌面端的阅读和操作体验。
- **组件实现**：优先复用现有组件和依赖，遵循项目约定；适用于 React 等前端项目。
- **交互与可访问性**：关注加载、空数据、错误与成功状态，以及键盘操作和可访问名称。
- **现有页面改版**：保留必要功能，控制修改范围，并检查重要用户流程。
- **验证与交付**：在工具可用时检查实际渲染结果，说明已验证内容和已知限制。

技能提供工作指导；具体实现和验证取决于项目代码、需求及可用工具。

## 安装

### 通过 Codex 安装

在支持 `$skill-installer` 的 Codex 环境中发送：

```text
$skill-installer 请安装以下 GitHub 目录中的技能：
https://github.com/mkbk11/personal-skills/tree/main/beautiful-web-design
```

### 手动安装

下载或克隆仓库：

```bash
git clone https://github.com/mkbk11/personal-skills.git
```

将整个 `beautiful-web-design` 文件夹复制到以下任一位置：

| 使用范围 | 目标目录 |
| --- | --- |
| 当前项目 | <项目根目录>/.agents/skills/beautiful-web-design/ |
| 当前用户的所有项目 | ~/.agents/skills/beautiful-web-design/ |

请保留 `SKILL.md`、`agents/` 和 `references/` 的目录结构。安装后，Codex 会自动检测技能；如果未显示，可重启 Codex。安装位置与调用方式详见 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills)。

## 使用示例

安装后，在请求中明确指定技能，并补充产品目标、技术栈和需要保留的功能。

**创建新页面**

```text
使用 $beautiful-web-design 为一个个人知识管理产品制作中文落地页。
使用 React 和 TypeScript，面向独立开发者，
包含产品介绍、功能展示和注册入口，兼顾手机与桌面端。
```

**优化已有界面**

```text
使用 $beautiful-web-design 优化当前仪表盘的视觉层级和移动端布局。
保留现有数据查询、筛选和导出功能，遵循项目现有的组件与样式约定。
```

**审查页面体验**

```text
使用 $beautiful-web-design 检查当前页面的排版、间距、对比度、
键盘操作和响应式表现，先列出主要问题，再修复最影响使用的部分。
```

## 仓库结构

```text
personal-skills/
├── README.md
└── beautiful-web-design/
    ├── SKILL.md                       # 技能说明与工作流程
    ├── agents/
    │   └── openai.yaml                # 显示名称、简介与默认提示
    └── references/
        └── design-guidelines.md       # 视觉、响应式与可访问性指南
```

## 反馈

如有使用问题或改进建议，欢迎通过 [Issues](https://github.com/mkbk11/personal-skills/issues) 反馈。描述具体场景、预期效果和实际表现，有助于完善技能。
