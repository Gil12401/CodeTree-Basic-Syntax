n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
N = 1000
count = 0 
max_count = 0
for i in range(n):
    if (i == 0 or arr[i] != arr[i-1]):
        max_count = max(max_count, count)
        count = 0
    count += 1
    
print(max_count)
