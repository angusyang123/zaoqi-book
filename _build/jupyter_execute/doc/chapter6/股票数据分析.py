#!/usr/bin/env python
# coding: utf-8

# # 股票数据分析
# 
# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```
# 
# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！
# ```

# ## 本页面数据说明
# 
# 
# 为了更好的介绍相关操作，本页面使用 **某股票数据** 数据进行展开，你应该对数据字段、数值、类型等相关信息做一个大致了解！

# In[1]:


import pandas as pd
import warnings
warnings.filterwarnings("ignore")
df1 = pd.read_csv("000001_daily.csv")
df2 = pd.read_csv("000001_5min.csv")
df1.head()


# ## 时间类型转换
# 
# 将 df1 和 df2 的 日期 列转换为 pandas 支持的时间格式

# In[2]:


df1['日期'] = pd.to_datetime(df1['日期'])
df2['时间'] = pd.to_datetime(df2['时间'])
# df1['日期'] = df1['日期'].astype('datetime64[ns]')


# ## 日期筛选

# ### 按区间筛选
# 
# 筛选出 df2 时间在 `2021-08-03 09:35:00` 与 `2021-08-04 15:00:00` 之间的数据

# In[3]:


df2[(df2['时间'] > '2021-08-03 09:35:00') & (df2['时间'] < '2021-08-04 15:00:00')]


# ### 按指定时间筛选
# 
# 筛选 df2 时间为 2021-08-03 的全部数据

# In[4]:


df2.set_index('时间').truncate(after=pd.Timestamp('2021-08-04'))


# ## 金融计算

# ### 涨跌额
# 
# `df1` 新增一列 涨跌，计算前后两日收盘价之差
# 
# 注意：虽然我们的df1包含涨跌额列，但是这个操作很常用，所以练习一下

# In[5]:


df1['涨跌']  = df1.收盘.diff()


# ### 涨跌幅
# 
# `df1` 新增一列 涨跌变化率，计算前后两日收盘价之差的变化率
# 
# 注意：虽然我们的df1包含涨跌幅列，但是这个操作很常用，所以练习一下，结果可以用于验证

# In[6]:


df1['涨跌变化率'] = (df1.收盘.pct_change()).apply(lambda x: format(x, '.2%'))


# ### 移动均值
# 
# 计算收盘价的5日移动均线

# In[7]:


df1.收盘.rolling(window=5).mean()


# ### 移动均值（可视化）
# 
# 计算并绘制收盘价的5日移动均线

# In[8]:


df1.收盘.rolling(window=5).mean().plot()


# ### 移动均值（可视化）
# 
# 同时计算并绘制 df1 的收盘价、5日均线、20日均线

# In[9]:


df1.set_index("日期")['收盘'].plot()
df1.set_index("日期")['收盘'].rolling(5).mean().plot()
df1.set_index("日期")['收盘'].rolling(20).mean().plot()


# ### 指数移动平均值（EMA）
# 
# 根据 df1 计算 EMA20

# In[10]:


df1['EMA20'] = df1['收盘'].ewm(span=20,min_periods=0,adjust=False,ignore_na=False).mean()


# ### MACD
# 
# 计算 df1 的 MACD 指标

# In[11]:


exp1 = df1['收盘'].ewm(span=12, adjust=False).mean()
exp2 = df1['收盘'].ewm(span=26, adjust=False).mean()
df1['MACD'] = exp1 - exp2
df1['Signal line'] = df1['MACD'].ewm(span=9, adjust=False).mean()


# ### 布林指标
# 
# 计算并绘制布林指标，计算方法参考[百度百科](https://baike.baidu.com/item/%E5%B8%83%E6%9E%97%E7%BA%BF%E6%8C%87%E6%A0%87/3325894?fromtitle=%E5%B8%83%E6%9E%97%E6%8C%87%E6%A0%87&fromid=258891&fr=aladdin)
# 

# In[12]:


df1['former 30 days rolling Close mean'] = df1['收盘'].rolling(20).mean()
df1['upper bound'] = df1['former 30 days rolling Close mean'] +     2*df1['收盘'].rolling(20).std()  # 在这里我们取20天内的标准差
df1['lower bound'] = df1['former 30 days rolling Close mean'] -     2*df1['收盘'].rolling(20).std()

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Songti SC'] #设置中文，如果本句代码导致失效，可以点击https://mp.weixin.qq.com/s/WKOGvQP-6QUAP00ZXjhweg

df1.set_index("日期")[['收盘', 'former 30 days rolling Close mean','upper bound','lower bound' ]].plot(figsize=(16, 6))

plt.show()


# ## 日期移动

# ### 移动值
# 
# 将 df1 的索引设置为日期，将 df1 数据向后移动一天

# In[13]:


df1.set_index('日期').shift(1)


# ### 移动索引
# 
# 将 df1 的索引设置为日期，并将全部日期向后移动一天

# In[14]:


import datetime
df1.set_index('日期').shift(freq=datetime.timedelta(1))


# ## 日期重采样

# ### 日 -> 周
# 
# 按周对 df1 进行重采样，保留每周最后一个数据

# In[15]:


df1.set_index('日期').resample('W').last()


# ### 日 -> 月
# 
# 按月对 df1 进行重采样，保留每月最后一个数据

# In[16]:


df1.set_index('日期').resample('M').last()


# ### 分钟 -> 日
# 
# 按日对 df2 进行重采样，保留每天最后一个数据

# In[17]:


df2.set_index('时间').resample('D').last()


# ### 低频 -> 高频
# 
# 将 df2 的 5分钟 数据改为 3分钟，缺失数据向前填充

# In[18]:


df_3min = df2.set_index('时间').resample('3min').last()
df_3min.ffill()

