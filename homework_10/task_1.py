def vowels(text):
    vowel = 'aeiouyAEIOUY'
    counter = 0
    for i in text:
        if i in vowel:
            counter += 1
    return counter


print(vowels("shinamanikeni sanamanikena"))
print(vowels("dUrurum dururAm"))