from collections import Counter

def solution(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)
    
    answer = participant - completion
    return list(answer)[0]