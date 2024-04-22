def solution(s):
    x = [set(map(int,j.split('}')[0].split(','))) for j in [i for i in s[1:-1].split('{') if i]]
    x = sorted(x,key=lambda x : len(x))

    result = []
    pre = set()
    for i in x:
        # print(i)
        current = i

        new = current - pre

        result.extend(new)

        pre = current
        
    return result