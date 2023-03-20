T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 오름차순 정렬 후
    arr.sort()

    minV = 1000
    for i in range(N-2): # 소 박스를 어디까지 넣을 것인가
        for j in range(i+1, N-1):   # 중 박스를 어디까지 넣을 것인가
            if arr[i] != arr[i+1] and arr[j] != arr[j+1]: # 박스 경계에 있는 수와 같지 않아야함
                A = i + 1
                B = j - i
                C = N - 1 - j
                if A*B*C != 0 and A <= N//2 and B <= N//2 and C <= N//2: # 빈박스랑 절반 초과 박스가 없으면
                    if minV > max(A, B, C) - min(A, B, C):
                        minV =  max(A, B, C) - min(A, B, C)
    if minV == 1000:
        minV = -1

    print(f"#{tc} {minV}")