def solution(n):
    k=1
    while n!=1:
        if n%2==1:
            n = (n-1)/2
            k+=1
        else:
            n/=2
        

    return k