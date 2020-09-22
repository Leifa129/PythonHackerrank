# Link to challenge
# https://www.hackerrank.com/challenges/funny-string/problem


def funnyString(s):
    reverse = s[::-1]
    firstValue = 0
    secondValue = 0

    for i in range(len(s) - 1):
        firstValue += abs(ord(s[i]) - ord(s[i + 1]))
        secondValue += abs(ord(reverse[i]) - ord(reverse[i + 1]))
        if firstValue != secondValue:
            return "Not Funny"

    return "Funny"
