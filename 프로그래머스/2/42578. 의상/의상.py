from collections import Counter
import math
import itertools

def solution(clothes):
    clothes = [i[1] for i in clothes]

    cnt_clothes = Counter(clothes)

    result = 1

    for i in cnt_clothes.values():
        result *= i+1

    return result -1