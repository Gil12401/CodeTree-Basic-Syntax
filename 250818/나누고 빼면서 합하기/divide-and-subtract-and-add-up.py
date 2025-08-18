n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def sum_magic_numbers(A):
    _m = m
    count = 0
    
    while True:
        idx = _m - 1
        count += A[idx]
      
        if (_m == 1):
            break
        
        if (_m%2 == 0):
            _m //= 2
           
        else:
            _m -= 1
        
        
    
    return count

print(sum_magic_numbers(A))
