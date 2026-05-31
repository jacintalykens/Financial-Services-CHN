# DeepSeek Agent 交接文档（项目调试专用）

> **本文件是给"接入 DeepSeek 的 Agent"的冷启动交接说明。**
> 阅读对象：另一台机器上、基于 DeepSeek 模型运行的 AI Agent（无本对话历史）。
> 目的：让该 Agent 在零上下文情况下，完整理解项目 → 快速加载全部 skills → 进入调试迭代。
>
> **请 DeepSeek Agent 先完整读完本文档，再开始任何操作。**

---

## 第 0 节：30 秒理解这个项目

**项目名**：Financial-Services-CN（中文金融 Claude Skills 工具包）

**一句话**：把 Anthropic 官方开源的 `financial-services` 金融插件（美股口径）改造成**中国 A 股 / 中国监管口径**的版本，服务**散户与中小机构**这个被大机构忽略的市场。

**产出形态**：11 个 "Skill"。每个 Skill 本质是 **一份结构化的超长中文提示词（SKILL.md）+ 配套参考文档（references/）+ 可选工具脚本（templates/）**。

**核心理念**：
- 不与中信/中金等头部券商竞争，专攻"大机构不愿做、做不了、商业上不划算"的长尾刚需
- 所有 Skill 用 A 股 / CAS 会计准则 / 中证协规范，**不用**美股 GAAP / FactSet
- 全部基于公开数据（巨潮、证监会、国家统计局），可解释、可溯源、合规

**当前状态**：11 个 SKILL.md 全部写完（共 5,386 行），已通过校验。references 三件套部分完成、部分为占位待填。

---

## 第 1 节：关键概念澄清（DeepSeek 必读）

### 1.1 什么是 "Skill"？

"Skill" 是 Anthropic Claude 的一种能力封装机制，格式为：

```
<skill-name>-cn/
├── SKILL.md          # 主文件：YAML 头 + 超长中文提示词（核心）
├── references/       # 参考文档：workflow / report-structure / best-practices
│   ├── workflow.md
│   ├── report-structure.md
│   └── best-practices.md
└── templates/        # 可选：Python 工具脚本（如 Excel/Word 生成器）
    └── *.py
```

`SKILL.md` 开头是 YAML frontmatter：

```yaml
---
name: earnings-analysis-cn
description: 一段长描述，含触发关键词和适用边界。
---
```

`name` 必须以 `-cn` 结尾；`description` 决定何时该激活这个 Skill。

### 1.2 ⚠️ DeepSeek 没有原生 Skills 机制 —— 这是最重要的一点

Claude Code 有 `/plugin install` 命令自动加载 Skills。**DeepSeek 没有这个机制。** 所以对 DeepSeek Agent 而言，"安装/使用一个 Skill" 实际是以下三种方式之一（见第 3 节详解）：

1. **手动注入**：把对应 `SKILL.md` 全文贴进 system prompt 或对话上下文
2. **RAG 检索**：把 11 个 SKILL.md 切块入向量库，按用户问题检索最相关的 Skill 提示词
3. **路由 + 注入**：先用 `description` 字段做关键词路由，命中后注入完整 SKILL.md

**本质**：Skill = 提示词工程产物。DeepSeek 调试这个项目，就是调试"这些中文提示词在 DeepSeek 上能否产出合格的中国金融分析"。

---

## 第 2 节：目录结构地图

