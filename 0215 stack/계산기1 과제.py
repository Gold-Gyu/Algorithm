import sys
sys.stdin = open('input.txt', 'r')

# 후위 표기식으로 바꾸기

def calcu(infix, n):
    answer = ""
    stack = []

    for z in range(n):
        if "0" <= infix[z] <= "9":    # 숫자면 answer에 추가
            answer += infix[z]

        else:                       # 숫자가 아니면
            if infix[z] == "+":     # 숫자가 아닌 기호 +라면
                if stack:           # 스택안이 비어있지 않다면
                    plus = stack.pop()
                    stack.append(infix[z])# 스택에서 하나 +를 뽑아서
                    answer += plus      # 문자열에 더해준다.
                else:                   # 스택안이 비었으면
                    stack.append(infix[z]) # +를 스택에 저장

    return answer


# 후위 표기식에서 계산하기
def calcu_result(anwser):      # postfix 는 후위 표기식
    stack = []

    for c in anwser:
        if "0" <= c <= "9":     # 숫자면 stack에 저장
            stack.append(int(c))    # int 정수형으로 더해준다
        else:                   # 연산자면
            right = stack.pop()
            left = stack.pop()
            if c == "+":
                res = left + right
            stack.append(res)
    else:
        if len(stack) == 2:
            r = stack.pop()
            l = stack.pop()
            final_ = l + r
            stack.append(final_)
        else:
            return "error"
    return stack.pop()




for tc in range(1, 11):
    N = int(input())
    lst = input()
    n = len(lst)
    gogo = calcu(lst, n)
    print(f"#{tc} {calcu_result(gogo)}")

