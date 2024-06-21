#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#添加以下代码以显示单元格中的所有输出
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False #显示负号


# # **第7课 科学计算基础 Pandas**

# ## **§7.1 pandas库的简介** 

#   **Pandas 是一个开源的第三方 Python 库，从 Numpy 和 Matplotlib   
# 的基础上构建而来，享有数据分析“三剑客之一”的盛名(NumPy、Matplotlib、Pandas)。  
#   Pandas 库的主要应用方向：针对多维结构化数据集的分析处理。  
#   Pandas 库为 Python 语言提供了高性能、易于使用的数据结构和数据  
# 分析工具集，它的目标是成为强大、灵活、可以支持任何编程语言的数据分析工具。**
pandas模块的导入:
  import numpy as np
  import pandas as pd 
#   **Pandas 库是以Numpy库为基础构建的，通常用来处理表格型(关系型)的数据集  
# 或与时间序列相关的数据集。  
#   Series对象有着与一维数组相似的结构，是带标签(索引)的一维同构数组。  
#   DataFrame是一个表格型的数据结构，是带标签的，大小可变的，二维异构表格。**

# ## **§7.2 Series对象的应用** 

# ### **1. Series对象的创建**

# **Series创建语句：pd.Series(data, index, dtype, name, copy)**

# #### **(1). ndarray创建,默认索引**

# In[ ]:


import numpy as np
import pandas as pd 


# In[ ]:


data = np.array([2, 4, 6, 8])
s1 = pd.Series(data)
print('默认索引: ')
s1


# #### **(2). ndarray创建,自定义索引**

# In[ ]:


### 自定义索引
data = np.array([2, 4, 6, 8])
s2 = pd.Series(data, index=[100, 101, 102, 103])
print("自定义索引：")
s2


# #### **(3) dict创建**

# In[ ]:


data = {'a': 0, 'b': 1, 'c': 2}
s1_dict = pd.Series(data)
print('没有传递索引:')
s1_dict


# #### **(4) dict创建,传递索引**

# In[ ]:


data = {'a': 0, 'b': 1, 'c': 2}
s2_dict = pd.Series(data, index=['a', 'b', 'c', 'd'])
print('传递索引:')
s2_dict


# #### **(5). 标量创建，则必须提供索引**

# In[ ]:


s3 = pd.Series(6, index=[0, 1, 2, 3])
print('标量值:')
s3


# #### **(6). Series的属性**

# In[ ]:


s1.axes
s1.dtype
s1.empty
s1.ndim


# In[ ]:


s1.size
s1.values
s1.index
s1.name = "Integers"
s1.name


# ### **2. Series的常见运算**

# **Series对象可以在对象上做常见的数组运算，如标量代数运算、  
# 数据过滤、应用数学函数等。**

# #### **(1).代数运算**

# In[ ]:


ls = ['a', 'b', 'c', 'd']
data = [10, 20, 30, 10]
s2 = pd.Series(data, index=ls)
s2


# In[ ]:


s2+s2
s2*s2
s2**2


# #### **(2).筛选数据**

# In[ ]:


s2[s2 > 10]


# #### **(3).函数(节选)**

# In[ ]:


s2.rank(method='dense')
'''
method{'average', 'min', 'max', 'first', 'dense'}, default 'average'
      How to rank the group of records that have the same value (i.e. ties):
dense: like 'min', but rank always increases by 1 between groups.
'''


# In[ ]:


np.sqrt(s2)
s2.sort_values()
s2.rank(method='dense')##对数据进行排序操作
s2.value_counts()


# ### **3. Series的索引与访问**

# **Series 访问数据分为两种方式: 一种是位置索引；另一种是标签索引**

# #### **(1). 位置索引**

# In[ ]:


s = pd.Series([1, 2, 3, 4, 5],
    index=['a', 'b', 'c', 'd', 'e'])
print('Series数据')
s


# In[ ]:


print('位置索引 = ' + str(s[0]))
print('\n前两个元素:')
s[:2]
print('\n最后三个元素:')
s[-3:]


# #### **(2). 标签索引**

# In[ ]:


print('\n访问单个元素 = ' + str(s["a"]))
print('\n访问多个元素: ')
s[["a", "b", "c"]]
print('\n访问不包括的标签g,会报异常: ')
#s["g"]


# ## **§7.3 DataFrame对象的应用** 

# ### **1. DataFrame的属性(节选)**

# |名称|属性描述|
# |---|---|
# |T|行和列转置|
# |index|返回一个仅以行轴标签和列轴标签为成员的列表。|
# |dtypes|返回每列数据的数据类型。|
# |empty|DataFrame中没有数据或者任意坐标轴的长度为0，则返回True。|
# |ndim|轴的数量，也指数组的维数。|
# |shape|返回一个元组，表示了 DataFrame 维度。|
# |size|DataFrame中的元素数量。|
# |values|使用 numpy 数组表示 DataFrame 中的元素值。|taFrame 中的元素值。
# 

