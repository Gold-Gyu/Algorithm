T = int(input())

for tc in range(1, T + 1):

    n = int(input())

    for i in range(int(n ** (1 / 3) - 1), int(n ** (1 / 3) + 2)):
        if i * i * i == n:
            print(f"#{tc} {i}")
            break
    else:
        print(f"#{tc} -1")

