n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
def get_optimal_max(nums):
    sorted_nums = sorted(nums)
    last = 2*n
    _max = 0

    for i in range(last):
        tmp_max = sorted_nums[i] + sorted_nums[last-1-i]
        _max=max(tmp_max, _max)
    
    return _max


print(get_optimal_max(nums))




