from collections import Counter


def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return 0

    if len(A) == 0:
        return -1

    count = Counter(A).most_common()

    if count[0][1] <= len(A)//2 and len(A) % 2 == 0:
        return -1
    else:
        for idx, val in enumerate(A):
            if val == count[0][0]:
                return idx
