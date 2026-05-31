# 安装与使用指南

## 系统要求

- 操作系统：Windows / macOS / Linux
- [Claude Code](https://claude.com/claude-code) ≥ 最新版本
- Python ≥ 3.9（如需运行 sync 与 check 脚本）

## 三种安装方式

### 方式 1：合并到 Anthropic 官方 financial-services（推荐）

适用场景：你已经在使用 Anthropic 官方 financial-services 插件，想增加中文能力。

```bash
# 1. 进入 Anthropic financial-services 仓库目录
cd path/to/anthropic/financial-services

# 2. 把本仓库的 plugins/ 内容合并进去（不覆盖英文 skill）
cp -r path/to/financial-services-cn/plugins/vertical-plugins/equity-research/skills/* \
      plugins/vertical-plugins/equity-research/skills/

cp -r path/to/financial-services-cn/plugins/vertical-plugins/financial-analysis/skills/* \
      plugins/vertical-plugins/financial-analysis/skills/

cp -r path/to/financial-services-cn/plugins/vertical-plugins/wealth-management/skills/* \
      plugins/vertical-plugins/wealth-management/skills/

cp -r path/to/financial-services-cn/plugins/vertical-plugins/operations/skills/* \
      plugins/vertical-plugins/operations/skills/

# 3. 同步到 agent-plugins 副本（Anthropic 架构要求）
python3 scripts/sync-agent-skills.py

# 4. 全文档校验
python3 scripts/check.py
# 应输出：OK 80+ file(s) checked, 0 issues.

# 5. 在 Claude Code 中加载 marketplace
# Anthropic 默认的 marketplace 名为 fsi-local
/plugin marketplace add path/to/anthropic/financial-services

# 6. 装需要的 plugin（带 -cn skill 的自动包含）
/plugin install equity-research@fsi-local
/plugin install financial-analysis@fsi-local
/plugin install wealth-management@fsi-local
/plugin install operations@fsi-local
```

### 方式 2：独立使用（不依赖 Anthropic 官方仓库）

适用场景：你只想使用中文 skill，不需要英文版。

```bash
# 1. clone 本仓库
git clone https://github.com/yourname/financial-services-cn.git
cd financial-services-cn

# 2. 创建 marketplace.json（位于 .claude-plugin/ 目录下）
mkdir -p .claude-plugin
cat > .claude-plugin/marketplace.json <<'EOF'
{
  "name": "financial-services-cn",
  "owner": {
    "name": "Financial-Services-CN Contributors"
  },
  "plugins": [
    {
      "name": "equity-research",
      "source": "./plugins/vertical-plugins/equity-research",
      "description": "A 股股票研究中文技能：财报点评 / 行业综述 / 首次覆盖 / 公告精读 / 宏观异动"
    },
    {
      "name": "financial-analysis",
      "source": "./plugins/vertical-plugins/financial-analysis",
      "description": "财务分析中文技能：A 股可比估值 / A 股 DCF / 模型质检"
    },
    {
      "name": "wealth-management",
      "source": "./plugins/vertical-plugins/wealth-management",
      "description": "财富管理中文技能：基金/信托合同魔鬼条款审查"
    },
    {
      "name": "operations",
      "source": "./plugins/vertical-plugins/operations",
      "description": "运营 / 合规中文技能：跨境监管函翻译 / 法规追踪与合规审查"
    }
  ]
}
EOF

# 3. 在 Claude Code 中添加 marketplace
/plugin marketplace add path/to/financial-services-cn

# 4. 装技能
/plugin install equity-research@financial-services-cn
/plugin install financial-analysis@financial-services-cn
/plugin install wealth-management@financial-services-cn
/plugin install operations@financial-services-cn
```

### 方式 3：仅复制单个 skill 使用

适用场景：你只对某一个 skill 感兴趣（如 earnings-analysis-cn）。

```bash
# 复制单个 skill 到你的 Claude Code skills 目录
cp -r path/to/financial-services-cn/plugins/vertical-plugins/equity-research/skills/earnings-analysis-cn \
      path/to/your/claude/skills/

# 在 Claude Code 中重新加载
```

## 验证安装

```bash
# 1. 列出已安装的 plugin
/plugin list

# 应看到（带 -cn skill 的 plugin）：
# equity-research
# financial-analysis
# wealth-management
# operations

# 2. 测试触发 skill
# 在 Claude Code 中输入：
"帮我点评华明装备 (002270.SZ) 2025 年年报"
# 应自动触发 earnings-analysis-cn
```

## 卸载

```bash
# 卸载单个 plugin
/plugin uninstall equity-research

# 卸载所有
/plugin uninstall equity-research financial-analysis wealth-management operations

# 移除 marketplace
/plugin marketplace remove financial-services-cn  # 或 fsi-local
```

## 常见问题（FAQ）

### Q1: sync-agent-skills.py 报错怎么办？

如果用方式 1 安装，需要 Anthropic 官方仓库的 `scripts/sync-agent-skills.py`。如果该脚本不存在，你可以：
- 跳过 sync 步骤（仅影响 agent-plugins 中的副本，不影响主用法）
- 或从 Anthropic 官方仓库复制该脚本

### Q2: skill 没有触发怎么办？

- 确认已安装 plugin：`/plugin list`
- 确认你的输入含触发关键词（每个 skill 的 description 列出至少 6 个关键词）
- 试着明确触发：`@equity-research:earnings 华明装备`

### Q3: 数据来源问题

本工具 v1 阶段不内置数据 API。需要用户在使用时：
- 提供公告 PDF / 文本（巨潮资讯网下载）
- 或粘贴公告 URL（Claude 通过 WebFetch 抓取）
- 或粘贴同花顺 iFinD / Wind / Choice 终端数据

v2 阶段（2026 年 8 月后）将通过 MCP 自动接入数据源。

### Q4: 如何自定义某个 skill？

每个 skill 是一个独立目录，包含 `SKILL.md` 和 `references/`。直接编辑这些文件即可（Markdown 格式）。修改后无需重启 Claude Code，下次触发时即生效。

### Q5: 我能商用吗？

可以。本仓库采用 Apache License 2.0，允许商业使用 / 修改 / 分发，仅需保留原版权声明。

## 进阶配置

### 配置 hooks（可选）

如果你希望某些 skill 自动触发（如每日宏观数据公布后自动跑 macro-alert-cn），可配置 hooks。详见 [docs/HOOKS.md](docs/HOOKS.md)（todo）。

### 配置 MCP（v2 路径）

未来版本将提供：
- `tushare-mcp`：A 股行情、财务数据
- `cninfo-mcp`：巨潮公告
- `regulatory-mcp`：监管法规

配置方法将在 v2 发布时补充。

## 报告问题

- Bug / 错误：在 [GitHub Issues](https://github.com/yourname/financial-services-cn/issues) 提交
- 功能建议：在 [GitHub Discussions](https://github.com/yourname/financial-services-cn/discussions) 提议
- 安全问题：邮件联系（见 [SECURITY.md](docs/SECURITY.md)）
