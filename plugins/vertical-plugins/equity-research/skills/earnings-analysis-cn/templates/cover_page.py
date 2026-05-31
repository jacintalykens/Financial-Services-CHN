"""
A 股业绩点评研报 - 首页双栏版式生成器（工具模块）

⚠️ AI 使用约定：
本模块是 earnings-analysis-cn skill 的**强制工具**，不是参考代码。
阶段 4（DOCX 生成）的第一步必须调用 build_cover_page()，
而不是手工用 add_paragraph 顺序拼装首页。

调用流程：
    from templates.cover_page import build_cover_page
    doc = build_cover_page(output_path, data)
    # 然后在 doc 之后追加第 2 页起的章节

依赖：python-docx >= 1.0.0
"""
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


# ═══════════════════════════════════════════════════════════════════
# 配色系统（券商标准 6 色，不要用其他颜色）
# ═══════════════════════════════════════════════════════════════════
COLOR_RED       = RGBColor(0xC8, 0x10, 0x2E)
COLOR_BLUE      = RGBColor(0x00, 0x20, 0x60)
COLOR_DIVIDER   = RGBColor(0xD9, 0xD9, 0xD9)
COLOR_GRAY      = RGBColor(0x59, 0x59, 0x59)
COLOR_WATERMARK = RGBColor(0xBF, 0xBF, 0xBF)
COLOR_BLACK     = RGBColor(0x00, 0x00, 0x00)
COLOR_WHITE     = RGBColor(0xFF, 0xFF, 0xFF)

HEX_RED  = 'C8102E'
HEX_BLUE = '002060'


