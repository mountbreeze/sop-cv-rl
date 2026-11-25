# SOP · CV · RL — Evidence-first Admissions Writing Skill

> 英美港新硕士、商学院及研究型项目申请材料的可复用写作工作流。由项目「PM机构文书」中的多轮申请写作、修改反馈、Master Prompt 与匿名化案例提炼。

**快速入口：阅读 [SKILL.md](SKILL.md)。** 它是给 AI 写作助手/顾问使用的总工作流；具体规范按需加载 `references/`。

## 适用任务

- **Story Mining**：从简历、成绩单、实习/科研素材与访谈记录，挖掘可核实、有方法变化的故事。
- **SOP / PS / Essays**：按学校官网与题目、字符/词数、项目偏好及职业方向定制。
- **CV / Resume**：英文商业/金融/研究型简历；动词、任务颗粒度、量化证据与版面。
- **RL / LOR**：教授、研究导师、实习主管视角独立写作；区分推荐人的证据和声音。
- **Cross-document QA**：文书/简历/推荐信/申请表口径对齐、事实核验、AI-style audit 与长度校验。
- **Interview**：将同一事实库转成 1 分钟表达、讨论题与 follow-up 问答。

## 文件地图

| 文件 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | 总路由、不可违反的事实标准、流程与交付 |
| [references/01-intake-and-facts.md](references/01-intake-and-facts.md) | 素材接收、事实台账、授权与矛盾处理 |
| [references/02-story-mining.md](references/02-story-mining.md) | 学生画像、6–8 个故事、冲突、方法升级 |
| [references/03-sop-ps-essays.md](references/03-sop-ps-essays.md) | 文书框架、开头、经历、学术、职业规划、语言风格 |
| [references/04-cv-resume.md](references/04-cv-resume.md) | CV 结构、实习 bullet、量化与学生身份边界 |
| [references/05-recommendation-letters.md](references/05-recommendation-letters.md) | 推荐信素材、推荐人视角与去模板化 |
| [references/06-program-research.md](references/06-program-research.md) | 官网调研、题目拆解、字数/字符合规 |
| [references/07-quality-assurance.md](references/07-quality-assurance.md) | 七道质量关、交叉文档一致性、红线 |
| [references/08-program-archetypes.md](references/08-program-archetypes.md) | Finance/Econ/AI/Management/Oxford/KCL/港新等定制策略 |
| [references/09-casebook.md](references/09-casebook.md) | 匿名案例与文书修改复盘 |
| [references/10-interview.md](references/10-interview.md) | 面试与故事复用 |
| [templates/intake-brief.md](templates/intake-brief.md) | 每名新学生的输入模板 |
| [templates/story-card.md](templates/story-card.md) | 故事卡/事实确认模板 |
| [templates/program-matrix.md](templates/program-matrix.md) | 多项目要求矩阵 |
| [templates/rl-evidence.md](templates/rl-evidence.md) | 按推荐人收集可见证据 |
| [scripts/check_limits.py](scripts/check_limits.py) | 文书字符/词数、CV bullet 统计 |

## 一次完整使用

1. 建立学生独立工作空间，输入真实资料并建立 `Evidence Ledger`。
2. 先做 Student Profile + Story Portfolio；不要直接从 CV 生出未经验证的长文。
3. 为每个项目单独建立官网核查记录和 essay-question matrix。
4. 执行文书、简历或推荐信相应子模块。
5. 使用质检清单与本地脚本检查；输出可编辑终稿及待确认项。
6. 原始学生材料、私人联系方式、推荐人签名、真实信件与未经授权的案例 **不要提交到公开仓库**。

## 事实与保密边界

这里存储的是**方法论和去标识化的示例**，不是学生个人档案。案例仅示范写作策略，不意味着这些情节适用于新学生，也不是可直接宣称的个人事实；对新申请者必须重新核验来源。所有历史学校要求只能作为「题型样例」，提交前以该申请季官方网站及网申为准。与推荐人相关的草稿只供实际推荐人审阅、认可并提交。

## 内容来源说明

综合项目中多轮 SOP/PS 修改、金融英文简历重写、研究助理与课程推荐信、商科 Master Prompt、Story Mining Master Prompt、学校题目与面试准备形成。仓库不会公开用户聊天原文、学生全名/联系方式、个人档案或未经同意的第三方文书。更新时优先积累**可迁移规则、反例、审核机制**，而不是累积学生隐私。
