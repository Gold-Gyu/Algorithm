# pattern = ["0001101", ....] 이런 방식으로 인덱스로 뽑아올 수 있음
pattern = {"0001101" : 0,
          "0011001" : 1,
          "0010011" : 2,
          "0111101" : 3,
          "0100011" : 4,
          "0110001" : 5,
          "0101111" : 6,
          "0111011" : 7,
          "0110111" : 8,
          "0001011" : 9}


# 시작을 알 수 없음
# 맨 오른쪽 부분은 1로 끝남
# 범위를 짤라내는법
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 입력이 주어지면 어떻게 저장할 것인가
    # 1.하나씩 끊어서 문자열(읽기만 할 경우, 만약 수정을 해야한다면 문자열은 비추)
    # 2.하나씩 끊어서 정수형
    arr = [input() for _ in range(N)]

    code = ""
    # 행은 위에서부터 내려오고
    for i in range(N):
        #열은 오른쪽부터 왼쪽으로
        for j in range(M-1, 54, -1): # 가장 왼쪽으로 치우친 패턴은 0 - 55까지 있기 때문에 거기까지만 체크한다.
    # 오른쪽 끝에서부터 맨 왼쪽까지 탐색
    # 55번쨰보다 작은 곳엔 암호가 존재할 수 없음 0~ 55 까지가 가장 왼쪽이라고 볼 수 있음
    # why? 문자가 56개니깐
            if arr[i][j] == "1": # 암호글자의 맨 끝 발견을 의미
                code = arr[i][j-55:j+1]
                break   # 가장 가까운 반복문 나감 # for j를 빠져나가는 break
        if code != "":
            break   # for i를 빠져나감

    password = [0] * 8 # 암호는 총 8개이기 때문에
    # 기준을 정해야함
    for i in range(8):
        password[i] = pattern[code[i*7:i*7+7]]
    # 0 ~ 6 번 인덱스까지 확인해서 암호와 비교
    # 즉 비교할 것을 저장해야할 필요가 있
    check = (password[0] + password[2] + password[4] + password[6]) * 3 + password[1] + password[3] + password[5] + password[7]
    # 또 다른 방 checksum = sum(password[0:8:2]) * 3 + sum(password[1:8:2])
    # [A:B:C] : A부터 B-1까지 C간격으로
    answer = 0
    if check % 10 == 0: # 10의 배수이면
        answer = sum(password)
    print(f"#{tc} {answer}")