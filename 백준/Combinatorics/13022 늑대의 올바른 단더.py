n = input()
lst = [0, 0, 0, 0]
# 각 문자의 개수가 n개가 나란히 나오면 O
# 문자 두개를 이은것도 올바른단어
# 굿굿
size = len(n)
flag = 0
for i in range(size):
    if n[i] == "w":
        lst[0] += 1
        if lst[0] == lst[1] == lst[2] == lst[3]:
            flag = 1
            break

    elif n[i] == "o":
        lst[1] += 1
        if lst[0] < lst[1] or lst[2] > lst[1] and lst[3] > lst[1]:
            flag = 1
            break

    elif n[i] == "l":
        lst[2] += 1
        if lst[2] > lst[0] or lst[2] > lst[1] or lst[3] > lst[2]:
            flag = 1
            break
    else:
        lst[3] += 1
        if lst[3] > lst[0] or lst[3] > lst[1] or lst[3] > lst[2]:
            flag = 1
            break

if flag == 0 and lst[0] == lst[1] == lst[2] == lst[3]:
    print(1)
else:
    print(0)

# wolffwwoollf