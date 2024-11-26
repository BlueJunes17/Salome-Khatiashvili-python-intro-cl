from random import randint

def main():
    numbers_list = [str(randint(10, 1000000000)) for i in range (100)]
    shortest_num = min(numbers_list, key = len)
    longest_num = max(numbers_list, key = len)
    ascend_num = [int(n) for n in sorted(numbers_list, key = len)]
    descend_num = [int(n) for n in sorted(numbers_list, key = len, reverse = True)]

    print("Random numbers' list: ", numbers_list)
    print("The shortest number: ", shortest_num)
    print("The longest number", longest_num)
    print("The numbers ascending: ", ascend_num)
    print("The numbers descending: ", descend_num)

if __name__ == "__main__":
    main()