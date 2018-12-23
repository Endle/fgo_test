# Base 指第几道题 1.branch 1+1 的 Base 都是1
# 假定第一行的题目是问卷的起点
#
import pandas as pd
import json
import re
import sys

inFile = 'demo.xlsx'
outputFile = 'web/result.json'

if (len(sys.argv) > 1):
    inFile = sys.argv[1]

print('Processing: ' + inFile)

df = pd.read_excel(inFile, sheet_name=0)

QUESTION_TYPES = ('choice', 'branch', 'fin')
DIMENSION      = 3

def decideType(qID):
    if (qID.find('fin') != -1):
        return ('fin',0)
    if (qID.find('branch') != -1):
        return ('branch',1)
    limit = 1
    if (qID.find('multi') != -1):
        x = re.search('<(\d+)>', qID)
        limit = int(x.group(1))
    return ('choice', limit)

def resolveChoice(s, qType):
    try:
        (desc, affects_unpack) = s.split('@')
    except ValueError:
        desc = s
        affects_unpack = ''
    affects_unpack = affects_unpack.replace(' ', '')

    data = {
        'description': desc,
    }

    if (qType == 'branch'):
        x = re.search('\{.+\}', affects_unpack)
        jumpto = x.group(0)
        affects_unpack = affects_unpack.replace(jumpto, '')
        jumpto =re.sub(r'[{}]', '', jumpto)
        data['jumpto'] = jumpto

    affection = []
    for i in range(DIMENSION): affection.append(0) #UGLY!

    for i, val in enumerate( affects_unpack.split('$') ):
        try:
            val = int(val)
        except ValueError:
            val = 0
        affection[i] = int(val)
        #print(val)

    data['affection'] = affection
    #data['affection'] = affects_unpack
    return data

def row2json(df):
    qID      = str(df[0])
    qDesc    = str(df[1])
    qBase    = qID.split('.')[0].split('+')[0]

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
        'Dimension':DIMENSION,
    }
    print(data)
    print('===============')
    return data

questions = []
for row in range(df.shape[0]):
    obj = row2json(df.loc[row])
    questions.append(obj)

with open(outputFile, 'w') as outfh:
    json.dump(questions, outfh, ensure_ascii=False)

