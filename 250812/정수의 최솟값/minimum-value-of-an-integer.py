a, b, c = map(int, input().split())

# Please write your code here.
def get_min_num(a,b,c):
    arr = []

    arr.append(a)
    arr.append(b)
    arr.append(c)

    min_num = arr[0]

    for i in range(3):
        if (arr[i] < min_num):
            min_num = arr[i]

    return (min_num)

print(get_min_num(a,b,c))