# Financial-Services-CN

> **服务于散户与中小机构的中国金融 Claude Skills 工具包**

为 Anthropic 官方 [financial-services](https://github.com/anthropics) 插件构建的**中国版分支**。在原有插件骨架上叠加 11 个中文金融 Claude Skills，覆盖 A 股研究、估值、合规、宏观、跨境等大机构盲区场景。

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Made for Claude](https://img.shields.io/badge/Made_for-Claude-orange.svg)](https://www.anthropic.com)
[![Skills](https://img.shields.io/badge/Skills-11-green.svg)](#技能清单)

---

## 🎯 项目定位

**不是**与中信、中金、华泰等头部券商研究所竞争，而是**填补大机构不愿做、做不了、或商业模式不允许做的市场盲区**：

- **散户 / 个人投资者**：单客户产值低，机构服务门槛 100 万起
- **中小机构 / 中小券商资管**：自建研究 + 合规中后台年成本 >300 万
- **跨场景刚需小工具**：大机构内部脚本不会对外提供

我们用**开源 + Claude Skills**让普通投资者也能拥有"卖方研究员级别"的工具。

---

## 📦 11 个技能清单

### 股票研究 (equity-research)

| # | 技能 | 行数 | 用户痛点 |
| :-: | :--- | ---: | :--- |
| 1 | `earnings-analysis-cn` | 935 | 财报点评、业绩预告解读（含 A 股法定 8 类业绩预告 / 双栏首页版式工具 / 自检脚本前置门） |
| 2 | `sector-overview-cn` | 392 | 行业综述、产业链图谱（含申万一级 31 行业全表 / 5 个真实行业案例） |
| 3 | `initiating-coverage-cn` | 420 | 首次覆盖深度报告（含实控人 7 维画像 / 商业模式画布 A 股版） |
| 7 | `announcement-digest-cn` | 391 | 上市公司公告精读（A 股法定 11 类标签 / 噪音过滤 90% / 散户友好 6 段式摘要） |
| 8 | `macro-alert-cn` | 468 | 宏观异动监控（9 大指标 / 三重检测规则 / 4 类资产传导路径） |

### 财务分析 (financial-analysis)

| # | 技能 | 行数 | 用户痛点 |
| :-: | :--- | ---: | :--- |
| 4 | `comps-cn` | 471 | A 股可比公司估值（申万二级 30+ 行业代码 / openpyxl 完整代码骨架） |
| 5 | `dcf-cn` | 375 | A 股口径 DCF 估值（WACC 中国本土化参数 / 5 行业 FCFF 示例 / 10 大常见错误） |
| 6 | `audit-xls-cn` | 445 | 财务模型与研报质检（11 类 A 股地雷扫描 / 真实造假案例库 / 50+ 禁止用语） |

### 财富管理 (wealth-management)

| # | 技能 | 行数 | 用户痛点 |
| :-: | :--- | ---: | :--- |
| 9 | `contract-devil-clause-cn` | 438 | 基金 / 信托合同魔鬼条款审查（8 大审查维度 / 中基协法规对照 / 白话翻译） |

### 运营 / 合规 (operations)

| # | 技能 | 行数 | 用户痛点 |
| :-: | :--- | ---: | :--- |
| 10 | `cross-border-compliance-cn` | 459 | 跨境监管函件翻译（7 大监管来源 SEC/FCA/SFC / 4 档紧急度 / 30+ 法律术语对照） |
| 11 | `compliance-watcher-cn` | 592 | 法规追踪 + 业务合规审查双轨工具（每日抓取 5+ 监管来源 / A/B/C/D 合规评分） |

**累计 5,386 行 SKILL.md 内容**，每个技能均含完整 YAML frontmatter、触发场景、严禁场景、核心执行要求、工作流、术语规范、产出物规范、协同设计。

---

## 🚀 快速上手

### 前置条件

- [Claude Code](https://claude.com/claude-code) 已安装并能正常运行
- 已 clone Anthropic 官方 [financial-services](https://github.com/anthropics) 插件包到本地

### 安装方式 1：合并到现有 Anthropic 插件包（推荐）

```bash
# 1. 进入 Anthropic financial-services 仓库目录
cd path/to/financial-services

# 2. 把本仓库 plugins/ 目录合并进去
cp -r path/to/financial-services-cn/plugins/* plugins/

# 3. 同步到 agent-plugins 副本
python3 scripts/sync-agent-skills.py

# 4. 校验
python3 scripts/check.py

# 5. 在 Claude Code 中加载 marketplace
/plugin marketplace add path/to/financial-services
/plugin install equity-research@fsi-local
/plugin install financial-analysis@fsi-local
# ... 装其他需要的 plugin
```

### 安装方式 2：独立使用（不依赖 Anthropic 官方仓库）

```bash
# 1. clone 本仓库
git clone https://github.com/yourname/financial-services-cn.git

# 2. 在 Claude Code 中添加 marketplace（需自己写 marketplace.json）
/plugin marketplace add path/to/financial-services-cn
```

详细安装指南见 [INSTALL.md](INSTALL.md)。

---

## 💡 典型使用场景

### 场景 1：散户读懂公告（announcement-digest-cn）

```
我：今天华明装备发布了什么公告？

Claude（自动触发 announcement-digest-cn）：
📊 华明装备(002270.SZ) 2026-05-29 公告精读

【标签】重大合同 🟢 利好
【核心数据】中标特高压换流变分接开关订单 X 亿元（占上年营收 Y%）
【影响判断】对全年盈利贡献约 +X%，强化"特高压国产替代"投资逻辑
【原文出处】巨潮：[公告链接]

不构成投资建议。
```

### 场景 2：散户审查私募合同（contract-devil-clause-cn）

```
我：[上传 50 页私募基金合同 PDF] 帮我审查

Claude（自动触发 contract-devil-clause-cn）：
8 大维度审查结果：
🔴 严重不利 2 项（无高水位线 / 业绩报酬基准 0%）
🟡 风险 3 项（锁定期 24 月 / 信息披露季度 / 仲裁地偏远）
✅ 标准 12 项

详见审查报告 + 建议协商点...

⚠️ 仅供参考，不构成法律意见。复杂场景建议咨询持牌律师。
```

### 场景 3：研究员快速估值（comps-cn + dcf-cn）

```
我：帮我对宁德时代做相对估值 + DCF 双锚交叉验证

Claude（依次触发 comps-cn + dcf-cn）：
1. comps-cn 输出可比公司 Excel（5 sheet 标准格式）
2. dcf-cn 输出 DCF Excel（6 sheet 标准格式）
3. 自动给出双锚目标价对比 + 偏离度判断
```

---

## 🛡️ 合规与免责

每个技能均内置 A 股监管合规设计：

- ✅ 强制免责声明
- ✅ 禁止买卖建议（50+ 禁用语清单）
- ✅ 数据来源标注规范（巨潮 / 监管原文链接）
- ✅ 中证协执业规范对齐
- ✅ 保密原则（合同 / 监管函等敏感材料不存储）

**本工具不构成投资建议 / 法律意见 / 合规意见**。复杂场景请咨询持牌专业人士。

---

## 🤝 贡献

欢迎贡献：

1. **新技能提案**：在 Issues 提出新场景需求
2. **完善 references 三件套**：5 个老骨架的 `references/` 仍待填充
3. **完善 templates/**：compliance-watcher-cn 的规则库与抓取脚本
4. **真实案例验证**：用真实 A 股标的跑通技能并反馈

详见 [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)。

---

## 📚 文档

- [INSTALL.md](INSTALL.md) — 详细安装指南
- [docs/PRD.md](docs/PRD.md) — 产品需求文档 v4.0
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — 架构设计
- [docs/USE_CASES.md](docs/USE_CASES.md) — 11 个典型使用场景
- [CHANGELOG.md](CHANGELOG.md) — 版本历史

---

## 📜 许可

Apache License 2.0 - 详见 [LICENSE](LICENSE)

兼容 Anthropic 官方 financial-services 插件包的许可。

---

## 🌟 致谢

- Anthropic 开源的 [financial-services](https://github.com/anthropics) 插件包提供基础架构
- Claude / Claude Code 团队
- 中国金融市场公开披露体系（巨潮资讯网、证监会、中证协、中基协等）

---

## 📮 联系

- Issues: [GitHub Issues](https://github.com/yourname/financial-services-cn/issues)
- Discussions: [GitHub Discussions](https://github.com/yourname/financial-services-cn/discussions)

---

**Made with ❤️ for 中国散户投资者 & 中小机构**
