
from p5At import setVariable,setFormat
varDict={}
forDict={'JUST': 'LEFT', 'BULLET': 'o', 'RM': '80', 'LM': '5', 'FLOW': 'YES'}
for line in open("p5Input.txt"):
    [start,variable,rest] = line.split(' ',2)
    if variable== 'VAR' :
        varDict=setVariable(rest, varDict)
    elif variable== 'FORMAT' :
        forDict=setFormat(rest, forDict)
    elif variable== 'PRINT' and rest=='VARS\n' :
        print(varDict)
    elif variable== 'PRINT' and rest=='FORMAT\n' :
        print(forDict)
    else:
        break

