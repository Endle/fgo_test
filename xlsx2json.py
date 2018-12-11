import pandas as pd
import json

file = 'demo.xlsx'

df = pd.read_excel(file, sheet_name=0)

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

def row2json(df):
    qID      = df[0]
    qDesc    = df[1]
    (qType,qLimit)    = decideType(qID)
    assert(qType in QUESTION_TYPES)
    choices  = []
    for col in df[2:]:
        if (pd.isna(col)):   break
        choices.append(col)
    data = {
        'ID':qID,
        'Desc':qDesc,
        'Type':qType,
        'Answers':qLimit,
    }
    json_data = json.dumps(data, ensure_ascii=False)
    print(json_data)
    return 1

def writeJson(obj):
    print("writing part stub")


for row in range(df.shape[0]):
    obj = row2json(df.loc[row])
    writeJson(obj)

#print(xl.sheet_names)
