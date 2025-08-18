a, b = map(int, input().split())

# Please write your code here.
def op_2nums(a, b):
    
    if (a < b):
        _a = a + 10
        _b = b * 2
    else:
        _a = a * 2
        _b = b + 10 
   
    return _a, _b
    

a, b = op_2nums(a, b)
print(a, b, end=" ")
    