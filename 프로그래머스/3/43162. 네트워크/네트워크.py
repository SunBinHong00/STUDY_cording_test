def solution(n, computers):
    answer = 0
    
    history = []
    
    def dfs(stack):

        while stack:

            idx = stack.pop()
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
                    for i in range(n):
                        if i not in history:
                            dfs([i])
                            break     

    dfs([0])
    return answer
def solution(n, computers):
    visited = set()
    answer = 0

    def dfs(node):
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                # Enqueue all connected, unvisited nodes
                stack.extend([i for i, connected in enumerate(computers[current]) if connected == 1 and i not in visited])

    for i in range(n):
        if i not in visited:
            dfs(i)
            answer += 1  # Each successful DFS from a new start node indicates a new network

    return answer


    