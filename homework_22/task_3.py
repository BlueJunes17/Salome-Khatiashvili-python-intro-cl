class Stack:
    def __init__(self):
        # ცარიელი სია ელემენტების შესანახად
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if not self.is_empty():
            return self.elements.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.elements[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)

if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())  #true
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.size())  #3
    print(stack.peek())  #30
    print(stack.pop())   #30
    print(stack.pop())   #20
    print(stack.size())  #1
    print(stack.is_empty())  #false
    print(stack.pop())   #10
    print(stack.is_empty())  #true

    try:
        stack.pop()  
    except IndexError as e:
        print(e) 
