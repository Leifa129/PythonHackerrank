# Link to challenge
# https://www.hackerrank.com/challenges/game-of-thrones/problem

import string


# Count each letter and make sure that at most one count is odd
def gameOfThrones(s):
    countOfOdd = 0
    for char in string.ascii_lowercase:
        if s.count(char) % 2 != 0:
            countOfOdd += 1
            if countOfOdd > 1:
                return "NO"

    return "YES"