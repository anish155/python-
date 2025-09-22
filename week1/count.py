# word='the man who is the young is the the the the'
# count=0
# for x in word.split(" "):
#     if x=='the':
#         count+=1
# print(count)

class counter:
    def Take(self):
        senmtence=input("Enter the sentences:")
        return senmtence
    
    def count(self,letters):
        count=0
        for x in letters.split(" "):
            if x:
                count+=1
        print(count)


counting=counter()
words=counting.Take()
counting.count(words)