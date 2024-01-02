from collections import deque

words = input()
size = len(words)
stack = []
flag = 0
ans = ""

for i in range(size):
    if flag == 0 and words[i] == "<":
        if stack:
          while stack:
            ans += stack.pop()
        flag = True
        ans += words[i]
    elif flag and words[i] == ">":
        flag = False
        ans += words[i]
    elif flag:
        ans += words[i]
    # elif words[i] == ">"
    elif words[i] == " " and stack:
        while stack:
          ans += stack.pop()
        ans += " "
    else:
        stack.append(words[i])
        # print(stack)

while stack:
    ans += stack.pop()

print(ans)