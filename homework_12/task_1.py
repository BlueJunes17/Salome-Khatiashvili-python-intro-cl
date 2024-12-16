def average(temperature: list):
    return round(sum(temperature) / len(temperature), 2)  

def average_multiple(* temperature_lists: list):
    averages = []
    for temperatures in temperature_lists:
        avg = average(temperatures)
        averages.append(avg)
    return averages

def main():
    temps = 22, 25, 19, 23, 25, 26, 23

    print(f"Averages: {average_multiple(temps)}")

if __name__ == "__main__":
    main()