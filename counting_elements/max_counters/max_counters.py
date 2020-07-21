def solution(N, A):
    # write your code in Python 3.6
    list_res = [0] * N
    max_val = -1

    for val in A:
        if 1 <= val and val <= N:
            list_res[val-1] += 1
            max_val = max(list_res)
        elif val == N+1:
            list_res = [max_val if x <= max_val else x for x in list_res]

    return list_res


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
