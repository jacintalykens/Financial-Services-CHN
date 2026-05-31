# 贡献指南

欢迎为 Financial-Services-CN 贡献！本项目欢迎以下类型贡献：

## 贡献类型

### 1. 新技能提案（Highest Impact）

如果你发现散户 / 中小机构的某个真实痛点尚未被覆盖，欢迎提案新技能。

**新技能必须满足**：
- ✅ 服务于"大机构盲区"（散户 / 中小机构 / 跨场景小工具）
- ✅ 中国市场口径
- ✅ 与现有 11 个技能无重复
- ✅ 可解释 + 合规可控

**提案流程**：
1. 在 Issues 开 "[新技能提案]" 标签
2. 描述：用户痛点、为什么大机构不做、技能名（`<name>-cn`）
3. 等待 maintainer 评审

### 2. 完善 references/ 三件套

5 个老骨架的 `references/` 仍是 TODO 占位。优先级：

- [ ] `sector-overview-cn/references/` × 3
- [ ] `initiating-coverage-cn/references/` × 3
- [ ] `comps-cn/references/` × 3
- [ ] `dcf-cn/references/` × 3
- [ ] `audit-xls-cn/references/` × 3

5 个新技能（announcement-digest / macro-alert / contract-devil-clause / cross-border-compliance / compliance-watcher）的 references 也未填充。

参考已完成的 `earnings-analysis-cn/references/` 三件套作为模板。

### 3. 完善 templates/ 工具脚本

- [ ] `comps-cn/templates/comps_xlsx.py`：可比公司 Excel 生成
- [ ] `dcf-cn/templates/dcf_xlsx.py`：DCF Excel 生成
- [ ] `compliance-watcher-cn/templates/regulatory_scraper.py`：多源监管法规抓取
- [ ] `compliance-watcher-cn/templates/rule_library/`：YAML 规则库初始 50+ 条

模板参考已完成的 `earnings-analysis-cn/templates/cover_page.py` + `check_layout.py`。

### 4. 真实案例验证

用真实 A 股标的 / 真实合同 / 真实监管函跑通技能并反馈：

- ✅ 跑通的案例：在 `tests/cases/` 下添加测试案例
- ❌ 失败的案例：在 Issues 报告 bug + 提供脱敏后的样例

每个技能至少需要 3 个真实案例验证才能进入 v1.x 稳定版。

### 5. 翻译

英文版 README / INSTALL（已部分支持）。

## 开发流程

### Step 1: Fork & Clone

```bash
git clone https://github.com/yourname/financial-services-cn.git
cd financial-services-cn
```

### Step 2: 创建分支

```bash
git checkout -b feature/<your-feature>
```

分支命名规范：
- `feature/<skill-name>-cn` — 新技能
- `fix/<skill-name>-cn-<bug-desc>` — bug 修复
- `docs/<doc-name>` — 文档改进
- `refs/<skill-name>-cn-<reference-name>` — references 补全

### Step 3: 开发

按 [ARCHITECTURE.md](ARCHITECTURE.md) 的规范开发。**重要约定**：

- 只编辑 `plugins/vertical-plugins/` 下的源文件
- **不要**直接编辑 `plugins/agent-plugins/` 下的副本（会被 sync 覆盖）
- SKILL.md ≥ 400 行（compliance 类 ≥ 500）
- 必含中国市场本土化深度内容
- 必含禁止用语清单
- 必含与其他 -cn 技能的协同矩阵

### Step 4: 自检

```bash
# 同步副本
python3 scripts/sync-agent-skills.py

# 全文校验
python3 scripts/check.py

# 应输出：OK X file(s) checked, 0 issues.
```

### Step 5: 提交 PR

PR 描述模板：

```markdown
## 类型
- [ ] 新技能
- [ ] References 补全
- [ ] Templates 工具
- [ ] 案例验证
- [ ] Bug 修复
- [ ] 文档改进

## 影响范围
- 修改了哪些 skill / 文件

## 测试
- [ ] 已运行 check.py，全部通过
- [ ] 已运行 sync-agent-skills.py
- [ ] 至少 X 个真实案例验证（如适用）

## 检查清单
- [ ] SKILL.md ≥ 400 行（如新技能）
- [ ] 含禁止用语清单
- [ ] 含散户友好性设计章节
- [ ] 含与其他 -cn 技能协同矩阵
- [ ] 数据源标注规范
- [ ] 强制免责声明
```

## 代码规范

### Markdown

- 中文文档：使用全角标点（。，！？）
- 英文术语：保留半角
- 代码块用三个反引号
- 表格用 GFM 标准
- 标题层级清晰：## 一级，### 二级，#### 三级

### Python

- 遵循 PEP 8
- 函数 / 类必含 docstring
- 中文注释允许
- 依赖最小化（templates 脚本只依赖 python-docx / openpyxl / requests 等基础包）

### YAML

- 缩进 2 空格
- key 全部小写 + 下划线
- 中文 value 用双引号

## 合规要求（重要）

**所有 skill 必须遵守**：

1. ❌ 禁止"买卖建议" / "保收益" / "稳赚" 等绝对化表述
2. ❌ 禁止预测货币政策 / 监管行为具体结果
3. ❌ 禁止伪造分析师身份 / SAC 编号 / 研报历史
4. ✅ 必须含免责声明
5. ✅ 必须使用 5 档 A 股评级标准（如适用）
6. ✅ 必须标注数据来源 + 披露日
7. ✅ 复杂场景必须建议咨询持牌律师 / 投资顾问

违反合规要求的 PR 会被直接拒绝。

## 行为准则

参与本项目须遵守以下准则：

- ✅ 友善：尊重每位贡献者
- ✅ 专业：技术讨论基于事实
- ✅ 中立：不为特定金融产品 / 公司 / 机构站台
- ❌ 禁止：人身攻击 / 歧视 / 垃圾推广
- ❌ 禁止：用本项目做任何牟利推荐

## 维护者

- @yourname (Lead Maintainer)
- @collaborators

## 联系

- 技术问题：[GitHub Issues](https://github.com/yourname/financial-services-cn/issues)
- 综合讨论：[GitHub Discussions](https://github.com/yourname/financial-services-cn/discussions)
- 安全问题：邮件至 maintainer

感谢你的贡献！🙏
