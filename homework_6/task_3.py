positive_number = input("Please enter your number form 1 to 10000 : ")

#განვსაზღვრო დაწერილი რიცხვი და მისი შეტრიალებული ვერსია
if int(positive_number) < 1 or int(positive_number) > 10000:
    print("Your number is not right : ")
else:
    print("Your number is : ", positive_number)
    index = len(positive_number)
    reversed_number = 0 
    sum_of_numbers = 0
    print("Your reversed number is : ", end = " ")


#განვსაზღვრო დაწერილი რიცხვის ციფრების ჯამი ???? 

while  reversed_number < index:
    digit_number = positive_number[index - reversed_number - 1] #ინდექსის გამოყენების ამბავი გადავამოწმო მაინც
    if reversed_number != index - 1:
        print(digit_number, end = "")
    else:
        print(digit_number)    
    reversed_number += 1
    sum_of_numbers += int(digit_number) 
print("Your number's sum of digits : ", sum_of_numbers)       

        
    