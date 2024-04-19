import collections

def solution(k, tangerine):
    answer = 0
    
    # 크기 별 개수 체크
    tangerine = dict(collections.Counter(tangerine))
    # 개수만 리스트에 넣기
    tangerine = [i[1] for i in tangerine.items()]
    # 큰 순으로 정렬
    tangerine = sorted(tangerine,reverse=True)
    answer = 0

    for i in tangerine:
        if k>0:
            k -= i
            answer += 1

    return answer