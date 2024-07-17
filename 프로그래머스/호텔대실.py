from collections import deque

def convert_to_minutes(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def solution(book_time):
    # 각 예약 시간을 분 단위로 변환하고, 종료 시간에 10분을 더해 정리 시간을 고려
    times = [(convert_to_minutes(start), convert_to_minutes(end) + 10) for start, end in book_time]
    times.sort()
    print(times)
    rooms = []  # 각 방의 다음 가능한 시작 시간을 저장
    for start, end in times:
        # 현재 예약을 넣을 방을 찾음
        placed = False
        for i in range(len(rooms)):
            if rooms[i] <= start:  # 방이 비어 있는 경우
                rooms[i] = end # 방이 끝나는 시간 최신화 시킴

                placed = True
                break
        # 방을 최신화시킬게 없다면
        if not placed:
            rooms.append(end)  # 새로운 방을 추가
            print("rooms add : ", rooms)
    return len(rooms)
