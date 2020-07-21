def solution(A):
    # write your code in Python 3.6
    zero = 0
    res = 0
    for x in A:
        if x == 0:
            zero += 1
        if x == 1:
            res += zero

        if 1000000000 < res:
            res = -1

    return res
