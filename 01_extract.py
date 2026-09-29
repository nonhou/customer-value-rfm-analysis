"""1、获取数据"""
import pandas as pd

datafile = r'TB201812.xls'
resultfile = r'view.xls'
data = pd.read_excel(datafile)
print(data.head())
