---
name: comps-cn
description: 构建 A 股标的的可比公司分析（Comparable Companies Analysis），输出机构级 Excel 工作簿（.xlsx），含申万行业筛选规则、A 股估值指标矩阵（PE/PB/PS/PEG/EV-EBITDA/股息率/ROE）、统计分位（中位数 / 平均数 / 25-75 分位）、Wind / Choice 一致预期取数、剔除 ST / *ST / 退市风险股 / 新股次新股、估值表与说明页一体化输出。触发关键词：'A 股可比公司'、'A 股估值对标'、'A 股 PE-PB 对比'、'申万行业可比'、'A 股估值矩阵'、'A 股相对估值'、'PEG 分析'、'A 股股息率排序'。适用范围：A 股标的；不适用纯港股 / 中概股（应触发英文 comps-analysis）。
---

# A 股可比公司分析规范 (A-share Comparable Companies Analysis)

构建符合 A 股研究规范的**可比公司分析模型**（Excel 工作簿），用于：

- 首次覆盖报告的相对估值章节
- 业绩点评报告的估值对标
- IPO / 定增 / 并购的价格区间测算
- 投委会决策支持

**核心交付物**：完整 .xlsx 文件（含数据页、Assumptions 页、估值矩阵页、统计页、说明页 5 大 sheet）。

---

## 触发场景 (When to Use)

**适用场景：**

- "做一份宁德时代的可比公司分析"
- "拉一张光伏龙头的 PE-PB 对比表"
- "对标 5 家创新药 CXO 公司的估值矩阵"
- "做特高压设备行业的相对估值"

**严禁使用本技能的场景：**

- 用户请求 DCF / 内在价值 → 触发 [dcf-cn]
- 用户请求行业综述 → 触发 [sector-overview-cn]
- 用户请求美股 / 港股可比 → 触发英文 comps-analysis
- 用户没有给具体公司（仅给行业概念）→ 应先引导用户挑出标的公司

---

## 核心执行要求

> ⚠️ 本节为骨架。主笔（邢邵楠）须按 [earnings-analysis-cn/SKILL.md](../../equity-research/skills/earnings-analysis-cn/SKILL.md) 的深度展开。

### 1. 可比公司筛选规则 ⭐ A 股本土化强制要求

**默认筛选条件**（5 条全部命中才进入候选池）：

1. **申万二级行业一致**（不用 GICS、不用 ICB；可在 references/workflow.md 中提供申万二级行业代码全表）
2. **流通市值在目标公司 ±50% 区间**（小盘对小盘、大盘对大盘）
3. **主营业务收入占比 ≥60% 一致**（避免选到多元化集团）
4. **剔除 ST / *ST / 退市风险警示股**（财务异常公司估值不可参照）
5. **剔除上市 <6 个月的新股次新股**（缺乏可比基期）

**手动调整空间**：

- 若候选池 <5 家，可放宽流通市值至 ±100%
- 若行业内 A 股可比稀缺，可加入 1-2 家**港股 / 美股海外对标**（需单独标注，不计入 A 股统计）
- 用户可手动指定可比池，但必须在 Assumptions 页留痕"用户指定，未走默认筛选"

**TODO**：邢邵楠补全申万二级行业代码与典型公司对照表（≥30 个常见行业），形成 references/workflow.md 的核心查表工具。

### 2. 估值指标矩阵（A 股标配）

每只可比公司必输出以下 8 个指标，按 TTM + 当年 E + 次年 E 三档口径展示：

| 指标 | 口径 | 数据源 |
| :--- | :--- | :--- |
| PE(TTM) | 滚动 12 个月归母净利润 | Wind / Choice 直接取 |
| PE(2025E) | Wind 一致预期 / 2025E 归母净利润 | Wind 一致预期截止日须标注 |
| PE(2026E) | Wind 一致预期 / 2026E 归母净利润 | 同上 |
| PB(MRQ) | 最新报告期净资产 | 季报披露后更新 |
| PS(TTM) | 滚动 12 个月营业收入 | Wind / Choice |
| PEG | PE(2025E) ÷ 2025E 归母净利润增速 | 一致预期 |
| EV/EBITDA(2025E) | 企业价值 / 息税折旧摊销前利润 | EV = 市值 + 净负债 |
| 股息率(TTM) | 近 12 个月分红总额 / 当前市值 | A 股投资者敏感指标 |
| ROE（加权） | 最新年报 / 半年报披露 | 财报 |

