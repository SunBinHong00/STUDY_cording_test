def solution(a, b):
    for i in range(min(a,b),0,-1):
        if (a%i==0) & (b%i==0):
            break
    b =  b//i

    for i in [2,5]:
        while not b%i:
            b//=i
    return 1 if b==1 else 2