A = input()

# Please write your code here.
# TODO. 공백 제거, 대소문자 구분 
def chk_palindrome(A):
    rev = A[::-1]
    if (A == rev):
        return "Yes"
    
    return "No"
    
print(chk_palindrome(A))