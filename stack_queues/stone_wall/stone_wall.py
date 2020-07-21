def solution(H):
    # write your code in Python 3.6
    res = 0
    stack = []

    for x in H:
        while (len(stack) > 0) and (stack[-1] > x):
            stack.pop()
        else:
            if (len(stack) == 0) or (stack[-1] < x):
                stack.append(x)
                res += 1

    return res
