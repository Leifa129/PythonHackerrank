# Link to challenge:
# https://www.hackerrank.com/challenges/unbounded-knapsack/problem


def unboundedKnapsack(k, arr):
    result = 0
    total = 0
    dp = []
    for value in range(k + 1):
        dp.append(0)

    for value in range(1, k + 1):
        for num in arr:
            if num <= value and dp[value - num] + num <= value:
                dp[value] = max(dp[value], dp[value - num] + num)

    return dp[k]