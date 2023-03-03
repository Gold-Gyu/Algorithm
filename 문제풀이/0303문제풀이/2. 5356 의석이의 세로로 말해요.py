import sys
sys.stdin = open("sample_input (4).txt", "r")

T = int(input())

for tc in range(1, T+1):
    arr = [input() for _ in range(5)]
    ans = ""
    for i in range(15):
        for j in range(5):
            if i < len(arr[j]):# i행의 길이
                ans += arr[j][i]

    print(f"#{tc} {ans}")