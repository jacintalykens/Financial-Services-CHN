# A 股业绩点评研报逐页模板与排版规范

本文档定义中信 / 中金 / 海通 / 国泰君安风格的 A 股业绩点评研报标准逐页模板，包含：双标题艺术、字号字体规范、表格样式、估值章节（PE/PB-Band/PB-ROE）、敏感性分析公式化排版、以及完整免责声明模板。

---

## 字体与字号总览

| 元素 | 中文字体 | 英文/数字字体 | 字号 | 加粗 | 颜色 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 主标题（封面） | 微软雅黑 / 宋体 | Arial | 18-20pt | ✅ | 黑色 |
| 副标题 | 微软雅黑 / 宋体 | Arial | 14pt | ✅ | 深灰 / 黑 |
| 一级标题 | 微软雅黑 / 黑体 | Arial | 14-16pt | ✅ | 深蓝 #1F4E79 |
| 二级标题 | 微软雅黑 / 宋体 | Arial | 12pt | ✅ | 黑色 |
| 三级标题 | 宋体 | Arial | 11pt | ✅ | 黑色 |
| 正文 | 宋体 | Times New Roman / Arial | 10.5pt（五号）或 11pt | — | 黑色 |
| 表格表头 | 微软雅黑 | Arial | 10pt | ✅ | 白色（深蓝底） |
| 表格正文 | 宋体 | Arial | 9pt | — | 黑色 |
| 图注脚注 | 宋体 | Arial | 9pt（小五） | — | 灰色 #595959 |
| 超链接 | 宋体 | Arial | 同正文 | — | 深蓝 #1F4E79，下划线 |
| 风险提示 | 宋体 | — | 10.5pt | ✅ | 红色 #C00000 |

**页面规范：**
- 页面：A4 纵向，上下边距 2.5cm，左右边距 2.5cm
- 行距：1.25 倍
- 段落间距：段前 0pt，段后 6pt
- 页眉：左侧 — 公司简称 + 股票代码；右侧 — 报告日期
- 页脚：左侧 — 券商名称 + 研究部门；中间 — 页码；右侧 — 免责声明缩略

---

## 第 1 页：封面与核心总控台

### 双标题艺术（A 股研报新财富级别写法）

```
═══════════════════════════════════════════════════════════════════
【主标题 - 18pt 加粗 黑体 居中 - 核心观点提炼，类似新闻标题】

业绩超预期，特高压与海外双轮驱动加速兑现

【副标题 - 14pt 加粗 宋体 居中 - 公司+股票代码+报告期+报告类型】

—— 华明装备（002270.SZ）2025 年三季报点评
═══════════════════════════════════════════════════════════════════
```

**主标题写作艺术：**
- 必须含明确的"观点"或"判断"，禁止平铺直叙
- 长度建议 12-20 字
- 优秀主标题示例：
  - "业绩超预期，海外市占率提升与特高压双轮驱动"
  - "Q3 单季扭亏为盈，组件价格止跌龙头率先迎来拐点"
  - "业绩低于预期，原材料压力 + 海运扰动短期承压"
  - "新车放量带动毛利率创新高，重申买入评级"
- 劣质主标题：
  - "2025 年三季报点评"（无观点，类似纯标题）
  - "稳健增长，符合预期"（流水账）
  - "业绩公告"（毫无信息量）

### 报告头部信息块

⚠️ **核心修订**：国内主流券商研报封面采用**双栏布局**：左栏放正文（双标题 + 报告要点 + 摘要表），右栏放垂直 Panel（评级 + 当前价 + 基本数据 + 股价走势图 + 相关研报 + 报告作者）。**不要写成一整块横排信息**。

#### 第 1 页布局总图（左 70% 正文 / 右 30% Panel）

```
┌──────────────────────────────────────────────────────────┬───────────────────────┐
│ 公司研究 \| 工业 \| 资本货物                              │  ┌─────────────────┐  │
│ 证券研究报告                                              │  │ 买入  \| 维持    │  │
│ [公司简称]([代码])[报告期]点评                            │  │                  │  │
│ 2026 年 05 月 24 日                                       │  └─────────────────┘  │
│                                                          │                       │
│ 【主标题 18-20pt 黑体加粗】                               │  当前价：             │
│ 海外出口加速、特高压批量化投运，                          │  17.85 元             │
│ 叠加 H 股上市启动，重申"买入"评级                         │  （2026-05-22 收盘）  │
│                                                          │                       │
│ 【副标题 14pt 宋体加粗】                                  │  ───────────────      │
│ —— 华明装备（002270.SZ）2025 年年度报告点评              │  基本数据             │
│                                                          │  52 周最高/最低（元）：│
│ 【报告要点】（paragraph 风格，4-5 段）                    │   xx.xx / xx.xx       │
│                                                          │  A 股流通股（百万）： │
│ ▍核心结论一句话立论 + 量化支撑                          │   xxx                 │
│   [一段 paragraph，约 80-120 字，不用 bullet 不分行]      │  A 股总股本（百万）： │
│                                                          │   xxx                 │
│ ▍第二个子结论                                            │  流通市值（百万元）： │
│   [一段 paragraph]                                       │   xx,xxx              │
│                                                          │  总市值（百万元）：   │
│ ▍第三个子结论                                            │   xx,xxx              │
│   [一段 paragraph]                                       │                       │
│                                                          │  ───────────────      │
│ ▍风险提示                                                │  过去一年股价走势     │
│   电网投资不及预期；地缘政治；原材料波动；汇率波动        │  [图：公司 vs 沪深300] │
│                                                          │                       │
│ ─────────────────────────────────                       │  ───────────────      │
│ 【财务数据和估值】（7×5 摘要表，紧接报告要点底部）        │  相关研究报告         │
│                                                          │  • XX 2024 年中报点评 │
│ [详见下方 7×5 标准摘要表]                                │  • XX 行业深度        │
│                                                          │                       │
│                                                          │  ───────────────      │
│                                                          │  报告作者             │
│                                                          │  分析师 XXX           │
│                                                          │  执业证书 SXXXXXXXXXX │
│                                                          │  电话 010-XXXXXXXX    │
│                                                          │  邮箱 xxx@xxx.com.cn  │
└──────────────────────────────────────────────────────────┴───────────────────────┘
```

#### 右栏 Panel 6 段式精确规范

**Panel 段 1：评级框**（**必须放在 panel 最上方**）

```
┌─────────────┐
│ 买入  | 维持 │   ← 评级 | 调整方向
└─────────────┘
```

- 评级用语只能为 5 档之一：**买入 / 增持 / 中性 / 减持 / 卖出**
- 调整方向用语只能为 3 档：**维持 / 上调 / 下调 / 首次**
- 评级框背景色：买入 / 增持 用券商红（RGB 200,16,46）；中性 用灰色；减持 / 卖出 用蓝色或绿色

**Panel 段 2：当前价（单独成行，字号加大至 14-16pt）**

```
当前价：
17.85 元
（2026-05-22 收盘）
```

**Panel 段 3：基本数据（5 行硬性字段）**

```
─────────────────
基本数据
52 周最高/最低价（元）：xx.xx / xx.xx
A 股流通股（百万股）： xxx.xx
A 股总股本（百万股）： xxx.xx
流通市值（百万元）：   xx,xxx.xx
总市值（百万元）：     xx,xxx.xx
─────────────────
```

**Panel 段 4：过去一年股价走势图**

- 横轴：12 个月（标注 2/1、5/3、8/2、11/1、1/31 等月份节点）
- 纵轴：累计收益率（%），通常 -23% ~ +95% 区间
- 两条折线：**公司（实色）** + **沪深 300（虚线灰色）**
- 图标题：无
- 数据源标注："资料来源：Wind"（图下方小字）

**Panel 段 5：相关研究报告（最多 3 条）**

```
─────────────────
相关研究报告
• [公司简称] 2024 年中报点评（2024-08-30）
• [公司简称] 2024 年三季报点评（2024-10-28）
• [行业] 行业深度报告（2024-12-01）
```

**Panel 段 6：报告作者（结尾位置）**

```
─────────────────
报告作者
分析师 [姓名]
执业证书编号 SXXXXXXXXXXXXXXXXX
电话 010-XXXXXXXX
邮箱 xxx@xxx.com.cn

联系人 [姓名]
电话 010-XXXXXXXX
邮箱 xxx@xxx.com.cn
```

#### 首页"财务数据和估值"摘要表（7×5 强制格式）

紧接报告要点下方，摆放**最关键的 7 行 × 5 列摘要表**：

```
┌────────────────────────┬────────┬────────┬────────┬────────┬────────┐
│ 财务数据和估值          │ 2023A  │ 2024A  │ 2025E  │ 2026E  │ 2027E  │
├────────────────────────┼────────┼────────┼────────┼────────┼────────┤
│ 营业收入（百万元）      │ x,xxx  │ x,xxx  │ x,xxx  │ x,xxx  │ x,xxx  │
│ 收入同比（%）           │ xx.xx  │ xx.xx  │ xx.xx  │ xx.xx  │ xx.xx  │
│ 归母净利润（百万元）    │ xxx    │ xxx    │ xxx    │ xxx    │ xxx    │
│ 归母净利润同比（%）     │ xx.xx  │ xx.xx  │ xx.xx  │ xx.xx  │ xx.xx  │
│ ROE（%）                │ xx.xx  │ xx.xx  │ xx.xx  │ xx.xx  │ xx.xx  │
│ 每股收益（元）          │ x.xx   │ x.xx   │ x.xx   │ x.xx   │ x.xx   │
│ 市盈率（P/E）           │ xx.xx  │ xx.xx  │ xx.xx  │ xx.xx  │ xx.xx  │
└────────────────────────┴────────┴────────┴────────┴────────┴────────┘

资料来源：Wind / 东方财富 Choice / [券商]研究所
```

