import sys
sys.stdin = open('sample_input (2).txt', 'r')
from pprint import pprint

T = int(input())

field = [[""] * 15 for _ in range(5)]

for tc in range(1, T+1):
    lst = [list(input()) for _ in range(5)]
    pprint(lst)
    maxV = 0
    for i in range(5):
        if maxV < len(lst[i]):
            maxV = len(lst[i])

    print(maxV)

    for i in range(maxV):
        for j in range(5):
            cnt = lst[j][i]

    for x in field:
        print(x, end = "")
