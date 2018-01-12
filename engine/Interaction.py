# -*- coding: UTF-8 -*-
import json
import shutil

from GenerateFacts import *
from Infer import *
from Explain import *

def loadrules():
    with open("rules/rules.txt") as f:
        rulelines = f.readlines()
    return rulelines

def saverules(rulelines):
    with open("rules/rules.txt",'w') as f:
        f.writelines(rulelines)

def saverulesjson(rules):
    with open("rules/rules.default.json",'w') as f:
        json.dump(rules,f)

def loadrulesjson():
    with open("rules/rules.default.json") as f:
        rules = json.load(f)
    return rules

def GetRet(info):
    facts = GetFacts(info)
    rules = loadrulesjson()
    activerules = forwardInfer(rules, facts)
    Description = GeneratorExplaintion(activerules)
    Rules = PrintRules(activerules)
    Suggestion = GetResult(activerules)

    return Suggestion, Rules, Description

def AddRule(rule):
    # make backup
    shutil.copyfile("rules/rules.txt", "rules/backup/rules.txt")
    shutil.copyfile("rules/rules.default.json", "rules/backup/rules.default.json")

    try:
        # update rule.default.json
        rules = loadrulesjson()
        size = len(rules)
        rule["id"] = size + 1
        cond = rule["condition"].split(u"，")
        rule["condition"] = cond

        rules.append(rule)
        saverulesjson(rules)


        # update rule.txt
        condstr = "["
        for i in range(0,len(rule["condition"])):
            if i != len(rule["condition"]) - 1:
                condstr += "\"" + rule["condition"][i] + "\""+ ","
            else:
                condstr += "\"" + rule["condition"][i] + "\"" + "]"

        ruleline = str(rule["id"]) + "\t" + condstr + "\t\"" \
                   + rule["result"] + "\"\t\"" + rule["description"] + "\"\n"
        ruleline = ruleline.encode("utf-8")

        rulelines = loadrules()
        rulelines.append(ruleline)
        saverules(rulelines)

    except BaseException, e:
        print e
        shutil.copyfile("rules/backup/rules.txt", "rules/rules.txt")
        shutil.copyfile("rules/backup/rules.default.json", "rules/rules.default.json")
        return False

    return True

def DeleteRule(id):
    # make backup
    shutil.copyfile("rules/rules.txt", "rules/backup/rules.txt")
    shutil.copyfile("rules/rules.default.json", "rules/backup/rules.default.json")

    try:
        rules = loadrulesjson()
        size = len(rules)
        if id > size or id <= 0:
            return False

        # update rule.default.json
        newrules = []
        for i in range(0, size):
            if i < id - 1:
                newrules.append(rules[i])
            elif i > id - 1:
                rules[i]["id"] -= 1
                newrules.append(rules[i])

        saverulesjson(newrules)

        # update rule.txt
        rulelines = loadrules()
        newrulelines = []
        for l in rulelines:
            parts = l.split("\t")
            lid = int(parts[0])
            if l == "\n" or lid == id:
                continue
            elif lid > id:
                newl = str(lid - 1) + "\t"
                newl += '\t'.join(parts[1:])
                newrulelines.append(newl)
            else:
                newrulelines.append(l)

        saverules(newrulelines)

    except BaseException, e:
        print e
        shutil.copyfile("rules/backup/rules.txt", "rules/rules.txt")
        shutil.copyfile("rules/backup/rules.default.json", "rules/rules.default.json")
        return False

    return True


def ModifyRule(ruleinfo):
    print "modify"
    # make backup
    shutil.copyfile("rules/rules.txt", "rules/backup/rules.txt")
    shutil.copyfile("rules/rules.default.json", "rules/backup/rules.default.json")

    try:
        # update rule.default.json
        rules = loadrulesjson()
        size = len(rules)
        if ruleinfo["id"] > size or ruleinfo["id"] <= 0:
            return False

        rule = rules[ruleinfo["id"] - 1]

        if ruleinfo["condition"] != '':
            cond = ruleinfo["condition"].split(u"，")
            rule["condition"] = cond
        if ruleinfo["result"] != '':
            rule["result"] = ruleinfo["result"]
        if ruleinfo["description"] != '':
            rule["description"] = ruleinfo["description"]

        print ruleinfo
        print rule

        rules[ruleinfo["id"] - 1] = rule
        saverulesjson(rules)

        # update rule.txt
        condstr = "["
        for i in range(0, len(rule["condition"])):
            if i != len(rule["condition"]) - 1:
                condstr += "\"" + rule["condition"][i] + "\"" + ","
            else:
                condstr += "\"" + rule["condition"][i] + "\"" + "]"

        rulelines = loadrules()
        ruleline = str(rule["id"]) + "\t" + condstr + "\t\"" \
                   + rule["result"] + "\"\t\"" + rule["description"] + "\"\n"
        ruleline = ruleline.encode("utf-8")

        newrulelines = []
        for l in rulelines:
            parts = l.split("\t")
            lid = int(parts[0])
            if l == "\n" or lid == ruleinfo["id"]:
                newrulelines.append(ruleline)
            else:
                newrulelines.append(l)

        saverules(newrulelines)

    except BaseException, e:
        print e
        shutil.copyfile("rules/backup/rules.txt", "rules/rules.txt")
        shutil.copyfile("rules/backup/rules.default.json", "rules/rules.default.json")
        return False

    return True

def Reset():
    shutil.copyfile("rules/backup/rules.txt", "rules/rules.txt")
    shutil.copyfile("rules/backup/rules.default.json", "rules/rules.default.json")
    return True




