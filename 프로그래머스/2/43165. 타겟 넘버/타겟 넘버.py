def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def dfs(idx,cnt):
        
        if n>idx:
            num = numbers[idx]
            
            for i in [1,-1]:
                
                dfs(idx+1,cnt+num*i)
        
        else: 
            if cnt == target:
                nonlocal answer
                answer+=1
    
    dfs(0,0)
    
    return answer