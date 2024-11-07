def main():
    list_1 = [2, 4, 6, 8]
    list_2 = [1, 3, 5, 7, 9]
    list_3 = [17, 18, 21, 24, 47]
    print(list(map(lambda x, y, z : x + y + z, list_1, list_2, list_3)))

if __name__ == "__main__":
    main()