**特殊行业的指标替换**：

- 银行：弃用 PE，主用 PB + ROE + 股息率
- 保险：主用 P/EV（市值 / 内含价值）+ PB
- 地产：主用 NAV + PB
- 未盈利成长股（科创板）：主用 PS + EV/Sales
- 周期股：主用 PB 历史分位 + EV/Capacity

**TODO**：邢邵楠补全行业-估值方法映射表（参考 earnings-analysis-cn 第 5.3 节扩展）。

### 3. 统计分位分析

可比池数据必须输出 5 档统计：

- 最小值（Min）
- 25% 分位
- 中位数（Median）
- 75% 分位
- 最大值（Max）
- 算术平均数（Mean）
- 标准差（Std）

**目标公司位置标注**：

- 在中位数附近 → 估值合理
- 高于 75% 分位 → 估值偏贵，需要业绩超预期支撑
- 低于 25% 分位 → 估值偏便宜，需查明是否有"隐性问题"

**TODO**：补统计页 Excel 公式样例（百分位 PERCENTILE.INC、中位数 MEDIAN、条件格式高亮）。

### 4. 一致预期取数规范 ⭐ 时效性强制要求

- **数据源优先级**：Wind > 东方财富 Choice > 同花顺 iFinD > FactSet（A+H 标的可补 FactSet）
- **截止日期**：默认取目标公司财报披露日前 1 个交易日收盘后
- **覆盖券商数量**：须 ≥5 家覆盖才采用一致预期，<5 家须备注"覆盖券商较少，预期可信度偏低"
- **极端值处理**：剔除最高与最低各 1 家券商预期后再求均值（修剪平均法）

**TODO**：补 Wind WSD / WSS 函数与 Choice EM_API 取数代码示例。

### 5. Excel 工作簿结构 ⭐ 硬性输出规范

输出 .xlsx 必须包含且仅包含以下 5 个 sheet（顺序固定）：

1. **Cover**（封面页）：报告标题、目标公司、分析日期、分析师、合规声明
2. **Assumptions**（假设页）：可比公司筛选条件、一致预期截止日、特殊调整说明
3. **Raw Data**（原始数据页）：每家公司当期财务数据 + Wind / Choice 取数原值
4. **Valuation Matrix**（估值矩阵页）：8 大估值指标 × 3 档口径 × N 家公司
5. **Stats & Conclusion**（统计与结论页）：5 档统计 + 目标公司位置 + 估值结论

**格式规范**：

- 颜色：表头采用券商深蓝（RGB 0,32,96），数字蓝色（RGB 0,0,128），公式黑色
- 字体：Arial 9pt（数字），微软雅黑 10pt（中文标签）
- 数字格式：金额以"亿元"为单位保留 2 位小数；比率以"%"显示保留 1 位小数；倍数 PE/PB 保留 1 位小数
- **禁止硬编码**：所有计算单元格必须用公式引用 Raw Data 页，不允许直接输入数字
- **公式可追溯**：复杂公式必须用单元格批注（Comment）解释逻辑

**TODO**：李苏润提供 openpyxl 生成 .xlsx 的示例脚本（含公式写入、单元格样式、合并单元格、条件格式），主笔邢邵楠仅需在 SKILL.md 写字段约定。

### 6. 引用、溯源与合规披露 ⭐⭐⭐【硬性强制要求】

- Raw Data 页每列底部必须标注数据源（Wind 字段名 / Choice 字段名 / 公告名）
- Assumptions 页必须列出每家可比公司被选入的理由 + 是否人工调整
- Cover 页底部必须含标准免责声明
- 完全沿用 earnings-analysis-cn 第 4 节的合规规范

---

## 工作流

> 详细分步见 [references/workflow.md](references/workflow.md)。

### 阶段 1：目标公司画像（30 分钟）

- 确认目标公司申万二级行业代码
- 提取目标公司流通市值、主营业务收入占比、上市日期、ST 状态
- 调用 earnings-analysis-cn 工作流第 1 阶段的"行情核查四步法"，确保数据时效性

### 阶段 2：可比池构建（1-2 小时）

- 按 5 条筛选规则筛选 A 股全市场
- 若候选池 <5 家则放宽规则，并在 Assumptions 页记录
- 输出候选公司名单（含筛选理由）

