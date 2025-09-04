n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
count = 0 
max_count = 0

for i in range(n):
    if i == 0 or arr[i] > arr[i-1]:
        count += 1
    else:
        count = 1
    
    # print(count,end=" ")
    max_count = max(count,max_count)
        
print(max_count)