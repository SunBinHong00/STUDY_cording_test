import math
def solution(progresses, speeds):
    schedule = [math.ceil((100-progress)/speed) for progress, speed in zip(progresses,speeds)]

    tmp = []

    result = []

    for i in (schedule):
        print(i)
        if not tmp:
            tmp.append(i)

        elif tmp[0] >= i:
            tmp.append(i)
        else:
            result.append(len(tmp))
            tmp=[]
            tmp.append(i)

    result.append(len(tmp))
    return result