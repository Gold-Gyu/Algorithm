txt = input()
stack = []
calculate = 0
# 스택에 이전에도 열린 괄호가 들어왔고 또 열린게 들어오면 곱하기로 진행

# 잘못된 괄호가 된다면 답은 0
# 즉, stack이 남아 있다면  0
for i in txt:
  stack.append(i)