**强制要求**：
- 5 列必须含 **2 历史年 + 3 预测年**（年报点评）或 **1 历史年 + 4 预测年**（一季报 / 中报 / 三季报点评）
- 历史标 `A`，预测标 `E`
- 金额单位**百万元**（不用亿元），右对齐 2 位小数
- 比率单位 **%**，保留 2 位小数
- 表格采用**简洁三线表**（顶线 + 表头底线 + 表尾线）—— 不用网格全框

### 三方业绩偏差汇总表（核心总结表 1/3）

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 表 1：2025 Q3 单季业绩 vs Wind 一致预期 vs 业绩预告对比                  │
├──────────────────┬──────────┬──────────┬──────────────┬──────────────────┤
│ 指标             │ 实际值   │ Wind     │ 业绩预告中枢 │ 偏差判定         │
├──────────────────┼──────────┼──────────┼──────────────┼──────────────────┤
│ 营业收入（亿元） │ X.XX     │ X.XX     │ N/A          │ 超预期 +X.X%     │
│ YoY              │ +XX.X%   │ +XX.X%   │ —            │                  │
├──────────────────┼──────────┼──────────┼──────────────┼──────────────────┤
│ 归母净利润（亿） │ X.XX     │ X.XX     │ [X.X-X.X]    │ 超预期 +X.X%     │
│ YoY              │ +XX.X%   │ +XX.X%   │ +XX.X%       │ 落入上限         │
├──────────────────┼──────────┼──────────┼──────────────┼──────────────────┤
│ 扣非净利润（亿） │ X.XX     │ X.XX     │ N/A          │ 超预期 +X.X%     │
│ YoY              │ +XX.X%   │ +XX.X%   │ —            │                  │
├──────────────────┼──────────┼──────────┼──────────────┼──────────────────┤
│ 毛利率           │ XX.X%    │ XX.X%    │ —            │ 高 +X.Xpct       │
│ 净利率           │ XX.X%    │ XX.X%    │ —            │ 高 +X.Xpct       │
│ EPS（元）        │ X.XX     │ X.XX     │ —            │ 超预期 +X.X%     │
└──────────────────┴──────────┴──────────┴──────────────┴──────────────────┘

数据来源：公司《2025 年第三季度报告》（公告日期：2025-10-27）；Wind 一致预期
（截止 2025-10-25）；公司《2025 年前三季度业绩预告》（公告日期：2025-10-12）
[点击查阅三季报原文] [点击查阅业绩预告原文]
```

### 核心要点（3-4 条 - 用 ■ 符号 + 段落式展开）

```
■ 业绩超预期，主营业务全线开花，单季营收 / 归母净利润 / 扣非净利润齐创历
  史新高

  Q3 单季营业收入 X.XX 亿元（YoY +XX.X%，QoQ +XX.X%），超 Wind 一致预期
  X.XX 亿元 X.X%；归母净利润 X.XX 亿元（YoY +XX.X%），落入此前业绩预告
  区间（X.X-X.X 亿元）上限位置；扣非净利润 X.XX 亿元（YoY +XX.X%），扣
  非占比 XX%，业绩质量延续高水平。本季业绩超预期主要由 [具体原因] 驱动，
  我们认为 [核心判断]。

■ 毛利率提升 X.Xpct 至 XX.X%，海外业务占比提升带动结构性升级

  [段落分析 150-200 字]

■ 合同负债环比 +XX% 至 X.XX 亿元，下季业绩能见度抬升

  [段落分析 150-200 字]

■ 维持"买入"评级，上调目标价至 XX.XX 元（前次 XX.XX 元，+XX%）

  [段落分析投资结论 150-200 字]
```

### 关键财务摘要（核心总结表 2/3 - 含旧 vs 新预测）

```
┌────────────────────────────────────────────────────────────────────────┐
│ 表 2：盈利预测调整对比表                                                │
├──────────────────┬──────────┬──────────┬─────────┬──────────┬──────────┤
│ 指标             │ 2025E 旧 │ 2025E 新 │ 调整%   │ 2026E 新 │ 2027E 新 │
├──────────────────┼──────────┼──────────┼─────────┼──────────┼──────────┤
│ 营业收入（亿元） │ XX.X     │ XX.X     │ +X.X%   │ XX.X     │ XX.X     │
│ 收入增速         │ XX.X%    │ XX.X%    │ +Xpct   │ XX.X%    │ XX.X%    │
│ 毛利率           │ XX.X%    │ XX.X%    │ +Xpct   │ XX.X%    │ XX.X%    │
│ 归母净利润（亿） │ X.X      │ X.X      │ +X.X%   │ X.X      │ X.X      │
│ 扣非净利润（亿） │ X.X      │ X.X      │ +X.X%   │ X.X      │ X.X      │
│ EPS（元）        │ X.XX     │ X.XX     │ +X.X%   │ X.XX     │ X.XX     │
│ ROE（加权）      │ XX.X%    │ XX.X%    │ +Xpct   │ XX.X%    │ XX.X%    │
│ 对应 PE          │ XX       │ XX       │         │ XX       │ XX       │
│ 对应 PB          │ X.X      │ X.X      │         │ X.X      │ X.X      │
└──────────────────┴──────────┴──────────┴─────────┴──────────┴──────────┘

注：旧版预测来自团队 2025 年中报点评（发布日：2025-08-30）。
数据来源：公司年报、本团队预测模型
```

---

## 首页双栏版式 python-docx 完整实现配方 ⭐⭐⭐【强制复制使用】

⚠️ **核心警告**：直接用 `doc.add_paragraph(...)` 顺序堆叠生成首页 = **必然单栏**。国内研报首页必须用**无边框表格作为布局容器**才能正确呈现双栏 + 嵌套结构。

以下代码已在国元证券、中信建投、华泰证券等真实研报版式上验证可行。**复制使用，不要从零拼装**。

### 完整工具函数库

```python
"""
A 股业绩点评研报 - 首页双栏版式生成器
依赖：python-docx >= 1.0.0
"""
from docx import Document
from docx.shared import Cm, Pt, RGBColor, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ═══════════════════════════════════════════════════════════════════
# 配色系统（券商标准 6 色）
# ═══════════════════════════════════════════════════════════════════
COLOR_RED       = RGBColor(0xC8, 0x10, 0x2E)  # 券商红
COLOR_BLUE      = RGBColor(0x00, 0x20, 0x60)  # 券商深蓝
COLOR_DIVIDER   = RGBColor(0xD9, 0xD9, 0xD9)  # 浅灰分隔
COLOR_GRAY      = RGBColor(0x59, 0x59, 0x59)  # 灰色文字
COLOR_WATERMARK = RGBColor(0xBF, 0xBF, 0xBF)  # 极浅灰水印
COLOR_BLACK     = RGBColor(0x00, 0x00, 0x00)
COLOR_WHITE     = RGBColor(0xFF, 0xFF, 0xFF)

HEX_RED         = 'C8102E'
HEX_BLUE        = '002060'

# ═══════════════════════════════════════════════════════════════════
# XML 辅助函数（python-docx 高层 API 不直接支持的功能）
# ═══════════════════════════════════════════════════════════════════
def set_cell_background(cell, hex_color):
    """单元格背景色（深蓝表头 / 红色评级框）"""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def remove_cell_borders(cell):
    """移除单元格所有边框 — 双栏布局容器必须"""
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for edge in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        b = OxmlElement(f'w:{edge}')
        b.set(qn('w:val'), 'nil')
        tcBorders.append(b)
    tcPr.append(tcBorders)

def set_cell_margin(cell, top=100, bottom=100, left=100, right=100):
    """单元格内边距（单位：1/100 mm，100 = 0.1cm）"""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for edge, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{edge}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_horizontal_divider(paragraph, color=COLOR_DIVIDER):
    """在段落上方添加 0.5pt 灰色分隔线"""
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    top = OxmlElement('w:top')
    top.set(qn('w:val'), 'single')
    top.set(qn('w:sz'), '4')      # 0.5pt
    top.set(qn('w:space'), '4')
    top.set(qn('w:color'), 'D9D9D9')
    pBdr.append(top)
    pPr.append(pBdr)

def add_paragraph_with_run(parent, text, font='宋体', size=10, bold=False, 
                           color=COLOR_BLACK, align=None, space_after=Pt(2)):
    """添加格式化段落 — parent 可以是 cell 或 doc"""
    p = parent.add_paragraph()
    if align is not None:
        p.alignment = align
    p.paragraph_format.space_after = space_after
    p.paragraph_format.space_before = Pt(0)
    run = p.add_run(text)
    run.font.name = font
    run.font.size = Pt(size)
    run.bold = bold
    run.font.color.rgb = color
    # 设置中文字体
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.append(rFonts)
    rFonts.set(qn('w:eastAsia'), font)
    return p

# ═══════════════════════════════════════════════════════════════════
# 区段 A：页面初始化与页眉条
# ═══════════════════════════════════════════════════════════════════
def setup_page(doc):
    """A4 纵向，券商标准页边距"""
    sec = doc.sections[0]
    sec.page_height = Cm(29.7)
    sec.page_width = Cm(21.0)
    sec.top_margin = Cm(1.8)
    sec.bottom_margin = Cm(1.8)
    sec.left_margin = Cm(2.0)
    sec.right_margin = Cm(2.0)

