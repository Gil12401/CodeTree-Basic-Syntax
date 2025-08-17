a, b = map(int, input().split())

# Please write your code here.

def count_onjeonsoo(a,b):
    count = 0
    for i in range (a,b+1):
        digit_ones = i % 10
        if i%2 == 0:
            continue
        elif digit_ones == 5:
            continue
        elif i%3 == 0 and i%9 != 0:
            continue
        count += 1
    
    return count 

print(count_onjeonsoo(a,b))
        