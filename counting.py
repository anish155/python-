word="hello how is your life"
freq={}
for letter in word:
    if letter !=" ":
        if letter in freq:
            freq[letter]+=1
        else:
            freq[letter]=1
print(freq)