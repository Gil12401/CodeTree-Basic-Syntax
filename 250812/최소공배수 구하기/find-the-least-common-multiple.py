n, m = map(int, input().split())

# Please write your code here.
def find_GCD(n,m):
    min_num = min(n,m)
    result = 0
    for i in range(min_num, 0, -1):
        cond_A = (n % i == 0)
        cond_B = (m % i == 0)
        
        if ( cond_A and cond_B):
            return i 

    
def find_LCM(n,m):
    lcm = (n * m) // find_GCD(n,m)
    print(lcm)

find_LCM(12,18)