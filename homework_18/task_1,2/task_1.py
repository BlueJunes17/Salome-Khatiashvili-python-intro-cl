def process_purchases(homework_18):
    try:
        with open(homework_18, 'r') as data_file, \
             open('small.txt', 'w') as small_file, \
             open('high.txt', 'w') as high_file:

            for line in data_file:
                line = line.strip()  # Remove leading/trailing whitespace
                if not line:  # Skip empty lines
                    continue

                try:
                    # Parse the line
                    user_name, product_name, amount, price = line.split(',')
                    amount = float(amount)  # Convert amount to float
                    price = float(price)    # Convert price to float
                    total_cost = amount * price  # Calculate total cost

                    # Write to the appropriate file based on the cost
                    if total_cost < 10:
                        small_file.write(line + '\n')
                    else:
                        high_file.write(line + '\n')

                except ValueError:
                    print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print(f"File '{homework_18}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the function
process_purchases('data.txt')
