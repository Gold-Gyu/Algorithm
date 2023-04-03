"""

상호배타집합 : 서로 겹치는게 없는 집합 = 서로소

즉 서로소 == 대표자(식별할 수 있는 집합의 이름)

이러한 사호배타 집합 연산
1. make-set(x) : 아무것도 없는 초기상태에서 x 대표의 집합을 만듬
2. find-set(x) : x가 속해있는 집합의 대표자(식별할 수 있는 집합의 이름)는 누구인지
3. union(x, y) : x가 속한 집합과 y가 속한 집합을 합병 즉, 규칙에 맞게 대표를 하나 정해서 그 안에 넣는다( ex) y에 속한 집합에 이제 x가 속하게됨)


★ 연결리스트로 표현하는 방법
★ 트리로 표현하는 방법


"""

# p[x] => x 의 부모
# p[x] == x => x의 집합 대표가 x이다. x는 대표자
p = [0] * 10

# 1. 집합 초기화
def makeSet(x):
    p[x] = x

# 2. x가 속한 집합의 대표를 얻는 연산
def findSet(x):
    if p[x] == x:
        return x
    else :
        return findSet(p[x])

# 3. 두 집합을 합치는 연산
# x가 속한 집합과 y가 속한 집합을 합치는 연산
# 집합의 대표를 앞에 나온 인자가 속한 대표로 정한다.
def union(x, y):
    p[findSet(y)] = findSet(x)

def findSet2(x):
    while x != p[x] :
        x = findSet2(p[x])
    return x

for i in range(1, 7):
    makeSet(i)
union(1, 3)
union(2, 3)
union(5, 6)
print(p)
for i in range(1, 7):
    print(findSet2(i))
print(p)