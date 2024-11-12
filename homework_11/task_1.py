def temperature_converter(temperature, unit):
    if unit == "C":
        return temperature * 9/5 + 32
    elif unit == "F":
        return (temperature - 32) * 5/9 
    else:
        print("WRONG UNIT")

def main():
    print(temperature_converter(50, "F"))
    print(temperature_converter(17, "C"))
    print(temperature_converter(-47, "C"))
    print(temperature_converter(47, "F"))

if __name__ == "__main__":
    main()    