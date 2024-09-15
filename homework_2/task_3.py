number = int(input(" Enter number from 1 to 10: "))

if number <= 1 or number > 10 :
    print(" WRONG ")
    exit(1)

else :
    if number % 2 == 0 and number % 3 == 0 :
        print(" 2,3 ")    
    elif number % 2 == 0 and number % 3 != 0 and number % 5 != 0 :  
        print(" 2 ")      
    elif number % 2 == 0 and number % 5 == 0 :
        print(" 2,5 ")    
    elif number % 3 == 0 and number % 2 != 0 :
        print(" 3 ")    
    elif number % 5 == 0 and number % 2 != 0 :
        print (" 5 ")    
    else :
        print(" 7 ")  
