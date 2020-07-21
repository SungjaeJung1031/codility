def solution(S):
    # write your code in Python 3.6
    cnt_open_bracket = 0
    res = 1

    for c in S:
        if c == "(":
            cnt_open_bracket += 1
        else:
            if cnt_open_bracket == 0:
                res = 0
                break

            cnt_open_bracket -= 1

    if cnt_open_bracket != 0:
        res = 0

    return res
