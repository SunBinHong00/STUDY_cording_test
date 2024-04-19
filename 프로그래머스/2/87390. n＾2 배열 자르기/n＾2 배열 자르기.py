import math

def s(n,index):
    
    # 층수
    floor = math.ceil(index/n)
    # 가로에서 몇번째 
    idx = index%n
    # idx==0 가로 끝인 경우 n
    idx = n if idx==0 else idx
    
    return max(floor, idx)

def solution(n, left, right):
    
    
    
    return [s(n,idx+1) for idx in range(left, right+1)]