def add_header_strip(doc, industry_tag, report_date):
    """页眉条：左 行业分类 | 右 报告日期；下方 2pt 深蓝粗线"""
    tbl = doc.add_table(rows=1, cols=2)
    tbl.autofit = False
    tbl.columns[0].width = Cm(11.0)
    tbl.columns[1].width = Cm(6.0)
    
    left, right = tbl.rows[0].cells
    for c in [left, right]:
        remove_cell_borders(c)
        set_cell_margin(c, top=0, bottom=0, left=0, right=0)
    
    # 左：行业分类
    p = left.paragraphs[0]
    run = p.add_run(industry_tag)
    run.font.name = '微软雅黑'
    run.font.size = Pt(9)
    run.font.color.rgb = COLOR_GRAY
    
    # 右：报告日期（右对齐）
    p = right.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run(f'证券研究报告  |  {report_date}')
    run.font.name = '微软雅黑'
    run.font.size = Pt(9)
    run.font.color.rgb = COLOR_GRAY
    
    # 下方 2pt 深蓝粗线（通过新段落的上边框实现）
    sep = doc.add_paragraph()
    sep.paragraph_format.space_before = Pt(0)
    sep.paragraph_format.space_after = Pt(6)
    pPr = sep._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    top = OxmlElement('w:top')
    top.set(qn('w:val'), 'single')
    top.set(qn('w:sz'), '16')     # 2pt
    top.set(qn('w:space'), '1')
    top.set(qn('w:color'), HEX_BLUE)
    pBdr.append(top)
    pPr.append(pBdr)

# ═══════════════════════════════════════════════════════════════════
# 区段 B：标题区（主标题 + 副标题）
# ═══════════════════════════════════════════════════════════════════
def add_title_block(doc, main_title, sub_title):
    """居中双标题"""
    # 主标题
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.2
    run = p.add_run(main_title)
    run.font.name = '微软雅黑'
    run.font.size = Pt(20)
    run.bold = True
    run.font.color.rgb = COLOR_BLACK
    rPr = run._element.get_or_add_rPr()
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:eastAsia'), '微软雅黑')
    rPr.append(rFonts)
    
    # 副标题
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(18)
    run = p.add_run(f'—— {sub_title}')
    run.font.name = '宋体'
    run.font.size = Pt(14)
    run.bold = True
    run.font.color.rgb = COLOR_BLUE
    rPr = run._element.get_or_add_rPr()
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:eastAsia'), '宋体')
    rPr.append(rFonts)

# ═══════════════════════════════════════════════════════════════════
# 区段 C：双栏主体区（核心 — 无边框 1×2 表格作为布局容器）
# ═══════════════════════════════════════════════════════════════════
def add_two_column_body(doc, data):
    """
    主体区：左栏 11.5cm 报告要点+财务摘要表，右栏 5.5cm Panel
    必须用无边框表格容器，不能用顺序段落。
    """
    layout = doc.add_table(rows=1, cols=2)
    layout.autofit = False
    layout.alignment = WD_TABLE_ALIGNMENT.CENTER
    layout.columns[0].width = Cm(11.5)
    layout.columns[1].width = Cm(5.5)
    
    left_cell, right_cell = layout.rows[0].cells
    
    for c in [left_cell, right_cell]:
        remove_cell_borders(c)
        c.vertical_alignment = WD_ALIGN_VERTICAL.TOP
        set_cell_margin(c, top=50, bottom=50, left=100, right=100)
    
    fill_left_column(left_cell, data)
    fill_right_column(right_cell, data)
    
    return layout

def fill_left_column(cell, data):
    """左栏：报告要点（4 paragraphs with ▎ marker）+ 财务摘要表 7×6"""
    
    # 清空默认空段落
    cell.paragraphs[0]._p.getparent().remove(cell.paragraphs[0]._p)
    
    # 小标题"报告要点"
    add_paragraph_with_run(cell, '报告要点', font='微软雅黑', size=12, 
                            bold=True, color=COLOR_BLUE,
                            space_after=Pt(6))
    
    # 4 段 paragraph 风格要点（不用 bullet）
    for point in data['report_points']:
        p = cell.add_paragraph()
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.line_spacing = 1.4
        p.paragraph_format.first_line_indent = Cm(0)
        
        # ▎ 标记（红色加粗）
        marker = p.add_run('▎ ')
        marker.font.name = '微软雅黑'
        marker.font.size = Pt(11)
        marker.bold = True
        marker.font.color.rgb = COLOR_RED
        
        # 子结论 headline（加粗黑色）
        head = p.add_run(point['headline'])
        head.font.name = '微软雅黑'
        head.font.size = Pt(10.5)
        head.bold = True
        head.font.color.rgb = COLOR_BLACK
        rPr = head._element.get_or_add_rPr()
        rFonts = OxmlElement('w:rFonts')
        rFonts.set(qn('w:eastAsia'), '微软雅黑')
        rPr.append(rFonts)
        
        # 换行 + body
        p.add_run().add_break()
        body = p.add_run(point['body'])
        body.font.name = '宋体'
        body.font.size = Pt(10)
        body.font.color.rgb = COLOR_BLACK
        rPr = body._element.get_or_add_rPr()
        rFonts = OxmlElement('w:rFonts')
        rFonts.set(qn('w:eastAsia'), '宋体')
        rPr.append(rFonts)
    
    # 间隔
    cell.add_paragraph()
    
    # 财务摘要表（7 数据行 + 1 表头 = 8 行 × 6 列）
    fin_table = cell.add_table(rows=8, cols=6)
    fin_table.autofit = False
    # 列宽分配
    col_widths = [Cm(3.5), Cm(1.5), Cm(1.5), Cm(1.5), Cm(1.5), Cm(1.5)]
    for i, w in enumerate(col_widths):
        fin_table.columns[i].width = w
    
    # 表头行（深蓝底白字）
    headers = ['财务数据和估值', '2023A', '2024A', '2025E', '2026E', '2027E']
    for i, h in enumerate(headers):
        c = fin_table.rows[0].cells[i]
        set_cell_background(c, HEX_BLUE)
        c.paragraphs[0].text = ''
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i > 0 else WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(h)
        run.font.name = '微软雅黑'
        run.font.size = Pt(8)
        run.bold = True
        run.font.color.rgb = COLOR_WHITE
    
    # 数据行
    row_defs = [
        ('营业收入（百万元）', 'revenue', '{:,.2f}'),
        ('收入同比（%）', 'rev_yoy', '{:.2f}'),
        ('归母净利润（百万元）', 'np', '{:,.2f}'),
        ('归母净利润同比（%）', 'np_yoy', '{:.2f}'),
        ('ROE（%）', 'roe', '{:.2f}'),
        ('每股收益（元）', 'eps', '{:.2f}'),
        ('市盈率（P/E）', 'pe', '{:.2f}'),
    ]
    for ri, (label, key, fmt) in enumerate(row_defs, 1):
        # 标签列
        c = fin_table.rows[ri].cells[0]
        c.paragraphs[0].text = ''
        p = c.paragraphs[0]
        run = p.add_run(label)
        run.font.name = '宋体'
        run.font.size = Pt(8)
        # 数据列
        for ci, val in enumerate(data['fin_table'][key], 1):
            c = fin_table.rows[ri].cells[ci]
            c.paragraphs[0].text = ''
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            run = p.add_run(fmt.format(val) if isinstance(val, (int, float)) else str(val))
            run.font.name = 'Arial'
            run.font.size = Pt(8)
    
    # 三线表样式：仅顶部和底部和表头下方有横线，其他无边框
    apply_three_line_table_borders(fin_table)
    
    # 资料来源
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    run = p.add_run(f'资料来源：Wind、{data["broker"]}研究所')
    run.font.name = '宋体'
    run.font.size = Pt(7)
    run.font.color.rgb = COLOR_GRAY

def apply_three_line_table_borders(table):
    """三线表样式：顶线 + 表头下线 + 底线（其余无边框）"""
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    
    tbl = table._tbl
    # 清除所有默认边框
    for row in tbl.iter(qn('w:tr')):
        for cell in row.iter(qn('w:tc')):
            tcPr = cell.find(qn('w:tcPr'))
            if tcPr is None:
                tcPr = OxmlElement('w:tcPr')
                cell.insert(0, tcPr)
            existing = tcPr.find(qn('w:tcBorders'))
            if existing is not None:
                tcPr.remove(existing)
            borders = OxmlElement('w:tcBorders')
            for edge in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
                b = OxmlElement(f'w:{edge}')
                b.set(qn('w:val'), 'nil')
                borders.append(b)
            tcPr.append(borders)
    
    # 顶线（表头行上方）
    rows = list(table.rows)
    for cell in rows[0].cells:
        tcPr = cell._tc.find(qn('w:tcPr'))
        borders = tcPr.find(qn('w:tcBorders'))
        top = borders.find(qn('w:top'))
        top.set(qn('w:val'), 'single')
        top.set(qn('w:sz'), '8')
        top.set(qn('w:color'), '000000')
        bottom = borders.find(qn('w:bottom'))
        bottom.set(qn('w:val'), 'single')
        bottom.set(qn('w:sz'), '4')
        bottom.set(qn('w:color'), '000000')
    
    # 底线（最后一行下方）
    for cell in rows[-1].cells:
        tcPr = cell._tc.find(qn('w:tcPr'))
        borders = tcPr.find(qn('w:tcBorders'))
        bottom = borders.find(qn('w:bottom'))
        bottom.set(qn('w:val'), 'single')
        bottom.set(qn('w:sz'), '8')
        bottom.set(qn('w:color'), '000000')

