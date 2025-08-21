m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
last_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week =["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# m1, d1 -> monday 
def get_days_from_date(m,d):
    days = 0
    days += d 
    for i in range(m-1):
        days += last_days[i]

    return days


def count_day_of_week(mon_days,end_days,day):
    count = 0
    if day in day_of_week:
        day_idx = day_of_week.index(day)
    else:
        day_idx = -1 

    start_days = mon_days + day_idx
    count += 1
    count += (end_days - start_days) // 7

    return count 


mon_days = get_days_from_date(m1,d1)
end_days = get_days_from_date(m2,d2)
print(count_day_of_week(mon_days,end_days,A))