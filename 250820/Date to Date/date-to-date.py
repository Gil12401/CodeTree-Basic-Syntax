m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
last_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_days_from_date(m,d):
    days = 0
    days += d 
    for i in range(m):
        days += last_days[i]

    return days

days_start = get_days_from_date(m1,d1)
days_end = get_days_from_date(m2,d2)
days_diff = days_end - days_start

print(days_diff)





    
    

        

    

