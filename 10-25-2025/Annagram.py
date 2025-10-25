class Annagram:
    def __init__(self):
        self.word1=None;
        self.word2=None;

    def Input(self):
        self.word1=input("Enter the first word:")
        self.word2=input("Enter the second word:")

    def Check(self):
        reversed_word1=self.word1[::-1]
        reversed_word2=self.word2[::-1]

        if reversed_word1==self.word2 and reversed_word2==self.word1:
            print("the word ", self.word1," is a Annagram to ",self.word2)
        
        else:
            print("the word ", self.word1," is not a Annagram to ",self.word2)

an=Annagram()
an.Input()
an.Check()