"""4、数据转换：构建 R / F / M 三维指标并做标准化"""
import pandas as pd

datafile = r'data.xls'
# 注：实训报告原文此处拼写为 transoformdata.xls，此处统一为 transformdata.xls
transformfile = r'transformdata.xls'
data = pd.read_excel(datafile)
data = data[['R', 'F', '买家实际支付金额']]
data = (data - data.mean(axis=0)) / (data.std(axis=0))
data.columns = ['R', 'F', 'M']
data.to_excel(transformfile, index=False)
print(data.head())