# ### **2. DataFrame的统计方法(节选)**

# |名称|方法描述|
# |---|---|
# |head()|返回前n行数据。|
# |tail()|返回后n行数据。|
# |shift()|将行或列移动指定的步幅长度|
# |count()|统计某个非空值的数量。|
# |sum()|求和|
# |mean()|求均值|
# |std()|求标准差|
# |min()|求最小值|
# |max()|求最大值|
# |abs()|求绝对值|

# ### **3. 数据文件的导入和导出**

# #### **(1). csv文件的读写**

# In[ ]:


import numpy as np
import pandas as pd 
df = pd.read_csv('File&Figure/data1.csv', header=0)
df.to_csv('File&Figure/result2.csv')


# #### **(2). excel文件的读**

# In[ ]:


df1 = pd.read_excel('File&Figure/data3.xlsx')
df1.to_excel('File&Figure/result1.xlsx', sheet_name='sheet1')


# #### **(3). html文件的读写**

# In[ ]:


df2 = pd.read_html('File&Figure\Advanced\mobile1.html')
df.to_html('File&Figure\Advanced\result4.html')


# <img style="float:left;" src="File&Figure\Advanced\71pandasfile1.png" width="75%">

# ### **4. 创建DataFrame对象**

# **创建DataFrame语法格式：pd.DataFrame( data, index, columns, dtype, copy)**

# #### **(1). 由字典创建，字典中每个键对应的数据是等长的列表或Numpy数组。**

# In[ ]:


import numpy as np
import pandas as pd 
dic ={'城市':['北京','上海','广州','深圳','重庆'],
      '人口':[2171,2418,1090,1404,3372],
      'GDP':[28000,30133,21500,22286,19530]}
df =pd.DataFrame(dic)
df


# In[ ]:


df1 = pd.DataFrame(dic, index=[i for i in range(len(dic['城市']))])
df1


# #### **(2). 由字典创建，自定义索引**

# In[ ]:


df =pd.DataFrame(dic,    index=[2,1,4,3,5],
                 columns=['城市','GDP','人口'])
df


# #### **(3). 由Series创建**

# In[ ]:


dic = {'城市': pd.Series(['北京', '上海', '广州', '深圳', '重庆']),
    '人口': pd.Series([2171, 2418, 1090, 1404, 3372]),
    'GDP': pd.Series([28000, 30133, 21500, 22286, 19530])}
df1 = pd.DataFrame(dic)
df1


# #### **(4). 由Series创建，自定义索引**

# In[ ]:


df1 = pd.DataFrame(dic, index=[2, 1, 4, 3, 0])
df1


# #### **(5). DataFrame的属性**
df1.shape
df1.index
df1.columns
df1.values
df1.dtypes
df1.ndim
df1.size
df1.T
# In[ ]:


df1.shape


# In[ ]:


df1.ndim


# In[ ]:


df1.info


# #### **(6). 统计计算(节选)**
df1.max()
df1.count()
df1.sum()
df1.mean()
df1['人口'].abs()
df1.cumsum()
# In[ ]:


df1['人口'].abs()


# In[ ]:


df1.count()


# ## **§7.5. DataFrame对象的数据操作**

# #### **行与列的增删改查、数据清洗等操作**
# #### **数据操作时，又分索引和不索引两种，例如：**

# In[ ]:


import numpy as np
import pandas as pd
dic = {'城市': pd.Series(['北京', '上海', '广州', '深圳', '重庆']),
    '人口': pd.Series([2171, 2418, 1090, 1404, 3372]),
    'GDP': pd.Series([28000, 30133, 21500, 22286, 19530])}
df = pd.DataFrame(dic)
df


# ### **不加索引时，默认以序号为关键字操作，例如：**

# #### **增加与修改**

# In[ ]:


df.loc[10] = ['镇江', 285, 910]
df.loc[0] = 1  # 第一行都改成 1
df


# #### **查询**

# In[ ]:


df.loc[10]
df.iloc[1:3]


# #### **删除**

# In[ ]:


df.drop(10, inplace=False)
print("\n删除记录 10(True)：\n")
df


# In[ ]:


df.drop(1, inplace=False)
print("\n删除记录 1(False)：\n")
df


# ### **下面操作以‘城市’标签索引为例**

# In[ ]:


import numpy as np
import pandas as pd
dic = {'城市': pd.Series(['北京', '上海', '广州', '深圳', '重庆']),
    '人口': pd.Series([2171, 2418, 1090, 1404, 3372]),
    'GDP': pd.Series([28000, 30133, 21500, 22286, 19530])}
df =pd.DataFrame(dic, columns=['城市','GDP','人口'])
#'城市'索引
df = df.set_index(['城市'])
df


