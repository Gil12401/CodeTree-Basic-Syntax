n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def get_middle_num_list(arr):
    _list = []
    middle_num_list = [] 
    for num in range(0 ,len(arr),2):
        _list = sorted(arr[:num+1])
        middle_num = _list[len(_list)//2]
        middle_num_list.append(middle_num)
    
    return middle_num_list
        

for middle_num in get_middle_num_list(arr):
    print(middle_num,end=" ")
