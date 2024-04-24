def solution(s):
    s = sorted(list(map(int,s.split())))
    return str(min(s)) + " " + str(max(s))

