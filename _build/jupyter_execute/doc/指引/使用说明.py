#!/usr/bin/env python
# coding: utf-8

# (content:document)=
# 
# # 使用说明
# 
# 本网站是一份 pandas 教程，改编自微信公众号「[早起Python](https://pic.liuzaoqi.com/picgo/202112150908823.jpeg) 」出品的「 [Pandas进阶修炼300题](https://mp.weixin.qq.com/s/GW6OxfwIp2X8p2X9fcQZOg) 」
# 
# ## 诞生日记
# 
# 
# 即使我已经使用 `pandas` 近四年，但是对于一些命令、参数，我也只能达到了解的程度，常常也需要阅读官方文档或者检索一些教程。
# 
# 在这期间我分享了很多 pandas 相关操作解析的文章，意外的收到了很多的朋友的好评，于是为了更系统的帮助更多用户学习 pandas，[Pandas进阶修炼120题与300题](https://mp.weixin.qq.com/s/GW6OxfwIp2X8p2X9fcQZOg) 先后诞生了。
# 
# 伴随着刷题人数越来越多，很多粉丝问我能否提供一份查询版，答案就附在习题下面，但整理出来之后发现偶尔想查询一些小的操作都需要启动 `Jupyter Notebook` ，再点开多层文件夹才能找到，使用体验并不是很好。
# 
# 并且相信大家在搜索部分 `pandas` 操作时，并不难找到相关的帖子或者教程，但是在阅读这些文章时会有一个体验即**看上去很过瘾，自己一操作就各种报错，加上有些作者并没有分享源数据，导致很多文章内的操作复现很难**。
# 
# 我也在阅读某些讲解时，常常会想<font color='tomato'>**要是能直接在这个页面执行一下该有多爽**</font>！
# 
# 于是，干脆直接将这份习题做成了网页版，考虑到很多新手朋友，该版本添加了一些入门讲解，并对一些核心章节（分组、合并、透视、聚合）添加了过程图解，以方便更多刚接触 Pandas 的用户快速上手。
# 
# 更重要的是，在「**图解Pandas**」中，大部分页面的代码支持**在线执行**，你可以先通过页面开头的数据预览对本页面的数据结构有一个大致的了解，<font color='tomato'>**之后无需跳转到其他网站，可以在感兴趣的单元格下直接执行对应代码，或者修改相关参数来验证你的想法**</font>。
# 
# 要了解更多与在线执行代码更详细的说明可以参阅[在线执行代码](在线执行.md)
# 
# 
# ## 善用搜索
# 
# 如果你想快速查询某个函数的用法，最简单的方法就是使用搜索功能，通过在页面左上方搜索框输入对应关键词可以返回所有包含该关键词的全部页面，并高亮显示
# 
# ```{admonition} 注意
# :class: attention
# 
# 目前仅支持检索英文关键词，所有包含中文的返回结果都将为空。
# ```
# 
# 
# ## 刷题结合
# 
# 网站内大多数教程改编自微信公众号「[早起Python](https://pic.liuzaoqi.com/picgo/202112150908823.jpeg) 」出品的「 [Pandas进阶修炼300题](https://mp.weixin.qq.com/s/GW6OxfwIp2X8p2X9fcQZOg) 」，建议想进一步学习或者评估自己 `Pandas` 数据分析能力的用户可以[下载这份习题](https://mp.weixin.qq.com/s/GW6OxfwIp2X8p2X9fcQZOg) 或者[在线练习](https://www.heywhale.com/mw/project/6146c0318447b8001769ff20) ，习题内含有更多真实数据集分析操作，欢迎体验。
# 
# ## 规范转载
# 
# 本网站内容大多数教程改编自微信公众号「[早起Python](https://pic.liuzaoqi.com/picgo/202112150908823.jpeg) 」出品的「 [Pandas进阶修炼300题](https://mp.weixin.qq.com/s/GW6OxfwIp2X8p2X9fcQZOg) 」，转载请联系公众号「[早起Python](https://pic.liuzaoqi.com/picgo/202112150908823.jpeg) 」，未获得授权请勿以任何形式进行转载。
# 
# ## 提个issue💡
# 
# 从内容设计到网站开发都是一个人完成，难免会有一些疏忽、遗漏。
# 
# 对于网站内任何页面，都可以也欢迎给我提出建议，您的建议可以是技术相关，例如某个操作的更多实现方法，某个参数更直接明了的解释，也可以是网站体验相关，例如某个页面加载太慢，字体、图片大小不合适或者希望添加相关内容的讲解，都可以点击页面右上方 `GitHub` 按钮进入仓库提 `issue`。 
# ```{raw} html
# <script src="https://utteranc.es/client.js"
#         repo="liuhuanshuo/zaoqi-book"
#         issue-term="pathname"
#         theme="github-light"
#         crossorigin="anonymous"
#         async>
# </script>
# ```
