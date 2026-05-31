# templates/ — 首页双栏版式工具

⚠️ **AI 执行约定**：本目录的两个 .py 文件是 earnings-analysis-cn 的**强制工具**，不是参考代码。阶段 4（DOCX 生成）必须按以下流程执行，**禁止用 `add_paragraph` 自由拼装首页**。

## 文件清单

| 文件 | 角色 | 强制 |
| :--- | :--- | :--- |
| `cover_page.py` | 首页双栏版式生成器（300+ 行 python-docx） | ✅ 必须调用 |
| `check_layout.py` | 首页 8 项自检脚本（前置门） | ✅ 必须通过 |
| `README.md` | 本文件 | — |

## 强制流程（阶段 4 第 1 步）

```python
# Step 1: 调用模板生成首页（创建新 docx）
import sys
sys.path.insert(0, '<skill 根目录>/templates')
from cover_page import build_cover_page

data = {
    'industry_tag': '公司研究  |  工业  |  资本货物',
    'report_date': '2026 年 05 月 24 日',
    'main_title': '...',     # 主标题观点 12-20 字
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
    'price_chart_path': 'price_trend.png',  # 或 None
    'related_reports': [
        {'title': '...', 'date': 'YYYY-MM-DD'},
        ...
    ],
    'analyst': {
        'name': '...', 'cert_id': 'S0...',
        'phone': '...', 'email': '...',
    },
    'broker': '国元',
    'report_points': [   # 必须恰好 4 段
        {'headline': '一句话立论', 'body': '80-120 字 paragraph'},
        ...
    ],
    'fin_table': {       # 5 列：2 历史年 + 3 预测年
        'revenue': [...], 'rev_yoy': [...],
        'np':      [...], 'np_yoy':  [...],
        'roe':     [...], 'eps':     [...], 'pe': [...],
    },
}

doc = build_cover_page('output.docx', data)
# doc 是 Document 对象，可以继续追加第 2 页起的章节
```

## 强制自检（阶段 4 末尾）

```bash
python check_layout.py output.docx
```

返回码 `0` = 通过；`1` = 未通过，必须**回到阶段 4 重做首页**。

## 8 项自检规则

1. 存在 1×2 布局容器表（左栏 ~11.5cm，右栏 ~5.5cm）
2. 该容器左栏嵌套财务摘要表（8×6）
3. 该容器右栏嵌套评级框（1×1）
4. 评级框背景为券商红色（#C8102E 或类似）
5. 财务摘要表表头为深蓝（#002060 或类似）
6. 左栏含 "▎" 红色报告要点标记
7. 页眉含 "请务必阅读正文之后的免责条款部分"
8. 页脚含 PAGE / NUMPAGES 自动页码字段

## 数据字段契约

详见 `cover_page.py` 末尾的 `SAMPLE_DATA` 字典 — 这是字段名、类型、嵌套结构的唯一来源，**直接复制 + 替换值**即可。

## 命令行测试

```bash
# 生成样张（用 SAMPLE_DATA）
python cover_page.py 样张.docx

# 检查样张
python check_layout.py 样张.docx
```

## 修复指引（如自检不通过）

| 不通过项 | 修复 |
| :--- | :--- |
| 缺布局容器表 | 没调 `build_cover_page()` — 必须用模板而非手动 add_paragraph |
| 缺嵌套财务摘要表 | data['fin_table'] 字段缺失或 build_cover_page 抛错 |
| 缺嵌套评级框 | data['rating'] / data['rating_change'] 缺失 |
| 评级框非红色 | 中间被修改，重新调 build_cover_page，禁止覆盖颜色 |
| 表头非深蓝 | 同上 |
| 缺 "▎" 标记 | data['report_points'] 为空或被改成 bullet 格式 |
| 页眉缺免责声明 | 没调 `setup_footer_header()` — build_cover_page 内部已调，检查是否后续覆盖了 header |
| 页脚缺页码字段 | 同上 |