### 阶段 3：数据拉取与原值入库（1-2 小时）

- Wind / Choice 拉取每家公司 8 大估值指标 × 3 档口径原值
- 一致预期截止日统一
- 入库 Raw Data 页

### 阶段 4：估值矩阵生成与统计分析（30 分钟）

- 公式联动生成 Valuation Matrix
- 自动计算统计分位
- 高亮目标公司在分布中的位置

### 阶段 5：结论撰写与合规质检（30 分钟）

- 一句话估值结论（合理 / 偏贵 / 偏便宜）
- 标注 3 条核心驱动（PE / PB / 股息率最显著的差异）
- 跑 [audit-xls-cn](../audit-xls-cn/) 做 Excel 公式自检

---

## 关键术语规范化清单

| 全称 | 简称 |
| :--- | :--- |
| 市盈率（动态） | 动态 PE / PE(TTM) |
| 市净率 | PB |
| 市销率 | PS |
| PE 与盈利增速之比 | PEG |
| 企业价值 / 息税折旧摊销前利润 | EV/EBITDA |
| 加权平均净资产收益率 | ROE（加权） |
| 滚动 12 个月 | TTM |
| 最近报告期 | MRQ |
| 当年预测 | 2025E |

**禁止用语清单：**

- ❌ "估值便宜值得买入" → ✅ "PE 低于行业中位数 X%，处于近 5 年 15% 分位"
- ❌ "建议关注" → ✅ "估值位于行业 25% 分位以下，需结合基本面判断"

---

## 产出物最终交付技术规范

**核心交付成果**：Excel 文件（.xlsx）

**规范文件命名**：`[公司简称]_[代码].[交易所]_可比公司分析_A股证券研究_[YYYYMMDD].xlsx`

**示例：**

- `宁德时代_300750.SZ_可比公司分析_A股证券研究_20260615.xlsx`
- `贵州茅台_600519.SH_可比公司分析_A股证券研究_20260615.xlsx`

---

## 关联参考资源库

### references/workflow.md
TODO：申万二级行业代码全表（≥30 个）；Wind WSD / WSS 函数与 Choice EM_API 取数代码模板；ST 股识别脚本；新股次新股查询接口。

### references/report-structure.md
TODO：5 sheet 详细模板（每个 sheet 的列结构、字体、颜色、公式样例）；openpyxl 生成代码模板（由李苏润提供基础版，主笔补字段映射）；条件格式与数据条配置。

### references/best-practices.md
TODO：优秀 vs 劣质可比分析案例对比；常见错误（行业归类错误、口径不一致、未剔除 ST、未对齐一致预期截止日）；行业-估值方法映射的最佳实践；质检清单。

---

## 依赖与配置

**必需依赖：**

- Python（openpyxl、pandas）
- 网络访问能力（Wind / Choice / iFinD）
- 数据源：Wind 终端 API 或 Choice EM_API
- [audit-xls-cn](../audit-xls-cn/) 用于 Excel 公式自检

**可选依赖：**

- FactSet API（A+H 标的或港股交叉对标）
- 中国证券登记结算公司接口（流通股本数据）

---

---

## 中国市场本土化深度内容 ⭐⭐⭐【强制填充段】

### 申万二级行业代码典型 30+ 行表（A 股估值对标核心）

