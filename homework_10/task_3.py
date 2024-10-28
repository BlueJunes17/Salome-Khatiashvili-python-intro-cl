def factorial(a):
    if not isinstance(a, int)or a < 0:
        return
    b = 1
    for i in range(2, a + 1):
        b *= i
    return b

print(factorial(17))
print(factorial(-47))    