def take():
    word=input("Enter the number:")
    return word

def count(word):
    vowel="aeiouAEIOU"
    vowel_count=0
    for letter in word:
        if letter in vowel:
            vowel_count+=1
    return vowel_count

letter=take()
print(f"The word '{letter}' has {count(letter)} vowels.")