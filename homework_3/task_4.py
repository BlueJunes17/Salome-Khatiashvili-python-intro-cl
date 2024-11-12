import random

colour_list = ["clubs", "diamonds", "hearts", "spades"]
randcolour = random.choice(colour_list)

#print(randcolour)

number_list = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
randnumber = random.choice(number_list)

#print(randnumber)

print(randcolour, "-", randnumber)