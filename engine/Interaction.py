# -*- coding: UTF-8 -*-
import json

from GenerateFacts import *
from Infer import *
from Explain import *

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