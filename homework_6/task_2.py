
positive_number = int(input("Please enter your number from 1 to 1000 : "))



if positive_number < 1 or positive_number > 1000:
    print("Your number is not right")
else:
    print(positive_number, end = " ") 
    while positive_number != 1:
        if positive_number % 2 == 0:
            positive_number = int(positive_number/2)
            print(positive_number, end = " ")
        elif positive_number % 2 != 0:   #2ზე გაყოფადი 
            positive_number = positive_number * 3 + 1 #3ზე მრავლდებოდეს +1
            print(positive_number, end = " ")    