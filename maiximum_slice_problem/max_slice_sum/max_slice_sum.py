def solution(A):
    # write your code in Python 3.6
    max_sum_slice = A[0]
    tmp_sum_slice = 0

    for x in A:
        tmp_sum_slice += x
        if tmp_sum_slice > max_sum_slice:
            max_sum_slice = tmp_sum_slice

        if tmp_sum_slice < 0:
            tmp_sum_slice = 0

    return max_sum_slice
