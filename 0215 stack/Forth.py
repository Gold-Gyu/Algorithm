def postfix(txt):
    stack = []
    for i in txt:
        # 숫자를 만나면 스택에 넣는다.
        if "0" <= i <= "9":
            stack.append(int(i))
        elif i == ".":
            if len(stack) != 1:
                return "error"
            else:
                return stack.pop()
        else:  # 사칙연산을 만났을 때 스택에서 뺀 후 계산하고 다시 그 값을 넣음
            if len(stack) >= 2:
                right = stack.pop()
                left = stack.pop()
                if i == "+":
                    res = int(left + right)
                elif i == "-":
                    res = int(left - right)
                elif i == "/":
                    res = int(left // right)
                elif i == "*":
                    res = int(left * right)
                stack.append(res)
            else:
                return "error"
    return


T = int(input())

for tc in range(1, T + 1):
    string = input().split()
    answer = postfix(string)
    print(f"#{tc} {answer}")