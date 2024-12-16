class Queue:
    def __init__(self):
        self.elements = []

    def insert(self, element):
        self.elements.append(element)

    def pop(self):
        if self.elements:
            return self.elements.pop(0)
        else:
            raise IndexError("სია ცარიელია")


if __name__ == "__main__":
    q = Queue()
    q.insert(1)
    q.insert(2)
    q.insert(3)
    print(q.pop())  #1
    print(q.pop())  #2
    print(q.pop())  #3

    try:
        print(q.pop()) 
    except IndexError as e:
        print(e)  
