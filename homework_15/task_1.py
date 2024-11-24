import random

random_numbers = [random.randint(1, 100) for _ in range(100)]

sum_number = {"even": sum(1 for num in random_numbers if num % 2 == 0), "odd": sum(1 for num in random_numbers if num % 2 != 0)}

print("Generated numbers:", random_numbers)
print("Sum:", sum_number)
