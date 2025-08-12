y = int(input())

# Please write your code here.
def is_leapyear(y):
    if (y % 4) != 0:
        return "false"
    
    if (y % 100 == 0):
        if(y % 400 != 0):
            return "false"

    
    return "true"

print(is_leapyear(y))