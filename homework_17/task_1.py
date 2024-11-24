# ჩვეულებრივი ფუნქცია
def generate_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:  # თუ ლუწია
            n //= 2
        else:  # თუ კენტია
            n = 3 * n + 1
    sequence.append(1) 
    return sequence

# ქეშირებით ფუნქცია
cache = {}

def generate_sequence_cached(n):
    if n in cache:  
        return cache[n]
    
    original_n = n
    sequence = []
    while n != 1:
        if n in cache:  # თუ ქეშში შეხვდა შუალედური მნიშვნელობა
            sequence.extend(cache[n])
            break
        sequence.append(n)
        if n % 2 == 0:  # თუ ლუწია
            n //= 2
        else:  # თუ კენტია
            n = 3 * n + 1
    
    sequence.append(1)  
    cache[original_n] = sequence  
    return sequence


while True:
    try:
        n = int(input("შეიყვანეთ დადებითი მთელი რიცხვი: "))
        if n <= 0:
            print("გთხოვთ, შეიყვანეთ დადებითი რიცხვი")
            continue
        break
    except ValueError:
        print("შეყვანილი მონაცემი არ არის რიცხვი. სცადეთ ისევ.")


print("ჩვეულებრივი ფუნქცია:", generate_sequence(n))
print("ქეშირებით ფუნქცია:", generate_sequence_cached(n))
print("ქეშის მდგომარეობა:", cache)
