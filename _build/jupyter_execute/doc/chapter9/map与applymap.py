#!/usr/bin/env python
# coding: utf-8

# # map 与 applymap
# 
# 
# `pandas` 中的 `map` 和 `applymap` 可以对指定列（map）或整个数据框（applymap）工作
# 
# 完成替换、格式化、计算等操作，是 `Pandas` 数据分析中十分重要的工具。
# 
# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```
# 
# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！
# ````

# ## 本页面数据说明
# 
# 为了更好的介绍相关操作，你应该对数据字段、数值、类型等相关信息做一个大致了解！

# In[1]:


import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': ['A0', 'A1', np.nan, 'A3'],
                    'B': ['B0',np.nan,'B3',np.nan],
                    'C': ['C0','C1','C2',np.nan],
                    'D': np.random.randn(4),
                    'E': np.random.randn(4),
                   'F': np.random.randn(4)},
                   index=[0, 1, 2, 3])

df1


# ## 基本使用
# 
# 将 `df1` 第一列中的 `A0` 替换为 `cat`，`A3` 替换为 `rabbit`，其余为设置为`NaN`（缺失值）

# In[2]:


df1['A'] = df1['A'].map({'A0':'cat','A3':'rabbit'})
df1


# ## 匿名函数
# 
# 在上一题的结果上，将 df1 第 1 列中的字符末尾追加「今天关注了早起Python」

# In[3]:


df1['A'] = df1['A'].map(lambda x:f'{x} 今天关注了早起Python')
df1


# ## 跳过缺失值
# 
# 上一题中，nan（缺失值）也被同步追加了字符串
# 
# 现在重新对第二列执行同样的操作，并跳过缺失值

# In[4]:


df1['B'] = df1['B'].map(lambda x:f'{x} 今天关注了早起Python', na_action='ignore')
df1


# ## 自定义函数
# 
# 除了 lambda ，map还可以接受自定义函数，现在对第三列，使用自定义函数完成上一题的任务

# In[5]:


def mapfun(x):
    
    return str(x) + "今天关注了早起Python"

df1['C'] = df1['C'].map(mapfun, na_action='ignore')
df1


# ## applymap
# 
# `applymap`可以对整个 `dataframe` 工作，现在将 df1 的最后三列保留两位小数

# In[6]:


df1[['D','E','F']] = df1[['D','E','F']].applymap(lambda x:"%.2f" % x)
df1