| 二级代码 | 二级行业 | 典型公司（流通市值 100 亿以上）|
| :--- | :--- | :--- |
| 801081 | 半导体 | 中芯国际 / 北方华创 / 韦尔股份 / 兆易创新 |
| 801082 | 元件 | 沪电股份 / 风华高科 / 三环集团 |
| 801083 | 光学光电子 | 京东方 A / TCL 科技 / 立讯精密 |
| 801084 | 消费电子 | 立讯精密 / 工业富联 / 歌尔股份 |
| 801121 | 白酒 | 贵州茅台 / 五粮液 / 泸州老窖 / 山西汾酒 |
| 801122 | 啤酒 | 青岛啤酒 / 重庆啤酒 / 燕京啤酒 |
| 801141 | 包装印刷 | 裕同科技 / 合兴包装 |
| 801151 | 化学制药 | 恒瑞医药 / 复星医药 |
| 801152 | 生物制品 | 长春高新 / 智飞生物 |
| 801153 | 医疗器械 | 迈瑞医疗 / 联影医疗 |
| 801154 | 医药商业 | 上海医药 / 国药一致 |
| 801155 | CXO | 药明康德 / 凯莱英 / 泰格医药 |
| 801156 | 中药 | 片仔癀 / 同仁堂 / 云南白药 |
| 801731 | 电网设备 | 国电南瑞 / 特变电工 / 中国西电 / 华明装备 / 思源电气 |
| 801732 | 电池 | 宁德时代 / 比亚迪 / 国轩高科 |
| 801733 | 光伏设备 | 隆基绿能 / 通威股份 / TCL 中环 / 阳光电源 |
| 801734 | 风电设备 | 金风科技 / 明阳智能 / 东方电气 |
| 801761 | 互联网传媒 | 分众传媒 / 三七互娱 |
| 801781 | 银行 | 招商银行 / 兴业银行 / 工商银行 |
| 801781 | 股份制银行 | 招商银行 / 中信银行 / 平安银行 |
| 801791 | 证券 | 中信证券 / 海通证券 / 国泰君安 / 华泰证券 |
| 801792 | 保险 | 中国平安 / 中国人寿 / 新华保险 |
| 801880 | 整车 | 比亚迪 / 长城汽车 / 上汽集团 / 长安汽车 |
| 801881 | 汽车零部件 | 福耀玻璃 / 华域汽车 / 拓普集团 |
| 801891 | 工程机械 | 三一重工 / 中联重科 / 徐工机械 |
| 801961 | 油气开采 | 中国石油 / 中国海油 / 中国石化 |
| 801171 | 港口 | 上港集团 / 宁波港 |
| 801172 | 机场 | 上海机场 / 白云机场 |
| 801173 | 航空运输 | 中国国航 / 南方航空 / 东方航空 |

### 行业-估值方法映射详细表（A 股版）

| 行业属性 | 主估值方法 | 辅助估值方法 | 不适用方法 | 典型公司 |
| :--- | :--- | :--- | :--- | :--- |
| **高 ROE 稳定型**（白酒/医药白马/家电） | PB-ROE | DCF / 股息率 | PEG | 贵州茅台、片仔癀、格力电器 |
| **高增长成长股**（半导体/新能源/CXO） | PE-Band | PEG / EV/EBITDA | DCF（现金流不稳） | 韦尔股份、宁德时代、药明康德 |
| **银行** | PB-ROE | 股息率 / PE | DCF / PS | 招商银行、工商银行 |
| **保险** | P/EV（市值/内含价值） | PB | PE / PS | 中国平安、中国人寿 |
| **券商** | PB（重资本） | PE 顺周期 | DCF | 中信证券、华泰证券 |
| **地产** | NAV / PB | PE（顺周期低估） | DCF | 万科 A、保利发展 |
| **公用事业** | 股息率 | PE / DCF | PEG | 长江电力、中国神华 |
| **强周期股**（钢铁/煤炭/化工） | PB 历史分位 | EV/Capacity | DCF / PEG | 宝钢股份、万华化学 |
| **未盈利成长股**（创业板/科创板） | PS-Band | EV/Sales | PE / DCF | 部分科创板新股 |
| **平台型公司**（互联网） | EV/EBITDA / PE | PEG | DCF | 部分互联网（受限） |

### openpyxl 生成 5 sheet Excel 完整代码骨架（150 行）

