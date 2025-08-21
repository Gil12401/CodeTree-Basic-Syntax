a, b = map(int, input().split())
n = input()

decimal_value = int(n, a)

def decimal_to_base(num, base):
    if num == 0:
        return "0"
    digits = []
    while num > 0:
        digits.append(str(num % base))
        num //= base
    return ''.join(reversed(digits))

print(decimal_to_base(decimal_value, b))