class pangram():
    def word(self):
        letter=input("enter the word:")
        return letter.lower()
    def check_pangram(self,sentence):
        alphabets="abcdefghijklmnopqrstuvwxyz"
        for char in alphabets:
            if  char not in sentence:
                print("the sentence is not a pangram.")
                return            
        print("the word is a pangram.")
        
p=pangram()
word=p.word()
p.check_pangram(word)