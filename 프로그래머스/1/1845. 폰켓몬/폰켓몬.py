def solution(nums):
    num_poketmon = len(nums)/2
    
    num_kind_of_poketmon = len(set(nums))
    
    return min(num_poketmon, num_kind_of_poketmon)