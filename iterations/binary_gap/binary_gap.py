def solution(N):
    # write your code in Python 3.6
    list_binary_seq = bin(N)[2:].strip('0').split('1')
    return max([len(binary_seq) for binary_seq in list_binary_seq])
