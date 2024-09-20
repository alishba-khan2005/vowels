word=input()
print(word)
vowels=("a","e","i","o","u","A","E","I","O","U")
result=""
for letter in word:
    if letter not in vowels:
        result+=letter
print(result)

