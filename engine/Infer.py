# -*- coding: UTF-8 -*-
def forwardInfer(rules, facts):
    stop = False
    factSet = set(facts)
    visit = []
    activerules = []
    while not stop :
        curactiverules = []
        for r in rules:
            if r in visit:
                continue
            cond = set(r["condition"])
            if(cond.issubset(factSet)):
                curactiverules.append(r)
        if len(curactiverules) > 0:
            activerule = DealConflict(curactiverules, visit)
            activerules.append(activerule)
            factSet.add(activerule["result"])
            stop = False
        else:
            stop = True

    return activerules

def DealConflict(curactiverules, visit):
    maxMatch = 0
    activerule = curactiverules[0]
    for r in curactiverules:
        if len(r["condition"]) > maxMatch:
            maxMatch = len(["condition"])
            activerule = r

    visit.append(activerule)
    cond = set(activerule["condition"])
    for r in curactiverules:
        if r != activerule and set(r["condition"]).issubset(cond) and not r["condition"] == cond:
            if r["id"] <= 24 :
                if activerule["id"] <= 24:
                    visit.append(r)

    return activerule

def GetResult(activerule):
    ret = set([])
    activerule = sorted(activerule, key=lambda d: d["id"])
    for r in activerule:
        print r["id"]
        if r["result"].startswith("level"):
            continue
        result = set(r["result"].split(u"、"))
        print r["result"]
        if(len(ret) == 0):
            ret |= result
        elif(len(result) > 1):
            ret &= result
        else:
            ret |= result

    suggestion = ""
    for r in ret:
        suggestion += r + "\n"

    return suggestion




