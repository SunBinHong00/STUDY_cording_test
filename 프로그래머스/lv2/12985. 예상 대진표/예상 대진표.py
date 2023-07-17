def solution(n,a,b):
    for i in range(1,21):
        if 2**i == n:
            break
            
    if a > b :
        a,b = b,a
        
    
    for _ in range(i-1):
        
        x = n/2 >= a
        y = n/2 >= b
        
        if x == y:  
            i -= 1
            n /= 2
            
            if not x:
                a -= n
                b -= n

        else:
            return i
        
    return i