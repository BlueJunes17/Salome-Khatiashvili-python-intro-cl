class Inset:
    def __init__(self):
        self.elements = []

    def insert(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def member(self, element):
        return element in self.elements

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
        else:
            raise ValueError("ვერ ვიპოვე")

    def __str__(self):
        return str(sorted(self.elements))


if __name__ == "__main__":
    inset = Inset()
    inset.insert(5)
    inset.insert(3)
    inset.insert(5)  #დუბლირებული ელემენტი რომ არ დაემატოს
    print(inset)

    print(inset.member(3))  #true
    print(inset.member(7))  #alse

    inset.remove(3)
    print(inset)  

    try:
        inset.remove(7)  
    except ValueError as e:
        print(e)  #"ვერ ვიპოვე"