def fill_right_column(cell, data):
    """右栏 Panel：评级框 + 当前价 + 基本数据 + 股价图 + 相关研报 + 报告作者"""
    cell.paragraphs[0]._p.getparent().remove(cell.paragraphs[0]._p)
    
    # === 段 1：评级框（红底白字，单格表格） ===
    rating_tbl = cell.add_table(rows=1, cols=1)
    rating_tbl.autofit = False
    rating_tbl.columns[0].width = Cm(5.2)
    rc = rating_tbl.rows[0].cells[0]
    set_cell_background(rc, HEX_RED)
    set_cell_margin(rc, top=80, bottom=80, left=0, right=0)
    rc.paragraphs[0].text = ''
    p = rc.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(f'{data["rating"]}  |  {data["rating_change"]}')
    run.font.name = '微软雅黑'
    run.font.size = Pt(14)
    run.bold = True
    run.font.color.rgb = COLOR_WHITE
    
    # === 段 2：当前价 ===
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run('当前价：')
    run.font.name = '宋体'
    run.font.size = Pt(9)
    run.font.color.rgb = COLOR_GRAY
    
    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(f'{data["current_price"]:.2f} 元')
    run.font.name = 'Arial'
    run.font.size = Pt(18)
    run.bold = True
    run.font.color.rgb = COLOR_RED
    
    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run(f'（{data["price_date"]} 收盘）')
    run.font.name = '宋体'
    run.font.size = Pt(8)
    run.font.color.rgb = COLOR_GRAY
    
    # === 段 3：基本数据 ===
    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    add_horizontal_divider(p)
    run = p.add_run('基本数据')
    run.font.name = '微软雅黑'
    run.font.size = Pt(10)
    run.bold = True
    run.font.color.rgb = COLOR_BLUE
    
    basic_fields = [
        ('52 周高/低（元）', data['basic']['high_low_52w']),
        ('A 股流通股（百万股）', f'{data["basic"]["float_a"]:,.2f}'),
        ('A 股总股本（百万股）', f'{data["basic"]["total_a"]:,.2f}'),
        ('流通市值（百万元）', f'{data["basic"]["float_mv"]:,.0f}'),
        ('总市值（百万元）', f'{data["basic"]["total_mv"]:,.0f}'),
    ]
    for label, val in basic_fields:
        p = cell.add_paragraph()
        p.paragraph_format.space_after = Pt(1)
        run1 = p.add_run(f'{label}：')
        run1.font.name = '宋体'
        run1.font.size = Pt(8.5)
        run2 = p.add_run(str(val))
        run2.font.name = 'Arial'
        run2.font.size = Pt(8.5)
        run2.bold = True
    
    # === 段 4：股价走势图 ===
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    add_horizontal_divider(p)
    run = p.add_run('过去一年股价走势')
    run.font.name = '微软雅黑'
    run.font.size = Pt(10)
    run.bold = True
    run.font.color.rgb = COLOR_BLUE
    
    if data.get('price_chart_path'):
        p = cell.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(data['price_chart_path'], width=Cm(5.0))
    
    # === 段 5：相关研究报告 ===
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    add_horizontal_divider(p)
    run = p.add_run('相关研究报告')
    run.font.name = '微软雅黑'
    run.font.size = Pt(10)
    run.bold = True
    run.font.color.rgb = COLOR_BLUE
    
    for ref in data['related_reports'][:3]:
        p = cell.add_paragraph()
        p.paragraph_format.space_after = Pt(1)
        run = p.add_run(f'• {ref["title"]}')
        run.font.name = '宋体'
        run.font.size = Pt(8)
        p = cell.add_paragraph()
        p.paragraph_format.left_indent = Cm(0.3)
        p.paragraph_format.space_after = Pt(3)
        run = p.add_run(f'（{ref["date"]}）')
        run.font.name = '宋体'
        run.font.size = Pt(7.5)
        run.font.color.rgb = COLOR_GRAY
    
    # === 段 6：报告作者 ===
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    add_horizontal_divider(p)
    run = p.add_run('报告作者')
    run.font.name = '微软雅黑'
    run.font.size = Pt(10)
    run.bold = True
    run.font.color.rgb = COLOR_BLUE
    
    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(1)
    run = p.add_run(f'分析师 {data["analyst"]["name"]}')
    run.font.name = '宋体'
    run.font.size = Pt(8.5)
    run.bold = True
    
    for label, val in [
        ('执业证书', data['analyst']['cert_id']),
        ('电话', data['analyst']['phone']),
        ('邮箱', data['analyst']['email']),
    ]:
        p = cell.add_paragraph()
        p.paragraph_format.space_after = Pt(1)
        run1 = p.add_run(f'{label} ')
        run1.font.name = '宋体'
        run1.font.size = Pt(8)
        run1.font.color.rgb = COLOR_GRAY
        run2 = p.add_run(str(val))
        run2.font.name = 'Arial' if label != '执业证书' else '宋体'
        run2.font.size = Pt(8)

# ═══════════════════════════════════════════════════════════════════
# 区段 D：页脚配置（每页应用）
# ═══════════════════════════════════════════════════════════════════
def setup_footer_header(doc):
    """所有页：页眉'请务必阅读正文之后的免责条款部分' + 页脚'X / Y'"""
    sec = doc.sections[0]
    
    # 页眉
    header = sec.header
    p = header.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('请务必阅读正文之后的免责条款部分')
    run.font.name = '宋体'
    run.font.size = Pt(9)
    run.font.color.rgb = COLOR_GRAY
    
    # 页脚：X / Y 页码
    footer = sec.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    # 当前页字段
    run = p.add_run()
    fldChar_begin = OxmlElement('w:fldChar')
    fldChar_begin.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText')
    instrText.text = 'PAGE'
    fldChar_end = OxmlElement('w:fldChar')
    fldChar_end.set(qn('w:fldCharType'), 'end')
    run._element.append(fldChar_begin)
    run._element.append(instrText)
    run._element.append(fldChar_end)
    run.font.name = 'Arial'
    run.font.size = Pt(9)
    run.font.color.rgb = COLOR_GRAY
    
    sep = p.add_run(' / ')
    sep.font.name = 'Arial'
    sep.font.size = Pt(9)
    sep.font.color.rgb = COLOR_GRAY
    
    # 总页数字段
    run = p.add_run()
    fldChar_begin = OxmlElement('w:fldChar')
    fldChar_begin.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText')
    instrText.text = 'NUMPAGES'
    fldChar_end = OxmlElement('w:fldChar')
    fldChar_end.set(qn('w:fldCharType'), 'end')
    run._element.append(fldChar_begin)
    run._element.append(instrText)
    run._element.append(fldChar_end)
    run.font.name = 'Arial'
    run.font.size = Pt(9)
    run.font.color.rgb = COLOR_GRAY

# ═══════════════════════════════════════════════════════════════════
# 主程序：生成完整首页
# ═══════════════════════════════════════════════════════════════════
def build_cover_page(output_path, data):
    """生成首页（双栏版式）"""
    doc = Document()
    setup_page(doc)
    setup_footer_header(doc)
    add_header_strip(doc, data['industry_tag'], data['report_date'])
    add_title_block(doc, data['main_title'], data['sub_title'])
    add_two_column_body(doc, data)
    # 首页结束，插入分页符
    doc.add_page_break()
    doc.save(output_path)
    return doc

# ═══════════════════════════════════════════════════════════════════
# 调用示例（华明装备 2025 年报点评）
# ═══════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    sample_data = {
        'industry_tag': '公司研究  |  工业  |  资本货物',
        'report_date': '2026 年 05 月 24 日',
        'main_title': '海外出口加速、特高压批量化投运，叠加 H 股上市启动，重申"买入"评级',
        'sub_title': '华明装备（002270.SZ）2025 年年度报告点评',
        'rating': '买入',
        'rating_change': '维持',
        'current_price': 17.85,
        'price_date': '2026-05-22',
        'basic': {
            'high_low_52w': '21.50 / 13.20',
            'float_a': 759.22,
            'total_a': 896.23,
            'float_mv': 13544,
            'total_mv': 15996,
        },
        'price_chart_path': 'price_trend.png',  # 预先生成的图片路径
        'related_reports': [
            {'title': '华明装备 2024 年年报点评', 'date': '2025-04-28'},
            {'title': '华明装备 2025 年中报点评', 'date': '2025-08-30'},
            {'title': '输变电设备行业深度报告', 'date': '2024-12-15'},
        ],
        'analyst': {
            'name': 'XXX',
            'cert_id': 'S0020522110002',
            'phone': '021-51097188',
            'email': 'xxx@gyzq.com.cn',
        },
        'broker': '国元',
        'report_points': [
            {
                'headline': '业绩判定：电力设备主业符合预期，海外出口大超预期',
                'body': '华明装备发布 2025 年年报：全年实现营业收入 24.27 亿元（同比 +4.50%），归母净利润 7.10 亿元（同比 +15.54%），扣非净利润 6.71 亿元（同比 +15.27%）。剔除股权激励费用 0.38 亿元后扣非净利润达 7.09 亿元（同比 +21.79%），真实经营业绩超此前团队及市场一致预期。',
            },
            {
                'headline': '海外出口大超预期，全球化布局正式进入兑现期',
                'body': '电力设备业务直接 + 间接出口 7.14 亿元（+47.37%）。印尼工厂正式投产 + 土耳其工厂稳定运营 + 新加坡区域总部成立。我们判断公司海外业务有望在 2026-2027 年保持 35-45% 高速增长。',
            },
            {
                'headline': '特高压 CHVT 批量化投运，打破海外品牌垄断',
                'body': 'CHVT 型换流变分接开关在陇东至山东 ±800kV 特高压直流输电工程批量投运。国家电网"十五五"4 万亿投资落地后，公司是国内分接开关环节几乎唯一受益标的。',
            },
            {
                'headline': '维持"买入"评级，上调目标价至 21.50 元',
                'body': '上调 2026-2028E 归母净利润预测至 8.55 / 10.10 / 11.65 亿元。给予 2026E 22.5x PE，对应目标价 21.50 元，较当前股价有 +20.4% 上行空间。',
            },
        ],
        'fin_table': {
            'revenue': [2146.07, 2323.45, 2427.05, 2855.32, 3340.96],
            'rev_yoy': [25.38, 8.27, 4.50, 17.65, 17.00],
            'np': [541.11, 614.50, 710.05, 855.20, 1010.30],
            'np_yoy': [50.54, 13.56, 15.54, 20.44, 18.13],
            'roe': [16.08, 18.74, 22.04, 23.50, 24.20],
            'eps': [0.60, 0.69, 0.79, 0.96, 1.13],
            'pe': [29.75, 25.87, 22.59, 18.59, 15.84],
        },
    }
    build_cover_page('华明装备_002270.SZ_2025A_业绩点评研报_首页.docx', sample_data)
    print('首页生成完毕')
