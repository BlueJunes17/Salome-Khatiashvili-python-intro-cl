import json
from collections import defaultdict

def process_sales(homework_18):
    try:
        user_purchase_counts = defaultdict(int)
        user_total_values = defaultdict(float)  
        product_counts = defaultdict(int)  
        total_purchase_values = 0  
        total_quantities = 0  
        total_purchases = 0  

        
        with open(homework_18, 'r') as data_file:
            for line in data_file:
                line = line.strip()
                if not line:  #თავისუფალი ხაზები რომ გამოტოვოს
                    continue

                try:
                    
                    user_name, product_name, amount, price = line.split(',')
                    amount = int(amount)
                    price = float(price)
                    total_cost = amount * price

                    #სტატისტიკის განახლება
                    user_purchase_counts[user_name] += amount
                    user_total_values[user_name] += total_cost
                    product_counts[product_name] += amount
                    total_purchase_values += total_cost
                    total_quantities += amount
                    total_purchases += 1
                except ValueError:
                    print(f"Skipping invalid line: {line}")

        #ყველაზე მეტი შესყიდვის მქონე მომხმარებელი(რაოდენობით)
        max_purchase_quantity = max(user_purchase_counts.values(), default=0)
        max_purchase_users = [user for user, count in user_purchase_counts.items() if count == max_purchase_quantity]

        #ყველაზე მეტი შესყიდვის მქონე მომხმარებელი(ჯამური ღირებულება)
        max_total_value = max(user_total_values.values(), default=0)
        max_value_users = [user for user, value in user_total_values.items() if value == max_total_value]

        #ყველაზე გაყიდვადი პროდუქტები
        max_sold_quantity = max(product_counts.values(), default=0)
        max_sold_products = [product for product, count in product_counts.items() if count == max_sold_quantity]

        #საშუალო
        avg_purchase_value = total_purchase_values / total_purchases if total_purchases > 0 else 0
        avg_purchase_quantity = total_quantities / total_purchases if total_purchases > 0 else 0

        #dictionary
        stats = {
            "max_purchase_users_by_quantity": max_purchase_users,
            "max_purchase_users_by_value": max_value_users,
            "avg_purchase_value": avg_purchase_value,
            "avg_purchase_quantity": avg_purchase_quantity,
            "most_sold_products": max_sold_products
        }

        
        with open('stats.json', 'w') as json_file:
            json.dump(stats, json_file, indent=4)

        print("Statistics written to stats.json successfully.")

    except FileNotFoundError:
        print(f"File '{homework_18}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



process_sales('data.txt')
