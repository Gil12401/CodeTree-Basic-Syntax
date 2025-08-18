a, b = map(int, input().split())

# Please write your code here.
def op_2nums(a, b):
    
    if (a < b):
        _a = a * 2
        _b = b + 25
    else:
        _a = a + 25
        _b = b * 2 
   
    return _a, _b
    

a, b = op_2nums(a, b)
print(a, b, end=" ")
    