```

### 关键设计要点

| 要点 | 说明 |
| :--- | :--- |
| **布局容器** | 必须用 `add_table(rows=1, cols=2)` 的**无边框表格**做双栏容器 — **不能**用 add_paragraph 顺序堆 |
| **列宽锁定** | `layout.autofit = False` + `columns[i].width = Cm(...)` 防止自动调整 |
| **垂直对齐** | 两栏均 `vertical_alignment = WD_ALIGN_VERTICAL.TOP` |
| **嵌套表格** | 左栏内财务摘要表、右栏内评级框都是嵌套 table — python-docx 完全支持 |
| **段间分隔线** | 右栏每段开始时给当前段落加 `pBdr/top` 的 0.5pt 灰线 |
| **三线表** | 财务摘要表必须用 `apply_three_line_table_borders()` 函数清掉网格，只保留顶 / 表头底 / 底三条线 |
| **中文字体** | 必须同时设 `run.font.name` 与 `rFonts.eastAsia` 两处，否则中文不会切换字体 |
| **颜色填充** | 通过 OxmlElement 注入 `w:shd` 元素实现单元格背景色 |
| **页码字段** | 用 OxmlElement 注入 `fldChar` + `PAGE` / `NUMPAGES` 字段，确保打开 Word 时自动计算 |

### 调用流程图

```
build_cover_page(path, data)
        │
        ├─→ setup_page(doc)              ← A4 + 边距
        ├─→ setup_footer_header(doc)     ← 页眉/页脚
        ├─→ add_header_strip(doc, ...)   ← 区段 A
        ├─→ add_title_block(doc, ...)    ← 区段 B
        └─→ add_two_column_body(doc, data)  ← 区段 C
                  │
                  ├─→ fill_left_column(cell, data)
                  │       ├─→ "报告要点" 标题
                  │       ├─→ 4 个 ▎ 段落
                  │       ├─→ 嵌套 8×6 财务摘要表
                  │       └─→ 资料来源
                  │
                  └─→ fill_right_column(cell, data)
                          ├─→ 评级框（嵌套 1×1 红底表）
                          ├─→ 当前价 块
                          ├─→ 基本数据（分隔线 + 5 字段）
                          ├─→ 股价走势图（分隔线 + 图片）
                          ├─→ 相关研究（分隔线 + 3 条）
                          └─→ 报告作者（分隔线 + 4 字段）
