"""
# print(solution([1, 2, 3, 4, 5, 6, 7])) # 반환값 : ["1 2 4 5 3 6 7", "4 2 5 1 6 3 7", "4 5 2 6 7 3 1"]
"""

# 전위순회

def preorder(nodes, idx):
    if idx < len(nodes):
        # 부모부터 확인
        ret = str(nodes[idx]) + " "
        # 좌측 노드 확인
        ret += preorder(nodes, idx * 2 + 1)
        # 우측 노드 확인
        ret += preorder(nodes, idx * 2 + 2)
        return ret
    else:
        return ""

def inorder(nodes, idx):
    if idx < len(nodes):
        ret = inorder(nodes, idx * 2 + 1)
        ret += str(nodes[idx]) + " "
        ret += inorder(nodes, idx * 2 + 2)
        return ret
    else:
        return ""

def postorder(nodes, idx):
    if idx < len(nodes):
        ret = postorder(nodes, idx * 2 + 1)
        ret += postorder(nodes, idx * 2 + 2)
        ret += str(nodes[idx]) + " "
        return ret
    else:
        return ""

def solution(nodes):
    return [
        preorder(nodes, 0)[:-1],
        inorder(nodes, 0)[:-1],
        postorder(nodes, 0)[:-1],
    ]

print(solution([1, 2, 3, 4, 5, 6, 7]))