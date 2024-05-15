from collections import defaultdict

def solution(tickets):
    d = defaultdict(list)

    for i in tickets:
        d[i[0]].append(i[1])

    for i in d:
        d[i].sort()
    
    def dfs(node, path):
        if len(path) == len(tickets) + 1 :
            return path

        for i, city in enumerate(d[node]):
            d[node].pop(i)

            newPath = path[:]
            newPath.append(city)

            result = dfs(city,newPath)
            if result : return result

            d[node].insert(i,city)


    answer = dfs('ICN',['ICN'])
    
    return answer