word_list = ["esa", "mesa", "gadis", "esa", "shinamanikeni sanamanikena"]

def filtered():
    new_word_list = [i.upper() for i in word_list if len(i) <= 3]
    return new_word_list

def main():
    print("Original words: ", word_list)
    print("Filtered Words: ", filtered())

if __name__ == "__main__":
    main()
