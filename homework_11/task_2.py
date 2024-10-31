a = int(input("Please, enter nummber a: "))
b = int(input("Please, enter number b: "))

if a <= 0 or a > 10000 or b <= 0 or b > 10000:
        print("Invalid Input")
        exit(1)


def gcd_rec(a, b):
    if b == 0:
        return a 
    return gcd_rec(b, a % b)

def gcd_iter(a, b):
    m = min(a, b)
    while m > 0:
        if a % m == 0 and b % m == 0:
            return m 
        m -= 1
    return m     

def main():
     print(f"GCD of {a} and {b} is {gcd_rec(a, b)}")
     print(f"GCD of {a} and {b} is {gcd_iter(a, b)}")

if __name__ == "__main__":
     main()