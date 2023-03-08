N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

print(arr)
# 인접리스트를 만든다
visited = [[0] * M for _ in range(N)]
r=c=0
q = []