# ### **1. 增加**

# #### **(1). 增加新行**

# In[ ]:


df.loc['镇江'] = [285, 910]
df


# #### **(2). 增加新列**

# In[ ]:


### I. 
df['新增的列'] = range(1,len(df)+1)
df['新增的列2'] = range(10,len(df)+10)
df['新增的列5'] = [i*20 for i in range(1,len(df)+1)]
df['新增的列3'] = ['abc','bc',np.nan,'addc','efsgs',np.nan]
df['新增的列4'] = ['fabc','fdgbc','cdgfdd',np.nan,'efsgs','toefsgs']
df


# ### **2. 修改**

# #### **(1). 修改一个元素**

# In[ ]:


df.loc['深圳', '新增的列2'] = 5
df.at['上海', '新增的列2'] = 2841
df.loc['广州', '新增的列2'] = 25100
df


# #### **(2). 修改一行**

# In[ ]:


df.loc['广州'] = [1100, 22000, 7, 87, 88, 'jkjkkj', 'trdfh']
df


# #### **(3). 修改一列**

# In[ ]:


df['新增的列5'] = [i*55 for i in range(len(df))]### 修改
df


# #### **(4). 修改区间(闭区间)**

# In[ ]:


df.loc['广州', '新增的列':'新增的列5'] = [3, 4, 5]
df.loc['上海': '重庆', '新增的列'] = [12300, 9800, 23000, 7]
df


# ### **3. 删除**
DataFrame.drop(labels=None, *, axis=0, index=None, columns=None,
               level=None, inplace=False, errors='raise')
     axis=1表示针对列的操作，inplace为True
# #### (1). 删除指定行与列、多列 drop()

# In[ ]:


df.drop('镇江',axis=0, inplace=True) # axis=0代表删除行
df


# In[ ]:


#删除多列
df.drop('新增的列5',axis=1, inplace=True) # axis=1代表删除列
df.drop(['新增的列','新增的列2'],axis=1, inplace=True) # axis=1代表删除列
df


# #### **(2). 删除字段为空的行与列，dropna函数**

# **dropna函数默认删除所有出现空的行，即一行中任意一个字段为空，就会被删除。  
# 当只需要删除某一列的空行时，需要设置subset参数，例如dropna(subset=['city'])**

# In[ ]:


df.dropna(subset=["新增的列4"],inplace=True) 
df


# #### **(3). 删除字段重复的行**
# drop_duplicates(subset = '列名',keep='first')
# ### **4. 查找**

# #### **(1). 点**

# In[ ]:


df.at['上海', '人口']


# #### **(2). 行**

# In[ ]:


df.loc['北京']


# #### **(3). 列**

# In[ ]:


df['GDP']


# #### **(4). 区间**

# In[ ]:


### 行区间
df.loc['北京':'广州']


# In[ ]:


## 特定字符行
df.loc[['北京', '广州', '重庆']]


# In[ ]:


df.loc['北京':'广州', 'GDP']


# In[ ]:


df.loc['北京':'广州', 'GDP':'人口']


# #### **(5) 数据筛选**

# In[ ]:


df[df['人口'] > 3000]
df.loc[(df['GDP'] > 20000) & (df['人口'] > 2000)]


# ### **5. 排序**

# In[ ]:


dic = {'城市': ['广州', '苏州', '杭州',
                '南京','宁波','深圳'],
       '人口': [1090, 1065, 919,  827, 788, 1404],
       'GDP': [21500, 17319, 12556, 11715, 9846, 22286],
       '省份': ['广东','江苏','浙江','江苏','浙江','广东']}
df = pd.DataFrame(dic, columns=['省份', '城市', 'GDP', '人口'])
#df = df.set_index(['城市'])
df


# In[ ]:


print('按城市GDP从高到低排序')
df.sort_values('GDP', ascending=False)


# In[ ]:


print('按城市人口从高到低排序')
df.sort_values(by='人口', ascending=False)


# ### **6. 数据的分组**

# In[ ]:


group = df.groupby('省份')
group


# In[ ]:


print('各省GDP值最高的城市')
group.max()


# In[ ]:


total = group.sum()
print('各省人均GDP值(2位小数)')
(total['GDP']/total['人口']).round(2)


# ### **7. 给数据打标签**

# In[ ]:


df['等级'] = pd.cut(df['GDP'], bins=[0, 10000, 20000, 30000, 40000], labels=['D','C','B','A'])
df


# ### **8. 绘制GDP及人口柱形图**

# In[ ]:


from matplotlib import  pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['SimHei']   #显示中文
dic = {'城市': ['广州', '苏州', '杭州', '南京', '宁波', '深圳'],
       '人口': [1090, 1065, 919,  827, 788, 1404],
       'GDP': [21500, 17319, 12556, 11715, 9846, 22286],
       '省份': ['广东', '江苏', '浙江', '江苏', '浙江', '广东']}
