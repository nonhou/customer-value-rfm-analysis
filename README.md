# 客户价值分析（RFM 模型 + K-Means 聚类）

对淘宝店铺订单数据构建 R / F / M 三维客户价值指标，用 K-Means 完成客户分层，输出各客户群的聚类中心与指标密度分布图，替代人工经验分组。

## 数据

- 来源：某淘宝店铺订单数据（`TB201812.xls`）
- 使用字段：订单付款时间、买家会员名、买家实际支付金额、数据采集时间

> 原始数据未上传，请自备同类订单数据，字段名与上表一致即可运行。

## 方法

分析流程分五步，对应仓库中的五个脚本。

1. **数据抽取**（`01_extract.py`）：读取订单表，保留订单付款时间、买家会员名、买家实际支付金额、数据采集时间四列。

2. **数据探索分析**（`02_explore.py`）：用 `describe(percentiles=[], include='all')` 统计各字段的非空值数、最大值、最小值，定位缺失与异常分布，结果写入 `view.xls`。

3. **数据清洗**（`03_clean.py`）：
   - 剔除订单付款时间为空的记录
   - 剔除实际支付金额为 0 的记录（未付款订单）
   - 构建 `R` 指标：数据采集时间 − 订单付款时间，按天计算
   - 按买家会员名聚合：`R` 取最小值，`M` 取实际支付金额均值，`F` 取订单条数
   - 结果写入 `data.xls`

4. **数据转换**（`04_transform.py`）：取 `R`、`F`、`M` 三列，做标准化 `(x - mean) / std`，结果写入 `transformdata.xls`。

5. **客户聚类与可视化**（`05_cluster.py`）：
   - `sklearn.cluster.KMeans`，`n_clusters=4`，`max_iter=500`
   - 输出各客户群的聚类中心与各类别客户数
   - 对每个客户群绘制 R / F / M 三张核密度估计（KDE）分布图，标题标注客户群编号与规模

## 结果

将客户聚为 **4 类**客户群，输出各群的聚类中心与 R / F / M 密度分布图，用于识别高价值客户与待挽留客户，支撑差异化运营。

| 客户群 | 规模 |
| --- | --- |
| 客户群 0 | 563 |
| 客户群 1 | 753 |
| 客户群 2 | 753 |

> 客户群 3 的规模未在实训报告中留存，重新运行 `05_cluster.py` 即可得到当前数据下的完整结果。

## 运行

```bash
pip install -r requirements.txt
```

1. 把订单数据放到项目根目录，命名为 `TB201812.xls`。
2. 按顺序运行五个脚本：

```bash
python 01_extract.py
python 02_explore.py
python 03_clean.py
python 04_transform.py
python 05_cluster.py
```

中间结果 `view.xls`、`data.xls`、`transformdata.xls`、`data_type.xls` 会写入项目根目录。

> 图表中的中文标签依赖 `SimHei` 字体。Linux / macOS 下请改成系统已有的中文字体，例如把 `plt.rcParams['font.sans-serif'] = ['SimHei']` 改成 `['Noto Sans CJK SC']`。

## 目录结构

```
customer-value-rfm-analysis/
├── README.md
├── requirements.txt
├── .gitignore
├── 01_extract.py
├── 02_explore.py
├── 03_clean.py
├── 04_transform.py
└── 05_cluster.py
```

## 代码说明

脚本基本保留实训报告中的原始写法，仅修正了两处笔误并在代码中加了注释标明：

| 位置 | 原文 | 修正 |
| --- | --- | --- |
| `02_explore.py` | `view.colums = [...]` | `view.columns = [...]` |
| `04_transform.py` | `transoformdata.xls` | `transformdata.xls` |

另外 `05_cluster.py` 补上了 `from sklearn.cluster import KMeans` 的导入语句（报告原文中该导入在上下文里省略）。

## 说明

- 课程实训项目，按实验任务独立完成。
- 原始订单数据含买家会员名等个人信息，未上传。
