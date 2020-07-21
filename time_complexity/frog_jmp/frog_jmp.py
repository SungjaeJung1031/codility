# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    diviend = Y - X
    quatient = diviend//D
    remainder = diviend % D
    count = quatient

    if remainder > 0:
        count += 1

    return count
