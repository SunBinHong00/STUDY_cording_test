def solution(name, yearning, photo):
    dic = {i:v for i,v in zip(name,yearning)}
    return [sum([dic[i] for i in j if i in dic.keys()]) for j in photo]