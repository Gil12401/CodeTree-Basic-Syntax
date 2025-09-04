N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
count = 0 
max_count = 0
for i in range(N):
    if (i == 0 or arr[i]*arr[i-1] < 0):
        count = 0
    count += 1
    max_count = max(max_count, count)
    
print(max_count)