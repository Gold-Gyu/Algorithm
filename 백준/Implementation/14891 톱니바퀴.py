from pprint import pprint
arr = [list(map(int, input())) for _ in range(4)]

k = int(input())

for tc in range(k):
    pick, direction = map(int, input().split())

    if direction == 1:  # 시계방향
        if pick == 1:
            if arr[pick-1][2] != arr[1][-2] and arr[1][2]!= arr[2][-2] and arr[2][2] != arr[3][-2]:
                temp = arr[pick-1].pop()
                arr[pick-1].insert(0, temp)
                temp = arr[1].pop(0)
                arr[1].insert(7, temp)
                temp = arr[2].pop()
                arr[2].insert(0, temp)
                temp = arr[3].pop(0)
                arr[3].insert(7, temp)
            elif arr[pick-1][2] != arr[1][-2] and arr[1][2]!= arr[2][-2]:
                temp = arr[pick-1].pop()
                arr[pick-1].insert(0, temp)
                temp = arr[1].pop(0)
                arr[1].insert(7, temp)
                temp = arr[2].pop()
                arr[2].insert(0, temp)
            elif arr[pick-1][2] != arr[1][-2]:
                temp = arr[pick-1].pop()
                arr[pick-1].insert(0, temp)
                temp = arr[1].pop(0)
                arr[1].insert(7, temp)
            else:
                temp = arr[pick - 1].pop()
                arr[pick - 1].insert(0, temp)


        elif pick == 2:
            if arr[pick-1][2] != arr[2][-2] and arr[pick-1][-2] != arr[0][2] and arr[2][2] != arr[3][-2]:
                temp = arr[pick-1].pop()
                arr[pick-1].insert(0, temp)
                temp = arr[2].pop(0)
                arr[2].insert(7, temp)
                temp = arr[0].pop(0)
                arr[0].insert(7, temp)
                temp = arr[3].pop()
                arr[3].insert(0, temp)
            elif arr[pick - 1][2] != arr[2][-2] and arr[pick - 1][-2] != arr[0][2]:
                temp = arr[pick - 1].pop()
                arr[pick - 1].insert(0, temp)
                temp = arr[2].pop(0)
                arr[2].insert(7, temp)
                temp = arr[0].pop(0)
                arr[0].insert(7, temp)
            elif arr[pick - 1][2] != arr[2][-2]:
                temp = arr[pick - 1].pop()
                arr[pick - 1].insert(0, temp)
                temp = arr[2].pop(0)
                arr[2].insert(7, temp)
            elif arr[pick - 1][2] != arr[0][-2]:
                temp = arr[pick - 1].pop()
                arr[pick - 1].insert(0, temp)
                temp = arr[0].pop(0)
                arr[0].insert(7, temp)
            else:
                temp = arr[pick - 1].pop()
                arr[pick - 1].insert(0, temp)

        elif pick == 3:
            if arr[pick - 1][2] != arr[3][-2] and arr[pick - 1][-2] != arr[1][2] and arr[0][2] != arr[1][-2]:
                temp = arr[pick - 1].pop()
                arr[pick - 1].insert(0, temp)
                temp = arr[3].pop(0)
                arr[3].insert(7, temp)
                temp = arr[1].pop(0)
                arr[1].insert(7, temp)
                temp = arr[0].pop()
                arr[0].insert(0, temp)
            elif arr[pick - 1][2] != arr[3][-2] and arr[1][2] != arr[pick-1][-2]:
                temp = arr[pick - 1].pop()
                arr[pick - 1].insert(0, temp)
                temp = arr[3].pop(0)
                arr[3].insert(7, temp)
                temp = arr[1].pop(0)
                arr[1].insert(7, temp)
            elif arr[pick - 1][2] != arr[3][-2]:
                temp = arr[pick - 1].pop()
                arr[pick - 1].insert(0, temp)
                temp = arr[3].pop(0)
                arr[3].insert(7, temp)
            elif arr[1][2] != arr[pick-1][-2]:
                temp = arr[pick - 1].pop()
                arr[pick - 1].insert(0, temp)
                temp = arr[1].pop(0)
                arr[1].insert(7, temp)
                temp = arr[1].pop(0)
                arr[1].insert(7, temp)
            else:
                temp = arr[pick - 1].pop()
                arr[pick - 1].insert(0, temp)

        else:
            if arr[pick - 1][-2] != arr[2][2] and arr[1][2] != arr[2][-2] and arr[0][2] != arr[1][-2]:
                temp = arr[pick - 1].pop()
                arr[pick - 1].insert(0, temp)
                temp = arr[2].pop(0)
                arr[2].insert(7, temp)
                temp = arr[1].pop()
                arr[1].insert(0, temp)
                temp = arr[0].pop(0)
                arr[0].insert(7, temp)

            elif arr[pick - 1][-2] != arr[2][2] and arr[1][2] != arr[2][-2]:
                temp = arr[pick - 1].pop()
                arr[pick - 1].insert(0, temp)
                temp = arr[2].pop(0)
                arr[2].insert(7, temp)
                temp = arr[1].pop()
                arr[1].insert(0, temp)

            elif arr[pick - 1][-2] != arr[2][2]:
                temp = arr[pick - 1].pop()
                arr[pick - 1].insert(0, temp)
                temp = arr[2].pop(0)
                arr[2].insert(7, temp)
            else:
                temp = arr[pick - 1].pop()
                arr[pick - 1].insert(0, temp)


    elif direction == -1: # 반시계방향
        if pick == 1:
            if arr[pick-1][2] != arr[1][-2] and arr[1][2]!= arr[2][-2] and arr[2][2] != arr[3][-2]:
                temp = arr[pick - 1].pop(0)
                arr[pick - 1].insert(7, temp)
                temp = arr[1].pop()
                arr[1].insert(0, temp)
                temp = arr[2].pop(0)
                arr[2].insert(7, temp)
                temp = arr[3].pop()
                arr[3].insert(0, temp)
            elif arr[pick - 1][2] != arr[1][-2] and arr[1][2] != arr[2][-2]:
                temp = arr[pick - 1].pop(0)
                arr[pick - 1].insert(7, temp)
                temp = arr[1].pop()
                arr[1].insert(0, temp)
                temp = arr[2].pop(0)
                arr[2].insert(7, temp)
            elif arr[pick - 1][2] != arr[1][-2]:
                temp = arr[pick - 1].pop(0)
                arr[pick - 1].insert(7, temp)
                temp = arr[1].pop()
                arr[1].insert(0, temp)
            else:
                temp = arr[pick - 1].pop(0)
                arr[pick - 1].insert(7, temp)

        elif pick == 2:
            if arr[pick-1][2] != arr[2][-2] and arr[pick-1][-2] != arr[0][2] and arr[2][2] != arr[3][-2]:
                temp = arr[pick - 1].pop(0)
                arr[pick - 1].insert(7, temp)
                temp = arr[2].pop()
                arr[2].insert(0, temp)
                temp = arr[0].pop()
                arr[0].insert(0, temp)
                temp = arr[3].pop()
                arr[3].insert(0, temp)
            elif arr[pick - 1][2] != arr[2][-2]:
                temp = arr[pick - 1].pop(0)
                arr[pick - 1].insert(7, temp)
                temp = arr[2].pop()
                arr[2].insert(0, temp)

            elif arr[pick - 1][-2] != arr[0][2]:
                temp = arr[pick - 1].pop(0)
                arr[pick - 1].insert(7, temp)
                temp = arr[0].pop()
                arr[0].insert(0, temp)
            else:
                temp = arr[pick - 1].pop(0)
                arr[pick - 1].insert(7, temp)

        elif pick == 3:
            if arr[pick - 1][2] != arr[3][-2] and arr[pick - 1][-2] != arr[1][2] and arr[0][2] != arr[1][-2]:
                temp = arr[pick - 1].pop(0)
                arr[pick - 1].insert(7, temp)
                temp = arr[3].pop()
                arr[3].insert(0, temp)
                temp = arr[1].pop()
                arr[1].insert(0, temp)
                temp = arr[0].pop(0)
                arr[0].insert(7, temp)
            elif arr[pick - 1][2] != arr[3][-2]:
                temp = arr[pick - 1].pop(0)
                arr[pick - 1].insert(7, temp)
                temp = arr[3].pop()
                arr[3].insert(0, temp)
            else:
                temp = arr[pick - 1].pop(0)
                arr[pick - 1].insert(7, temp)

        else:
            if arr[pick - 1][-2] != arr[2][2] and arr[1][2] != arr[2][-2] and arr[0][2] != arr[1][-2]:
                temp = arr[pick - 1].pop(0)
                arr[pick - 1].insert(7, temp)
                temp = arr[2].pop()
                arr[2].insert(0, temp)
                temp = arr[1].pop(0)
                arr[1].insert(7, temp)
                temp = arr[0].pop()
                arr[0].insert(0, temp)

            elif arr[pick - 1][-2] != arr[2][2] and arr[1][2] != arr[2][-2]:
                temp = arr[pick - 1].pop(0)
                arr[pick - 1].insert(7, temp)
                temp = arr[2].pop()
                arr[2].insert(0, temp)
                temp = arr[1].pop(0)
                arr[1].insert(7, temp)

            elif arr[pick - 1][-2] != arr[2][2]:
                temp = arr[pick - 1].pop(0)
                arr[pick - 1].insert(7, temp)
                temp = arr[2].pop()
                arr[2].insert(0, temp)
            else:
                temp = arr[pick - 1].pop(0)
                arr[pick - 1].insert(7, temp)

answer = 0
point = [1, 2, 4, 8]
for ans in range(4):
    if arr[ans][0] == 1:
        answer += point[ans]


print(answer)
pprint(arr)
"""
11001100
00001101
11000100
11010001
10
3 1
1 -1
3 1
2 -1
3 1
2 -1
4 1
1 1
3 1
2 -1

11111110
00000000
11111111
11111111
1
2 -1
"""