```
financial-services-cn/
├── README.md                  # 项目对外介绍
├── DEEPSEEK_HANDOFF.md         # ← 本文件
├── INSTALL.md                  # Claude Code 安装指南（DeepSeek 看第 3 节即可）
├── CHANGELOG.md                # 版本历史
├── LICENSE                     # Apache 2.0
├── .claude-plugin/
│   └── marketplace.json        # Claude marketplace 配置（DeepSeek 不用）
├── docs/
│   ├── PRD.md                  # ★ 产品需求文档 v4.0（最完整的项目说明，必读）
│   ├── ARCHITECTURE.md         # 架构设计
│   ├── USE_CASES.md            # 11 个使用场景 + 协同流程
│   └── CONTRIBUTING.md         # 贡献规范
├── scripts/
│   ├── check.py                # ★ 校验脚本（校验 11 个 Skill 是否合规）
│   └── sync-agent-skills.py    # 同步脚本（Claude 架构用，DeepSeek 可忽略）
└── plugins/vertical-plugins/
    ├── equity-research/skills/         # 股票研究（5 个）
    │   ├── earnings-analysis-cn/       # 财报点评（935 行，质量基线 ★）
    │   ├── sector-overview-cn/         # 行业综述（392 行）
    │   ├── initiating-coverage-cn/     # 首次覆盖（420 行）
    │   ├── announcement-digest-cn/     # 公告精读（391 行）
    │   └── macro-alert-cn/             # 宏观异动（468 行）
    ├── financial-analysis/skills/      # 财务分析（3 个）
    │   ├── comps-cn/                   # 可比估值（471 行）
    │   ├── dcf-cn/                     # DCF 估值（375 行）
    │   └── audit-xls-cn/               # 模型/研报质检（445 行）
    ├── wealth-management/skills/       # 财富管理（1 个）
    │   └── contract-devil-clause-cn/   # 合同魔鬼条款审查（438 行）
    └── operations/skills/              # 运营合规（2 个）
        ├── cross-border-compliance-cn/ # 跨境监管翻译（459 行）
        └── compliance-watcher-cn/      # 法规追踪+合规审查（592 行）
```

**DeepSeek 上手优先级**：先读 `docs/PRD.md`（全局），再读 `earnings-analysis-cn/SKILL.md`（质量基线 + 最完整的范例），其余 10 个 Skill 同构。

---

## 第 3 节：11 个 Skill 清单（含触发关键词 + 路由表）

DeepSeek 做"路由 + 注入"时用这张表：用户输入命中关键词 → 加载对应 SKILL.md。

| # | Skill | 触发关键词（节选） | 输入 | 输出 |
| :-: | :--- | :--- | :--- | :--- |
| 1 | earnings-analysis-cn | 财报点评/业绩点评/季报/年报/业绩预告 | 公司代码+财报期 | DOCX 业绩点评研报 |
| 2 | sector-overview-cn | 行业研究/产业链/行业综述/申万行业 | 行业名 | DOCX 行业报告 |
| 3 | initiating-coverage-cn | 首次覆盖/深度报告/公司深度 | 公司代码 | DOCX 30-50 页深度报告 |
| 4 | comps-cn | 可比公司/估值对标/PE-PB对比 | 公司代码 | XLSX 可比估值表 |
| 5 | dcf-cn | DCF/内在价值/现金流折现/WACC | 公司代码 | XLSX DCF 模型 |
| 6 | audit-xls-cn | 财报审计/研报审核/模型自检/勾稽核查 | 研报或 Excel | MD 审计报告 |
| 7 | announcement-digest-cn | 公告精读/公告解读/减持公告/利好利空 | 公司/日期范围 | MD 公告摘要 |
| 8 | macro-alert-cn | 宏观数据/PMI/CPI/社融/宏观异动 | 宏观指标 | MD 异动报告 |
| 9 | contract-devil-clause-cn | 基金合同审查/信托合同/魔鬼条款/理财说明书 | 合同 PDF/文本 | MD 审查报告 |
| 10 | cross-border-compliance-cn | 跨境监管/SEC/FCA/监管函翻译/出海合规 | 监管函英文 | MD 双语审查报告 |
| 11 | compliance-watcher-cn | 法规追踪/监管动态/合规自查/产品合规审查 | 业务材料/订阅 | MD 法规日报或合规报告 |

---

## 第 4 节：DeepSeek 如何"安装/加载"这些 Skills

### 方式 A：单 Skill 手动注入（最简单，先用这个跑通）

```
1. 用户说"帮我点评华明装备 2025 年报"
2. DeepSeek Agent 按第 3 节路由表识别 → earnings-analysis-cn
3. 读取 plugins/vertical-plugins/equity-research/skills/earnings-analysis-cn/SKILL.md 全文
4. 把 SKILL.md 全文作为 system prompt 注入
5. 同时注入该 Skill 的 references/*.md（如上下文窗口够大）
6. DeepSeek 按提示词产出报告
```

