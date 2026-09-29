"""3、数据清洗：剔除未付款与金额为 0 的记录，构建 R 指标"""
import pandas as pd
import numpy as np
from pandas import to_datetime

datafile = r'TB201812.xls'
resultfiles = r'data.xls'
df = pd.DataFrame(pd.read_excel(datafile))
df1 = df[['订单付款时间', '买家会员名', '买家实际支付金额', '数据采集时间']]

# 剔除付款时间为空、实际支付金额为 0 的记录
df1 = df1[df1['订单付款时间'].notnull() & df1['买家实际支付金额'] != 0]

# R = 数据采集时间 - 订单付款时间（天）
df1['R'] = (pd.to_datetime(df1['数据采集时间']) - pd.to_datetime(df1['订单付款时间'])).values / np.timedelta64(1, 'D')
df1 = df1[['订单付款时间', '买家会员名', '买家实际支付金额', 'R']]

# 按客户聚合：R 取最小值，M 取支付金额均值
df2 = df1.groupby('买家会员名').agg({'R': 'min', '买家实际支付金额': 'mean'})
# F = 同一客户的订单条数
df2['F'] = df1.groupby(['买家会员名'])['买家会员名'].size()
df2.to_excel(resultfiles)
print(df2.head())
