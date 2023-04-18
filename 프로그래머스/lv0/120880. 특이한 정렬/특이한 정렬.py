def solution(numlist, n):
    answer = [[i,abs(i-n)] for i in numlist]
    answer = sorted(answer,key=lambda x : (x[1],-x[0]))
    answer = [i[0] for i in answer]
    return answer