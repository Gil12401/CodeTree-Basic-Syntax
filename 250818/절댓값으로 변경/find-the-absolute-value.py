n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def modify_abs(list):
    for i in range(n):
        if (list[i] < 0):
            list[i] = -list[i]
    
    for i in range(n):
        print(list[i], end=" ")
    
    
modify_abs(arr[:])

