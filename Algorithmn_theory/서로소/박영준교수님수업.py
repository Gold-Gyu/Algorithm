def findset(x): # x가 속한 집합의 대표 원소를 찾는다
   # 누가 대표원소일까
    while rep[x] != x:  # x == rep[x]가 될 때 까지 반복
        rep[x] = x
    return x

def union(x, y):    # y의 대표원소가 x의 대표원소를 가르키도록 즉, x라는 대표원소 안으로 y가 들어가는것임.
    rep[findset(y)] = findset(x)
    # y가 속한 대표원소를 찾아가봐




# makeset()

# index값이 x가되는 것이고
# rep은 인덱스에 해당하는 값이다.


rep = [i for i in range(6)]
print(rep)

if 2 in (1, 3, 5, 7, 2):
    print("good")