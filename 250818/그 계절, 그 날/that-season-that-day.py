Y, M, D = map(int, input().split())
last_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Please write your code here.
def is_leapyear(y):
    if (y % 4) != 0:
        return False
    if (y % 100 == 0) and (y % 400 != 0):
        return False
    return True
    
    
def get_season_from_month(M):
    if M in (3, 4, 5):
        return "Spring"
    elif M in (6, 7, 8):
        return "Summer"
    elif M in (9, 10, 11):
        return "Fall"
    elif M in (12, 1, 2):
        return "Winter"
    else:
        return "Out of Range in Month"


def get_season_from_date(Y,M,D):
    season = ""
    
    if(is_leapyear(Y)):
        last_days[1] = 29
    
    valid_date = (1 <= M <= 12) and (1 <= D <= last_days[M-1])
    
    if (valid_date):
        season = get_season_from_month(M)
        return season
    else:
        return -1


print(get_season_from_date(Y,M,D))
    