**伪代码**（Python）：

```python
import os, re

SKILLS_ROOT = "plugins/vertical-plugins"

def load_skill(skill_name: str) -> str:
    """加载指定 skill 的完整提示词（SKILL.md + references）"""
    for vertical in os.listdir(SKILLS_ROOT):
        skill_dir = os.path.join(SKILLS_ROOT, vertical, "skills", skill_name)
        skill_md = os.path.join(skill_dir, "SKILL.md")
        if os.path.exists(skill_md):
            parts = [open(skill_md, encoding="utf-8").read()]
            ref_dir = os.path.join(skill_dir, "references")
            if os.path.isdir(ref_dir):
                for ref in sorted(os.listdir(ref_dir)):
                    if ref.endswith(".md"):
                        parts.append(f"\n\n# 参考文档：{ref}\n")
                        parts.append(open(os.path.join(ref_dir, ref), encoding="utf-8").read())
            return "\n".join(parts)
    raise FileNotFoundError(f"未找到 skill: {skill_name}")

# 注入为 system prompt
system_prompt = load_skill("earnings-analysis-cn")
```

### 方式 B：关键词路由 + 注入（推荐生产用）

```python
import os, re, yaml

def build_router():
    """扫描全部 SKILL.md 的 YAML frontmatter，建立 name->description 路由表"""
    router = {}
    for root, _, files in os.walk("plugins/vertical-plugins"):
        if "SKILL.md" in files and root.endswith("-cn"):
            content = open(os.path.join(root, "SKILL.md"), encoding="utf-8").read()
            m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if m:
                fm = yaml.safe_load(m.group(1))
                router[fm["name"]] = {
                    "description": fm["description"],
                    "path": os.path.join(root, "SKILL.md"),
                }
    return router

# 路由：把 router 的 name+description 喂给 DeepSeek，让它选 skill
# 然后用方式 A 的 load_skill 注入选中的 skill
```

### 方式 C：RAG 检索（上下文窗口受限时）

把 11 个 SKILL.md 按章节切块（## 二级标题切分），入向量库；用户问题检索 Top-K 块注入。**缺点**：可能丢失 SKILL.md 的整体结构，质量不如全文注入。**仅在上下文窗口 <32K 时考虑。**

### ⚠️ DeepSeek 上下文窗口注意

- earnings-analysis-cn 的 SKILL.md 是 935 行（约 25K-30K tokens）
- 加 references 三件套可能超过 64K tokens
- **建议**：DeepSeek 若窗口够大（128K+），直接全文注入 SKILL.md + references；窗口小则只注入 SKILL.md 主文件，references 按需检索

---

## 第 5 节：怎么调试（核心）

### 5.1 调试目标

判断"这些为 Claude 写的中文提示词，在 DeepSeek 上能否产出合格的中国金融分析"。可能需要针对 DeepSeek 的特性微调提示词。

### 5.2 标准调试流程

```
对每个 Skill：
1. 选 1 个真实 A 股案例（如华明装备 002270.SZ）
2. 准备真实数据（公告 PDF / 同花顺数据，禁止编造）
3. 注入 SKILL.md → 让 DeepSeek 产出
4. 用第 6 节验收清单逐项核对输出
5. 不合格 → 定位是"提示词问题"还是"DeepSeek 能力问题"
   - 提示词问题 → 改 SKILL.md
   - DeepSeek 能力问题 → 加更强约束 / 拆分步骤 / 加示例
6. 改完重测，直到通过验收
```

### 5.3 校验脚本

```bash
# 校验 11 个 Skill 的结构合规性（YAML 头、命名、行数、references）
python3 scripts/check.py
# 期望输出：✅ 全部 11 个 -cn 技能通过校验
```

`check.py` 只校验**结构**，不校验**输出质量**。输出质量靠第 6 节人工验收。

### 5.4 DeepSeek 调试常见问题预判

