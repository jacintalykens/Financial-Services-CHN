"""
首页双栏版式自检脚本（前置门）

⚠️ AI 使用约定：
阶段 4 生成 DOCX 后必须运行本脚本。
返回码 0 = 通过；返回码 1 = 不通过（必须返回阶段 4 重做首页）。

调用：
    python check_layout.py 路径/到/报告.docx

校验 8 项视觉验收：
1. 存在 1×2 布局容器表（左 ≥ 10cm，右 4-7cm）
2. 该容器左单元格内含嵌套表（财务摘要表）
3. 该容器右单元格内含嵌套表（评级框）
4. 评级框单元格背景为红色（C8102E）或券商色
5. 财务摘要表表头背景为深蓝（002060）或券商深色
6. 文档段落中含 "▎" 红色标记（左栏要点格式）
7. 页眉含 "请务必阅读" 字样
8. 页脚含 PAGE 字段或 X / Y 模式
"""
import sys
from docx import Document
from docx.oxml.ns import qn


def check_layout(docx_path):
    """返回 (is_pass, report_lines)"""
    doc = Document(docx_path)
    results = []
    fail_count = 0

    def add(ok, msg):
        nonlocal fail_count
        if ok:
            results.append(f'  ✓ {msg}')
        else:
            results.append(f'  ✗ {msg}')
            fail_count += 1

    # 1+2+3: 找双栏布局容器（必须含嵌套表，否则可能是页眉条）
    layout_table = None
    fin_table = None
    rating_table = None

    candidates = []  # 所有符合宽度的 1×2 表
    for t in doc.tables:
        if len(t.rows) == 1 and len(t.columns) == 2:
            try:
                w0 = t.columns[0].width.cm if t.columns[0].width else 0
                w1 = t.columns[1].width.cm if t.columns[1].width else 0
            except Exception:
                continue
            if 10 <= w0 <= 13 and 4 <= w1 <= 7:
                candidates.append(t)

    # 优先选含嵌套表的（双栏主体），其次回退到第一个候选
    for t in candidates:
        left_nested = t.rows[0].cells[0].tables
        right_nested = t.rows[0].cells[1].tables
        if left_nested or right_nested:
            layout_table = t
            if left_nested:
                fin_table = left_nested[0]
            if right_nested:
                rating_table = right_nested[0]
            break
    if layout_table is None and candidates:
        layout_table = candidates[0]

    add(layout_table is not None,
        '存在 1×2 布局容器表（左 ~11.5cm / 右 ~5.5cm）')
    add(fin_table is not None,
        '布局表左栏嵌套财务摘要表')
    add(rating_table is not None,
        '布局表右栏嵌套评级框（1×1 表）')

    # 4: 评级框红底
    rating_red = False
    if rating_table is not None:
        rc = rating_table.rows[0].cells[0]
        tcPr = rc._tc.find(qn('w:tcPr'))
        if tcPr is not None:
            shd = tcPr.find(qn('w:shd'))
            if shd is not None:
                fill = shd.get(qn('w:fill'), '').upper()
                if fill in ('C8102E', 'CC0000', 'C00000', 'B22222',
                            'A52A2A', 'DC143C'):
                    rating_red = True
    add(rating_red, '评级框背景为红色 / 券商红')

    # 5: 财务摘要表表头深色
    fin_header_dark = False
    if fin_table is not None and len(fin_table.rows) > 0:
        hc = fin_table.rows[0].cells[0]
        tcPr = hc._tc.find(qn('w:tcPr'))
        if tcPr is not None:
            shd = tcPr.find(qn('w:shd'))
            if shd is not None:
                fill = shd.get(qn('w:fill'), '').upper()
                if fill in ('002060', '1F4E79', '203864', '0F243E',
                            '002F6C', '003B7E'):
                    fin_header_dark = True
    add(fin_header_dark, '财务摘要表表头为深蓝 / 券商深色')

    # 6: 文档含 "▎" 红色标记
    has_marker = False
    for para in doc.paragraphs:
        if '▎' in para.text:
            has_marker = True
            break
    if not has_marker and layout_table is not None:
        # 在左栏单元格里找
        for para in layout_table.rows[0].cells[0].paragraphs:
            if '▎' in para.text:
                has_marker = True
                break
    add(has_marker, '左栏含 "▎" 报告要点段落标记')

    # 7: 页眉含 "请务必阅读"
    header_ok = False
    sec = doc.sections[0]
    for para in sec.header.paragraphs:
        if '请务必阅读' in para.text:
            header_ok = True
            break
    add(header_ok, '页眉含 "请务必阅读正文之后的免责条款部分"')

    # 8: 页脚有 PAGE 字段
    footer_ok = False
    for para in sec.footer.paragraphs:
        # 检查段落 XML 是否含 fldChar / instrText PAGE
        xml = para._p.xml
        if 'PAGE' in xml and 'fldChar' in xml:
            footer_ok = True
            break
    add(footer_ok, '页脚含 PAGE / NUMPAGES 自动页码字段')

    return fail_count == 0, results


def main():
    if len(sys.argv) < 2:
        print('用法：python check_layout.py 路径/到/报告.docx')
        sys.exit(2)
    docx_path = sys.argv[1]
    print(f'\n首页版式自检：{docx_path}')
    print('=' * 60)
    is_pass, lines = check_layout(docx_path)
    for line in lines:
        print(line)
    print('=' * 60)
    if is_pass:
        print('✅ 全部 8 项通过 — 首页版式合规')
        sys.exit(0)
    else:
        print('❌ 检查未通过 — 必须返回阶段 4 重做首页')
        print('\n修复指引：')
        print('  1. 必须 from templates.cover_page import build_cover_page')
        print('  2. 用 build_cover_page() 生成首页，不要手动堆 add_paragraph')
        print('  3. 数据契约见 templates/cover_page.py 末尾的 SAMPLE_DATA')
        sys.exit(1)


if __name__ == '__main__':
    main()
