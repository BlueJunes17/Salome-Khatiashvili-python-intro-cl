import random

# მივიღოთ მოთამაშეების რაოდენობა
number_of_players = int(input("Enter number of players: "))

for i in range(1, number_of_players+1):
    random_number1 = random.randint(1, 6)
    random_number2 = random.randint(1, 6)

    # დაპრინტე
    print(random_number1, random_number2)

