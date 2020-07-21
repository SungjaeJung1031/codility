def solution(A):
    # write your code in Python 3.6
    if len(A) < 2:
        return 0

    max_profit = 0
    min_price = A[0]
    for price in A[1:]:
        price_diff = price - min_price
        if price_diff > 0:
            if max_profit < price_diff:
                max_profit = price_diff
        else:
            min_price = price

    return max_profit
