text = input()
pattern = input()

# Please write your code here.
def get_index_of_substr(text, pattern):
    for i in range(len(text)):
        if(text[i] == pattern[0]):
            begin = i
            end = min(len(text), begin + len(pattern))
            tmp_substr = text[begin:end]
            # print("tmp_substr",tmp_substr)
            if(tmp_substr == pattern):
                return i
    return -1
    

print(get_index_of_substr(text, pattern))