def solution(n):
    a=1
    b=1
    num=2

    while n!=num:
        num += 1
        a = a + b
        a, b = b, a
    return b%1234567