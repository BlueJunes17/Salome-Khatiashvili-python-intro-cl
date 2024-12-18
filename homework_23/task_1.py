class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_info(self):
        return f"Name: {self._name}, Age: {self._age}"

person1 = Person("Salome", 28)
person2 = Person("Nika", 32)
person3 = Person("Anna", 25)

#თითოეული ადამიანის ინფორმაცია
print(person1.get_info())
print(person2.get_info())
print(person3.get_info())
