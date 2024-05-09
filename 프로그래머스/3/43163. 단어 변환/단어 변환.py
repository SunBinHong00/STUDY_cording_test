import re

def solution(begin, target, words):
    answer = []
    history = set()
    
    def bfs(w, h):

        h.add(w)
        
        for i in range(len(w)):
            tmp = list(w)
            tmp[i] = '.'
            tmp = ''.join(tmp)

            p = re.compile(tmp)
            matched = [p.match(word).group() for word in words if p.match(word)]
            matched = [i for i in matched if i not in h]

            
            if target in matched:
                answer.append(h)
            
            elif matched:
                for m in matched:
                    bfs(m,h)
            else:
                answer.append(0)    

    bfs(begin,history)
    
    answer = [i for i in answer if i!=0]

    if answer:
        return min([len(i) for i in answer])
    else:
        return 0
from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque([(begin, 0)])  # (current word, transformation steps)
    visited = set([begin])

    while queue:
        current_word, steps = queue.popleft()

        if current_word == target:
            return steps

        for word in words:
            if word not in visited and sum(1 for a, b in zip(word, current_word) if a != b) == 1:
                visited.add(word)
                queue.append((word, steps + 1))

    return 0