a, b = map(int, input().split())

# Please write your code here.
def get_pow(a,b):
    result = 1
    for _ in range(b):
        result *= a
    
    return result

print (get_pow(a,b))
