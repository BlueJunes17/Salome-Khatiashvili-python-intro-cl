#(5 ქულა) Დაწერეთ პროგრამა რომელიც მომხმარებელს მოსთხოვს შეიყვანოს შემდეგი მონაცემები: სახელი, გვარი, ასაკი და ქალაქი.
# Ეს ინფორმაცია Პროგრამამ ეკრენზე უნდა დაბეჭდოს შემდეგ ფორმატში: Hello სახელი გვარი. Age: ასაკი. City: ქალაქი.

name = input("Please, enter your name: ")
surname = input("Please, enter your surname: ")
age = input("Please, enter your age: ")
city = input("Please, enter your city:")

print(f"Hello {name} {surname}")
print(f"Age: {age}")
print(f"City: {city}")