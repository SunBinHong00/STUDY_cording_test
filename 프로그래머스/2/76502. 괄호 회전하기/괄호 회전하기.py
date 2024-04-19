import copy
from collections import deque

def solution(s):
    s = deque(s)
    answer = []

    for _ in range(len(s)):
        s.rotate(-1)
        answer.append(s.copy())    

    result = 0

    m = {')':'(',
         '}':'{',
         ']':'['}

    for i in answer:
        stack = []
        valid = True


        for tmp in i:
            if tmp in ['(','{','[']:
                stack.append(tmp)
            elif stack and stack[-1] == m[tmp]:
                stack.pop()
            else:
                valid = False
                break

        if valid and not stack:
            result += 1
            
    return result