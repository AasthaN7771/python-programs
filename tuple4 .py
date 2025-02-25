# List of tuples containing food items and their prices
food_items = [
    ("Pizza", 12.5),
    ("Burger", 8.0),
    ("Pasta", 15.0),
    ("Salad", 7.5),
    ("Sushi", 20.0),
    ("Taco", 9.5)
]

# Sort the list in descending order by price
sorted_food_items = sorted(food_items, key=lambda x: x[1], reverse=True)

# Print the sorted list
print(sorted_food_items)
