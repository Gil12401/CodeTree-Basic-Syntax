a, b, c = map(int, input().split())

# Please write your code here.
MAX_HOURS = 24
MAX_MINS = 60

def get_mins_from_firstday(d, h, m):
    return ((d-1)*MAX_HOURS*MAX_MINS + h*MAX_MINS + m )

mins_start = get_mins_from_firstday(11,11,11)
mins_end = get_mins_from_firstday(a,b,c)
mins = mins_end - mins_start

print(mins)




