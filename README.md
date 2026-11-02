# Personal Skills

个人维护的 AI / Codex / ChatGPT Skills 集合，将常用的开发方法、科研分析流程和实践经验沉淀为可复用的技能。

## 技能列表

| 技能 | 用途 | 适用场景 |
| --- | --- | --- |
| [beautiful-web-design](./beautiful-web-design/SKILL.md) | 设计、构建和优化美观、易用的响应式 Web 界面 | 落地页、仪表盘、Web 应用、React 组件、已有页面改版 |
| [analyze-research-paper](./analyze-research-paper/SKILL.md) | 深度解读论文、审视实验结果、提炼可迁移研究 Idea | 论文精读、导师组会、模型复现、Baseline 分析、科研创新探索 |
| [photo-coach](./photo-coach/SKILL.md) | 尼康拍摄指导、照片点评、后期修图与循序摄影练习 | 旅游、城市扫街、人像、风光、静物、运动摄影 |

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

## Photo Coach · 私人摄影导师

`photo-coach` 是面向摄影爱好者的 **AI 私人摄影导师 + 实战陪练**。它不只告诉你“这张照片好不好看”，更重要的是解释：**为什么这样拍、画面哪里有问题、如何在下一次拍摄中改进**。默认用中文交流，专业术语会配合通俗解释。

适合旅行记录、城市扫街、人像、风光、夜景、静物和运动摄影；既可以在出门前做拍摄准备，也可以在回来后点评照片、指导后期，逐步培养自己的审美与拍摄习惯。

### 核心能力

| 模式 | 你提供什么 | Photo Coach 会给出什么 |
| --- | --- | --- |
| **照片点评** | 一张或多张照片，最好补充拍摄意图 | 画面亮点、构图与光线分析、最值得改善的 2–3 点、重拍与后期建议 |
| **拍前指导** | 场景、时间、题材、现有器材 | 镜头选择、光圈/快门/ISO 起始设置、对焦建议、现场调整思路 |
| **后期修图** | 原图、目标风格、修图软件 | 裁剪、白平衡、曝光、局部蒙版、色彩和降噪的操作顺序 |
| **多图选片** | 一组近似照片或旅行相册 | 选片理由、排序逻辑、照片故事和作品集建议 |
| **摄影陪练** | 学习目标、可用时间、拍摄作品 | 15–30 分钟的小练习、点评反馈、下一阶段练习内容 |
| **旅行摄影** | 目的地、时间、体力、想拍的题材 | 轻松的拍摄任务、题材清单、适合的光线与镜头取舍 |
| **器材咨询** | 现有设备、预算、遇到的问题 | 兼容性、实际提升、性价比与是否真的有必要购买 |

### 个人尼康器材参考

针对此前讨论的组合，Skill 预设了三项**候选器材**，可随时根据实际情况更新：

- **Nikon Z6II**：作为机身参考，指导曝光、自动对焦、机身防抖和拍摄模式。
- **NIKKOR Z 24–200mm f/4–6.3 VR**：侧重旅游一镜走天下、风光、建筑、扫街和远处细节。
- **TTArtisan AF 50mm f/1.8 NEO**：侧重人像、夜间扫街、静物与浅景深创作。

> **注意：**以上是此前的选购讨论，并不代表已经购买。Skill 不会把计划中的器材当作已拥有设备。任何拍摄参数都是可调整的起点，需要结合实际光线、主体移动速度和画面效果判断；防抖不能代替高速快门来冻结运动主体。

### 三步开始使用

1. **说明目的**：例如“点评这张照片”“我明天去澳门扫街”“教我拍夜景人像”。
2. **提供素材或条件**：上传照片，或者说明题材、光线、使用镜头、可用时间；有 EXIF、RAW/JPEG 信息也可以附上。
3. **选择希望的反馈深度**：速评、详细点评、相机参数速查、后期操作教程，或一周摄影练习。

