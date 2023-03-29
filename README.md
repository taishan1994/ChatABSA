# ChatSA
基于ChatGPT的情感分析，

简单的情感分析：给定一个句子，判断该句子所属的情感。

复杂点的情感分析，总共有7个子任务。

另外对比了一下百度的[UIE](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/applications/sentiment_analysis/unified_sentiment_extraction)

![7个ABSA子任务](https://img-blog.csdnimg.cn/20210623094417195.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2MjM0NDQx,size_16,color_FFFFFF,t_70)

### 如何使用

1、首先你得有一个openai的账号，并且在[Account API Keys - OpenAI API](https://platform.openai.com/account/api-keys)创建一个api key。

2、其次你得有一个vpn，vpn代理为全局模式。

3、修改main.py里面的df_access里面的api key。

4、选择不同的子任务运行即可。

### 结果

```python
---SA---
---begin---
给你一个例子：
给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！
你应该判断该句子的情感是什么，情感从['正面的', '负面的', '中性的']里选择。
输出列表：["正面的"]
如果不存在，回答：没有。
返回结果为输出列表。

现在，我给你一个句子，如"散热很好、低噪音、做工扎实、键盘舒适"，你应该判断句子的情感倾向，并以列表的形式返回结果，如果不存在，则回答：没有。
{'sentence': '散热很好、低噪音、做工扎实、键盘舒适', 'type': '', 'access': '', 'task': 'SA', 'lang': 'chinese', 'result': ['正面的'], 'mess': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': '给你 一个例子：\n给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！\n你应该判断该句子的情感是什么，情感从[\'正面的\', \'负面的\', \'中性的\']里选择。\n输出列表：["正面的"]\n如果不存在，回答：没有。\n返回结果为输出列表。\n\n现在，我给你一个句子，如"散热很好、低噪音、做工扎实、键盘舒适"，你应该该句子的情感倾向，并以列表的形式返回结果，如果不存在，则回答：没有。'}]}

---AE---
---begin---
给你一个例子：
给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！
给定实体类型列表:['方面']
你应该提取该句子里面的所有方面，这里的观点可能是对某方面的评价、介绍等。
输出列表：["地方", "石头", "环境", "景色"]
如果不存在，回答：没有。
返回结果为输出列表。

现在，我给你一个句子，如"味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢"，你应该提取里面所有实体类型为方面的实体，并以列表的形式返回结果，如果不存在，则回答：没有。
{'sentence': '味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢', 'type': '', 'access': '', 'task': 'AE', 'lang': 'chinese', 'result': ['味道', '服务'], 'mess': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': '给你一个例子：\n给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起 游玩！\n给定实体类型列表:[\'方面\']\n你应该提取该句子里面的所有方面，这里的观点可能是对某方面的评价、介绍等。\n输出列表 ：["地方", "石头", "环境", "景色"]\n如果不存在，回答：没有。\n返回结果为输出列表。\n\n现在，我给你一个句子，如"味道很不 错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢"，你应该提取里面所有实体类型为方面的实体，并以列表的形式返回结果， 如果不存在，则回答：没有。'}]}

---OE---
---begin---
给你一个例子：
给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！
给定实体类型列表:['观点']
你应该提取该句子里面的所有观点，这里的观点可能是对某方面的评价、介绍等，请注意你只需要提取出观点，不要方面。
输出列表：["值得去", "奇特", "优美", "宜人"]
如果不存在，回答：没有。
返回结果为输出列表。

现在，我给你一个句子，如"味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢"，你应该提取里面所有实体类型为观点的实体，并以列表的形式返回结果，如果不存在，则回答：没有。
{'sentence': '味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢', 'type': '', 'access': '', 'task': 'OE', 'lang': 'chinese', 'result': ['味道很不错', '喜欢吃', '服务也很好感觉很亲切', '吃的很舒服'], 'mess': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': '给你一个例子：\n给出的句子是：值得去的地方，石头 很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！\n给定实体类型列表:[\'观点\']\n你应该提取该句子里面的所有观点，这里 的观点可能是对某方面的评价、介绍等，请注意你只需要提取出观点，不要方面。\n输出列表：["值得去", "奇特", "优美", "宜人"]\n如果不存在，回答：没有。\n返回结果为输出列表。\n\n现在，我给你一个句子，如"味道很不错，很喜欢吃。服务也很好感觉很亲切， 吃的很舒服，谢谢"，你应该提取里面所有实体类型为观点的实体，并以列表的形式返回结果，如果不存在，则回答：没有。'}]}

---ALSC---
---begin---
给你一个例子：
给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！
给定一个方面，你需要判断它的情感是什么，从['正面的', '负面的', '中性的']里进行选择。
比如，给定方面"地方"，输出列表：["正面的"]
如果不存在，回答：没有。
返回结果为输出列表。

现在，我给你一个句子，如"味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢"，和一个方面"味道"，你应该判断它的情感，并以列表的形式返回结果，如果不存在，则回答：没有。
{'sentence': '味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢', 'type': '', 'aspect': '味道', 'access': '', 'task': 'ALSC', 'lang': 'chinese', 'result': [('味道', '正面的')], 'mess': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': '给你一个例子：\n给出的句子是：值得去的地方，石头很奇特，景色优美，环境 宜人，适合与朋友家人一起游玩！\n给定一个方面，你需要判断它的情感是什么，从[\'正面的\', \'负面的\', \'中性的\']里进行选择。\n比如，给定方面"地方"，输出列表：["正面的"]\n如果不存在，回答：没有。\n返回结果为输出列表。\n\n现在，我给你一个句子，如"味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢"，和一个方面"味道"，你应该判断它的情感，并以列表的形式返回结果，如果不存在，则回答：没有。'}]}

---AOE---
---begin---
给你一个例子：
给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！
给定一个方面，你需要识别它的观点或者修饰词是什么。
比如，给定方面"地方"，输出列表：["值得去"]，请注意结果不要带上方面。
如果不存在，回答：没有。
返回结果为输出列表。

现在，我给你一个句子，如"味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢"，和一个方面"味道"，你应该输出它的观点或修饰词，并以列表的形式返回结果，如果不存在，则回答：没有。
给定方面"味道"，则输出列表：["很不错", "很喜欢吃"]。
{'sentence': '味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢', 'type': '', 'aspect': '味道', 'access': '', 'task': 'AOE', 'lang': 'chinese', 'result': [('味道', '很不错'), ('味道', '很喜欢吃')], 'mess': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': '给你一个例子：\n给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！\n给定一个方面，你需要识别它的观点或者修饰词是什么。\n比如，给定方面" 地方"，输出列表：["值得去"]，请注意结果不要带上方面。\n如果不存在，回答：没有。\n返回结果为输出列表。\n\n现在，我给你一 个句子，如"味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢"，和一个方面"味道"，你应该输出它的观点或修饰词，并以列表的形式返回结果，如果不存在，则回答：没有。'}]}

---PAIR---
---begin---
给你一个例子：
给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！
你需要提取里面所有的方面及其对应的观点，请注意，方面可能是主体或者具有一定意义的名词，观点是形容某个方面的词。
输出列表：[("地方", "值得去"),("石头","奇特"),("环境", "优美"),("景色","宜人")]
如果不存在，回答：没有。
返回结果为输出列表。

现在，我给你一个句子，如"味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢"，请识别出里面所有的方面及其对应的观点，并以列表的形式返回结果，如果不存在，则回答：没有。
{'sentence': '味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢', 'type': '', 'access': '', 'task': 'PAIR', 'lang': 'chinese', 'result': [('味道', '不错'), ('服务', '好'), ('感觉', '亲切'), ('口感', '舒服')], 'mess': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': '给你一个例子：\n给出的句子是：值得去的 地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！\n你需要提取里面所有的方面及其对应的观点，请注意，方面可能是主体或者具有一定意义的名词，观点是形容某个方面的词。\n输出列表：[("地方", "值得去"),("石头","奇特"),("环境", "优美"),("景色","宜人")]\n如果不存在，回答：没有。\n返回结果为输出列表。\n\n现在，我给你一个句子，如"味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢"，请识别出里面所有的方面及其对应的观点，并以列表的形式返回结果，如果不存在，则回答：没 有。'}]}

---TRIPLET---
---begin---
给你一个例子：
给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！
你需要提取里面所有的方面及其对应的观点和情感，情感从['正面的', '负面的', '中立的']中选择，请注意，方面可能是主体或者具有一定意义的名词，观点是形容某个方面的词。
输出列表：[("地方", "值得去","正面的"),("石头","奇特","正面的"),("环境", "优美","正面的"),("景色","宜人","正面的")]
如果不存在，回答：没有。
返回结果为输出列表。

现在，我给你一个句子，如"味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢"，请识别出里面所有的方面及其对应的观点和情感，并以列表的形式返回结果，如果不存在，则回答：没有。
{'sentence': '味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢', 'type': '', 'access': '', 'task': 'TRIPLET', 'lang': 'chinese', 'result': [('味道', '不错', '正面的'), ('服务', '好', '正面的'), ('感觉', '亲切', '正面的'), ('吃的', '舒服', '正面的')], 'mess': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': '给你一个例子：\n给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！\n你需要提取里面所有的方面及其对应的观点和情感，情感从[\'正面的\', \'负面的\', \'中立的\']中选择，请注意，方面可能是主体或者具有一定意义的名词，观点是形容某个方面的词。\n输出列表：[("地方", "值得去","正面的"),("石头","奇特","正面的"),("环境", "优美","正面 的"),("景色","宜人","正面的")]\n如果不存在，回答：没有。\n返回结果为输出列表。\n\n现在，我给你一个句子，如"味道很不错， 很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢"，请识别出里面所有的方面及其对应的观点和情感，并以列表的形式返回结果， 如果不存在，则回答：没有。'}]}
```

最后这里以triplet为例，对不同领域的文本进行识别：

#### 酒店

```python
感觉很好，服务也不错，还会一如既往的关注，支持
[('感觉', '好', '正面的'), ('服务', '不错', '正面的'), ('关注', '一如既往', '正面的'), ('支持', '', '正面的')]

baidu-uie
感觉很好，服务也不错，还会一如既往的关注，支持
[('服务', '不错', '正向'), ('感觉', '好', '正向')]
```

#### KTV

```python
服务态度很好，环境也不错，就是点歌系统不太好用。
[('服务态度', '好', '正面的'), ('环境', '不错', '正面的'), ('点歌系统', '不太好用', '负面的')]

baidu-uie
服务态度很好，环境也不错，就是点歌系统不太好用。
[('服务', '好', '正向'), ('系统', '不太好', '负向'), ('环境', '不错', '正向')]
```


#### 丽人

```python
感觉不是很满意，不能对顾客有敷衍了事的行为，每次讲话老是有这么多的理由，态度和效果有待提高
[('感觉', '不满意', '负面的'), ('顾客对待', '敷衍了事', '负面的'), ('讲话', '理由过多', '负面的'), ('态度和效果', '有待提高', '负面的')]

baidu-uie
感觉不是很满意，不能对顾客有敷衍了事的行为，每次讲话老是有这么多的理由，态度和效果有待提高
[('效果', '有待提高', '负向')]
```

#### 美食

```python
味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢
[('味道', '不错', '正面的'), ('服务', '好', '正面的'), ('感觉', '亲切', '正面的'), ('吃的', '舒服', '正面的')]

baidu-uie
味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢
[('味道', '不错', '正向'), ('服务', '好', '正向')]
```

#### 旅游

```python
值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！
[('地方', '值得去', '正面的'), ('石头', '奇特', '正面的'), ('环境', '优美', '正面的'), ('景色', '宜人', '正面的')]

baidu-uie
值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！
[('景色', '美', '正向'), ('地方', '去', '正向'), ('环境', '宜人', '正向')]
```

#### 健康

```python
环境不错，进去就有暖气，叫的11号技师，服务确实不错，95后妹子，技术好，挺不错的体验
[('环境', '不错', '正面的'), ('暖气', '有', '正面的'), ('技师', '11号', '正面的'), ('服务', '不错', '正面的'), ('妹子', '95后', '正面的'), ('技术', '好', '正面的'), ('体验', '不错', '正面的')]

baidu-uie
环境不错，进去就有暖气，叫的11号技师，服务确实不错，95后妹子，技术好，挺不错的体验
[('环境', '不错', '正向'), ('体验', '不错', '正向'), ('服务', '不错', '正向'), ('技术', '好', '正向')]
```

#### 教育

```python
环境非常好，古香古色的教室。老师不错，随时能沟通孩子学习及吃饭情况！
[('环境', '好', '正面的'), ('教室', '古香古色', '正面的'), ('老师', '不错', '正面的'), ('沟通', '随时能', '正面的'), ('孩子学习及吃饭情况', '沟通', '正面的')]

baidu-uie
环境非常好，古香古色的教室。老师不错，随时能沟通孩子学习及吃饭情况！
[('老师', '不错', '正向'), ('环境', '好', '正向')]
```

#### 商业

```python
服务好 态度好 产品好 一句话就是好
[('服务', '好', '正面的'), ('态度', '好', '正面的'), ('产品', '好', '正面的')]

baidu-uie
服务好 态度好 产品好 一句话就是好
[[('产品', '', '正向')], ('服务', '好', '正向')]
```

#### 房产

```python
这小区不错。房价也不低。
[('小区', '不错', '正面的'), ('房价', '不低', '负面的')]

baidu-uie
这小区不错。房价也不低。
[('小区', '不错', '正向'), ('房价', '不低', '负向')]
```

#### 汽车

```python
"经济实惠、动力不错、油耗低"
[('价格', '实惠', '正面的'), ('动力', '不错', '正面的'), ('油耗', '低', '正面的')]

baidu-uie
经济实惠、动力不错、油耗低
[('油耗', '低', '正向'), ('动力', '不错', '正向'), ('经济', '实惠', '正向')]
```

#### 生活

```python
很好的浴室，干净清爽！前台热情
[('浴室', '很好', '正面的'), ('前台', '热情', '正面的'), ('浴室', '干净清爽', '正面的')]

baidu-uie
很好的浴室，干净清爽！前台热情
[('前台', '热情', '正向'), ('浴室', '好', '正向')]
```

#### 购物

```python
这才是正规专卖店啊，服务好，产品全面
[('专卖店', '正规', '正面的'), ('服务', '好', '正面的'), ('产品', '全面', '正面的')]

baidu-uie
这才是正规专卖店啊，服务好，产品全面
[('服务', '好', '正向'), ('产品', '全面', '正向')]
```

#### 3C

```python
散热很好、低噪音、做工扎实、键盘舒适
[('散热', '很好', '正面的'), ('噪音', '低', '正面的'), ('做工', '扎实', '正面的'), ('键盘', '舒适', '正面的')]

baidu-uie
散热很好、低噪音、做工扎实、键盘舒适
[('散热', '好', '正向'), ('做工', '扎实', '正向'), ('键盘', '舒适', '正向')]
```

# 补充

该项目受https://github.com/cocacola-lab/ChatIE/ 的启发，代码参考其，在此表示感谢。

样例数据来源：https://ai.baidu.com/tech/nlp_apply/comment_tag

### 引用
```
@misc{ChatSA,
  author = {Oubo Gong},
  title = {Sentiment analysis with chatGPT},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  url="https://github.com/taishan1994/ChatSA",
}
```
