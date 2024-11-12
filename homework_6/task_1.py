from random import randint


computer_number = randint(0,100)

attempt = 0

while attempt <= 10:
    user_input = int(input("Guess the number : "))
    if user_input > computer_number:
        print("HIGH")
    elif user_input < computer_number:
        print("LOW")
    else:
        print("YOU ARE THE WINNER")    
        break 
if attempt > 10:
    print("COMPUTER IS THE WINNER")    