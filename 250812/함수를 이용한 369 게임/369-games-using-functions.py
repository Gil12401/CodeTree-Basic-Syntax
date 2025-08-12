a, b = map(int, input().split())

# Please write your code here.
def is_contain_369(n):
    ones = n % 10
    tens = n // 10

    cond_ones = ones in (3, 6, 9)
    cond_tens = tens in (3, 6, 9)

    return (cond_ones or cond_tens)


def count_magic_number(a, b):
    count = 0
    for i in range(a,b+1):
        if (i%3 == 0  or is_contain_369(i)):
            count += 1
    return count

print(count_magic_number(a,b))
