letter=input("enter the word:").lower()
freq={}
for word in letter:
    if word != " ":
        freq[word]=freq.get(word,0)+1

print("word frequencies:")
for word,count in freq.items():
    print(f"{word}:{count}")

