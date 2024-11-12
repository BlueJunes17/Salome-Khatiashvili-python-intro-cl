from task_2 import gcd_rec

def lcm(a, b):
    return (a * b) / gcd_rec(a, b)

def main():
    number_1 = int(input("Please, enter a number from 1 to 999: "))
    if number_1 < 1 or number_1 > 999:
        print("Wrong Number")
        exit(1)
        
    number_2 = int(input("Please enter the second number from 1 to 999: "))   
    if number_2 < 1 or number_2 > 999:
        print("Wrong Number") 
        exit(1)

    print(f"LCM of {number_1} and {number_2} is {lcm(number_1, number_2)}")

if __name__ == "__main__":
    main()