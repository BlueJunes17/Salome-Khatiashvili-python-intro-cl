input_number = int(input("please enter number from  1 to 49 : "))
if input_number <= 0 or input_number > 49:
    print("not correct")
    exit(1)

for number_of_lines in range(input_number + 1 ):
   if number_of_lines == input_number:
        for leaves in range(number_of_lines):
            print(" ", end= "")
        print("|")
   else:
        for leaves in range(input_number- number_of_lines):
            print(" ", end= "")
        for leaves in range(number_of_lines):
            print("/", end= "")
        if number_of_lines == 0:
            print("*")
        else:
            print("|", end= "")
        for leaves in range(number_of_lines):
            if leaves == number_of_lines - 1:
                print("\\",)
            else:
                print("\\", end= "")