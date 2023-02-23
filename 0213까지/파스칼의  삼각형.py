import sys
sys.stdin = open('input (18).txt', 'r')
from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = []
    arr.append([1])
    arr.append([1, 1])

    for i in range(1, N+1):
        arr = [1] * i
        pprint(arr)

    for j in range()
