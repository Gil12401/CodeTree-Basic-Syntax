N = input()

# Please write your code here.
def binary_to_decimal(binary):
    num = 0 
    binary_digits=[]
    for digit in binary:
        binary_digits.append(int(digit))

    for i in range(len(binary_digits)):
        num = num * 2 + binary_digits[i]

    return num 


def decimal_to_binary(n):
    digits= []

    while True:
        if n < 2:
            digits.append(n)
            break
        digits.append(n%2)
        n //= 2
    
    return digits[::-1]

num = binary_to_decimal(N)
num *= 17
binary_digits = decimal_to_binary(num)

for digit in binary_digits:
    print(digit,end="")