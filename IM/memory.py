T = int(input())

for tc in range(1, T + 1):
    target = list(input())
    n = len(target)
    bit = ["0"] * n

    # 고친 횟수
    cnt = 0

    # 앞에서부터 차례대로 비교해가면서 원래 문자열과 다르면 뒤까지 그냥 다 고친다.
    # 뒤가 다르면 그때가서 그냥 또 고치면 된다.
    for i in range(n):
        # 현재 i 번쨰 비트가 다르면 bit의 i번째 비트를 target의 i번쨰 비트로 바꾼다
        # 그 뒤도 다 바꿔준다.

        if target[i] != bit[i]:
            cnt += 1
            for j in range(i, n):
                bit[j] = target[i]

        if target == bit:
            break

    print(f"#{tc} {cnt}")

"""
T = int(input())
 
for tc in range(1, T + 1):
    target = list(input())
    n = len(target)
    bit = ["0"] * n
 
    # 고친 횟수
    cnt = 0
 
    # 앞에서부터 차례대로 비교해가면서 원래 문자열과 다르면 뒤에꺼까지 그냥 다고친다.
    # 뒤가 다르면 그때가서 그냥 또 고치면 된다. ==> 그러다보면 고쳐지게 되있다.
    for i in range(n):
        # 현재 i번째 비트가 다르면 bit의 i번째 비트를 target의 i번째 비트로 바꾼다.
        # 그뒤도 다 바꿔준다.
        if target[i] != bit[i]:
            cnt += 1
            for j in range(i, n):
                bit[j] = target[i]
 
        if target == bit:
            break
 
    print(f"#{tc} {cnt}")


"""

