"""sentence="python is fun"
for x in sentence.split(" "):
    print(x)"""
'''sentence="python is fun"
new_sentence = sentence.replace(" ", "_")
print(new_sentence)'''

# sentence="python is fun"
# for x in sentence.split(" "):
#     print(x[::-1])

def Take():
    sentence=input("Enter the word:")
    return sentence

def Replacing(words):
    new_word=words.replace(" ","_")
    print(new_word)

words=Take()
Replacing(words)