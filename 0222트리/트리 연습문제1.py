"""
간선의 개수 : 4
정점의 개수 : 5

4
1 2 1 3 3 4 3 5

"""

n = 5   # 정점의 개수
e = int(input())
tree = list(map(int, input().split()))

# 트리를 저장하는 두가지 방법
# 1. 부모 번호를 인덱스로 저장할 때
child_left = [0] * (n + 1)
child_right = [0] * (n + 1)

for i in range(e):
    parent = tree[i * 2]
    child = tree[i * 2 + 1]
    # 왼쪽 자식이 비어있으면 왼쪽에 추가
    if child_left[parent] == 0:
        child_left[parent] = child
    # 왼쪽 자식이 이미 있으면 오른쪽에 추가
    else:
        child_right[parent] = child
print(child_left) # 0 2 0 4 0 0
print(child_right)  # 0 3 0 5 0 0
print("===================")

# 2. 자식 번호를 인덱스로 사용할 때
parent = [0] * (n+1)
for i in range(e):
    p = tree[i * 2]
    c = tree[i * 2 + 1]
    parent[c] = p

print(parent)

# 5 번 노드의 조상 노드 탐색
now = 5
# parent[now] == 0 이면 now가 루트노드이기 때문에 부모 노드가 존재하지 않는다.
while parent[now] != 0:
    print(parent[now])
    now = parent[now]
print(now)