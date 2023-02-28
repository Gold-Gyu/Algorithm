import sys
sys.stdin = open("sample_input(1).txt", "r")

T = int(input())

for tc in range(1, T+1):
    n = float(input()) # 실수 입력받기

    # 실수를 이진수로 바꾼 결과
    b = ""

    # 현재 내가 계싼하고 있는 자릿수
    cnt = 0


    # 반복문을 돌리면서 이진수로 바꾸기
    while cnt < 13 and n != 0:
    # 원래수*2를 한 결과가 1 이상 => 이진수에 1 추가
        n *= 2
        cnt += 1
        if n >= 1:
    # 1을 빼주고(정수부분) 다음 계산을 이어나간다.
            n -= 1
            b += "1"
    # 원래수 * 2 를 한 결과가 1 미만 => 이진수에 0 추가
        else:
            b += "0"
    print(f"#{tc}", end = " ")
    # 자릿수 13 이상이면 overflow
    if cnt < 13:
        print(b)
    else:
        print("overflow")
    # 결과가 0이면 반복 중단