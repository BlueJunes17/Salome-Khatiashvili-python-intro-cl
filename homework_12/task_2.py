import random 

random_list = list()
new_list = []

for i in range (50):
    random_list.append(random.randint(1, 30))

for e in random_list:
    for y in range(e):
        new_list.append(e)

print("List -", new_list)        
print("Length - ", len(new_list))

