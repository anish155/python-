word=input("Enter the word:")
word2=input("Enter the word:")
sorted_word=sorted(word)
sorted_word2=sorted(word2)
if(sorted_word==sorted_word2):
    print("the word is annagram.")
else:
    print("the word is not annagram.")