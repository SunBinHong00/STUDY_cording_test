import math

def solution(n):
    answer = 0
    r = 0

    while n >= r :
        answer += math.comb(n,r)

        n-=1
        r+=1
        
    return answer%1234567
    