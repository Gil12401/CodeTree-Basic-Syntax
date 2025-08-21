binary = input()

# Please write your code here.
def binary_to_decimal(binary):
    num = 0 
    binary_digits=[]
    for digit in binary:
        binary_digits.append(int(digit))

    for i in range(len(binary_digits)):
        num = num * 2 + binary_digits[i]

    return num 


print(binary_to_decimal(binary))
        


