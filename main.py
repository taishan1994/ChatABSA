# coding=utf-8
# openai==0.27.2
import openai
import urllib.request
import os
import regex

os.environ["http_proxy"] = "http://127.0.0.1:1080"
os.environ["https_proxy"] = "http://127.0.0.1:1080"
print(urllib.request.getproxies())

df_access = [
    ('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',)
]

df_sat = {
    "english": {"sentiment": ["positive", "negative", "neutral"]},
    "chinese": {"情感": ["正面的", "负面的", "中性的"]},
}

df_aet = {
    "english": ["aspect"],
    "chinese": ["方面"],
}
df_oet = {
    "english": ["opinion"],
    "chinese": ["观点"],
}
df_alsct = {
    "english": {"aspect": {"sentiment": ["positive", "negative", "neutral"]}},
    "chinese": {"方面": {"情感": ["正面的", "负面的", "中性的"]}},
}
df_aoet = {
    "english": {"aspect": "opinion"},
    "chinese": {"方面": "观点"},
}
df_aesct = {
    "english": {"aspect": {"sentiment": ["positive", "negative", "neutral"]}},
    "chinese": {"方面": {"情感": ["正面的", "负面的", "中性的"]}},
}
df_pairt = {
    "english": {"aspect": "opinion"},
    "chinese": {"方面": "观点"},
}
df_triplett = {
    "english": ["aspect", "opinion", {"sentiment": ["positive", "negative", "neutral"]}],
    "chinese": ["方面", "观点", {"情感": ["正面的", "负面的", "中立的"]}],
}
# ------------------------
sa_p = {
    "english": '''''',
    "chinese": '''给你一个例子：\n给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！\n你应该判断该句子的情感是什么，情感从{}里选择。\n输出列表：["正面的"]\n如果不存在，回答：没有。\n返回结果为输出列表。\n\n现在，我给你一个句子，如"{}"，你应该判断句子的情感倾向，并以列表的形式返回结果，如果不存在，则回答：没有。'''
}

ae_p = {
    "english": '''''',
    "chinese": '''给你一个例子：\n给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！\n给定实体类型列表:{}\n你应该提取该句子里面的所有{}，这里的观点可能是对某方面的评价、介绍等。\n输出列表：["地方", "石头", "环境", "景色"]\n如果不存在，回答：没有。\n返回结果为输出列表。\n\n现在，我给你一个句子，如"{}"，你应该提取里面所有实体类型为{}的实体，并以列表的形式返回结果，如果不存在，则回答：没有。'''
}

oe_p = {
    "english": '''''',
    "chinese": '''给你一个例子：\n给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！\n给定实体类型列表:{}\n你应该提取该句子里面的所有{}，这里的观点可能是对某方面的评价、介绍等，请注意结果不要带返回某方面，只需要评价或描述，比如不需要石头、景色、环境等方面。\n输出列表：["值得去", "奇特", "优美", "宜人"]\n如果不存在，回答：没有。\n返回结果为输出列表。\n\n现在，我给你一个句子，如"{}"，你应该提取里面所有实体类型为{}的实体，并以列表的形式返回结果，如果不存在，则回答：没有。请注意，结果不需要带上方面'''
}

alsc_p = {
    "english": '''''',
    "chinese": '''给你一个例子：\n给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！\n给定一个方面，你需要判断它的情感是什么，从{}里进行选择。\n比如，给定方面"地方"，输出列表：["正面的"]\n如果不存在，回答：没有。\n返回结果为输出列表。\n\n现在，我给你一个句子，如"{}"，和一个方面"{}"，你应该判断它的情感，并以列表的形式返回结果，如果不存在，则回答：没有。'''
}

aoe_p = {
    "english": '''''',
    "chinese": '''给你一个例子：\n给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！\n给定一个方面，你需要识别它的观点或者修饰词是什么。\n比如，给定方面"地方"，输出列表：["值得去"]，请注意结果不要带上方面。\n如果不存在，回答：没有。\n返回结果为输出列表。\n\n现在，我给你一个句子，如"{}"，和一个方面"{}"，你应该输出它的观点或修饰词，并以列表的形式返回结果，如果不存在，则回答：没有。'''
}

