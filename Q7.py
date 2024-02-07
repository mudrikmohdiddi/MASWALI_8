"""7. Write a function filter_long_words() that takes a list of words and
an integer n and returns the list of words that are longer than n."""

def long_words(word,integer):
    long_word=[]
    list=word.split(",")
    for i in list:
        if(len(i)>integer):
            long_word.append(i)
    return f"List of words that are longer than {integer} length of string is {long_word}"
def true_integer(number):
    try:
        intege=int(number)
        return True
    except ValueError:
        return False
def main():
    word=input("Please enter list of word:")
    number=""
    while((" " in word) or ("," not in word)):
        print("You enter invalid input, please try angain")
        word=input("Please enter list of word:")
    integer=input("Please enter integer:")
    while(true_integer(integer)==False):
        print("You enter wrong input, try again")
        integer=input("Please enter integer:")
    print(long_words(word,int(integer)))
main()
        
            
