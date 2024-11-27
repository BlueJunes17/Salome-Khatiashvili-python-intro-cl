
def midpoint(x1, y1, x2, y2):
    x_midpoint = (x1+x2)/2
    y_midpoint = (y1+y2)/2
    return (x_midpoint, y_midpoint)


def main():
    print(midpoint(1,2,4,5))
    print(midpoint(7,9,12,15))
    print(midpoint(17,42,34,25))
    print(midpoint(69,11,18,3))

main()