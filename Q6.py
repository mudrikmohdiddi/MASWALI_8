"""6. Write a function find_longest_word()
that takes a list of words and returns the length of the longest one."""

def longest_word(word):
    list=word.split(",")
    large=0
    word_large=""
    for i in list:
        if(large<len(i)):
           large=len(i)
           word_large=i
    return f"The longest word is {word_large} at length of {large}"
def main():
    word=input("Please enter list of word:")
    for i in word:
        if(i.isdecimal()):
            number=i
    while((" " in word)==True or ("," in word)==False):
        print("You enter invalid input, please try angain")
        word=input("Please enter list of word:")
    print(longest_word(word))
main()

    

