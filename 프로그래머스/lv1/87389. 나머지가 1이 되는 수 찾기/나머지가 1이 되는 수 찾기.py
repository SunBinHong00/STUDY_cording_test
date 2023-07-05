def solution(n):
    nums = [i for i in range(1,n) if not n%i==0]
    result = []
    for i in nums:
        if n%i==1:
            result.append(i)
    return min(result)