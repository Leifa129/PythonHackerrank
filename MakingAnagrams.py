# Link to challenge:
# https://www.hackerrank.com/challenges/making-anagrams/problem

import string


def makingAnagrams(s1, s2):
    count = 0
    for char in string.ascii_lowercase:
        count += abs(s1.count(char) - s2.count(char))

    return count
