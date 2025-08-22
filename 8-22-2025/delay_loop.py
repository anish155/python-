import time
class Printer:
    def __init__(self):
        self.__word=None
    
    def take(self):
        self.__word=input("Enter your word:")
    
    def loop_print(self,delay=0.5):
        
        for x in range(1,len(self.__word)+1):
            print(self.__word[:x])
            time.sleep(delay)
    
p=Printer()
p.take()
p.loop_print()
