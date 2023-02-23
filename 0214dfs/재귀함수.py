def function(num):

    print("now", num)

    #1. 반드시 종료조건을 정한다.(기저조건)
    if num == 0:
        return

    # 2 종료 조건이 아닌 경우에 재귀 호출
    # 언젠가는 종료조건을 만족하도록 설정을 해야함.
    else:
        function(num - 1)

    print("back", num)

function(5)