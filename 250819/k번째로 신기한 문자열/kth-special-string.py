n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
def chk_substr(string, pattern):
    result = False
    compare_count = len(string) - len(pattern) + 1 
    for i in range(compare_count):
        _substr = string[i:i+len(pattern)]
        if(_substr == pattern):
            result = True
    
    return result

def get_sorted_substr_list(str):
    sorted_substr = []
    sorted_str = sorted(str)

    for word in sorted_str:
        if(chk_substr(word, t)):
            sorted_substr.append(word)
    
    return sorted_substr

_sorted_substr = get_sorted_substr_list(str)
print(_sorted_substr[k-1])


        

    