from pprint import pprint
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, input().split())
print(n, m)
field = [list(map(int, input().split())) for _ in range(n)]

pprint(field)
for i in range(m):
    d, s = map(int, input().split())
    # n-2, 0을 d 방향으로 s 만큼 이동
    r = n-2 + (dr[d] * s)
    c = 0 + (dc[d] * s)
    if r > 0 and c > n:
        r = n-r
        c = c-n
    elif r > 0 and c > n:
        r = n-r
        c = c-n


    print(field[n-2 + (dr[d] * s)][0 + (dc[d] * s)])