```python
"""
A 股可比公司估值分析 - Excel 工作簿生成器
依赖：openpyxl >= 3.0
输出：5 sheet 标准格式（Cover / Assumptions / RawData / ValuationMatrix / Stats）
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# 配色（券商标准）
COLOR_BLUE = '002060'      # 表头深蓝
COLOR_RED = 'C8102E'        # 强调红
COLOR_GRAY = '595959'       # 灰色文字
COLOR_WHITE = 'FFFFFF'

# 字体规范
FONT_HEADER = Font(name='Microsoft YaHei', size=10, bold=True, color=COLOR_WHITE)
FONT_BODY = Font(name='Arial', size=9)
FONT_LABEL = Font(name='SimSun', size=9)
FONT_NOTE = Font(name='SimSun', size=8, color=COLOR_GRAY)

# 边框
BORDER_THIN = Border(left=Side(style='thin', color='000000'),
                     right=Side(style='thin', color='000000'),
                     top=Side(style='thin', color='000000'),
                     bottom=Side(style='thin', color='000000'))

# 填充
FILL_HEADER = PatternFill(start_color=COLOR_BLUE, end_color=COLOR_BLUE, fill_type='solid')
FILL_HIGHLIGHT = PatternFill(start_color='FFE699', end_color='FFE699', fill_type='solid')

def create_cover_sheet(wb, data):
    """Sheet 1: Cover - 封面页"""
    ws = wb.create_sheet('Cover', 0)
    ws['A1'] = 'A 股可比公司估值分析'
    ws['A1'].font = Font(name='Microsoft YaHei', size=18, bold=True)
    ws['A2'] = f"目标公司：{data['target_company']}（{data['target_code']}）"
    ws['A3'] = f"分析日期：{data['analysis_date']}"
    ws['A4'] = f"分析师：{data.get('analyst', '研究团队')}"
    # 标准免责声明
    ws['A6'] = '【免责声明】'
    ws['A6'].font = Font(name='SimSun', size=10, bold=True, color=COLOR_RED)
    ws['A7'] = '本估值分析仅供参考，不构成投资建议。本表格基于公开数据生成。'
    ws['A8'] = '一致预期数据来源于同花顺 iFinD/Wind/Choice 终端，使用前请用户复核。'
    return ws

def create_assumptions_sheet(wb, data):
    """Sheet 2: Assumptions - 假设页（蓝色输入单元格）"""
    ws = wb.create_sheet('Assumptions')
    headers = ['筛选规则', '当前设置', '备注']
    for c, h in enumerate(headers, 1):
        cell = ws.cell(row=1, column=c, value=h)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
        cell.alignment = Alignment(horizontal='center')
    
    rules = [
        ('申万二级行业', data['shenwan_industry'], '严格一致'),
        ('流通市值区间', f"{data['mv_low']}-{data['mv_high']} 亿元", '±50% 区间'),
        ('主营业务占比', f"≥{data['main_biz_ratio']}%", '严格筛选'),
        ('剔除 ST/*ST', '是', '财务异常股不可对标'),
        ('剔除上市 <6 个月新股', '是', '缺乏可比基期'),
        ('一致预期数据源', data['consensus_source'], '取数日期见 RawData'),
        ('一致预期截止日', data['consensus_date'], ''),
        ('覆盖券商数量阈值', '≥5 家', '<5 家须备注'),
    ]
    for r, (rule, setting, note) in enumerate(rules, 2):
        ws.cell(row=r, column=1, value=rule).font = FONT_LABEL
        cell = ws.cell(row=r, column=2, value=setting)
        cell.font = Font(name='Arial', size=9, color='0000FF')  # 蓝色 = 输入项
        ws.cell(row=r, column=3, value=note).font = FONT_NOTE
    return ws

def create_raw_data_sheet(wb, data, companies):
    """Sheet 3: RawData - 原始数据页（每家公司当期财务数据）"""
    ws = wb.create_sheet('RawData')
    headers = ['公司简称', '代码', '申万二级', '流通市值(亿)',
               'PE_TTM', 'PE_2025E', 'PE_2026E',
               'PB_MRQ', 'PS_TTM',
               'PEG', 'EV_EBITDA',
               '股息率', 'ROE_加权', '主营业务收入占比']
    for c, h in enumerate(headers, 1):
        cell = ws.cell(row=1, column=c, value=h)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
    for r, comp in enumerate(companies, 2):
        ws.cell(row=r, column=1, value=comp['name'])
        ws.cell(row=r, column=2, value=comp['code'])
        ws.cell(row=r, column=3, value=comp['shenwan'])
        ws.cell(row=r, column=4, value=comp['mv'])
        ws.cell(row=r, column=5, value=comp['pe_ttm'])
        # ... 填充其他列
    # 数据源标注（底部）
    src_row = len(companies) + 3
    ws.cell(row=src_row, column=1, value='数据来源').font = FONT_LABEL
    ws.cell(row=src_row, column=2, value=data['consensus_source']).font = FONT_NOTE
    return ws

def create_valuation_matrix_sheet(wb, target, peers):
    """Sheet 4: ValuationMatrix - 估值矩阵页（公式联动）"""
    ws = wb.create_sheet('ValuationMatrix')
    # 公式必须引用 RawData！禁止硬编码
    # 示例：ws['B2'] = '=RawData!E2'
    # ... 实现矩阵
    return ws

def create_stats_sheet(wb, peers):
    """Sheet 5: Stats - 统计页（5 档统计 + 目标公司位置高亮）"""
    ws = wb.create_sheet('Stats')
    headers = ['指标', '最小值', '25%分位', '中位数', '75%分位', '最大值', '平均数', '标准差', '目标位置']
    for c, h in enumerate(headers, 1):
        cell = ws.cell(row=1, column=c, value=h)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
    # 使用 PERCENTILE.INC 函数
    metrics = ['PE_TTM', 'PE_2025E', 'PB_MRQ', 'ROE_加权']
    for r, m in enumerate(metrics, 2):
        ws.cell(row=r, column=1, value=m)
        col_letter = chr(ord('E') + metrics.index(m))  # RawData 中的列
        # 最小值
        ws.cell(row=r, column=2, value=f'=MIN(RawData!{col_letter}2:{col_letter}10)')
        # 25% 分位
        ws.cell(row=r, column=3, value=f'=PERCENTILE.INC(RawData!{col_letter}2:{col_letter}10,0.25)')
        # 中位数
        ws.cell(row=r, column=4, value=f'=MEDIAN(RawData!{col_letter}2:{col_letter}10)')
        # 75% 分位
        ws.cell(row=r, column=5, value=f'=PERCENTILE.INC(RawData!{col_letter}2:{col_letter}10,0.75)')
        # 最大值
        ws.cell(row=r, column=6, value=f'=MAX(RawData!{col_letter}2:{col_letter}10)')
        # 平均数
        ws.cell(row=r, column=7, value=f'=AVERAGE(RawData!{col_letter}2:{col_letter}10)')
        # 标准差
        ws.cell(row=r, column=8, value=f'=STDEV(RawData!{col_letter}2:{col_letter}10)')
    return ws

def build_comps_xlsx(output_path, data, target, peers):
    """主入口"""
    wb = Workbook()
    wb.remove(wb['Sheet'])  # 删除默认 sheet
    create_cover_sheet(wb, data)
    create_assumptions_sheet(wb, data)
    create_raw_data_sheet(wb, data, peers + [target])
    create_valuation_matrix_sheet(wb, target, peers)
    create_stats_sheet(wb, peers + [target])
    wb.save(output_path)
    return wb
```

