def solution(citations):
    result = []
    for i in range(max(citations),-1,-1):
        
        cnt = len([j for j in citations if j >= i])
        
        if i <= cnt:
            return i