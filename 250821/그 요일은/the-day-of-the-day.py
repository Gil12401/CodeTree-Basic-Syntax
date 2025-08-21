m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
last_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# 특정 월/일(m,d)을 1월 1일부터 며칠째인지 변환하는 함수
# 예: 3월 1일 → 31(1월) + 29(2월) + 1 = 61
def get_days_from_date(m, d):
    days = 0
    days += d  # 해당 달의 일 수 더함
    for i in range(m-1):      # 이전 달들의 모든 일 수 더함
        days += last_days[i]
    return days  # 1월 1일 기준으로 며칠째인지 반환


# 특정 요일(A)이 시작일~끝일까지 몇 번 나오는지 세는 함수
def count_day_of_week(mon_days, end_days, day):
    count = 0
    
    # 입력받은 요일 문자열이 day_of_week 리스트 안에 있으면 그 인덱스를 구함
    # 예: "Sat" → 5
    if day in day_of_week:
        day_idx = day_of_week.index(day)
    else:
        day_idx = -1  # 잘못된 입력이면 -1
    
    # 기준점: (시작일이 월요일이라는 가정 하에) 
    # mon_days + day_idx = 처음으로 해당 요일이 나오는 "날짜 수"
    start_days = mon_days + day_idx
    
    # 첫 번째 해당 요일 무조건 1번 카운트
    count += 1
    
    # 나머지는 7일 간격마다 반복 → (끝날짜 - 첫날짜) // 7 만큼 추가됨
    count += (end_days - start_days) // 7
    
    return count


# (m1,d1)과 (m2,d2)를 1월 1일 기준 "며칠째"로 변환
mon_days = get_days_from_date(m1, d1)
end_days = get_days_from_date(m2, d2)

# 해당 요일이 몇 번 나오는지 출력
print(count_day_of_week(mon_days, end_days, A))

# ----------------------------------------- Comment --------------------------------------------------
# 변수 선언 및 입력
m1, d1, m2, d2 = tuple(map(int, input().split()))
A = input()


def num_of_days(m, d):
    # 계산 편의를 위해 월마다 몇 일이 있는지를 적어줍니다. 
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    
    # 1월부터 (m - 1)월 까지는 전부 꽉 채워져 있습니다.
    for i in range(1, m):
        total_days += days[i]
    
    # m월의 경우에는 정확이 d일만 있습니다.
    total_days += d
    
    return total_days


def num_of_day(s):
    # 간단한 비교를 위해 요일을 숫자로 나타내줍니다.
    if s == "Mon": 
        return 0
    elif s == "Tue": 
        return 1
    elif s == "Wed": 
        return 2
    elif s == "Thu": 
        return 3
    elif s == "Fri": 
        return 4
    elif s == "Sat": 
        return 5
    return 6


ans = 0   
start_date = num_of_days(m1, d1)
end_date = num_of_days(m2, d2)
cur_day = num_of_day("Mon")

for date in range(start_date, end_date + 1):
    # 오늘의 요일이 A요일과 같다면 정답에 추가합니다.
    if cur_day == num_of_day(A): 
        ans += 1

    cur_day = (cur_day + 1) % 7

# 출력
print(ans)
