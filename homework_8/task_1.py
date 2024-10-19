string = input("Please, write a word: ")
letters = 'abcdefghijklmnopqrstuvwxyz'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#ანბანის სხვანაირად(უფრო მოკლე მოქმედებით) განსაზღვრა თუ შეიძლება??


for i in string:
    if i not in letters and i not in upper_letters:
        string = string.replace(i, "")

string = string.lower()

if string[0:] == string[::-1]:
    print("It is palidrome")
else:
    print("It is not palidrome")    



