import itertools

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums_cycle = itertools.cycle(range(1,10))
n = int(input())


# Please write your code here.
def write_decimal_square(n):
    for _ in range(n):
        for _ in range(n):
            print(next(nums_cycle), end=" ")  
        print()    
    

write_decimal_square(n)