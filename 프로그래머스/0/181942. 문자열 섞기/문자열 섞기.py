def solution(str1, str2):
    answer = []
    str1 = [i for i in str1]
    str2 = [i for i in str2]
    print(str1)
    
    for _ in range(len(str1)):
        answer.append(str1.pop(0))
        answer.append(str2.pop(0))
        
        
    return ''.join(answer)