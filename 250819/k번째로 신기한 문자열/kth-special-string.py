n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
def chk_start_with_T(string, pattern): 
    if len(string) < len(pattern):
        return False

    for i in range(len(pattern)):
        if(string[i] != pattern[i]):
            return False

    return True

def get_sorted_substr_list(str):
    sorted_substr = []
    sorted_str = sorted(str)

    for word in sorted_str:
        if(chk_start_with_T(word, t)):
            sorted_substr.append(word)
    
    return sorted_substr

_sorted_substr = get_sorted_substr_list(str)
print(_sorted_substr[k-1])