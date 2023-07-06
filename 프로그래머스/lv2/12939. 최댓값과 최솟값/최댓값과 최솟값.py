def solution(s):
    a, *_, b = sorted(list(map(int,s.split())))
    return f'{min(a,b)} {max(a,b)}'

