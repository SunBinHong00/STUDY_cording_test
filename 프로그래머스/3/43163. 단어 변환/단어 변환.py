import re

def solution(begin, target, words):
    answer = []
    history = set()
    
    def dfs(w, h):

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
                    print(m,h)
                    dfs(m,h)
            else:
                answer.append(0)    

    dfs(begin,history)
    
    answer = [i for i in answer if i!=0]
    print(answer)
    if answer:
        return min([len(i) for i in answer])
    else:
        return 0
