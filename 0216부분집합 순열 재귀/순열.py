# 장점은 코드가 간결하다
# 바꿀 수 있을 떄 까지 바꿈


def f(i, k):  # i는 n번째 자리   , #k 는 원소개수
    if i == k:
        print(p)
    else:
        for j in range(i, k):       #
            p[i], p[j] = p[j], p[i]
            # 위 코드를 통해 p[i]가 이미 결정, p[i]와 관련된 작업 가능
            f(i+1, k)
            p[i], p[j] = p[j], p[i]


p = [1, 2, 3]
N = len(p)
f(0, N)
