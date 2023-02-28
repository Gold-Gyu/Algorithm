import sys
sys.stdin= open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    n, hex_num = input().split()

    # int(hex_num, 16)    # 16진수로 바꿔줌
    n = int(n)
    answer = ""
    for i in range(n):
        num = int(hex_num[i], 16)  # 10진수로 바꾸고
        # 2진수의 3번, 2번, 1번, 0 번째 비트를 검사해서
        for j in range(3, -1, -1):
            if num & (2**j) > 0:    # 1을 포함하면 1
                answer += "1"
            else:               # 아니면 0
                answer += "0"
    print(f"#{tc} {answer}")
        # num & (2**j): num의 j번째 비트에 1이 있는지 검사하는 방법
