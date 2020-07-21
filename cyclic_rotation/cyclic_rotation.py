def solution(A, K):
    # write your code in Python 3.6
    if not A or K == 0:
        return A
    else:
        for _ in range(K):
            tail = A.pop(-1)
            A.insert(0, tail)

    return A