在支持个人 Skills 的 ChatGPT 中，如果已经安装，可直接输入 `@photo-coach` 并附上请求；其他环境需先安装对应 Skill。

### 怎样提问效果更好？

| 关键信息 | 示例 |
| --- | --- |
| **拍摄目标** | “想拍有电影感的澳门夜间街景” |
| **实际设备** | “Z6II + 24–200mm，只带一支镜头” |
| **现场条件** | “晚上 8 点、手持、街上有人走动” |
| **遇到的问题** | “照片有些糊、背景太杂、霓虹灯过曝” |
| **希望得到的结果** | “给我一套拍摄参数起点，并解释怎么现场调整” |

不需要一次填写全部信息；如果你只是上传一张照片，Skill 也会先从画面本身展开分析，不会凭空推断照片的相机参数。

### 点评遵循的原则

- **先讲优点，再指出问题**：避免空泛夸奖，也不会为了挑错而挑错。
- **优先解决最影响观感的问题**：通常只强调最值得改进的 2–3 项。
- **区分“还能修”和“需要重拍”**：后期无法真正还原严重失焦或错过的决定性瞬间。
- **尊重个人风格**：纪实、自然、电影感、黑白等风格没有唯一正确答案。
- **诚实说明限制**：没有 EXIF 就不假装知道 ISO、快门或焦距；压缩预览图也不足以精准判断像素级锐度。

相关资料：[完整 Skill 说明](./photo-coach/SKILL.md) · [尼康器材档案](./photo-coach/references/gear-profile.md) · [场景拍摄指南](./photo-coach/references/shooting-playbooks.md) · [点评与后期指南](./photo-coach/references/critique-and-editing.md)。

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

### Photo Coach 使用示例

**示例 1｜上传照片，进行专业点评**

```text
使用 $photo-coach 点评我上传的这张照片。
请分析主体、构图、光线、色彩、背景和画面故事。
先告诉我最成功的一点，再按优先级列出 3 个改进建议。
区分哪些可以用后期修复，哪些需要下次重拍。
```

**示例 2｜澳门城市扫街，拍前准备**

```text
使用 $photo-coach 帮我准备一次澳门城市扫街。
参考 Nikon Z6II、24–200mm 和 50mm f/1.8 的候选组合，
以轻松旅行、城市记录为主，推荐镜头、焦段、参数起点、
对焦模式和 5 个具体的拍摄任务，并说明遇到弱光时如何调整。
```

**示例 3｜夜景人像参数指导**

```text
使用 $photo-coach 教我拍夜景人像。
场景：晚上、手持、有人走动，背景有霓虹灯。
请解释镜头选择、光圈、快门、Auto ISO、对焦和白平衡的取舍，
并告诉我如何避免人物虚焦、运动模糊和背景灯牌过曝。
```

**示例 4｜Lightroom 后期调色**

```text
使用 $photo-coach 帮我制定这张照片的 Lightroom 修图方案。
目标是自然、有层次的城市电影感，不要过度饱和。
请按裁剪、白平衡、基础曝光、局部蒙版、颜色和细节的顺序指导，
说明每一步为什么这样调整。没有原始数据时不要编造精确滑块值。
```

**示例 5｜一组照片选片与摄影成长**

```text
使用 $photo-coach 从这组旅行照片中帮我挑选 6 张。
我想做一套有故事感的摄影作品集。
请说明每张入选和淘汰的理由，安排叙事顺序，
并根据共同问题给我安排下一周的 3 个短时摄影练习。
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
├── analyze-research-paper/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── references/
│       ├── analysis-template.md
│       ├── experiment-audit.md
│       └── research-idea-lab.md
└── photo-coach/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        ├── gear-profile.md
        ├── shooting-playbooks.md
        └── critique-and-editing.md
```

## 反馈

如有使用问题或改进建议，欢迎通过 [Issues](https://github.com/mkbk11/personal-skills/issues) 反馈。描述具体场景、预期效果和实际表现，有助于不断完善技能。
