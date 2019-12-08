import random
def getA(answernum):
    if answernum == 1:
        return 'it is certain'
    elif answernum == 2:
        return 'good'
    elif answernum == 3:
        return 'awesome'
r = random.randint(1,3)
fortune= getA(r)
print (fortune)