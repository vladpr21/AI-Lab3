from random import randint

def generateNewValue(lim1,lim2):
    return randint(lim1,lim2)

def reprez(ret):
    repres = [generateNewValue(0, ret['noNodes']-1) for _ in range(ret['noNodes'])]
    for i in range(0, len(repres),3):
        for j in range(0, len(repres)):
            if ret['mat'].item(i, j) == 1:
                repres[j] = repres[i]
    return repres