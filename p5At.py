def setVariable(rest, varDict) :
    key,value = [x.replace('@','') for x in rest.split('=')]
    value = value.replace('"','')
    value=value.replace("\n",'')
    varDict[key]=value
    return varDict


def setFormat(rest, forDict) :
    values=rest.split(" ")
    values=[s.strip('\n') for s in values]
    values=[x for x in values if x]
    for val in values:
        key,value =  val.split('=')
        forDict[key]=value 
    return forDict
