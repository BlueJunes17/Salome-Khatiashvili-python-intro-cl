word_input = input("Please, write any word: ")

count = {}
for character in word_input:
    count[character] = count.get(character, 0) + 1

for character, count in count.items():
    print(f"{character} – {count}")