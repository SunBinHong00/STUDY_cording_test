def solution(elements):
    result = set()

    for i in range(1,len(elements)+1):

        for j in range(len(elements)):
            if j+i > len(elements):
                result.add(sum(elements[j:len(elements)]+elements[0:j+i-len(elements)]))
            else:
                result.add(sum(elements[j:j+i]))
                
    return len(result)