# 架构设计

## 概览

Financial-Services-CN 是 Anthropic 官方 [financial-services](https://github.com/anthropics) 插件包的中文分支。整体架构完全遵循 Anthropic 原项目的 **"two wrappers from one source"** 原则。

```
financial-services-cn/
├── plugins/
│   └── vertical-plugins/                   ← 技能源（唯一编辑入口）
│       ├── equity-research/
│       │   ├── .claude-plugin/plugin.json  (用户自补)
│       │   ├── commands/                    (用户自补，可复用 Anthropic 官方)
│       │   ├── hooks/                       (用户自补)
│       │   └── skills/                      ← 5 个 -cn 技能
│       │       ├── earnings-analysis-cn/
│       │       │   ├── SKILL.md
│       │       │   ├── references/
│       │       │   │   ├── workflow.md
│       │       │   │   ├── report-structure.md
│       │       │   │   └── best-practices.md
│       │       │   └── templates/
│       │       │       ├── cover_page.py
│       │       │       └── check_layout.py
│       │       ├── sector-overview-cn/
│       │       ├── initiating-coverage-cn/
│       │       ├── announcement-digest-cn/
│       │       └── macro-alert-cn/
│       ├── financial-analysis/skills/       ← 3 个 -cn 技能
│       ├── wealth-management/skills/        ← 1 个 -cn 技能
│       └── operations/skills/               ← 2 个 -cn 技能
├── scripts/                                ← 同步与校验脚本
└── docs/                                   ← 文档
```

## 核心架构原则

### 1. 技能共存（不替换英文）

CN 技能与英文技能**共存**于同一 vertical 的 `skills/` 目录下，通过 description 的中文触发关键词自然分流：

- 用户说 "Q3 earnings analysis Tesla" → 触发英文 `earnings-analysis`
- 用户说 "华明装备 2025 年报点评" → 触发 `earnings-analysis-cn`

**不需要**改 commands、hooks、`.mcp.json`，与 Anthropic 官方架构完全兼容。

### 2. 技能唯一源原则（two wrappers）

- `plugins/vertical-plugins/<vertical>/skills/<skill>/` 是技能**唯一编辑源**
- `plugins/agent-plugins/<agent>/skills/<skill>/` 是 `sync-agent-skills.py` **自动同步的副本**
- 编辑只改前者，跑脚本后后者自动更新

### 3. 工具化前置门（执行铁律）

对于 AI 容易"跑偏"的环节（如首页双栏排版、多 sheet Excel 生成、自检逻辑），强制通过 `templates/` 目录下的 **Python 工具脚本**生成，并以自检脚本作为**发布前置门**：

```
SKILL.md 阶段 4：
  Step 1: from cover_page import build_cover_page → 生成首页
  Step 2: python check_layout.py output.docx → 8 项自检
  Step 3: 返回码 0 才可继续；非 0 必须返工
```

已在 earnings-analysis-cn 验证有效。其他技能可按此模式扩展。

### 4. 数据层策略（v1 vs v2）

**v1（当前发布）**：
- SKILL.md 内约定数据源（巨潮、互动易、国家统计局、证监会等）
- Claude 通过 `WebFetch` 工具主动抓取
- 或用户粘贴公告 PDF / 文本

**v2（未来）**：
- 编写 MCP server：`tushare-mcp`、`cninfo-mcp`、`regulatory-mcp`
- 挂载至各 vertical 的 `.mcp.json` 自动可用
- compliance-watcher-cn 是 v1 即引入定时抓取的特例

### 5. 质量基线

每个 -cn skill 的 SKILL.md ≥ 400 行（compliance-watcher-cn ≥ 500），包含：

- 完整 YAML frontmatter（≥6 中文触发关键词 + 适用边界）
- 触发场景 / 严禁场景（明确不做什么）
- 核心执行要求（5-12 个本土化子节）
- 工作流（≥4 阶段）
- 关键术语规范化 + 禁止用语清单
- 输出产出物规范
- 关联资源 / 依赖 / 与其他 -cn 技能协同

## 技能间协同矩阵

11 个技能不是孤立的，互相会调用 / 协同：

```
                  earnings    sector    init-cov    comps    dcf    audit
                  ↑              ↑          ↑          ↑       ↑      ↑
公告精读 ─────────┘              │          │          │       │      │
宏观异动 ─────────────────────────┘          │          │       │      │
合同审查（独立）                              │          │       │      │
跨境合规（独立）                              │          │       │      │
法规追踪 → audit-xls-cn 双重质量门 ──────────┴──────────┴───────┴──────┘
```

详见 [USE_CASES.md](USE_CASES.md) 中 "协同流程示例"。

## 文件命名规范

| 类型 | 规范 |
| :--- | :--- |
| Skill 目录 | `<skill-name>-cn/` （必须 `-cn` 后缀） |
| 主提示词 | `SKILL.md` |
| 参考资源 | `references/workflow.md` / `report-structure.md` / `best-practices.md` |
| 工具脚本 | `templates/*.py` |
| 用户输出 | `[主体]_[代码]_[报告期]_[报告类型]_CN.docx/.xlsx/.md` |

## YAML frontmatter 规范

每个 SKILL.md 必须以以下格式开头：

```yaml
---
name: <skill-name>-cn
description: 一段较长的描述，含 6+ 中文触发关键词，明确适用范围与边界。例如：'A 股财报点评'、'巨潮公告'、... 适用范围：A 股 / CAS 准则；不适用纯港股 / 美股。
---
```

`name` 必须以 `-cn` 结尾；`description` 必须含 "适用范围" 和 "不适用" 两段。

## 提示词分层

每个 SKILL.md 内部的内容分层逻辑：

```
1. YAML frontmatter        — 触发与定位
2. # 一级标题               — 技能名称与简要
3. ## 触发场景 / 严禁场景    — 边界声明
4. ## 核心执行要求           — 本土化深度（最重要）
5. ## 工作流                — 步骤化指引
6. ## 关键术语规范化         — 输出一致性
7. ## 产出物规范             — 交付规范
8. ## 关联资源              — references/ 三件套指引
9. ## 依赖与配置             — 技术依赖
10. ## 与其他 CN 技能协同     — 横向集成
```

## 触发分流机制

Claude Skills 触发是基于 description 中关键词的模糊匹配。本项目所有 CN 技能采用以下策略避免误触发：

1. **强中文关键词**：description 含 6+ 个明确的中文术语
2. **适用边界声明**：明确写 "不适用纯港股 / 美股"
3. **触发场景列举**：在 SKILL.md 开头列举 5-7 个典型触发问句
4. **严禁场景列举**：列举 5+ 个应触发其他 skill 的场景

测试方法：用 5 个边界场景手工触发，确认 Claude 选对了 skill。

## 校验流程

每次提交前必跑：

```bash
python3 scripts/check.py
```

校验项：
- 所有 SKILL.md 的 YAML frontmatter 合法
- 所有 references/*.md 文件存在
- 所有 `<skill>-cn` 命名规范
- vertical-plugins 与 agent-plugins 同步状态

返回码 0 = 通过，非 0 = 阻断提交。

## 同步流程

```bash
python3 scripts/sync-agent-skills.py
```

将 `vertical-plugins/<vertical>/skills/<skill>/` 全量复制到所有 `agent-plugins/<agent>/skills/<skill>/` 位置（按 Anthropic 原架构）。

## 与 Anthropic 官方架构的兼容性

本仓库与 Anthropic 官方 financial-services 100% 架构兼容。具体表现：

- ✅ 目录结构完全一致
- ✅ SKILL.md / references / templates 规范一致
- ✅ marketplace.json / plugin.json 格式一致
- ✅ sync-agent-skills.py / check.py 复用同一脚本
- ✅ 触发分流不冲突

**结果**：本仓库可作为独立项目使用，也可直接合并到 Anthropic 官方仓库（详见 [INSTALL.md](../INSTALL.md) 安装方式 1）。

## 未来路线图

- **v1.1**（2026 Q3）：完善所有技能的 references/ 三件套
- **v1.2**（2026 Q4）：compliance-watcher-cn 规则库扩展至 100+ 条
- **v2.0**（2027 Q1）：MCP 数据层集成（tushare-mcp / cninfo-mcp / regulatory-mcp）
- **v2.5**（2027 Q2）：港股 / 中概股专用模板
- **v3.0**（2027 Q3）：跨境投资完整工具包