| 现象 | 可能原因 | 调试方向 |
| :--- | :--- | :--- |
| 输出编造数据 | DeepSeek 未严格遵守"禁止编造"约束 | 在注入提示词最前面加强制声明："只用我提供的数据，缺失就标注【待补】" |
| 输出格式跑偏（如该出表格出段落） | DeepSeek 对长提示词后段遵守度下降 | 把关键格式要求前移 / 拆成多轮对话 |
| 触发了错误的 Skill | 路由关键词冲突 | 优化第 3 节路由表 / 用 description 做语义路由 |
| Excel/Word 生成失败 | DeepSeek 不能直接产二进制文件 | 让 DeepSeek 产出结构化数据（JSON/Markdown 表格）+ 用 templates/ 的 Python 脚本本地生成文件 |
| 合规话术违规（出现"建议买入"） | DeepSeek 未遵守禁用语清单 | 把禁用语清单前移 + 输出后用 audit-xls-cn 二次扫描 |

### 5.5 工具脚本调试（templates/）

`earnings-analysis-cn/templates/` 有两个已验证的 Python 脚本：
- `cover_page.py`：生成研报首页双栏版式 DOCX
- `check_layout.py`：校验生成的 DOCX 首页 8 项视觉要素（前置门）

调试模式：DeepSeek 产出结构化数据 → 调 `cover_page.py` 生成 DOCX → 跑 `check_layout.py` 自检 → 不通过则返工。这是"AI 产数据、脚本产文件"的分工，绕开 DeepSeek 不能直接产二进制文件的限制。

```bash
# 测试首页生成（用内置 SAMPLE_DATA）
cd plugins/vertical-plugins/equity-research/skills/earnings-analysis-cn/templates
python3 cover_page.py 测试首页.docx
python3 check_layout.py 测试首页.docx   # 期望 8/8 通过
```

依赖：`pip install python-docx openpyxl`

---

## 第 6 节：输出验收清单（质量门）

每个 Skill 的输出必须满足以下通用项 + 专项。

### 6.1 通用验收（全部 11 个 Skill）

- [ ] **零编造**：所有数字都来自用户提供的真实数据，缺失项标注【待补：xxx】
- [ ] **数据溯源**：每个关键数字附来源（巨潮/同花顺/国家统计局）+ 披露日
- [ ] **合规话术**：无"建议买入/卖出/稳赚/保本/必涨"等禁用语
- [ ] **免责声明**：报告含"不构成投资建议/法律意见"声明
- [ ] **A 股口径**：用 CAS 准则 / 归母净利润 / 扣非 / 申万行业，不用美股术语
- [ ] **评级规范**（如适用）：用买入/增持/中性/减持/卖出 5 档，相对沪深 300

### 6.2 重点 Skill 专项验收

**earnings-analysis-cn（财报点评）**：
- [ ] 三档利润口径（净利润/归母/扣非）齐全
- [ ] 业绩预告按 A 股法定 8 类分类（预增/略增/续盈/扭亏/首亏/续亏/预减/略减）
- [ ] A 股地雷扫描（商誉/质押/减持/合同负债/非经常占比）
- [ ] 首页双栏版式（评级框红底 + 财务摘要三线表）
- [ ] DOCX 含页眉"请务必阅读..."+ 页脚页码

