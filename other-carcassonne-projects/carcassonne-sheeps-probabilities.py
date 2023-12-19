import random

def coger(quedan, points, precision):
    """
    lobo = -points
    """
    result=0
    for i in range(precision):
        result+=random.randint(0,len(quedan))
    return result/precision, result/precision>points

print(coger([1,2,3,4,3,2,3,-5,-5,2],5,100000))
