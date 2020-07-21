# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    len_A = len(A)

    exp_total = int((len_A+1) * (1 + (len_A + 1)) / 2)

    return exp_total - sum(A)
