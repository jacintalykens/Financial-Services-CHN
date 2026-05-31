# comps-cn — 工作流操作指南

> ⚠️ **本文件为骨架占位**。主笔：邢邵楠。6/19 前完成主体，6/26 前定稿。基线：[earnings-analysis-cn/references/workflow.md](../../../equity-research/skills/earnings-analysis-cn/references/workflow.md)。

## 待补章节

1. **申万二级行业代码全表**（≥30 个常见行业，含代码 + 名称 + 典型公司 3-5 家）
   - 示例：801080 电子 / 801082 半导体 / 801085 元件 …

2. **Wind 取数函数模板**
   - WSD（时序）
   - WSS（截面）
   - WSET（数据集）
   - 一致预期字段名（est_eps / est_np / est_rev_yoy）

3. **Choice EM_API 取数模板**
   - 历史数据 EM.CSD
   - 截面数据 EM.CSS
   - 一致预期 EM.CFC

4. **ST 股识别脚本**
   - 通过股票简称识别 ST / *ST
   - 退市风险警示判别

5. **新股次新股查询接口**
   - 上市日期 < 6 个月
   - 流通股 < 总股本一定比例（限售股未解禁）

6. **openpyxl 生成 5 sheet Excel 代码模板**（李苏润提供基础版）
   - 单元格样式定义
   - 公式批量写入
   - 条件格式（高亮目标公司位置）
   - 数据验证（下拉框）

## 验收标准

- 内容 ≥ 200 行
- 至少 2 个完整 Python 代码块可运行
- 申万二级行业代码表 ≥ 30 个
