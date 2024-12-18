import json
from collections import defaultdict

def load_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File {filename} not found. Please check the path and try again.")
        exit(1)


def find_stores_for_recipe(recipe_name, recipes, markets):
    needed_ingredients = set(recipes[recipe_name]["ingredients"])
    market_ingredients = {market: set(items) for market, items in markets.items()}
    
    #შევამოწმოთ ყველა ინგრედიენტი ხელმისაწვდომია თუ არა
    all_available = set.union(*market_ingredients.values())
    if not needed_ingredients.issubset(all_available):
        return None  #თუ ინგრედიენტი არ მოიძებნა
    
    #ინგრედიენტების მინიმალური მაღაზიებით შეძენა
    stores_to_visit = []
    remaining_ingredients = needed_ingredients.copy()
    while remaining_ingredients:
        best_store = max(market_ingredients, key=lambda m: len(remaining_ingredients & market_ingredients[m]))
        stores_to_visit.append(best_store)
        remaining_ingredients -= market_ingredients[best_store]
    
    return f"'To prepare {recipe_name} you need to go to these stores: {', '.join(stores_to_visit)}"

#რეცეპტის არჩევა
def get_valid_recipe_name(recipes):
    recipe_names = {name.lower(): name for name in recipes} 
    while True:
        recipe_name_input = input("Which dish do you want to prepare? ").strip().lower()
        if recipe_name_input in recipe_names:
            return recipe_names[recipe_name_input]  #lower case-ში დაწერის შემთხვევაში მაინც რომ წაიკითხოს კერძის სახელი და upper-ში დაგვიბრუნოს
        else:
            print(f"We don't have {recipe_name_input.title()}'s recipe in out list. Try again. \n")


if __name__ == "__main__":
    recipes_file = "recipes.json"
    markets_file = "markets.json"
    
    recipes = load_data(recipes_file)
    markets = load_data(markets_file)
    
    while True:
        #რეცეპტის სახელის მოთხოვნა
        recipe_name = get_valid_recipe_name(recipes)
        
        #მაღაზიების პოვნა
        result = find_stores_for_recipe(recipe_name, recipes, markets)
        
        if result:
            print(result)
            break 
        else:
            print(f"We can't find ingredients for {recipe_name}. Try another dish.\n")
