# 版本历史

本文档遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/) 规范，版本号遵循 [SemVer](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### 计划中
- 完善 5 个老骨架（sector-overview-cn / initiating-coverage-cn / comps-cn / dcf-cn / audit-xls-cn）的 `references/` 三件套
- compliance-watcher-cn 的 `templates/` 完整实现（规则库 + 抓取脚本 + 匹配引擎）
- 5 个新技能（announcement-digest-cn 等）的 `references/` 三件套
- tushare-mcp / cninfo-mcp / regulatory-mcp 等 MCP 集成

## [1.0.0] - 2026-07-31（计划）

### 新增（首次发布）

#### 股票研究（equity-research，5 个技能）
- **earnings-analysis-cn** (935 行)
  - A 股财报点评工具
  - 含 A 股法定 8 类业绩预告分类
  - 首页双栏版式工具（`templates/cover_page.py`）+ 8 项自检脚本前置门
  - 三档利润口径（净利润 / 归母 / 扣非）
  - 5 档 A 股标准评级
  - 11 类 A 股地雷扫描
  - 6 种估值方法适配

- **sector-overview-cn** (392 行)
  - A 股行业综述工具
  - 申万一级 31 行业代码全表
  - 5 个真实行业案例（新能源车 / 光伏 / CXO / 半导体 / 特高压）
  - 政策事件时间线模板
  - 候选标的卡片标准格式

- **initiating-coverage-cn** (420 行)
  - A 股首次覆盖深度报告工具
  - 实控人 7 维深度调查
  - 商业模式画布 A 股版（9 格）
  - 30-50 页章节模板
  - 5 个真实首次覆盖案例

- **announcement-digest-cn** (391 行)
  - A 股公告精读工具
  - A 股法定 11 类公告标签
  - 智能筛选规则（剔除 90% 模板化噪音）
  - 6 段式 ≤200 字摘要标准
  - 关联交叉验证（同议题多公告合并）

- **macro-alert-cn** (468 行)
  - 中国宏观异动监控工具
  - 9 大核心指标（PMI/CPI/PPI/社融/M1M2/工业增加值/固投/社零/进出口）
  - 三重异动检测规则
  - 4 维驱动因素分析
  - 4 类资产传导路径（股/债/商品/汇率）

#### 财务分析（financial-analysis，3 个技能）
- **comps-cn** (471 行)
  - A 股可比公司估值
  - 申万二级 30+ 行业代码典型表
  - 行业-估值方法映射详表
  - openpyxl 150 行完整代码骨架
  - 5 sheet 标准输出（Cover / Assumptions / RawData / ValuationMatrix / Stats）

- **dcf-cn** (375 行)
  - A 股口径 DCF 估值
  - WACC 中国本土化参数实数范例
  - 5 个典型行业 FCFF 测算
  - 10 大 A 股 DCF 常见错误
  - 何时不用 DCF 详表

- **audit-xls-cn** (445 行)
  - 财务模型与研报质检
  - CAS 准则三表勾稽规则
  - 11 类 A 股地雷扫描详细规则
  - 50+ 禁止用语清单
  - 真实造假案例库（康得新 / 康美 / 瑞幸 / 獐子岛）

#### 财富管理（wealth-management，1 个技能）
- **contract-devil-clause-cn** (438 行)
  - 中国资管合同魔鬼条款审查
  - 8 大审查维度（费用 / 赎回 / 投资范围 / 关联交易 / 信披 / 变更终止 / 不可抗力 / 争议解决）
  - 中基协 / 资管新规 / 信托法对照
  - 白话翻译 + 协商建议
  - 保密原则（不存储用户合同）

#### 运营 / 合规（operations，2 个技能）
- **cross-border-compliance-cn** (459 行)
  - 跨境监管函件翻译
  - 7 大监管来源（SEC / OFAC / CFIUS / FCA / SFC / MAS / ESMA）
  - 4 档紧急度判定
  - 30+ 法律术语对照
  - 行业聚焦：金融 / TMT / 新能源

- **compliance-watcher-cn** (592 行) ⭐ 双轨制
  - 法规追踪 + 业务合规审查
  - 5+ 监管来源每日抓取
  - YAML 规则库结构
  - A/B/C/D 合规评分体系
  - MVP 期重点 2 场景：研报合规 + 资管产品发行（30+ 规则）

### 累计
- 11 个 SKILL.md 文件，共 **5,386 行**
- 覆盖 4 个 vertical：equity-research / financial-analysis / wealth-management / operations
- 全部基于 Apache License 2.0 开源

### 工具脚本
- `templates/cover_page.py`（earnings-analysis-cn 首页双栏生成器，验证可用）
- `templates/check_layout.py`（8 项视觉验收前置门，验证可用）

---

## [0.x.0] - 开发期版本

### [0.4.0] - 2026-05-29
- 新增 5 个 SKILL.md（announcement-digest / macro-alert / contract-devil-clause / cross-border-compliance / compliance-watcher）
- 老骨架升级：sector-overview / initiating-coverage / comps / dcf / audit-xls 全部添加中国本土化深度内容

### [0.3.0] - 2026-05-29
- earnings-analysis-cn 升级为质量基线（935 行）
- 首页双栏版式工具化（templates/cover_page.py + check_layout.py）
- PRD v4.0 定稿

### [0.2.0] - 2026-05-29
- 5 个老骨架就位（sector-overview / initiating-coverage / comps / dcf / audit-xls，各 ~250 行）

### [0.1.0] - 2026-05-25
- earnings-analysis-cn 初版完成
- 项目架构对齐 Anthropic financial-services 标准结构

---

[Unreleased]: https://github.com/yourname/financial-services-cn/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/yourname/financial-services-cn/releases/tag/v1.0.0
