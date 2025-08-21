m1, d1, m2, d2 = map(int, input().split())

# 각 달의 마지막 날짜 (2011년은 윤년이 아니므로 2월 = 28일)
last_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 기준일(m, d)이 그 해 1월 1일부터 며칠째 되는 날인지 계산
def get_days_from_date(m, d):
    days = 0
    # 먼저 같은 달 안에서 날짜만큼 더함
    days += d
    # 그 전 달까지의 날짜를 모두 합산
    for i in range(m-1):
        days += last_days[i]
    return days


# 기준일(m1,d1)이 월요일이라 가정했을 때
# 다른 날짜(m2,d2)의 요일을 구하는 함수
def get_day_of_week(mon_days, unknown_days):
    # mon_days : m1,d1이 1월1일부터 몇 번째 날인지
    # unknown_days : m2,d2가 1월1일부터 몇 번째 날인지

    # 기준일(m1,d1) 이후 날짜라면 정상적인 요일 순서
    if(mon_days <= unknown_days):
        day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # 기준일 이전 날짜라면 역순으로 요일을 계산해야 함
    else:
        day_of_week = ["Mon", "Sun", "Sat", "Fri", "Thu", "Wed", "Tue"]
        
    # 두 날짜 차이를 7로 나눈 나머지가 요일 차이
    day_idx = abs(mon_days - unknown_days) % 7
    
    # 해당 요일 반환
    return day_of_week[day_idx]


# 기준일(월요일인 날짜)의 절대 일수
mon_days = get_days_from_date(m1, d1)
# 구하고 싶은 날짜의 절대 일수
unknown_days = get_days_from_date(m2, d2)

# 최종 결과 출력
print(get_day_of_week(mon_days, unknown_days))
