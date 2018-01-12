# -*- coding: UTF-8 -*-
def GetFacts(info):
    facts = []
    if info['weather'] == "option1":
        facts.append(u"天气：晴朗")
    elif info['weather'] == "option2":
        facts.append(u"天气：阴天")
    else:
        facts.append(u"天气：下雨")

    temp = float(info['temperature'])
    if temp >= 35:
        facts.append(u"气温：炎热")
    elif temp >= 28:
        facts.append(u"气温：热")
    elif temp >= 25:
        facts.append(u"气温：热舒适")
    elif temp >= 23:
        facts.append(u"气温：较舒适")
    elif temp >= 18:
        facts.append(u"气温：舒适")
    elif temp >= 15:
        facts.append(u"气温：温凉")
    elif temp >= 8:
        facts.append(u"气温：凉")
    elif temp >= 5:
        facts.append(u"气温：微冷")
    elif temp >= 0:
        facts.append(u"气温：较冷")
    elif temp >= -5:
        facts.append(u"气温：冷")
    elif temp >= -10:
        facts.append(u"气温：寒冷")
    else:
        facts.append(u"气温：极冷")

    if info['humidity'] == "option1":
        facts.append(u"湿度：干燥")
    elif info['humidity'] == "option2":
        facts.append(u"湿度：正常")
    else:
        facts.append(u"湿度：潮湿")

    if info['wind'] == "option1":
        facts.append(u"风力：小")
    elif info['wind'] == "option2":
        facts.append(u"风力：正常")
    else:
        facts.append(u"风力：大")

    if info['gender'] == "option1":
        facts.append(u"男")
    elif info['gender'] == "option2":
        facts.append(u"女")

    if info['cold'] == "option2":
        facts.append(u"体弱")

    if info['style'] == "option1":
        facts.append(u"正式")
    elif info['style'] == "option2":
        facts.append(u"休闲")


    return facts
