from random import uniform
from math import sqrt

number = int(input("Please, enter the number more than 1: "))

if number <= 1:
    print("Wrong number, try again!")
    exit(1)

i = 0
counter = 0

while i <= number:
    number_a = uniform(0, 1)
    number_b = uniform(0, 1)
    while number_a == 0:
        number_a = uniform(0,1) 
    while number_b == 0:
        number_b = uniform(0,1)
    if sqrt(number_a ** 2 + number_b ** 2) <= 1:
        counter += 1
    i += 1

final_number = counter * 4 / number

print(final_number)