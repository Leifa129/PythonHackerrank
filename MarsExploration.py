# Link to challenge
# https://www.hackerrank.com/challenges/mars-exploration/problem


def marsExploration(s):
    factor = int(len(s) / 3)
    sos = "SOS" * factor
    count = 0
    for i in range(len(s)):
        if s[i] != sos[i]:
            count += 1

    return count