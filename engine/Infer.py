# -*- coding: UTF-8 -*-
import re

def forwardInfer(rules, facts):
    stop = False
    factSet = set(facts)
    visit = []
    activerules = []
    while not stop :
        curactiverules = []
        print visit
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
        print r["condition"]
        if len(r["condition"]) > maxMatch:
            maxMatch = len(r["condition"])
            activerule = r

    print maxMatch
    visit.append(activerule)
    cond = set(activerule["condition"])
    for r in curactiverules:
        if r != activerule and set(r["condition"]).issubset(cond) and not r["condition"] == cond:
            if r["id"] <= 24 :
                if activerule["id"] <= 24:
                    visit.append(r)
            else:
                visit.append(r)

    return activerule

def GetResult(activerule):
    ret = set([])
    activerule = sorted(activerule, key=lambda d: d["id"])
    for r in activerule:
        if r["result"].startswith("level"):
            continue
        result = set(re.split(u"、|。", r["result"]))
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




