a, b = map(int, input().split())

# 1 <= a,b <= 100 

# Please write your code here.

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True
    

def get_sum_digits(n):
    sum = 0
    while(n > 0):
        digit = n % 10
        n = n // 10
        sum += digit
    
    return sum 


def count_magic_prime(a,b):
    count = 0
    for i in range (a,b+1):
        if(is_prime(i) and get_sum_digits(i)%2 == 0):
            count += 1
    return count
    

print(count_magic_prime(a,b))
