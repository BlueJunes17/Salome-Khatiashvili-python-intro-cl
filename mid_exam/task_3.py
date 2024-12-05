# (12 ქულა) Დაწერეთ თამაში rock, paper, scissor.
# Დაწერეთ ფუნქცია რომელიც დააგენერირებს შემთხვევითად ერთ-ერთ სიმბოლოს ჩამოთვლილი სამიდან R,P,S.
# Დაწერეთ მეორე ფუნქცია main, რომელშიც მომხმარებელს შეაყვანინებთ თავის არჩევანს R, P ან S.
# სიმარტივისთვის შეგიძლიათ უგულებელყოთ ყველა შემოწმება მომხმარებლის ინფუთზე.
# Შეადარეთ ერთმანეთს მომხმარებლის შემოყვანილი სიმბოლო და თქვენი ფუნქციის დაგენერირებული სიმბოლო და გამოავლინეთ გამარჯვებული.
# Წესები: R ამარცხებს S, S ამარცხებს P, P ამარცხებს R
# P P, R R, S S არის ფრე იმ შემთხვევაში თუ გვაქვს ფრე, უნდა მისცეთ კიდევ ერთი თამაშის საშუალება.

import random

def randomsymbol():
    choices = ["R", "P", "S"]
    computer_choice = random.choice(choices)
    return computer_choice

def main():
    while True:
        player_choice = input("Please, enter your choice from - R, P or S: ")
        print(f"You chose {player_choice}")
        computer_choice = randomsymbol()
        print(f"Computer chose {computer_choice}")
        if player_choice == computer_choice:
            print("It's a draw! Try again!")
            continue
        else:
            break

    if player_choice == "R":
        if computer_choice == "S":
            print("You win! R beats S")
        elif computer_choice == "P":
            print("You Lose! P beats R")    
    elif player_choice == "P":
        if computer_choice == "R":
            print("You win! P beats R")        
        elif computer_choice == "S":
            print("You lose! S beats P")
    elif player_choice == "S":
        if computer_choice == "P":
            print("You win! S beats P")        
        elif computer_choice == "R":
            print("You lose! R beats S")

main()