```

### 视觉验收清单

生成首页后必检以下 8 项，**任一项不达标都要返工**：

- [ ] **左右栏可视分离**：左栏正文与右栏 Panel **明显左右排开**，不是上下堆叠
- [ ] **评级框红色高亮**：右栏顶部"买入 | 维持"是红底白字 14pt 加粗
- [ ] **当前价红色加大**：右栏"17.85 元"是 18pt Arial 加粗红色
- [ ] **左栏要点段以 ▎ 红色标记开头**：每段独立 paragraph 而非 bullet list
- [ ] **财务摘要表三线表样式**：仅顶/表头底/底三条线，无网格
- [ ] **右栏段间灰色分隔线**：基本数据 / 股价图 / 相关研究 / 报告作者**各段之间**有 0.5pt 灰线
- [ ] **页眉粗深蓝线**：标题区上方有 2pt 深蓝色横线
- [ ] **页脚"1 / 14"**：右下角自动显示页码

---

## 第 2-3 页：财报整体业绩拆解

### 2.1 收入端深度拆解（约 1 页）

#### 子章节标题示例

**Q3 单季营收 X.XX 亿元创历史新高，超 Wind 一致预期 X.X%**

[正文段落 - 6-8 段 - 详细分析]

包含子项：
1. 单季营收 YoY / QoQ 变动 + 历史季节性对比
2. 累计前三季度营收变动 + 完成全年指引进度
3. 与 Wind 一致预期偏差归因
4. 与业绩预告中枢偏差归因
5. α/β 拆解

#### 嵌入图表

**图 1：近 8 个季度单季营业收入及同比增速**（柱状 + 折线叠加）

**Figure 1 - Q3 2023 至 Q3 2025 单季营业收入及同比增速**

[图表占位 - 8cm × 5cm]

```
数据来源：公司历年定期报告（巨潮资讯网）
[点击跳转：http://www.cninfo.com.cn/new/disclosure/stock?stockCode=002270]
```

### 2.2 利润端深度拆解（约 1 页）

#### 子章节标题示例

**归母净利润 X.XX 亿元，业绩落入预告上限位置；扣非占比 XX% 业绩纯净度高**

[正文段落 - 详细分析三档利润口径]

#### 嵌入图表

**图 2：近 8 个季度单季归母净利润 vs 扣非净利润对比**（双柱状图）

#### 关键勾稽表（核心表 3/3）

```
┌────────────────────────────────────────────────────────────────────┐
│ 表 3：单季三档利润口径勾稽（百万元）                                │
├──────────────────────┬──────────┬──────────┬──────────┬───────────┤
│ 项目                 │ Q3 2024  │ Q2 2025  │ Q3 2025  │ YoY 变动  │
├──────────────────────┼──────────┼──────────┼──────────┼───────────┤
│ 营业收入             │ XXX      │ XXX      │ XXX      │ +XX%      │
│ 营业成本             │ XXX      │ XXX      │ XXX      │ +XX%      │
│ 毛利                 │ XXX      │ XXX      │ XXX      │ +XX%      │
│ 毛利率               │ XX.X%    │ XX.X%    │ XX.X%    │ +X.Xpct   │
│                      │          │          │          │           │
│ 销售费用             │ XX       │ XX       │ XX       │ +X%       │
│ 管理费用             │ XX       │ XX       │ XX       │ +X%       │
│ 其中：股权激励摊销   │ X        │ X        │ X        │ +X%       │
│ 研发费用             │ XX       │ XX       │ XX       │ +X%       │
│ 财务费用             │ X        │ X        │ X        │ +X%       │
│                      │          │          │          │           │
│ 营业利润             │ XX       │ XX       │ XX       │ +XX%      │
│ 利润总额             │ XX       │ XX       │ XX       │ +XX%      │
│ 所得税               │ X        │ X        │ X        │ +X%       │
│ 净利润               │ XX       │ XX       │ XX       │ +XX%      │
│ 少数股东损益         │ X        │ X        │ X        │ +X%       │
│ 归母净利润           │ XX       │ XX       │ XX       │ +XX%      │
│ 非经常性损益         │ X        │ X        │ X        │ +X%       │
│ 扣非归母净利润       │ XX       │ XX       │ XX       │ +XX%      │
│ 扣非占归母比例       │ XX%      │ XX%      │ XX%      │ +Xpct     │
└──────────────────────┴──────────┴──────────┴──────────┴───────────┘

数据来源：公司《2025 年第三季度报告》（公告日期：2025-10-27）
```

#### 嵌入图表

**图 3：近 5 年毛利率 / 净利率走势曲线**

---

## 第 4-5 页：业务板块经营穿透与财务质量把脉

### 4.1 业务板块量价拆解（约 1 页）

#### 分产品 / 分业务

[正文分析每个板块的量价驱动]

#### 嵌入图表

**图 4：业务板块收入结构拆分**（堆叠柱状图）

#### 分地区（如适用）

[正文分析国内 / 海外结构]

### 4.2 财务质量穿透与 A 股地雷监控（约 1 页）

#### 净现比与回款质量

[正文 + 关键指标计算]

#### 资产负债表蓄水池

**重点关注：合同负债 + 应收账款 + 存货周转**

#### 嵌入图表

**图 5：四费率季度走势叠加**

**图 6：应收账款 / 存货周转天数历史对比**

**图 7：合同负债期末余额季度环比变动**

#### A 股特色地雷监控强制审查

```
─────────────────────────────────────────────────────────────────
A 股地雷监控审查表（强制核查项）

商誉账面价值：           X.XX 亿元（占总资产 X%，[无 / 有] 减值迹象）
非经常性损益占比：       X.X%（[健康 / 警示]，警戒线 30%）
应收账款周转天数：       XX 天（YoY ±X 天，行业均值 XX 天）
存货周转天数：           XX 天（YoY ±X 天，行业均值 XX 天）
控股股东累计质押比例：   X.X%（[正常 / 警示 / 高危]，警戒线 70%）
报告期前后 30 日减持：   XX 万股（占总股本 X.X%，[无 / 轻微 / 显著]）
研发投入资本化比例：     XX%（科创板硬指标核查）

整体地雷评级：[绿色无忧 / 黄色关注 / 红色预警]
─────────────────────────────────────────────────────────────────

数据来源：公司财报附注、巨潮资讯网"权益变动"与"股份减持"专栏
[点击查阅最新质押公告] [点击查阅最新减持公告]
```

---

## 第 6-7 页：行业格局与投资逻辑动态再评估

### 6.1 行业景气度跟踪（约 1 页）

[行业宏观数据：PMI、行业景气指数、政策催化（如"十五五"规划）、原材料价格走势、海外需求]

### 6.2 投资逻辑三大支柱动态评估

针对首次覆盖报告中确立的投资逻辑支柱，本季度业绩对其是 **加强** / **维持** / **削弱**：

```
■ 逻辑支柱 1：[原投资逻辑陈述]

  状态：[加强 / 维持 / 削弱]

  Q3 业绩 [支持 / 挑战] 该逻辑支柱，原因 [具体证据]。[详细分析 150-200 字]

■ 逻辑支柱 2：[原投资逻辑陈述]

  [类似分析]

■ 逻辑支柱 3：[原投资逻辑陈述]

  [类似分析]
```

### 6.3 新增催化剂 / 风险点识别

[列出新出现的正面催化与负面风险]

#### 嵌入图表

**图 8：实际业绩 vs Wind 一致预期 vs 业绩预告中枢三方偏差对比**

---

## 第 8-10 页：估值与盈利预测

### 8.1 盈利预测假设详解（约 1 页）

#### 关键驱动假设（自适应配置）

```
─────────────────────────────────────────────────────────────────
未来 3 年关键假设（更新于本次点评）：

板块 A 收入：
- 2025E：XX 亿（YoY +X%），主因 [产能释放 / 大客户突破]
- 2026E：XX 亿（YoY +X%）
- 2027E：XX 亿（YoY +X%）

板块 B 收入：
- 2025E：XX 亿（YoY +X%）
...

毛利率假设：
- 2025E：XX.X%（受益于 [因素]）
- 2026E：XX.X%
- 2027E：XX.X%

四费率假设：
- 2025E 销售费用率：X.X%
- 2025E 管理费用率：X.X%
- 2025E 研发费用率：X.X%
- 2025E 财务费用率：X.X%
─────────────────────────────────────────────────────────────────
```

### 8.2 估值矩阵与可比公司对比（约 1 页）

#### 估值方法选择说明

**根据 [公司所属行业]，本次采用 [PE-Band / PB-Band / PB-ROE / PS-Band / 综合估值] 作为主估值方法。**

#### PE-Band 估值通道（成长股默认）

**图 9：公司历史 PE-Band 估值通道**（折线图叠加 ±1σ 区间，含历史均值线）

#### 可比公司估值对标表

```
┌──────────────────────────────────────────────────────────────────────────┐
│ 表：可比公司估值对比（截至 2025-10-27）                                   │
├──────────────┬─────────┬─────────┬──────┬──────┬──────┬──────┬───────────┤
│ 公司         │ 代码    │ 市值    │ 2025E│ 2026E│ 2025E│ 2026E│ ROE 2025E │
│              │         │（亿元） │ PE   │ PE   │ PB   │ PB   │           │
├──────────────┼─────────┼─────────┼──────┼──────┼──────┼──────┼───────────┤
│ 华明装备     │ 002270  │ XXX     │ XX   │ XX   │ X.X  │ X.X  │ XX%       │
│ 思源电气     │ 002028  │ XXX     │ XX   │ XX   │ X.X  │ X.X  │ XX%       │
│ 平高电气     │ 600312  │ XXX     │ XX   │ XX   │ X.X  │ X.X  │ XX%       │
│ 国电南瑞     │ 600406  │ XXXX    │ XX   │ XX   │ X.X  │ X.X  │ XX%       │
├──────────────┼─────────┼─────────┼──────┼──────┼──────┼──────┼───────────┤
│ 可比均值     │ —       │ —       │ XX   │ XX   │ X.X  │ X.X  │ XX%       │
│ 可比中位数   │ —       │ —       │ XX   │ XX   │ X.X  │ X.X  │ XX%       │
└──────────────┴─────────┴─────────┴──────┴──────┴──────┴──────┴───────────┘

数据来源：Wind 一致预期（截至 2025-10-27 收盘）
```

#### 嵌入图表

**图 10：可比公司 2026E PE / PB 估值多维度对比**

**图 11：公司 PB-ROE 散点图（含可比公司）** — 适用于高 ROE 消费医药白马股

#### 标准 DCF 估值表（可选 - 若主估值方法用 DCF）⭐

**触发条件**：当公司属于稳定经营 / 成熟期 / 现金流可预测的标的，且主估值方法选择 DCF 时，必须按以下标准格式呈现。**禁止仅给一个内在价值数字，必须完整披露假设、两阶段 FCFF、估值汇总**。参考中信建投《紫光股份》图表 58。

```
┌─────────────────────────────────────────────────────────────────────┐
│ 表：DCF 估值表                                                       │
├─────────────────────────────────────────────────────────────────────┤
│ 【假设】                                                              │
│ 第二阶段年数              8 年                                       │
│ 第二阶段增长率            5.00%                                      │
│ 长期增长率                2.00%                                      │
│ 无风险利率 Rf             3.00%   （10 年期中国国债收益率）           │
│ β                         1.11                                       │
│ Rm                        8.50%   （沪深 300 近 10 年滚动平均收益）   │
│ Ke                        9.10%                                      │
│ 税率                      15%     （高新技术企业，需核查认定有效期） │
│ Kd                        4.50%                                      │
│ Ve                        xxx,xxx （股权价值，百万元）               │
│ Vd                        x,xxx   （债务价值，百万元）               │
│ WACC                      7.85%                                      │
├─────────────────────────────────────────────────────────────────────┤
│ 【第一阶段：明确预测期 FCFF（百万元）】                              │
│              2026E    2027E    2028E    2029E    2030E               │
│ FCFF         x,xxx    x,xxx    x,xxx    x,xxx    x,xxx               │
├─────────────────────────────────────────────────────────────────────┤
│ 【第二阶段：稳定增长期 FCFF（百万元）】                              │
│              2031E    2032E    2033E    2034E    2035E ... 2038E      │
│ FCFF         x,xxx    x,xxx    x,xxx    x,xxx    x,xxx     x,xxx     │
├─────────────────────────────────────────────────────────────────────┤
│ 【FCFF 估值汇总】                                                    │
│                          现金流折现值（百万元）   价值百分比         │
│ 第一阶段                 xx,xxx                  xx.xx%              │
│ 第二阶段                 xx,xxx                  xx.xx%              │
│ 第三阶段（终值）         xx,xxx                  xx.xx%              │
│ ───────────────────────────────────────────                          │
│ 企业价值 AEV             xxx,xxx                 100.00%             │
│ ＋非核心资产             x,xxx                                       │
│ －少数股东权益           x,xxx                                       │
│ －净债务                 x,xxx                                       │
│ ───────────────────────────────────────────                          │
│ 总股本价值               xxx,xxx                                     │
│ 股本（百万股）           x,xxx                                       │
│ 每股价值（元）           xx.xx                                       │
└─────────────────────────────────────────────────────────────────────┘

数据来源：Wind 一致预期 / [券商] 研究所测算
注：A 股市场参数本土化要求详见 dcf-cn skill 的 references/best-practices.md。
```

**A 股市场 DCF 参数典型区间速查表**：

| 参数 | A 股典型区间 | 数据源 |
| :--- | :--- | :--- |
| Rf（10Y 国债） | 2.5% – 3.5% | 中国债券信息网 |
| Rm 或 ERP | 5% – 8% | 沪深 300 全收益 10 年滚动 |
| β（行业平均） | 0.8 – 1.5 | Wind 60 周回归 |
| 税率 | 15% / 25% | 高新技术企业 vs 标准 |
| WACC（综合） | 7% – 10% | 上述参数计算 |
| 长期增长率 g | 1.5% – 3.5% | 中国长期 GDP+CPI 上限 |
| 第二阶段增长率 | 3% – 6% | 公司中期成长性 |

### 8.3 敏感性分析与目标价推导（约 1 页）

#### 二维敏感性分析表

```
┌────────────────────────────────────────────────────────────────┐
│ 表：2026E EPS 二维敏感性（关键变量 × 关键变量）                 │
├─────────────┬─────────────────────────────────────────────────┤
│ 海外出货占比│ 国内特高压招标量（吉瓦）                         │
│             ├─────────┬─────────┬─────────┬─────────┬─────────┤
│             │ XX      │ XX      │ XX      │ XX      │ XX      │
├─────────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│ 15%         │ X.XX    │ X.XX    │ X.XX    │ X.XX    │ X.XX    │
│ 20%         │ X.XX    │ X.XX    │ X.XX    │ X.XX    │ X.XX    │
│ 25%（基准） │ X.XX    │ X.XX    │ X.XX    │ X.XX    │ X.XX    │
│ 30%         │ X.XX    │ X.XX    │ X.XX    │ X.XX    │ X.XX    │
│ 35%         │ X.XX    │ X.XX    │ X.XX    │ X.XX    │ X.XX    │
└─────────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
```

#### 情景分析

```
─────────────────────────────────────────────────────────────────
情景            EPS 2026E    目标 PE    目标价    相对当前涨幅
─────────────────────────────────────────────────────────────────
乐观情景        X.XX 元      XX 倍      XX.XX 元    +XX%
中性情景（基准）X.XX 元      XX 倍      XX.XX 元    +XX%
悲观情景        X.XX 元      XX 倍      XX.XX 元    +XX%
─────────────────────────────────────────────────────────────────
```

#### 目标价推导

```
目标价推导（中性情景）：
- 2026E EPS：X.XX 元
- 目标 PE：XX 倍（[溢价 / 折价] 于可比公司均值 XX 倍，理由：成长性溢价 / 龙头溢价 / 海外业务 alpha）
- 目标价 = X.XX × XX = XX.XX 元
- 当前股价 XX.XX 元（2025-10-27 收盘）
- 绝对收益预期：+XX%（未来 6-12 个月）
- 相对沪深 300 超额收益预期：+XX%（假设沪深 300 同期涨跌 +/-X%）

评级决策：维持"买入"（前次"买入"），上调目标价至 XX.XX 元（前次 XX.XX 元）
```

#### 嵌入图表

**图 12（可选）：北上资金陆股通持股比例变动趋势**

---

## 第 13 页：附录·财务预测表 ⭐⭐⭐【国内研报硬性强制】

⚠️ **本节是国内卖方研报与海外 sell-side note 的最大架构差异**。国元证券、中信建投、海通证券、华泰证券、招商证券等所有主流券商在报告末尾（参考资料章节前）必须附 **5 年完整三表预测 + 主要财务比率**。**禁止省略**，也**禁止只给摘要**。

参考样式：国元证券《华明装备 2024-02-01 跟踪报告》第 14 页。**典型排版**：单页两栏并排：左栏 = 资产负债表，右栏 = 利润表；下一页左栏 = 现金流量表，右栏 = 主要财务比率。

### 13.1 资产负债表预测（单位：百万元）

```
┌──────────────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ 会计年度          │ 2023A    │ 2024A    │ 2025E    │ 2026E    │ 2027E    │
├──────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│ 【流动资产】      │          │          │          │          │          │
│   现金            │ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │
│   应收账款        │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│   其他应收款      │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│   预付账款        │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│   存货            │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│   其他流动资产    │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│ 【非流动资产】    │          │          │          │          │          │
│   长期股权投资    │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│   固定资产        │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│   在建工程        │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│   无形资产        │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│   商誉            │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│   其他非流动资产  │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│ 【资产总计】      │ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │
│ 【流动负债】      │          │          │          │          │          │
│   短期借款        │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│   应付账款        │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│   合同负债        │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│   其他流动负债    │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│ 【非流动负债】    │          │          │          │          │          │
│   长期借款        │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│   其他非流动负债  │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│ 【负债合计】      │ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │
│ 【所有者权益】    │          │          │          │          │          │
│   归属母公司      │ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │
│   少数股东权益    │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│ 【负债和所有者权益│ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │
└──────────────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```

### 13.2 利润表预测（单位：百万元）

```
┌──────────────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ 会计年度          │ 2023A    │ 2024A    │ 2025E    │ 2026E    │ 2027E    │
├──────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│ 营业收入          │ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │ x,xxx.xx │
│ 营业成本          │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│ 营业税金及附加    │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│ 销售费用          │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│ 管理费用          │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│ 研发费用          │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│ 财务费用          │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│ 资产减值损失      │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│ 公允价值变动收益  │     x.xx │     x.xx │     x.xx │     x.xx │     x.xx │
│ 投资净收益        │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│ 营业利润          │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│ 营业外收入        │     x.xx │     x.xx │     x.xx │     x.xx │     x.xx │
│ 营业外支出        │     x.xx │     x.xx │     x.xx │     x.xx │     x.xx │
│ 利润总额          │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│ 所得税            │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│ 净利润            │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│ 少数股东损益      │     x.xx │     x.xx │     x.xx │     x.xx │     x.xx │
│ 归属母公司净利润  │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│ EBITDA            │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│ EPS（元）         │     x.xx │     x.xx │     x.xx │     x.xx │     x.xx │
└──────────────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```

### 13.3 现金流量表预测（单位：百万元）

```
┌──────────────────────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ 会计年度                  │ 2023A    │ 2024A    │ 2025E    │ 2026E    │ 2027E    │
├──────────────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│ 【经营活动现金流】        │          │          │          │          │          │
│   净利润                  │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│   折旧摊销                │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│   财务费用                │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│   投资损失                │     x.xx │     x.xx │     x.xx │     x.xx │     x.xx │
│   营运资金变动            │   -xx.xx │   -xx.xx │   -xx.xx │   -xx.xx │   -xx.xx │
│   其他经营现金流          │     x.xx │     x.xx │     x.xx │     x.xx │     x.xx │
│   经营活动现金流净额      │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
│ 【投资活动现金流】        │          │          │          │          │          │
│   资本支出                │  -xxx.xx │  -xxx.xx │  -xxx.xx │  -xxx.xx │  -xxx.xx │
│   长期投资                │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│   其他投资现金流          │     x.xx │     x.xx │     x.xx │     x.xx │     x.xx │
│   投资活动现金流净额      │  -xxx.xx │  -xxx.xx │  -xxx.xx │  -xxx.xx │  -xxx.xx │
│ 【筹资活动现金流】        │          │          │          │          │          │
│   短期借款增加            │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│   长期借款增加            │    xx.xx │    xx.xx │    xx.xx │    xx.xx │    xx.xx │
│   普通股增加              │     x.xx │     x.xx │     x.xx │     x.xx │     x.xx │
│   现金股利分红            │   -xx.xx │   -xx.xx │   -xx.xx │   -xx.xx │   -xx.xx │
│   其他筹资现金流          │     x.xx │     x.xx │     x.xx │     x.xx │     x.xx │
│   筹资活动现金流净额      │   -xx.xx │   -xx.xx │   -xx.xx │   -xx.xx │   -xx.xx │
│ 【现金净增加额】          │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │   xxx.xx │
└──────────────────────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```

### 13.4 主要财务比率（强制 5 大类）

```
┌──────────────────────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
│ 会计年度                  │ 2023A   │ 2024A   │ 2025E   │ 2026E   │ 2027E   │
├──────────────────────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│ 【成长能力】              │         │         │         │         │         │
│   营业收入（%）           │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │
│   归母净利润（%）         │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │
│   EBITDA（%）             │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │
│ 【获利能力】              │         │         │         │         │         │
│   毛利率（%）             │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │
│   净利率（%）             │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │
│   ROE（加权，%）          │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │
│   ROIC（%）               │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │
│ 【偿债能力】              │         │         │         │         │         │
│   资产负债率（%）         │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │
│   净负债比率（%）         │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │
│   流动比率                │ x.xx    │ x.xx    │ x.xx    │ x.xx    │ x.xx    │
│   速动比率                │ x.xx    │ x.xx    │ x.xx    │ x.xx    │ x.xx    │
│ 【营运能力】              │         │         │         │         │         │
│   总资产周转率            │ x.xx    │ x.xx    │ x.xx    │ x.xx    │ x.xx    │
│   应收账款周转率          │ x.xx    │ x.xx    │ x.xx    │ x.xx    │ x.xx    │
│   存货周转率              │ x.xx    │ x.xx    │ x.xx    │ x.xx    │ x.xx    │
│ 【每股指标 & 估值】       │         │         │         │         │         │
│   每股收益（元）          │ x.xx    │ x.xx    │ x.xx    │ x.xx    │ x.xx    │
│   每股经营现金流（元）    │ x.xx    │ x.xx    │ x.xx    │ x.xx    │ x.xx    │
│   每股净资产（元）        │ x.xx    │ x.xx    │ x.xx    │ x.xx    │ x.xx    │
│   P/E                     │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │
│   P/B                     │ x.xx    │ x.xx    │ x.xx    │ x.xx    │ x.xx    │
│   EV/EBITDA               │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │ xx.xx   │
└──────────────────────────┴─────────┴─────────┴─────────┴─────────┴─────────┘

数据来源：公司年报、本团队预测模型。
```

### 13.5 附录排版强制规范

- **页面布局**：第 13 页采用**两栏并排**（资产负债表左 / 利润表右），第 14 页两栏并排（现金流左 / 财务比率右），节省页数
- **字号**：表头 9pt 加粗，表格正文 8pt（小五），单位标注 8pt 灰色
- **数字格式**：保留 2 位小数，右对齐，负数用括号或减号
- **科目顺序**：严格按 CAS 准则定期报告的科目顺序，**不得**省略商誉、合同负债、研发费用等 A 股关键科目
- **数据源标注**：表格底部统一注"数据来源：公司年报、本团队预测模型"

---

## 第 11-12 页：风险提示 + 免责声明 + 参考资料

### 11.1 风险提示（强制 3+ 项，量化 + 三层结构）

```
─────────────────────────────────────────────────────────────────
风险提示

一、宏观层面风险
1. 经济下行风险：若 2026 年宏观经济增速降至 X% 以下，下游电力投资可能
   缩减，对公司订单造成不利影响。敏感性测算显示，宏观 GDP 增速每下降
   1pct，预计公司营收增速下行 X-Xpct。

二、行业层面风险
2. 原材料价格波动风险：硅钢片 / 铜材占公司直接材料成本约 XX%，若 2026
   年价格上涨 10%，预计毛利率下行 X-Xpct，EPS 下行 X-X%。
3. 国家电网招标节奏不及预期风险：若特高压招标量低于本团队预期 XX%，
   2026E 营收预测下调风险 X-Xpct。
4. 海外贸易壁垒风险：欧美对中国电力设备的反倾销 / 反补贴调查升级，可
   能影响海外业务出货节奏。

三、公司层面风险
5. 大客户集中风险：前五大客户收入占比 XX%，若主要客户订单下滑，对公
   司业绩冲击较大。
6. 应收账款回款风险：截止 2025 Q3 末应收账款 X.XX 亿元，若回款周期
   延长 30 天，预计现金流压力上升。
7. 商誉减值风险：账面商誉 X.XX 亿元，若 2025 年并购标的业绩不达承诺
   值，存在 X-X 亿元减值风险。
8. 股权激励解锁风险：若 2025-2027 年业绩考核未达标，可能影响管理团
   队稳定性。
─────────────────────────────────────────────────────────────────
```

### 11.2 完整参考资料与信息来源

```
─────────────────────────────────────────────────────────────────
参考资料及信息来源

一、上市公司官方公告
• 《2025 年第三季度报告全文》（公告日期：2025-10-27）
  [点击跳转巨潮资讯网公告原文]
• 《2025 年前三季度业绩预告》（公告日期：2025-10-12）
  [点击跳转业绩预告原文]
• 《2025 年半年度报告全文》（公告日期：2025-08-30）
  [点击跳转半年报原文]
• 《2024 年度报告全文》（公告日期：2025-04-25）
  [点击跳转年报原文]

二、投资者关系活动记录
• 《深交所投资者关系活动记录表（2025-10-28 调研）》
  [点击跳转深交所互动易凭证]
• 《2025 年度业绩说明会会议纪要》
  [点击跳转上证 e 互动 / 深交所互动易]

三、第三方数据终端
• 万得（Wind）金融终端：盈利预测一致预期（截至 2025-10-25）
• 东方财富 Choice：北上资金陆股通持股变动（截至 2025-10-27 收盘）
• 同花顺 iFinD：机构调研频次排名（2025 Q3）
• 港交所披露易：QFII / 沪深股通持股明细
  [点击跳转 https://sc.hkexnews.hk/...]

四、监管法规依据
• 中国证券业协会《发布证券研究报告执业规范》
• 中国证监会《上市公司信息披露管理办法》
• 上海 / 深圳证券交易所《上市公司自律监管指引》
─────────────────────────────────────────────────────────────────
```

### 11.3 标准免责声明（券商执业规范强制要求）

```
─────────────────────────────────────────────────────────────────
分析师承诺

负责本研究报告的分析师特此声明：本人具有中国证券业协会授予的证券投资
咨询执业资格，本报告所采用的数据均来自合规渠道，分析逻辑基于本人专业
理解，准确反映本人观点。本人的薪酬不会因本报告中具体的推荐意见或观点
而支付。

免责声明

本报告仅供 [券商名称] 客户使用。客户应当认识到，证券市场和金融市场存
在固有的风险，本报告中所提及的任何证券、投资组合或衍生品价格均可能波
动，过往业绩不预示未来表现。客户在投资决策前应自行判断本报告所载内容
和观点的合理性，并就投资决策征求各方面专业人士的意见。

本报告基于公开信息编制，但本公司对相关信息的准确性、完整性、时效性不
做任何保证。本报告中的任何分析意见仅代表本报告作者发布之日的观点和判
断，本公司或其关联机构有权随时更改而不另行通知。

本报告版权归 [券商名称] 所有，未经本公司书面许可，任何机构或个人不得
以任何形式翻版、复制和发布。

投资评级体系说明（未来 6-12 个月相对沪深 300 指数收益）：
- 买入：相对沪深 300 超额收益 > 15%
- 增持：相对沪深 300 超额收益 5% - 15%
- 中性：相对沪深 300 超额收益 -5% - 5%
- 减持：相对沪深 300 超额收益 -15% - -5%
- 卖出：相对沪深 300 超额收益 < -15%

行业评级体系说明：
- 强于大市：相对沪深 300 超额收益 > 10%
- 同步大市：相对沪深 300 超额收益 -10% - 10%
- 弱于大市：相对沪深 300 超额收益 < -10%
─────────────────────────────────────────────────────────────────
```

---

## 第 14 页：分析师介绍 + 研究服务联系人 ⭐【国内研报硬性章节】

⚠️ 国内顶级券商研报末尾必须含"分析师介绍 + 报告贡献人 + 研究服务联系人"完整模块。参考中信建投《紫光股份》第 28 页。

### 14.1 分析师介绍

```
─────────────────────────────────────────────────────────────────
分析师介绍

[姓名]：[所属行业] 首席分析师，[毕业院校] 学士 / 硕士 / 博士，
近 X 年 [行业 / 公司] 工作经验，X 年证券研究经验。专注于 [细分
赛道 1]、[细分赛道 2]、[细分赛道 3] 等领域研究。系 X 年《新
财富》、《水晶球》、Wind [行业] 最佳分析师 [第 N 名]，X 年金
牛奖最佳分析师 [团队核心成员 / 团队负责人]。
─────────────────────────────────────────────────────────────────
```

**关键字段约定**：
- **毕业院校**：通常列出最高学历院校（清华 / 北大 / 复旦 / 上海交大 / 中国人大 / 中科大等优先）
- **工作经验**：列出在金融机构或实体行业的总年限（如"近 8 年中国移动工作经验"）
- **研究经验**：列出在卖方研究所的总年限
- **专注领域**：列出 3-5 个细分赛道（不能过于宽泛）
- **获奖情况**：必须给出具体年份与排名（如"2019 年第一名"、"连续 5 年第一名团队核心成员"）
- **首席分析师 / 高级分析师 / 分析师** 三档头衔须如实标注

### 14.2 报告贡献人

```
─────────────────────────────────────────────────────────────────
报告贡献人

[贡献人 1 姓名]  010-XXXXXXXX  [邮箱]
[贡献人 2 姓名]  021-XXXXXXXX  [邮箱]
─────────────────────────────────────────────────────────────────
```

**说明**：
- 报告贡献人指对报告有实质性贡献但非主笔分析师的研究员
- 通常为助理分析师 / 行业研究员
- 至少列出 1 名，最多 3 名

### 14.3 研究服务联系人（强制 5 大销售组）

```
─────────────────────────────────────────────────────────────────
研究服务

北京机构销售组（保险 / 公募 / 社保）
  [姓名 1]  010-XXXXXXXX  [邮箱 1]
  [姓名 2]  010-XXXXXXXX  [邮箱 2]
  [姓名 3]  010-XXXXXXXX  [邮箱 3]

上海机构销售组（公募 / 私募 / 险资）
  [姓名 1]  021-XXXXXXXX  [邮箱 1]
  [姓名 2]  021-XXXXXXXX  [邮箱 2]
  [姓名 3]  021-XXXXXXXX  [邮箱 3]

深圳 / 广州机构销售组
  [姓名 1]  0755-XXXXXXXX  [邮箱 1]
  [姓名 2]  0755-XXXXXXXX  [邮箱 2]

公募基金销售专组
  [姓名 1]  XXX-XXXXXXXX  [邮箱 1]

保险资管销售专组
  [姓名 1]  XXX-XXXXXXXX  [邮箱 1]

海外 / QFII 销售组（可选）
  [姓名 1]  XXX-XXXXXXXX  [邮箱 1]
─────────────────────────────────────────────────────────────────
```

**强制要求**：
- 最少含 3 个销售组（北京 / 上海 / 深圳）
- 每组列 2-5 名联系人
- 电话区号必须匹配（北京 010 / 上海 021 / 深圳 0755 / 广州 020 / 杭州 0571）
- 邮箱后缀须与发布机构一致（如 @csc.com.cn / @gyzq.com.cn）

### 14.4 页眉页脚水印规范

**页眉**（所有页）：
```
请务必阅读正文之后的免责条款部分
```
- 字号：9pt
- 颜色：灰色 #595959
- 位置：页面顶部居中（或左对齐）
- 与正文之间用细黑线分隔

**页脚**（所有页）：
```
                                                          [当前页] / [总页数]
```
- 字号：9pt
- 颜色：灰色 #595959
- 位置：右下角（如 "3 / 15"）

**底部水印**（可选，模拟券商研究所发布）：
```
[研究所唯一识别码] 用户 [机构 ID] 于 YYYY-MM-DD 日下载，仅供本人内部使用，不可传播与转载
```
- 字号：7pt
- 颜色：极浅灰 #BFBFBF
- 位置：每页底部最下方一行
- 国内研报均带此水印作为防止盗版传播的标识

---

## 排版与格式硬性要求

### 1. 第 1 页强制要素
- 双标题（主标题观点 + 副标题公司+期间+点评类型）
- 评级 + 目标价（含前次对比）
- 三方业绩偏差汇总表
- 3-4 条 ■ 符号要点

### 2. 所有表格强制要素
- 表头深蓝底色 #1F4E79，白色字体
- 数据来源 / 出处明确，含日期
- 超链接锚文本（蓝色下划线）指向官方公告

### 3. 所有图表强制要素
- "图 X：[标题]" 标注（图上方居中）
- "数据来源：[出处]" 标注（图下方左对齐 9pt 灰色）
- 配色冷色调（深蓝 / 灰 / 红强调）

### 4. 年份与数字规范
- 实际值用 A（如 2024A）
- 预测值用 E（如 2026E）
- 百分比保留 1 位小数（如 35.2%）
- 货币单位明确（亿元 / 百万元 / 元）
- pct 表示百分点变动（如毛利率 +3.5pct）
- bps 仅用于金融行业利率类指标

### 5. 写作风格规范
- 数字打头："营业收入同比 +35.2% 至 12 亿元"（✓）
- 禁用形容词："强劲增长"（✗）
- 必须给出数据支撑的判断

### 6. 超链接合规要求 ⭐⭐⭐
- 所有 URL 必须是 Word 中可 Ctrl+Click 的蓝色下划线链接
- 链接锚文本要有意义（如"点击查阅三季报原文"），禁止裸露 URL
- 所有引用的公告 / 研报 / 终端数据均带链接
- 链接经过验证（点击可打开正确页面）

---

## 引用范例（针对具体内容）

### 业绩判定引用
```
营业收入 X.XX 亿元超 Wind 一致预期 X.X%¹

¹ Wind 一致预期截至 2025-10-25 收盘；实际数据来自公司《2025 年第三季度
  报告全文》（公告日期：2025-10-27）
  [点击查阅三季报原文：http://www.cninfo.com.cn/...]
```

### 业绩预告引用
```
归母净利润 X.XX 亿元落入业绩预告 [X.X-X.X 亿元] 上限位置²

² 业绩预告类型为"预增"，来源：公司《2025 年前三季度业绩预告》
  （公告日期：2025-10-12）
  [点击查阅业绩预告原文]
```

### 调研纪要引用
```
管理层在 10 月 28 日深交所互动易调研中提到："Q4 在手订单已达 XX 亿元"³

³ 来源：深交所投资者关系活动记录表（2025-10-28 调研）
  [点击查阅互动易调研凭证]
```

### 机构持仓引用
```
北上资金陆股通持股比例从 2025-06-30 的 X.X% 提升至 2025-10-27 的 X.X%⁴

⁴ 数据来源：港交所披露易 / 东方财富 Choice（截至 2025-10-27 收盘）
  [点击跳转港交所披露易]
```
