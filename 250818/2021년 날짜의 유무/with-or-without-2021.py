M, D = map(int, input().split())

# Please write your code here.

def chk_valid_day_in_2021(M,D):
    last_day_in_2021 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    valid_date = (1 <= M <= 12) and (1 <= D <= last_day_in_2021[M-1])
    if (valid_date):
        return "Yes"
    else:
        return "No"


print(chk_valid_day_in_2021(M,D))
    