n, m = map(int, input().split())

# Please write your code here.
def get_GCD_from_2num(n,m):
    range_num = min(n,m)
    result = 0
    for i in range(range_num, 0, -1):
        cond_A = (n % i == 0)
        cond_B = (m % i == 0)
        
        if ( cond_A and cond_B):
            print(i)
            break
        

get_GCD_from_2num(n,m)
        