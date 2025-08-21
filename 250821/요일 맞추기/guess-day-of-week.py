m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
last_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# m1, d1 -> monday 
def get_days_from_date(m,d):
    days = 0
    days += d 
    for i in range(m-1):
        days += last_days[i]

    return days


def get_day_of_week(mon_days,unknown_days):
    day_of_week = []
    
    if(mon_days <= unknown_days):
        day_of_week =["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    else:
        day_of_week = ["Mon", "Sun", "Sat", "Fri", "Thu", "Wed", "Tue"]
        
    day_idx = abs(mon_days - unknown_days) % 7
    
    return day_of_week[day_idx]


mon_days = get_days_from_date(m1,d1)
unknown_days = get_days_from_date(m2,d2)

# 12 23 12 24
print(get_day_of_week(mon_days,unknown_days))