aesc_p = {
    "english": '''''',
    "chinese": '''给你一个例子：\n给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！\n给定一个方面，你需要判断它的情感是什么，从{}里进行选择。\n比如，给定方面"地方"，输出列表：[("地方", "正面的")]\n如果不存在，回答：没有。\n返回结果为输出列表。\n\n现在，我给你一个句子，如"{}"，和一个方面"{}"，你应该判断它的情感，并以列表的形式返回结果，如果不存在，则回答：没有。'''
}

pair_p = {
    "english": '''''',
    "chinese": '''给你一个例子：\n给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！\n你需要提取里面所有的方面及其对应的观点，请注意，方面可能是主体或者具有一定意义的名词，观点是形容某个方面的词。\n输出列表：[("地方", "值得去"),("石头","奇特"),("环境", "优美"),("景色","宜人")]\n如果不存在，回答：没有。\n返回结果为输出列表。\n\n现在，我给你一个句子，如"{}"，请识别出里面所有的方面及其对应的观点，并以列表的形式返回结果，如果不存在，则回答：没有。'''
}

triplet_p = {
    "english": '''''',
    "chinese": '''给你一个例子：\n给出的句子是：值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！\n你需要提取里面所有的方面及其对应的观点和情感，情感从{}中选择，请注意，方面可能是主体或者具有一定意义的名词，观点是形容某个方面的词。\n输出列表：[("地方", "值得去","正面的"),("石头","奇特","正面的"),("环境", "优美","正面的"),("景色","宜人","正面的")]\n如果不存在，回答：没有。\n返回结果为输出列表。\n\n现在，我给你一个句子，如"{}"，请识别出里面所有的方面及其对应的观点和情感，并以列表的形式返回结果，如果不存在，则回答：没有。'''
}

df_proxy = 'http://127.0.0.1:1080'


def get_resilt(text):
    res = regex.search("\[(.*?)\]", text)
    entity = []
    if res:
        start = res.start()
        end = res.end()
        entity = eval(text[start:end + 1].strip().replace("。", ""))
    return entity


def chat(mess):
    # 根据自己服务器的vpn情况设置proxy
    openai.proxy = df_proxy
    responde = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=mess
    )

    res = responde['choices'][0]['message']['content']
    return res

def chat_sa(inda, chatbot):
    print("---SA---")
    mess = [{"role": "system", "content": "You are a helpful assistant."}, ]  # chatgpt对话历史
    typelist = inda['type']
    sent = inda['sentence']
    lang = inda['lang']
    out = []
    try:
        print('---begin---')

        s1p = sa_p[lang].format(
            df_sat[lang]["情感"],
            sent,
        )
        print(s1p)

        # 请求chatgpt
        mess.append({"role": "user", "content": s1p})
        text1 = chatbot(mess)
        out = get_resilt(text1)
        return out, mess

    except Exception as e:
        print(e)
        return ['error:' + str(e)], mess

def chat_ae(inda, chatbot):
    print("---AE---")
    mess = [{"role": "system", "content": "You are a helpful assistant."}, ]  # chatgpt对话历史
    typelist = inda['type']
    sent = inda['sentence']
    lang = inda['lang']
    out = []
    try:
        print('---begin---')

        s1p = ae_p[lang].format(
            df_aet[lang],
            df_aet[lang][0],
            sent,
            df_aet[lang][0],
        )
        print(s1p)

        # 请求chatgpt
        mess.append({"role": "user", "content": s1p})
        text1 = chatbot(mess)
        out = get_resilt(text1)
        return out, mess

    except Exception as e:
        print(e)
        return ['error:' + str(e)], mess


def chat_oe(inda, chatbot):
    print("---OE---")
    mess = [{"role": "system", "content": "You are a helpful assistant."}, ]  # chatgpt对话历史
    typelist = inda['type']
    sent = inda['sentence']
    lang = inda['lang']
    out = []
    try:
        print('---begin---')

        s1p = oe_p[lang].format(
            df_oet[lang],
            df_oet[lang][0],
            sent,
            df_oet[lang][0],
        )
        print(s1p)

        # 请求chatgpt
        mess.append({"role": "user", "content": s1p})
        text1 = chatbot(mess)
        out = get_resilt(text1)
        return out, mess

    except Exception as e:
        print(e)
        return ['error:' + str(e)], mess


