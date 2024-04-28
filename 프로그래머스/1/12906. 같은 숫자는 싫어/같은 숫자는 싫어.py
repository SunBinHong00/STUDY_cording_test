def solution(arr):
    stack = []


    for a in arr:
        if stack == []:
            stack.append(a)

        if stack[-1]!=a:
            stack.append(a)

    return stack