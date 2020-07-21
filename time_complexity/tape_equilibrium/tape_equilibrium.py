# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    s = sum(A)
    m = float('inf')
    left_sum = 0
    for i in A[:-1]:
        left_sum += i
        m = min(abs(s - 2*left_sum), m)
    return m