df = pd.DataFrame(dic, columns=['省份', '城市', 'GDP', '人口'])
df = df.set_index(['城市'])
df['GDP'] = df['GDP']/10
df.rename({'GDP': 'GDP/10'}, axis='columns', inplace=True)
df.plot(kind='bar', title='2017年城市GDP及人口数据', figsize=(4.5, 3))
plt.show()


# ### **9. 数据清洗**

# **① 删除缺失数据行: df.dropna(how='any', inplace=False)  
# ② 数据填充--用平均值填充缺失的价格: df.fillna(avg_price)  
# ③ 统一数据格式: rename()函数：重命名某些选定列;   
#                使用.replace()、 .astype()、  .str.replace()、  
#                .str.replace().astype()方法统一数据格式。  
# ④ 去除重复数据: pd.concat([df1, df1])**

# In[ ]:


#添加以下代码以显示单元格中的所有输出
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
# 让notebook宽屏显示
from IPython.display import display, HTML
display(HTML('<style>.container{width:100% !important;}</style>'))
import numpy as np
import pandas as pd


# In[ ]:


datadic1 = {'编号': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009],
            '日期': pd.date_range('20181001', periods=9),
            '品牌': ['HW', 'Apple', 'samsung', 'HuaWei', 'xiaomi', 'oppo',
                    'APPLE', 'NOLIA', 'vivo'],
            '型号': ['P20 Pro', 'iPhone XR', 'Note 9', 'Mate 20', ' ',
                   'Find X', 'iPhone XS', 'NOLIA 8 Sirocco', 'NEX'],
            '配置/GB': ['6~128G', '4~128G', '6~128G', '6~128G', '8~128G',
                  '8~256G', '4~256G', '6~128G', '8~128G', ],
            '价格/元': [4988, 6999, 6999, np.nan  , 3599, 5999, 10165, 3499, 4298]}
df1 = pd.DataFrame(datadic1,
                   columns=['编号', '日期', '品牌', '型号', '配置/GB', '价格/元'])
df1 = df1.set_index('编号')#设置索引
df1


# In[ ]:


datadic2 = {'编号': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1010],
            '国家': ['China', 'USA', 'Korea', 'China', 'China', 'China',
                     'USA', 'Finland', 'Japan', ], 
            '系统': ['Android', 'ISO', 'Android', 'Android', 'Android',
                     'Android', 'ISO', 'Android', 'Android', ], 
            '屏幕尺寸': [6.1, 6.1, 6.4, 6.5, 6.2, 6.4, 5.8, 5.5, 6.0]}
df2 = pd.DataFrame(datadic2)
df2 = df2.set_index('编号')
df2


# #### **数据清洗. ① 删除缺失数据行**

# In[ ]:


df1.dropna(how='any', inplace=False)


# #### **数据清洗. ② 数据填充--用平均值填充缺失的价格**

# In[ ]:


avg_price = df1['价格/元'].mean() 
df1.fillna(avg_price)


# #### **数据清洗. ③ 统一数据格式**

# In[ ]:


df1['配置/GB'] = df1['配置/GB'].str.replace('G', '')
df_split = pd.DataFrame((x.split('~') for x in df1['配置/GB']),
                        index=df1.index,
                        columns=['运行内存/GB','存储容量'])
df1 = pd.merge(df1, df_split, right_index= True, left_index= True)
df1.drop('配置/GB', axis=1, inplace=True)
df1


# #### **数据清洗. ④ 合并两个表格**

# In[ ]:


df1 = pd.merge(df1,df2['屏幕尺寸'],  right_index= True, left_index= True)
df1


# #### **数据清洗. ⑤​​​ ​去除重复数据**

# In[ ]:


repeat = pd.concat([df1, df1])
print('两个数据帧合并后：')
repeat


# In[ ]:


print('删除重复数据后数据帧：')
repeat.drop_duplicates()


# ### **10. 表格的合并**

# |方法|简介|
# |---|---|
# |concat()|提供行方向和列方向进行内联或外联的拼接操作|
# |join()|提供类似于SQL数据库中的join连接功能，支持左联、右联、内联和外联等全部四种SQL连接操作类型|
# |merge()|提供行方向的拼接操作|
# |append()|提供列方向的拼接操作，支持左联、右联、内联和外联四种操作类型。|

# |参数值|连接方式|功能描述|
# |---|---|---|
# |inner|内连接(默认)|根据数据对象之间连接主键的交集进行合并|
# |outer|外连接|根据数据对象之间连接主键的并集进行合并|
# |left|左连接|只根据左数据表(第一个参数对象)的主键进行合并|
# |right|右连接|只根据右数据表(第二个参数对象)的主键进行合并|

# ## **§7.7 数据分析相关库应用实例** 

# ## End
