n = int(input())

# Please write your code here.
def is_magic_number(n):
    tens = n // 10
    ones = n % 10
    digit_sum = tens + ones 

    cond_even = (n % 2 == 0)
    cond_fivetimes = (digit_sum % 5 == 0)
    
    if (cond_even and cond_fivetimes):
        return "Yes"
    else:
        return "No"
    
print(is_magic_number(n))
