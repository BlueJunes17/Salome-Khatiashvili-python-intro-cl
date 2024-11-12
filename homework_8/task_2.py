first_string = input("Please, enter the first word: ").strip().lower()
second_string = input("Please, enter the second word: ").strip().lower()
output = "YES"

if len(first_string) != len(second_string):
    output = "NO"
else:    
    for i in first_string:
        if first_string.count(i) != second_string.count(i):
            output = "NO"
        break #დაამთავროს შემოწმება თუ არ დაემთხვა

print(output)            