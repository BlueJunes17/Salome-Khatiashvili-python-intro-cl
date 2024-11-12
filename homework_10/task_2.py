def maximum(*args):
    result = args[0]
    for i in args:
        if i > result:
            result = i
    return result

print(maximum(2,3,4), maximum(17, 24, 89),)     
print(maximum(17, 27, 374), maximum(743, 117, 2567))   