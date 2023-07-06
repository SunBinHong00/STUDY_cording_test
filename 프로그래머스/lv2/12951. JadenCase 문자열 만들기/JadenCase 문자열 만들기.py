def solution(s):
    s = [i.lower() for i in s.split(' ')]
    result = []
    for i in s:
        if i != '' and i[0].isalpha():
            result.append(i[0].upper()+i[1:])
        else:
            result.append(i)
    return ' '.join(result)