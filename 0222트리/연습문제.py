"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

"""

n = int(input())
tree = list(map(int, input().split()))

# 부모 번호로 인덱스일 떄
cleft = [0] * (n+1)
cright = [0] * (n+1)

for i in range(n-1):    # 간선의 개수 = 정점의 개수 - 1
    p = tree[i*2]
    c = tree[i*2+1]
    if cleft[p] == 0:
        cleft[p] = c
    else:
        cright[p] = c

print(cleft)
print(cright)

# 전위 순회 VLR

def preorder(t):
    if t:
        print(t, end = " ")
        preorder(cleft[t])
        preorder(cright[t])
    # t 노드가 존재한다면
    # 데이터 처리(print)
    # 왼쪽 방문
    # 오른쪽 방문

# 중위 순회 LVR

def inorder(t):
    if t:
        inorder(cleft[t])
        print(t, end = " ")
        inorder(cright[t])

# 후위 순회 LRV

def postorder(t):
    if t:
        postorder(cleft[t])
        postorder(cright[t])
        print(t, end = " ")


preorder(1)
print()
inorder(1)
print()
postorder(1)