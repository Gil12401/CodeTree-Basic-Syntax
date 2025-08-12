n = int(input())

# Please write your code here.
def sum_until_n_div10(n):
    sum = 0
    for i in range(n+1):
        sum += i
    
    result = sum // 10
    return (result)

print(sum_until_n_div10(n))