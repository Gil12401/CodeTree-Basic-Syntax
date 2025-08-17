a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def do_plus(a,c):
    return a+c
        
def do_minus(a,c):
    return a-c
        
def do_multiple(a,c):
    return a*c
        
def do_divide(a,c):
    return int(a/c) 

if o == "+":
    print(a,o,c,"=",do_plus(a,c))
elif o == "-":
    print(a,o,c,"=",do_minus(a,c))
elif o == "*":
    print(a,o,c,"=",do_multiple(a,c))
elif o == "/":
    print(a,o,c,"=",do_divide(a,c))
else:
    print("False")