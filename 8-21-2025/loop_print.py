class Printer:
    def __init__(self):
        self.__word=None
    
    def take(self):
        self.__word=input("Enter your word:")
    
    def loop_print(self):
        word=self.__word.replace(" ","")
        for x in range(1,len(word)+1):
            print(word[:x])
    
p=Printer()
p.take()
p.loop_print()

    
