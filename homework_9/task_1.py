number = int(input("Please, enter a number more than 1 : "))

if number <= 1:
    print("Wrong number, try again!")
    exit(1)
else:
     x = 0
     for i in range(number):
         denom = 2 * i + 1 # კენტი რიცხვებისთვის
         
         if i % 2 == 0:
             x += 1 / denom
         else:
             x -= 1 / denom          

x = x * 4

print(x)

              
