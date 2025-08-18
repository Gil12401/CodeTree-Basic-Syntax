n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
# Ascend
nums.sort()
for num in nums:
    print(num,end=" ")

print()
# Descend
nums = nums[::-1]
for num in nums:
    print(num,end=" ")

