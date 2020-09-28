# Link to challenge
# https://www.hackerrank.com/challenges/coin-change/problem


def getWays(n, coins):
    dp = [1] + [0 for x in range(n)]
    for coin in coins:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]

    return dp[n]
