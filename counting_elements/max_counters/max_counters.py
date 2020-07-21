def solution(N, A):
    # write your code in Python 3.6
    counters = [0] * N
    max_counter = 0
    next_max_counter = 0

    for val in A:
        if 1 <= val and val <= N:
            cur_counter = counters[val -
                                   1] = max(counters[val-1] + 1, max_counter + 1)
            next_max_counter = max(cur_counter, next_max_counter)
        else:
            max_counter = next_max_counter

    return [c if c > max_counter else max_counter for c in counters]
