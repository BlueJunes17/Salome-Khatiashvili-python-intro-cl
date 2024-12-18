class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_info(self):
        return f"Name: {self._name}, Age: {self._age}"

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited: {amount}, New Balance: {self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            print("საკმარისი თანხა არ არის")
        else:
            self._balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self._balance}")

    def get_balance(self):
        return self._balance


person1 = Person("Salome", 28)
person2 = Person("Nika", 32)
person3 = Person("Anna", 25)


print(person1.get_info())
print(person2.get_info())
print(person3.get_info())


account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
print(f"Final Balance: {account.get_balance()}")
