n, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
def top_k_num(nums):
    sorted_nums = sorted(nums)
    return sorted_nums[k-1]


print(top_k_num(nums))