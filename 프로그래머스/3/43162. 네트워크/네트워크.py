def solution(n, computers):
    answer = 0
    
    history = []
    
    def dfs(stack):

        while stack:
            try:
                idx = stack.pop()
                print(idx)
                history.append(idx)

                nums = computers[idx]

                will_go = [i for i,v in enumerate(nums) if v==1 and i not in history]

                if will_go:
                    stack.extend(will_go)
                else:

                    if stack:
                        continue

                    else:
                        nonlocal answer
                        answer += 1
                        for i in range(n+1):
                            if i not in history:
                                dfs([i])
                                break     
            except:
                pass
    dfs([0])
    return answer

    