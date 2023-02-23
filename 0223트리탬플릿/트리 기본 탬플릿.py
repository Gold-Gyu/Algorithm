"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""

# 전위 순회
def preorder(i):
    if i: # == if i > 0
        print(i, end = " ")
        preorder(left[i])
        preorder(right[i])
    return
# 중위 순회
def inorder(i):
    if i: # == if i > 0
        inorder(left[i])
        print(i, end=" ")
        inorder(right[i])
    return

# 후위 순회
def postorder(i):
    if i: # == if i > 0
        postorder(left[i])
        postorder(right[i])
        print(i, end=" ")
    return
V = int(input())
arr = list(map(int, input().split()))
E = V - 1   # 간선의 수
left = [0] * (V+1)  # 부모를 인덱스로 왼쪽 자식 저장
right = [0] * (V+1) # 부모를 인덱스로 오른쪽 자식 저장

# 루트를 찾아야하는 경우
par = [0] * (V+1)   # 자식을 인덱스로 부모 저장

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]  # 부모, 자식을 가져와서
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    # 루트 찾기
    par[c] = p

root = 1
while par[root] != 0:       # 루트 찾기
    root += 1
print(root)
preorder(root)
print()
inorder(root)
print()
postorder(root)
print()