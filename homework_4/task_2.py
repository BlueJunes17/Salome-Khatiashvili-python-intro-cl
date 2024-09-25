import random

# დავწეროთ პროგრამა, რომელიც მიიღებს მთელ დადებით რიცხვს n
n = 100 #ეს უნდა იყოს 0-დან 30-მდე

while n > 30 or n < 0:
    n = int(input("Enter positive number between 0 and 30: "))

# დააგენერიროს n ცალი შემთხვევითი მთელი რიცხვი 0 - 1000 დიაპაზონიდან
random_number_list = []
for i in range(1, n+1):
    random_number = random.randint(0, 1000)
    random_number_list.append(random_number)
    # print(random_number_list)

# დაითვალოს მაქსიმალური და დაბეჭდოს
# print(random_number_list)
print(max(random_number_list))


