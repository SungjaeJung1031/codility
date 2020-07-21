def solution(A, B):
    # write your code in Python 3.6
    downstream_sz = []
    downstream_cnt = 0
    alive_cnt = 0

    for (sz, dir) in zip(A, B):
        if dir == 1:    # downstream
            downstream_sz.append(sz)
            downstream_cnt += 1
        elif dir == 0:  # upstream
            while downstream_cnt != 0:
                if downstream_sz[-1] < sz:
                    downstream_sz.pop()
                    downstream_cnt -= 1
                else:
                    break
            else:
                alive_cnt += 1

    alive_cnt += len(downstream_sz)

    return alive_cnt
