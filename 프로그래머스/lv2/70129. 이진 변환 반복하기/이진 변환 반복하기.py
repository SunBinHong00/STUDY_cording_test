def solution(a):
    result = [0, 0]
    while a != '1':
        n = a.count('1')
        result[0] += 1
        result[1] += len(a) - n
        a = bin(n)[2:]
    return result