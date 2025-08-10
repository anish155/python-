def take_sent():
    sentence=input("Enter the sentence:")
    return sentence

def removing(word):
    punctuations=",./';:!|$@#&?"
    result=""
    for char in word:
        if char not in punctuations:
            result+=char
    return result

sentence = take_sent()
print("Sentence without punctuation:", removing(sentence))