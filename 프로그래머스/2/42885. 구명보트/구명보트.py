def solution(people, limit):
    people = sorted(people)
    a = 0
    b = len(people)-1
    
    result = 0    
    
    while  a <= b:
        if people[a] + people[b] <= limit:
            a += 1
        b -= 1
        result += 1
        
                
    return result


# 50 70 80