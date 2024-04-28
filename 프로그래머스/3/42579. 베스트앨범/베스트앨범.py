from collections import defaultdict
    
def solution(genres, plays):
    rank_dict = defaultdict(int)

    for genre, play in zip(genres,plays):
        rank_dict[genre] += play

    ranks = sorted([(i,v) for i,v in rank_dict.items()],key=lambda x : x[1],reverse=True)
    ranks = [i[0] for i in ranks]

    genre_dict = defaultdict(list)

    n = 0
    for genre, play in zip(genres,plays):
        genre_dict[genre].append((n,play))
        n += 1

    result = []

    for rank in ranks:
        tmp = [i[0] for i in sorted(genre_dict[rank],key=lambda x:x[1],reverse=True)][:2]
        result.extend(tmp)
    return result