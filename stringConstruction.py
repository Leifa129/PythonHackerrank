# Link to challenge:
# https://www.hackerrank.com/challenges/string-construction/problem

from collections import OrderedDict


def stringConstruction(s):
    return len(''.join(OrderedDict.fromkeys(s)))