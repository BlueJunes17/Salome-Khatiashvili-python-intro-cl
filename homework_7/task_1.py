word = input("Please, enter the word: ")

for i in range (0, len(word)):
    if i % 2 == 0 and word[i] != "e":
        print(word[i], end = " ")


