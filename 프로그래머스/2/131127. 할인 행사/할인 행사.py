import collections

def solution(want, number, discount):

    chunk = 10

    list_range = len(discount)-chunk+1

    want_list = {i:v for i,v in zip(want,number)}

    answer = 0

    for i in range(list_range):
        discount_list = discount[i:i+chunk]

        if want_list == dict(collections.Counter(discount_list)):
            answer += 1

    return answer