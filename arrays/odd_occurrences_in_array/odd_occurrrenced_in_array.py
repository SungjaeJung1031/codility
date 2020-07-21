# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    count = {}
    res = 0

    for elem in A:
        if elem not in count:
            count[elem] = 1
        else:
            count[elem] += 1

    for key, val in count.items():
        if val % 2 != 0:
            res = key
            break

    return res
