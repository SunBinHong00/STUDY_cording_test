def solution(sides):
    sides = sorted(sides)
    return 1 if sum(sides[:2]) > sides[-1] else 2