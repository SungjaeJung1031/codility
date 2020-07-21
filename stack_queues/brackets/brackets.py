def isValidPair(open_bracket, close_bracket):
    if open_bracket == '(' and close_bracket == ')':
        return True
    if open_bracket == '[' and close_bracket == ']':
        return True
    if open_bracket == '{' and close_bracket == '}':
        return True
    return False


def solution(S):
    # write your code in Python 3.6
    open_bracket_stack = []
    res = 1

    for c in S:
        if c == '[' or c == '{' or c == '(':
            open_bracket_stack.append(c)
        else:
            if len(open_bracket_stack) == 0:
                res = 0
                break
            open_bracket = open_bracket_stack.pop()
            if not isValidPair(open_bracket, c):
                res = 0
                break

    if len(open_bracket_stack) != 0:
        res = 0

    return res
