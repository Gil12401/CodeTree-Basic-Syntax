a, b, c, d = map(int, input().split())

# Please write your code here.

def elapsed_time_from_zero(h,m):
    elapsed_time = 60*h + m 
    return elapsed_time

elapsed_time_start = elapsed_time_from_zero(a, b)
elapsed_time_end = elapsed_time_from_zero(c, d)

elapsed_time = elapsed_time_end - elapsed_time_start
print(elapsed_time)