**comps-cn / dcf-cn（估值）**：
- [ ] 可比公司剔除 ST/*ST/新股次新股
- [ ] DCF 用中国国债 Rf、沪深 300 ERP（不用美债/美股）
- [ ] 永续增长率 g < Rf 且在 1.5-3.5%
- [ ] 一致预期标注取数日期

**compliance-watcher-cn（法规）**：
- [ ] 引用真实监管法规原文 + 链接
- [ ] 合规评分 A/B/C/D 有明确依据
- [ ] 不预测监管处罚具体结果

详细验收标准见各 Skill 的 `references/best-practices.md`（部分为占位待填）。

---

## 第 7 节：绝对不能违反的红线（合规铁律）

DeepSeek Agent 在调试和产出时**必须**遵守，违反则输出作废：

1. ❌ **禁止编造金融数据**——股价、财务、一致预期、监管法规，全部需真实来源
2. ❌ **禁止给买卖建议**——评级仅作"分析结论"，不构成操作指引
3. ❌ **禁止伪造分析师身份**——不编造姓名、SAC 执业编号、研报历史
4. ❌ **禁止预测货币政策/监管处罚具体结果**——只做情景推演
5. ❌ **禁止替用户向监管机构提交文件 / 声称具法律效力**
6. ✅ **必须标注数据来源 + 披露日**
7. ✅ **必须含免责声明**
8. ✅ **复杂场景必须建议咨询持牌律师/投资顾问**

---

## 第 8 节：当前进度与待办（接力点）

### 已完成
- 11 个 SKILL.md 全部写完（5,386 行），check.py 通过
- earnings-analysis-cn 是质量基线（935 行 + 完整 references + 2 个验证过的 templates 脚本）
- earnings-analysis-cn 已用华明装备真实数据端到端跑通（产出过真实研报）

### 待办（DeepSeek 可接力）
- [ ] 5 个新技能（announcement-digest / macro-alert / contract-devil-clause / cross-border-compliance / compliance-watcher）的 references/ 三件套仍是占位，需填充实际内容（≥200 行/篇）
- [ ] 5 个老骨架（sector-overview / initiating-coverage / comps / dcf / audit-xls）的 references/ 需补全
- [ ] comps-cn / dcf-cn 的 templates/ Excel 生成脚本未写
- [ ] compliance-watcher-cn 的 templates/（规则库 YAML + 抓取脚本）未写
- [ ] 每个 Skill 需 ≥3 个真实 A 股案例端到端验证
- [ ] 计划新增 7 个 Skill（选股/三表建模/催化剂日历/财报前瞻/家庭理财/创业BP/单位经济），详见 PRD

### DeepSeek 优先做什么？
建议从 **用真实案例验证现有 11 个 Skill 在 DeepSeek 上的输出质量** 开始——这是判断"提示词是否需要针对 DeepSeek 微调"的最快路径。先跑 earnings-analysis-cn（最成熟），再逐个测其余。

---

## 第 9 节：快速自检命令清单

```bash
# 0. 安装依赖
pip install python-docx openpyxl pyyaml

# 1. 结构校验（应输出 11 个 Skill 全通过）
python3 scripts/check.py

# 2. 测试 templates 工具脚本
cd plugins/vertical-plugins/equity-research/skills/earnings-analysis-cn/templates
python3 cover_page.py 测试.docx && python3 check_layout.py 测试.docx
cd -

# 3. 统计项目规模
find plugins -name SKILL.md | wc -l            # 应为 11
find plugins -name SKILL.md -exec wc -l {} +    # 各 Skill 行数

# 4. 列出全部 Skill 的 description（建路由表用）
grep -A1 "^description:" plugins/vertical-plugins/*/skills/*-cn/SKILL.md
```

---

## 第 10 节：给 DeepSeek Agent 的开场指令模板

把下面这段作为 DeepSeek 的初始 system prompt，让它进入正确角色：

```
你是 Financial-Services-CN 项目的调试助手。这是一个把 Anthropic 金融插件
中文化、服务中国散户与中小机构的开源项目，包含 11 个金融分析 Skill。

你的任务：
1. 先读 DEEPSEEK_HANDOFF.md（本交接文档）和 docs/PRD.md 理解项目全貌
2. 按"方式 A/B"加载用户需要的 Skill（即读取对应 SKILL.md 全文作为你的工作提示词）
3. 严格遵守第 7 节的合规红线（禁编造、禁买卖建议、必溯源、必免责）
4. 输出后用第 6 节验收清单自查
5. 发现提示词在你（DeepSeek）上效果不佳时，定位原因并提出 SKILL.md 修改建议

铁律：所有金融数据必须真实，缺失就标注【待补】，绝不编造。
所有输出用 A 股 / CAS 准则 / 中证协规范口径。
```

---

**文档版本**：v1.0（2026-05）
**配套必读**：`docs/PRD.md`（项目全貌）、`earnings-analysis-cn/SKILL.md`（质量基线范例）
**遇到不理解的概念**：优先查 `docs/ARCHITECTURE.md` 和 `docs/USE_CASES.md`