def chat_alsc(inda, chatbot):
    print("---ALSC---")
    mess = [{"role": "system", "content": "You are a helpful assistant."}, ]  # chatgpt对话历史
    typelist = inda['type']
    aspect = inda['aspect']
    sent = inda['sentence']
    lang = inda['lang']
    out = []
    try:
        print('---begin---')

        s1p = alsc_p[lang].format(
            df_alsct[lang]["方面"]["情感"],
            sent,
            aspect,
        )
        print(s1p)

        # 请求chatgpt
        mess.append({"role": "user", "content": s1p})
        text1 = chatbot(mess)
        out_tmp = get_resilt(text1)
        for tmp in out_tmp:
            out.append((aspect, tmp))
        return out, mess

    except Exception as e:
        print(e)
        return ['error:' + str(e)], mess


def chat_aoe(inda, chatbot):
    print("---AOE---")
    mess = [{"role": "system", "content": "You are a helpful assistant."}, ]  # chatgpt对话历史
    typelist = inda['type']
    aspect = inda['aspect']
    sent = inda['sentence']
    lang = inda['lang']
    out = []
    try:
        print('---begin---')

        s1p = aoe_p[lang].format(
            sent,
            aspect,
        )
        print(s1p)

        # 请求chatgpt
        mess.append({"role": "user", "content": s1p})
        text1 = chatbot(mess)
        print(text1)
        out_tmp = get_resilt(text1)
        for tmp in out_tmp:
            out.append((aspect, tmp))
        return out, mess

    except Exception as e:
        print(e)
        return ['error:' + str(e)], mess


def chat_aesc(inda, chatbot):
    print("---AOE---")
    mess = [{"role": "system", "content": "You are a helpful assistant."}, ]  # chatgpt对话历史
    typelist = inda['type']
    aspect = inda['aspect']
    sent = inda['sentence']
    lang = inda['lang']
    out = []
    try:
        print('---begin---')

        s1p = aesc_p[lang].format(
            df_aesct[lang]["方面"]["情感"],
            sent,
            aspect,
        )
        print(s1p)

        # 请求chatgpt
        mess.append({"role": "user", "content": s1p})
        text1 = chatbot(mess)
        out = get_resilt(text1)
        return out, mess

    except Exception as e:
        print(e)
        return ['error:' + str(e)], mess


def chat_pair(inda, chatbot):
    print("---PAIR---")
    mess = [{"role": "system", "content": "You are a helpful assistant."}, ]  # chatgpt对话历史
    typelist = inda['type']
    sent = inda['sentence']
    lang = inda['lang']
    out = []
    try:
        print('---begin---')

        s1p = pair_p[lang].format(
            sent,
        )
        print(s1p)

        # 请求chatgpt
        mess.append({"role": "user", "content": s1p})
        text1 = chatbot(mess)
        out = get_resilt(text1)
        return out, mess

    except Exception as e:
        print(e)
        return ['error:' + str(e)], mess


def chat_triplet(inda, chatbot):
    print("---TRIPLET---")
    mess = [{"role": "system", "content": "You are a helpful assistant."}, ]  # chatgpt对话历史
    typelist = inda['type']
    sent = inda['sentence']
    lang = inda['lang']
    out = []
    try:
        print('---begin---')

        s1p = triplet_p[lang].format(
            df_triplett[lang][2]["情感"],
            sent,
        )
        print(s1p)

        # 请求chatgpt
        mess.append({"role": "user", "content": s1p})
        text1 = chatbot(mess)

        out = get_resilt(text1)
        print(out)
        return out, mess

    except Exception as e:
        print(e)
        return ['error:' + str(e)], mess


