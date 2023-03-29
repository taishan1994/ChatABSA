"""
python == 3.9.12
paddlepaddle == 2.3.2
paddlenlp == 2.5.2
wordcloud == 1.8.2.2
"""
from paddlenlp import Taskflow
from pprint import pprint

import paddlenlp
import paddle

print(paddlenlp.__version__)
print(paddle.__version__)

schema = [{"评价维度": ["观点词", "情感倾向[正向,负向,未提及]"]}]

senta = Taskflow("sentiment_analysis", model="uie-senta-base", schema=schema)
# print(senta('蛋糕味道不错，店家服务也很热情'))

sens = [
    "味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢",
    "感觉很好，服务也不错，还会一如既往的关注，支持",
    "服务态度很好，环境也不错，就是点歌系统不太好用。",
    "感觉不是很满意，不能对顾客有敷衍了事的行为，每次讲话老是有这么多的理由，态度和效果有待提高",
    "味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢",
    "值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！",
    "环境不错，进去就有暖气，叫的11号技师，服务确实不错，95后妹子，技术好，挺不错的体验",
    "环境非常好，古香古色的教室。老师不错，随时能沟通孩子学习及吃饭情况！",
    "服务好 态度好 产品好 一句话就是好",
    "这小区不错。房价也不低。",
    "经济实惠、动力不错、油耗低",
    "很好的浴室，干净清爽！前台热情",
    "这才是正规专卖店啊，服务好，产品全面",
    "散热很好、低噪音、做工扎实、键盘舒适",
]

for sen in sens:
    result = []
    res = senta(sen)
    for span in res:
        pjwds = span["评价维度"]
        for pjwd in pjwds:
            aspect = pjwd["text"]
            rel = pjwd["relations"]
            opinions = rel["观点词"] if "观点词" in rel else []
            sentiments = rel["情感倾向[正向,负向,未提及]"] if "情感倾向[正向,负向,未提及]" in rel else []
            if len(opinions) == len(sentiments):
                for opinion, sentiment in zip(opinions, sentiments):
                    opinion_text = opinion["text"]
                    sen_text = sentiment["text"]
                    result.append((aspect, opinion_text, sen_text))
            else:
                if len(opinions) != 0:
                    for opinion in opinions:
                        opinion_text = opinion["text"]
                        result.append([(aspect, opinion_text, "")])
                if len(sentiments) != 0:
                    for sentiment in sentiments:
                        sen_text = sentiment["text"]
                        result.append([(aspect, "", sen_text)])

    print(sen)
    print(result)
