A = input()

# Please write your code here.
def chk_alphabets(A):
    _set = set()

    for ch in A:
        _set.add(ch)
    
    if(len(_set) >= 2):
        return "Yes"
    
    return "No"

print(chk_alphabets(A))