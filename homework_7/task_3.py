word = input("Please, enter the word: ")
length= len(word)
counter = 0

if length % 2 == 0:
    middle_letter = word[(length // 2) - 1] + word[(length // 2)]
else:
    middle_letter = word[(length // 2)]

while counter < 5:
    print(word[1], middle_letter, word[-1])
    counter += 1    