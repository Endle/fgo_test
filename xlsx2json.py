import pandas as pd
import json

inFile = 'demo.xlsx'
outputFile = 'result.json'

df = pd.read_excel(inFile, sheet_name=0)

QUESTION_TYPES = ('choice', 'branch', 'fin')

def decideType(qID):
    if (qID.find('fin') != -1):
        return ('fin',0)
    if (qID.find('branch') != -1):
        return ('branch',1)
    limit = 1
    if (qID.find('multi') != -1):
        import re
        x = re.search('<(\d+)>', qID)
        limit = int(x.group(1))
    return ('choice', limit)

def resolveChoice(s, qType):
    data = {
        'description': s,
    }
    return data

def row2json(df):
    qID      = df[0]
    qDesc    = df[1]
    qBase    = qID.split('.')[0]
    (qType,qLimit)    = decideType(qID)
    assert(qType in QUESTION_TYPES)
    choices  = []
    for col in df[2:]:
        if (pd.isna(col)):   break
        choices.append(  resolveChoice(col, qType) )
    data = {
        'Base':qBase,
        'ID':qID,
        'Desc':qDesc,
        'Type':qType,
        'Limit':qLimit,
        'Choices':choices,
    }
    print(data)
    return data

questions = []
for row in range(df.shape[0]):
    obj = row2json(df.loc[row])
    questions.append(obj)

with open(outputFile, 'w') as outfh:
    json.dump(questions, outfh, ensure_ascii=False)

