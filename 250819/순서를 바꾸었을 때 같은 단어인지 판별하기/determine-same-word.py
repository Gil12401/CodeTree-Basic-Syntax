word1 = input()
word2 = input()

# Please write your code here.
# Please write your code here.
def chk_same_alphabets(word1,word2):
    sorted_wordA = sorted(word1)
    sorted_wordB = sorted(word2)
    if(sorted_wordA == sorted_wordB):
        return "Yes"

    return "No"

print(chk_same_alphabets(word1,word2))