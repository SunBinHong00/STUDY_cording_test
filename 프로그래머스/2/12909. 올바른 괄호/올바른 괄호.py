def solution(s):
    n = 0
    for i in s:
        if n >= 0:
            if i == '(':
                n += 1
            else:
                n -= 1
        else:
            return False
    if n != 0:
        return False
    return True