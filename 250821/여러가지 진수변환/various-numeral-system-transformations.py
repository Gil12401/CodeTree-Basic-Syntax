N, B = map(int, input().split())

# Please write your code here.
def decimal_to_base_N(n,b):
    digits= []

    while True:
        if n < b:
            digits.append(n)
            break
        digits.append(n%b)
        n //= b
    
    return digits[::-1]


base_N_digits = decimal_to_base_N(N,B)
for digit in base_N_digits:
    print(digit,end="")
