def gcd(N, M):
    if M == 0:
        return N
    return gcd(M, N % M)


def solution(N, M):
    # write your code in Python 3.6
    return int(N / gcd(N, M))
