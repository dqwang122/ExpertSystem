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
        if r != activerule and set(r["condition"]).issubset(cond):
            visit.append(r)

    return activerule

def GetResult(activerule):
    ret = set([])
    for r in activerule:
        if r["result"].startswith("level"):
            continue
        result = set(r["result"].split(u"、"))
        if(len(result) > 1 and len(ret) > 0):
            ret &= result
        else:
            ret |= result

    print ret
    suggestion = ""
    for r in ret:
        suggestion += r + "\n"

    return suggestion




