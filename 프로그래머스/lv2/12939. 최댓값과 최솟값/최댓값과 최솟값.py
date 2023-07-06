def solution(s):
    a, *_, b = sorted([int(i) for i in s.split()])
    return f'{min(a,b)} {max(a,b)}'

