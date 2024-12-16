class ExtendedList(list):
    def min(self):
        if not self:
            raise ValueError("სიაში მინიმალური მნიშნელობა ვერ მოიძებნა - სია ცარიელია")
        return min(self)

    def max(self):
        if not self:
            raise ValueError("სიაში მაქსიმალური მნიშნელობა ვერ მოიძებნა - სია ცარიელია")
        return max(self)


if __name__ == "__main__":
    elist1 = ExtendedList([5, 3, 9, 1])
    elist2 = ExtendedList([10, 20, 30, 40])
    elist3 = ExtendedList([])  #ცარიელი სია

    
    print("ლისთ #1 მინიმუმი:", elist1.min())  #1
    print("ლისთ #1 მაქსიმუმი:", elist1.max())  #9

    print("ლისთ #2 მინიმუმი:", elist2.min())  #10
    print("ლისთ #2 მაქსიმუმი:", elist2.max())  #40

    try:
        print("ლისთ #3 მინიმუმი:", elist3.min())
    except ValueError as e:
        print(e)  

    try:
        print("ლისთ #3 მაქსიმუმი:", elist3.max())
    except ValueError as e:
        print(e)  
