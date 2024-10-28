def is_prime(number):
    output = "TRUE"
    if number % 1 !=0 or number <=1:
        output = "FALSE"
    else:
        for i in range(2, number):
            if number % i == 0:
                output = "FALSE"    
                break
    return output
        
print(is_prime(17))
print(is_prime(121))
