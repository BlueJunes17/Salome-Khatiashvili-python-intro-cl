def process_purchases(homework_18):
    try:
        with open(homework_18, 'r') as data_file, \
             open('small.txt', 'w') as small_file, \
             open('high.txt', 'w') as high_file:

            for line in data_file:
                line = line.strip()  #ვაითსფეისების ამოღება
                if not line:  #ცარიელი ხაზები რომ გამოტოვოს
                    continue

                try:
                    user_name, product_name, amount, price = line.split(',')
                    amount = float(amount)  
                    price = float(price)    
                    total_cost = amount * price  #მთლიანი ღირებულების გამოთვლა

                    
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



process_purchases('data.txt')
