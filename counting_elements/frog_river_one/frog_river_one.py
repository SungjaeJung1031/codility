def solution(X, A):
    # write your code in Python 3.6
    check_A = dict(zip(range(1, X+1), [1] * X))
    cnt = 0
    res = 0

    if X <= 0 or len(A) <= 0:
        res = -1
    else:
        for idx, key in enumerate(A):
            if key in check_A and check_A[key] == 1:
                cnt += 1
                check_A[key] = 0

            if cnt == X:
                res = idx
                break

    return res
