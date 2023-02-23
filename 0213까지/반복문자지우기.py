import sys
sys.stdin = open('sample_input (9).txt', 'r')
from pprint import pprint

T = int(input())

for tc in range(1, T + 1):
    text = input()

    # 스택 초기화
    size = 1000
    top = -1 # 원소가 없다.
    stack = [0] * size

    # 제일 처음 글자는 비교할 앞 글자가 없으니까 스택에 넣기
    top += 1
    stack[top] = text[0]


    # 현재 스택의 꼭대기(top)을 확인해서
    # 현재 글자와 다르면 push
    # 같으면 pop

    # top 은 내가 꺼내올 원소를 나타내는 것임
    for i in range(1, len(text)): # 이미 처음 글자는 비교할 글자가 없어서 미리 넣엇기 때문에 1부터 range 시작
        if top != -1 and stack[top] == text[i]: # top != -1을 하는 이유는 꺼내올 원소가 없음을 확인하기 위해
            top -= 1 # pop과 동일한 효과, 실제 stack에서 원소를 빼는 것은 아니지만 내가 꺼내올 원소의 인덱스를 나타낸다.
        else:
            top += 1
            stack[top] = text[i]
    print(f"#{tc} {top + 1}") # top에 +1을 해야 글자의 갯수를 알 수 있다.
