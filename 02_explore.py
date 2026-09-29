"""2、数据探索分析：统计各字段的非空值数、最大值、最小值"""
import pandas as pd
import numpy as np
from pandas import to_datetime

datafile = r'TB201812.xls'
resultfile = r'view.xls'
data = pd.read_excel(datafile)
data = data[['订单付款时间', '买家会员名', '买家实际支付金额', '数据采集时间']]

view = data.describe(percentiles=[], include='all').T
view['null'] = len(data) - view['count']
view = view[['null', 'max', 'min']]
# 注：实训报告原文写作 view.colums（笔误），此处修正为 columns
view.columns = [u'空值', u'最大值', u'最小值']
view.to_excel(resultfile)
print(view)
