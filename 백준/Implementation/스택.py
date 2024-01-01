n = int(input())
stack = []
answer = []
for i in range(n):
    order = input().split()
    if order[0] == "push":
        stack.append(order[1])
    elif order[0] == "top":
        if len(stack) == 0:
            answer.append(-1)
        else:
          answer.append(stack[-1])
    elif order[0] == "size":
        answer.append(len(stack))
    elif order[0] == "empty":
        if len(stack) == 0:
            answer.append(1)
        else:
            answer.append(0)
    else:
        if len(stack) == 0:
            answer.append(-1)
        else:
          ans = stack.pop()
          answer.append(ans)
for i in answer:
    
  print(i)