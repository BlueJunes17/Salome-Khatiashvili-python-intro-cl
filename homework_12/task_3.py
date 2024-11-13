import random

def random_list_generator():
    random_list = list()

    for i in range(50):
        random_list.append(random.randint(1, 30))

    new_list = []

    for e in random_list:
        if e not in new_list:
            new_list.append(e)
    return new_list

def main():
    result = random_list_generator()
    print("List - ", result)
    print("Length - ", len(result))


if "__main__" == __name__:
    main()