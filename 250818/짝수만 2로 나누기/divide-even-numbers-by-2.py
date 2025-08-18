n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def split_even_num(arr):
    for i in range(len(arr)):
        if(arr[i]%2 == 0):
            arr[i] //= 2 
    
    for num in arr:
        print(num, end=" ")

split_even_num(arr[:])


