# 1. in으로
# 2. 한칸씩 돌려가면서


T = int(input())

for tc in range(1, T+1):
    str_ = input()
    str2_ = input()

    cnt = 0
    if str_ in str2_:
        cnt = 1
    else:
        cnt = 0

    print(f"#{tc} {cnt}")