def chatsa(input_data):
    print('input data type:{}'.format(type(input_data)))
    print('input data:{}'.format(input_data))

    # 参数处理，默认参数
    task = input_data['task']
    lang = input_data['lang']
    typelist = input_data['type']
    access = input_data['access']

    ## account
    if access == "":
        print('using default access token')
        openai.api_key = df_access[0][0]
    else:
        openai.api_key = input_data['access']
    chatbot = chat
    try:
        if task == "SA":
            input_data["result"], input_data["mess"] = chat_sa(input_data, chatbot)
        elif task == "AE":
            input_data["result"], input_data["mess"] = chat_ae(input_data, chatbot)
        elif task == "OE":
            input_data["result"], input_data["mess"] = chat_oe(input_data, chatbot)
        elif task == "ALSC":
            input_data["result"], input_data["mess"] = chat_alsc(input_data, chatbot)
        elif task == "AOE":
            input_data["result"], input_data["mess"] = chat_aoe(input_data, chatbot)
        elif task == "AESC":
            input_data["result"], input_data["mess"] = chat_aesc(input_data, chatbot)
        elif task == "PAIR":
            input_data["result"], input_data["mess"] = chat_pair(input_data, chatbot)
        elif task == "TRIPLET":
            input_data["result"], input_data["mess"] = chat_triplet(input_data, chatbot)
    except Exception as e:
        print(e)

    return input_data


if __name__ == '__main__':
    sen = "味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢"
    sen = "感觉很好，服务也不错，还会一如既往的关注，支持"
    sen = "服务态度很好，环境也不错，就是点歌系统不太好用。"
    sen = "感觉不是很满意，不能对顾客有敷衍了事的行为，每次讲话老是有这么多的理由，态度和效果有待提高"
    sen = "味道很不错，很喜欢吃。服务也很好感觉很亲切，吃的很舒服，谢谢"
    sen = "值得去的地方，石头很奇特，景色优美，环境宜人，适合与朋友家人一起游玩！"
    sen = "环境不错，进去就有暖气，叫的11号技师，服务确实不错，95后妹子，技术好，挺不错的体验"
    sen = "环境非常好，古香古色的教室。老师不错，随时能沟通孩子学习及吃饭情况！"
    sen = "服务好 态度好 产品好 一句话就是好"
    sen = "这小区不错。房价也不低。"
    sen = "经济实惠、动力不错、油耗低"
    sen = "很好的浴室，干净清爽！前台热情"
    sen = "这才是正规专卖店啊，服务好，产品全面"
    sen = "散热很好、低噪音、做工扎实、键盘舒适"
    lang = "chinese"
    ind_sa = {
        "sentence": sen,
        "type": "",
        "access": "",
        "task": "SA",
        "lang": lang,
    }
    ind_ae = {
        "sentence": sen,
        "type": "",
        "access": "",
        "task": "AE",
        "lang": lang,
    }
    ind_oe = {
        "sentence": sen,
        "type": "",
        "access": "",
        "task": "OE",
        "lang": lang,
    }
    ind_alsc = {
        "sentence": sen,
        "type": "",
        "aspect": "味道",
        "access": "",
        "task": "ALSC",
        "lang": lang,
    }
    ind_aoe = {
        "sentence": sen,
        "type": "",
        "aspect": "味道",
        "access": "",
        "task": "AOE",
        "lang": lang,
    }
    ind_aesc = {
        "sentence": sen,
        "type": "",
        "aspect": "味道",
        "access": "",
        "task": "AESC",
        "lang": lang,
    }
    ind_pair = {
        "sentence": sen,
        "type": "",
        "access": "",
        "task": "PAIR",
        "lang": lang,
    }
    ind_triplet = {
        "sentence": sen,
        "type": "",
        "access": "",
        "task": "TRIPLET",
        "lang": lang,
    }
    post_data = chatsa(ind_sa)
    print(post_data)
    # post_data = chatsa(ind_ae)
    # print(post_data)
    # post_data = chatsa(ind_oe)
    # print(post_data)
    # post_data = chatsa(ind_alsc)
    # print(post_data)
    # post_data = chatsa(ind_aoe)
    # print(post_data)
    # post_data = chatsa(ind_aesc)
    # print(post_data)
    # post_data = chatsa(ind_pair)
    # print(post_data)
    # post_data = chatsa(ind_triplet)
    # print(post_data)
