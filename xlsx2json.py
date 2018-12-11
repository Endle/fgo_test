import pandas as pd

file = 'demo.xlsx'

df = pd.read_excel(file, sheet_name=0)

def row2json(df):
    qID      = df[0]
    qDesc    = df[1]
    choices  = []
    for col in df[2:]:
        if (pd.isna(col)):   break
        choices.append(col)
    print(choices)
    return 1

def writeJson(obj):
    print("writing part stub")


for row in range(df.shape[0]):
    obj = row2json(df.loc[row])
    writeJson(obj)

#print(xl.sheet_names)
