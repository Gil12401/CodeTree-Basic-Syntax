a, b = map(int, input().split())

# Please write your code here.
def is_contain_369(n):
   while(n > 0): 
    digit = n % 10
    if (digit in (3,6,9)):
        return True
    n //= 10

    
def count_magic_number(a, b):
    count = 0
    for i in range(a,b+1):
        if (i%3 == 0  or is_contain_369(i)):
            count += 1
    return count

print(count_magic_number(a,b))
