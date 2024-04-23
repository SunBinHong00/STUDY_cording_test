from itertools import permutations
def solution(k, dungeons):
    max_count = 0 # 최대 던전 수
    permut = list(permutations(dungeons, len(dungeons))) # 던전 탐험 순서의 순열
    
    for ds in permut:
        hp = k    # 체력
        count = 0 # 던전 수
        
        for minimum, consume in ds:
            # 체력이 최소 필요 피로도보다 작으면 break
            if hp < minimum:
                break
            # 아니면 던전 수 1 증가, 소모 피로도 감소
            else:
                count += 1    
                hp -= consume            
            
        # 최대 던전 수보다 크면 갱신
        if max_count < count:
            max_count = count
    
    return max_count