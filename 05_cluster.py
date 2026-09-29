"""5、客户聚类：K-Means（k=4）+ R/F/M 密度分布图"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

inputfile = r'transformdata.xls'
outputfile = r'data_type.xls'
data = pd.read_excel(inputfile)

k = 4
iteration = 500
kmodel = KMeans(n_clusters=k, max_iter=iteration)
kmodel.fit(data)

# 聚类中心 + 各类别数目
r1 = pd.Series(kmodel.labels_).value_counts()
r2 = pd.DataFrame(kmodel.cluster_centers_)
r = pd.concat([r2, r1], axis=1)
r.columns = list(data.columns) + [u'聚类类别']
print(r)

# 原始数据 + 对应类别
r3 = pd.Series(kmodel.labels_, index=data.index)
r = pd.concat([data, r3], axis=1)
r.columns = list(data.columns) + [u'聚类类别']
r.to_excel(outputfile)

# 各客户群的 R/F/M 密度分布图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
for i in range(k):
    cls = data[r[u'聚类类别'] == i]
    cls.plot(kind='kde', linewidth=2, subplots=True, sharex=False)
    plt.suptitle('客户群=%d;类聚数量=%d' % (i, r1[i]))
plt.legend()
plt.show()