# ═══════════════════════════════════════════════════════════════════
# 低层 XML 工具
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
    """单元格内边距（单位 dxa：1/20 pt，100 ≈ 0.18cm）"""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for edge, val in [('top', top), ('bottom', bottom),
                       ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{edge}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def add_horizontal_divider(paragraph, color=COLOR_DIVIDER):
    """在段落上方添加 0.5pt 灰色分隔线（右栏段间分隔用）"""
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    top = OxmlElement('w:top')
    top.set(qn('w:val'), 'single')
    top.set(qn('w:sz'), '4')
    top.set(qn('w:space'), '4')
    top.set(qn('w:color'), 'D9D9D9')
    pBdr.append(top)
    pPr.append(pBdr)


def _set_eastasia_font(run, font_name):
    """设置中文 eastAsia 字体（python-docx 高层 API 不直接支持）"""
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.append(rFonts)
    rFonts.set(qn('w:eastAsia'), font_name)


def add_paragraph_with_run(parent, text, font='宋体', size=10, bold=False,
                           color=COLOR_BLACK, align=None, space_after=Pt(2)):
    """添加格式化段落（parent 可以是 cell 或 doc）"""
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
    _set_eastasia_font(run, font)
    return p


def apply_three_line_table_borders(table):
    """三线表样式：顶线 + 表头底线 + 底线（清掉所有网格）"""
    tbl = table._tbl
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

    rows = list(table.rows)
    # 顶线 + 表头底线
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
    # 底线
    for cell in rows[-1].cells:
        tcPr = cell._tc.find(qn('w:tcPr'))
        borders = tcPr.find(qn('w:tcBorders'))
        bottom = borders.find(qn('w:bottom'))
        bottom.set(qn('w:val'), 'single')
        bottom.set(qn('w:sz'), '8')
        bottom.set(qn('w:color'), '000000')


# ═══════════════════════════════════════════════════════════════════
# 区段 A：页面初始化 + 页眉条
# ═══════════════════════════════════════════════════════════════════
def setup_page(doc):
    """A4 纵向 + 券商标准页边距"""
    sec = doc.sections[0]
    sec.page_height = Cm(29.7)
    sec.page_width = Cm(21.0)
    sec.top_margin = Cm(1.8)
    sec.bottom_margin = Cm(1.8)
    sec.left_margin = Cm(2.0)
    sec.right_margin = Cm(2.0)


def add_header_strip(doc, industry_tag, report_date):
    """页眉条：左行业分类 / 右报告日期 + 下方 2pt 深蓝粗线"""
    tbl = doc.add_table(rows=1, cols=2)
    tbl.autofit = False
    tbl.columns[0].width = Cm(11.0)
    tbl.columns[1].width = Cm(6.0)

    left, right = tbl.rows[0].cells
    for c in [left, right]:
        remove_cell_borders(c)
        set_cell_margin(c, top=0, bottom=0, left=0, right=0)

    p = left.paragraphs[0]
    run = p.add_run(industry_tag)
    run.font.name = '微软雅黑'
    run.font.size = Pt(9)
    run.font.color.rgb = COLOR_GRAY
    _set_eastasia_font(run, '微软雅黑')

    p = right.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run(f'证券研究报告  |  {report_date}')
    run.font.name = '微软雅黑'
    run.font.size = Pt(9)
    run.font.color.rgb = COLOR_GRAY
    _set_eastasia_font(run, '微软雅黑')

    # 下方 2pt 深蓝粗线
    sep = doc.add_paragraph()
    sep.paragraph_format.space_before = Pt(0)
    sep.paragraph_format.space_after = Pt(6)
    pPr = sep._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    top = OxmlElement('w:top')
    top.set(qn('w:val'), 'single')
    top.set(qn('w:sz'), '16')   # 2pt
    top.set(qn('w:space'), '1')
    top.set(qn('w:color'), HEX_BLUE)
    pBdr.append(top)
    pPr.append(pBdr)


# ═══════════════════════════════════════════════════════════════════
# 区段 B：标题区
# ═══════════════════════════════════════════════════════════════════
def add_title_block(doc, main_title, sub_title):
    """居中双标题"""
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
    _set_eastasia_font(run, '微软雅黑')

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(18)
    run = p.add_run(f'—— {sub_title}')
    run.font.name = '宋体'
    run.font.size = Pt(14)
    run.bold = True
    run.font.color.rgb = COLOR_BLUE
    _set_eastasia_font(run, '宋体')


# ═══════════════════════════════════════════════════════════════════
# 区段 C：双栏主体区（核心 — 用无边框表格做容器）
# ═══════════════════════════════════════════════════════════════════
def add_two_column_body(doc, data):
    """
    主体区：左栏 11.5cm 报告要点+财务摘要表，右栏 5.5cm Panel。
    必须用无边框 1×2 表格作为容器 — 顺序段落必然单栏。
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
    """左栏：报告要点 4 段 + 财务摘要表 8×6 三线表"""
    cell.paragraphs[0]._p.getparent().remove(cell.paragraphs[0]._p)

    add_paragraph_with_run(cell, '报告要点', font='微软雅黑', size=12,
                           bold=True, color=COLOR_BLUE, space_after=Pt(6))

    for point in data['report_points']:
        p = cell.add_paragraph()
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.line_spacing = 1.4

        marker = p.add_run('▎ ')
        marker.font.name = '微软雅黑'
        marker.font.size = Pt(11)
        marker.bold = True
        marker.font.color.rgb = COLOR_RED

        head = p.add_run(point['headline'])
        head.font.name = '微软雅黑'
        head.font.size = Pt(10.5)
        head.bold = True
        head.font.color.rgb = COLOR_BLACK
        _set_eastasia_font(head, '微软雅黑')

        p.add_run().add_break()
        body = p.add_run(point['body'])
        body.font.name = '宋体'
        body.font.size = Pt(10)
        body.font.color.rgb = COLOR_BLACK
        _set_eastasia_font(body, '宋体')

    cell.add_paragraph()

    # 财务摘要表 8×6
    fin_table = cell.add_table(rows=8, cols=6)
    fin_table.autofit = False
    col_widths = [Cm(3.5), Cm(1.5), Cm(1.5), Cm(1.5), Cm(1.5), Cm(1.5)]
    for i, w in enumerate(col_widths):
        fin_table.columns[i].width = w

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
        _set_eastasia_font(run, '微软雅黑')

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
        c = fin_table.rows[ri].cells[0]
        c.paragraphs[0].text = ''
        p = c.paragraphs[0]
        run = p.add_run(label)
        run.font.name = '宋体'
        run.font.size = Pt(8)
        _set_eastasia_font(run, '宋体')

        for ci, val in enumerate(data['fin_table'][key], 1):
            c = fin_table.rows[ri].cells[ci]
            c.paragraphs[0].text = ''
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            run = p.add_run(fmt.format(val) if isinstance(val, (int, float)) else str(val))
            run.font.name = 'Arial'
            run.font.size = Pt(8)

    apply_three_line_table_borders(fin_table)

    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    run = p.add_run(f'资料来源：Wind、{data["broker"]}研究所')
    run.font.name = '宋体'
    run.font.size = Pt(7)
    run.font.color.rgb = COLOR_GRAY
    _set_eastasia_font(run, '宋体')


def fill_right_column(cell, data):
    """右栏 Panel：评级框 + 当前价 + 基本数据 + 股价图 + 相关研报 + 报告作者"""
    cell.paragraphs[0]._p.getparent().remove(cell.paragraphs[0]._p)

    # 段 1：评级框（嵌套 1×1 红底表）
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
    _set_eastasia_font(run, '微软雅黑')

    # 段 2：当前价
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run('当前价：')
    run.font.name = '宋体'
    run.font.size = Pt(9)
    run.font.color.rgb = COLOR_GRAY
    _set_eastasia_font(run, '宋体')

    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(f'{data["current_price"]:.2f} 元')
    run.font.name = 'Arial'
    run.font.size = Pt(18)
    run.bold = True
    run.font.color.rgb = COLOR_RED

    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run(f'({data["price_date"]} 收盘)')
    run.font.name = '宋体'
    run.font.size = Pt(8)
    run.font.color.rgb = COLOR_GRAY
    _set_eastasia_font(run, '宋体')

    # 段 3：基本数据
    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    add_horizontal_divider(p)
    run = p.add_run('基本数据')
    run.font.name = '微软雅黑'
    run.font.size = Pt(10)
    run.bold = True
    run.font.color.rgb = COLOR_BLUE
    _set_eastasia_font(run, '微软雅黑')

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
        _set_eastasia_font(run1, '宋体')
        run2 = p.add_run(str(val))
        run2.font.name = 'Arial'
        run2.font.size = Pt(8.5)
        run2.bold = True

    # 段 4：股价走势图
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    add_horizontal_divider(p)
    run = p.add_run('过去一年股价走势')
    run.font.name = '微软雅黑'
    run.font.size = Pt(10)
    run.bold = True
    run.font.color.rgb = COLOR_BLUE
    _set_eastasia_font(run, '微软雅黑')

    if data.get('price_chart_path'):
        p = cell.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(data['price_chart_path'], width=Cm(5.0))
    else:
        p = cell.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run('[此处插入股价走势折线图]')
        run.font.size = Pt(8)
        run.font.color.rgb = COLOR_GRAY

    # 段 5：相关研究
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    add_horizontal_divider(p)
    run = p.add_run('相关研究报告')
    run.font.name = '微软雅黑'
    run.font.size = Pt(10)
    run.bold = True
    run.font.color.rgb = COLOR_BLUE
    _set_eastasia_font(run, '微软雅黑')

    for ref in data['related_reports'][:3]:
        p = cell.add_paragraph()
        p.paragraph_format.space_after = Pt(1)
        run = p.add_run(f'• {ref["title"]}')
        run.font.name = '宋体'
        run.font.size = Pt(8)
        _set_eastasia_font(run, '宋体')
        p = cell.add_paragraph()
        p.paragraph_format.left_indent = Cm(0.3)
        p.paragraph_format.space_after = Pt(3)
        run = p.add_run(f'({ref["date"]})')
        run.font.name = '宋体'
        run.font.size = Pt(7.5)
        run.font.color.rgb = COLOR_GRAY
        _set_eastasia_font(run, '宋体')

    # 段 6：报告作者
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    add_horizontal_divider(p)
    run = p.add_run('报告作者')
    run.font.name = '微软雅黑'
    run.font.size = Pt(10)
    run.bold = True
    run.font.color.rgb = COLOR_BLUE
    _set_eastasia_font(run, '微软雅黑')

    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(1)
    run = p.add_run(f'分析师 {data["analyst"]["name"]}')
    run.font.name = '宋体'
    run.font.size = Pt(8.5)
    run.bold = True
    _set_eastasia_font(run, '宋体')

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
        _set_eastasia_font(run1, '宋体')
        run2 = p.add_run(str(val))
        run2.font.name = 'Arial' if label != '执业证书' else '宋体'
        run2.font.size = Pt(8)


# ═══════════════════════════════════════════════════════════════════
# 区段 D：页眉页脚（应用全文档）
# ═══════════════════════════════════════════════════════════════════
def setup_footer_header(doc):
    """所有页：页眉'请务必阅读正文之后的免责条款部分' + 页脚'X / Y'"""
    sec = doc.sections[0]
    header = sec.header
    p = header.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('请务必阅读正文之后的免责条款部分')
    run.font.name = '宋体'
    run.font.size = Pt(9)
    run.font.color.rgb = COLOR_GRAY
    _set_eastasia_font(run, '宋体')

    footer = sec.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    # 当前页字段
    run = p.add_run()
    for tag, attr_val in [('begin', None), ('PAGE', 'instr'), ('end', None)]:
        if attr_val == 'instr':
            it = OxmlElement('w:instrText')
            it.text = 'PAGE'
            run._element.append(it)
        else:
            fc = OxmlElement('w:fldChar')
            fc.set(qn('w:fldCharType'), tag)
            run._element.append(fc)
    run.font.name = 'Arial'
    run.font.size = Pt(9)
    run.font.color.rgb = COLOR_GRAY

    sep = p.add_run(' / ')
    sep.font.name = 'Arial'
    sep.font.size = Pt(9)
    sep.font.color.rgb = COLOR_GRAY

    run = p.add_run()
    for tag, attr_val in [('begin', None), ('NUMPAGES', 'instr'), ('end', None)]:
        if attr_val == 'instr':
            it = OxmlElement('w:instrText')
            it.text = 'NUMPAGES'
            run._element.append(it)
        else:
            fc = OxmlElement('w:fldChar')
            fc.set(qn('w:fldCharType'), tag)
            run._element.append(fc)
    run.font.name = 'Arial'
    run.font.size = Pt(9)
    run.font.color.rgb = COLOR_GRAY


# ═══════════════════════════════════════════════════════════════════
# 主入口
# ═══════════════════════════════════════════════════════════════════
def build_cover_page(output_path, data, doc=None, page_break_after=True):
    """
    生成首页双栏版式。

    参数：
        output_path：保存路径（.docx）；如果传 doc=None 会新建 Document
        data：见模块底部 SAMPLE_DATA 注释的字段约定
        doc：可选；若给定，则在该 Document 上追加首页（用于多页报告）
        page_break_after：是否在首页末尾插入分页符

    返回：
        doc 对象（可继续追加第 2 页起的内容）
    """
    if doc is None:
        doc = Document()
    setup_page(doc)
    setup_footer_header(doc)
    add_header_strip(doc, data['industry_tag'], data['report_date'])
    add_title_block(doc, data['main_title'], data['sub_title'])
    add_two_column_body(doc, data)
    if page_break_after:
        doc.add_page_break()
    if output_path:
        doc.save(output_path)
    return doc


# ═══════════════════════════════════════════════════════════════════
# 数据契约示例（实际调用时填入真实数据）
# ═══════════════════════════════════════════════════════════════════
SAMPLE_DATA = {
    'industry_tag': '公司研究  |  工业  |  资本货物',
    'report_date': '2026 年 05 月 24 日',
    'main_title': '海外出口加速、特高压批量化投运，重申"买入"',
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
    'price_chart_path': None,   # 传入 PNG 路径以嵌入股价走势图
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
            'body': '华明装备发布 2025 年年报：全年实现营业收入 24.27 亿元（同比 +4.50%），归母净利润 7.10 亿元（同比 +15.54%）。',
        },
        {
            'headline': '海外出口大超预期，全球化布局进入兑现期',
            'body': '电力设备业务直接 + 间接出口 7.14 亿元（+47.37%）。印尼工厂正式投产，全球化布局正式落地。',
        },
        {
            'headline': '特高压 CHVT 批量化投运，打破海外品牌垄断',
            'body': 'CHVT 在陇东 ±800kV 工程批量投运。国家电网"十五五" 4 万亿投资落地后公司是国内分接开关环节几乎唯一受益标的。',
        },
        {
            'headline': '维持"买入"评级，上调目标价至 21.50 元',
            'body': '上调 2026-2028E 归母至 8.55 / 10.10 / 11.65 亿。给予 22.5x PE，对应目标价 21.50 元。',
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


if __name__ == '__main__':
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else '首页样张.docx'
    build_cover_page(out, SAMPLE_DATA)
    print(f'首页已生成：{out}')
