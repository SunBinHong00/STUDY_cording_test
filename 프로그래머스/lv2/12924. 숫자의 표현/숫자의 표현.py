def solution(n):
    result = 1
    for j in range(1,n//2+1):
        num = 0 
        for i in range(j,n):
            num += i
            if num == n:
                result += 1
                break
            elif num > n:
                break
            
    return result