### A 股可比公司分析 8 大常见错误

| 错误 | 描述 | 后果 |
| :--- | :--- | :--- |
| 1. 用 GICS 而非申万分类 | 海外行业分类与 A 股不匹配 | 选到不可比公司 |
| 2. 未对齐一致预期截止日 | 不同公司用不同日期的预期 | 数据不可比 |
| 3. 未剔除 ST/*ST | 财务异常股拉低中位数 | 估值结论失真 |
| 4. 未剔除新股次新股 | 缺乏可比基期 / 估值畸高 | 拉高均值 |
| 5. 多元化集团按主业之外行业归类 | 业务结构混合 | 不可对标 |
| 6. A+H 标的双重计算 | A 股 + 港股池同时算 | 双重计数 |
| 7. 业绩报酬条款失真 | 高分红股股息率不剔除特别分红 | 误读股息率 |
| 8. 覆盖券商 <3 家用一致预期 | 一致预期不可靠 | 估值锚错位 |

### 与其他 CN 技能的协同

| 场景 | 协同技能 |
| :--- | :--- |
| 单家公司深度分析 | 引用 [initiating-coverage-cn] |
| 行业全景 | 引用 [sector-overview-cn] |
| 绝对估值锚 | 触发 [dcf-cn] 交叉验证 |
| 业绩点评修正一致预期 | 触发 [earnings-analysis-cn] |
| Excel 公式自检 | 触发 [audit-xls-cn] |

---

> **骨架说明**：本文件为 comps-cn 的初版骨架，由项目 PM 李苏润 5/30 输出。主笔 E 须按 earnings-analysis-cn（935 行）的深度继续展开 TODO，目标 6/12 前完成主体 SKILL.md，6/19 前完成 references/ 三件套。本次升级已添加申万二级代码 30+ 行、行业-估值映射详表、openpyxl 完整代码骨架、8 大常见错误案例、协同设计。完成后可分担 initiating-coverage-cn 后期工作。
