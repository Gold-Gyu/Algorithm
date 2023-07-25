n = input()

standard = {"w": 0, "o": 0, "l": 0, "f": 0}
lst = [0, 0, 0, 0]
# 각 문자의 개수가 n개가 나란히 나오면 O
# 문자 두개를 이은것도 올바른단어
size = len(n)

flag = 0
for i in range(size):
    if n[i] == "w":
        lst[0] += 1
        if lst[0] == lst[1] == lst[2] == lst[3]:
            flag = 1
            break
        elif lst[0] - lst[2] >= 2 or lst[0] - lst[3] >= 2:
            flag = 1
            break
    elif n[i] == "o":
        lst[1] += 1
        if lst[0] < lst[1] or lst[2] > lst[1] or lst[3] > lst[1]:
            flag = 1
            break

    elif n[i] == "l":
        lst[2] += 1
        if lst[2] > lst[0] or lst[2] < lst[3] or lst[1] < lst[2]:
            flag = 1
            break
    else:
        if lst[0] != 0 and lst[1] != 0 and lst[2] != 0 and lst[0] == lst[1] == lst[2]:
            lst[3] += 1
        else:
            flag = 1
            break

if flag == 0 and lst[0] == lst[1] == lst[2] == lst[3]:
    print(1)
elif flag == 1:
    print(0)
else:
    print(0)

#wolffwwoollf
#wowollff