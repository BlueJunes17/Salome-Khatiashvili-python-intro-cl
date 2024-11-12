"""დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს - n ,სადაც 0 < n < 50 . 
Პროგრამამ უნდა იპოვოს n მდე არსებული ყველა რიცხვის გამყოფები.
Დაბეჭდეთ მაქსიმუმ 3 ცალი გამყოფი. Მაგალითი : პროგრამამ მიიღო რიცხვი 12"""


number = int(input("please enter number from 1 to 49 : "))

if number <= 0 or number > 49:
    print('not correct')
    exit(1)

number_1 = 1
divisor = 1

while number_1 <= number:
        print(number_1, end=" - ")
        number_of_divisors = 1
        divisor = 1
        while divisor <= number_1 and number_of_divisors < 4:
            if number_1 % divisor == 0:
                if number_of_divisors !=3 and divisor != number_1:
                    print(divisor, end= " ")
                else:
                    print(divisor)
                number_of_divisors += 1
            divisor += 1
        number_1 += 1
