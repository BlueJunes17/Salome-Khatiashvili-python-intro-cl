word = input("Please, enter the word: ")

for i in word:
    if i not in "aeiou":
        print(i, end = " ")