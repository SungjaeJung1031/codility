def solution(N):
    # write your code in Python 3.6
    if N <= 0:
        return 0

    for i in range(int(N**0.5), 0, -1):
        if N % i == 0:
            return 2*(i+N//i)
