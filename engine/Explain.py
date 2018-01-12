# -*- coding: UTF-8 -*-
def GeneratorExplaintion(activerules):
    description = ""
    for r in activerules:
        if r["result"].startswith("level"):
            description = u"当前的着装指数是 " + r["result"] + "," + u"体感 " + r["description"] + "\n\n"
            break
    for r in activerules:
        if not r["result"].startswith("level"):
            description += u"因为 " + r["description"] + "\n"
            description += u"而您希望在 "
            if u"体弱" in r["condition"]:
                description += u"保暖一些 "
            for cond in r["condition"]:
                if cond != u"体弱" and cond != u"男" and cond != u"女" and not cond.startswith("level"):
                    description += cond + " "
            if u"男" in r["condition"]:
                description += u"的男士服装"
            elif u"女" in r["condition"]:
                description += u"的女士服装"
            description += u" 的条件下\n所以建议你穿 " + r["result"] + "\n"
    return description

def PrintRules(activerules):
    rulesprint = ""
    for r in activerules:
        rulesprint += "Rule " + str(r["id"]) + ":\n"
        rulesprint += "IF "
        for i in range(0,len(r["condition"])):
            if i != len(r["condition"]) - 1:
                rulesprint += r["condition"][i] + " AND "
            else:
                rulesprint += r["condition"][i] + "\n"
        rulesprint += "THEN " + r["result"] + "\n"
        rulesprint += "Because " + r["description"] + "\n"
        rulesprint += "-------------------------------------------------\n"
    return rulesprint
