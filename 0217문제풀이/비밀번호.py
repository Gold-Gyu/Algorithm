import sys
sys.stdin = open('s_input (2).txt', 'r')


def delete(M):

    for i in M:



for tc in range(1, 4):
    N, M = map(str, input().split())

    delete(M)
    stack = []
    postfix = ""

    for i in M:
        stack.append(i)

        if len(stack) >= 2 and stack[-1] == i:
            stack.pop()
            stack.pop()

    print(M)
