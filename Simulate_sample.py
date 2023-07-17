import numpy as np

# Define the food items with their serial numbers, names, and current prices
food_items = [
    {"sno": 1, "name": "Biryani", "price": 150},
    {"sno": 2, "name": "Shawarma", "price": 120},
    {"sno": 3, "name": "Appam", "price": 30},
    {"sno": 4, "name": "Dosa", "price": 70},
    {"sno": 5, "name": "Paratha", "price": 40},
    {"sno": 6, "name": "Samosa", "price": 20},
    {"sno": 7, "name": "Chicken Curry", "price": 140},
    {"sno": 8, "name": "Paneer Tikka", "price": 180},
    {"sno": 9, "name": "Mutton Biryani", "price": 250},
    {"sno": 10, "name": "Rasam", "price": 70},
    {"sno": 11, "name": "Palak Paneer", "price": 160},
    {"sno": 12, "name": "Fried Rice", "price": 130},
    {"sno": 13, "name": "Gulab Jamun", "price": 80},
    {"sno": 14, "name": "Chicken 65", "price": 160},
    {"sno": 15, "name": "Butter Chicken", "price": 200},
    {"sno": 16, "name": "Veg Meals", "price": 110},
    {"sno": 17, "name": "Chappathi", "price": 50},
    {"sno": 18, "name": "Aloo Gobi", "price": 140},
    {"sno": 19, "name": "Kadai Chicken", "price": 200},
    {"sno": 20, "name": "Fish Curry", "price": 140}
]

# Define the average number of orders for each food item for each day of the week
average_orders = [
    [30, 35, 20, 25, 40, 35, 30, 25, 35, 40, 50, 60, 45, 40, 60, 35, 45, 50, 45, 50],  # Monday
    [25, 30, 15, 20, 35, 30, 25, 30, 35, 40, 55, 65, 50, 45, 65, 40, 50, 55, 50, 55],  # Tuesday
    [35, 40, 25, 30, 45, 40, 35, 40, 45, 50, 40, 50, 35, 30, 50, 25, 35, 40, 35, 40],  # Wednesday
    [40, 45, 30, 35, 50, 45, 40, 45, 50, 55, 45, 55, 40, 35, 55, 30, 40, 45, 40, 45],  # Thursday
    [50, 55, 40, 45, 60, 55, 50, 55, 60, 65, 55, 65, 50, 45, 65, 40, 50, 55, 50, 55],  # Friday
    [60, 65, 50, 55, 70, 65, 60, 65, 70, 75, 65, 75, 60, 55, 75, 50, 60, 65, 60, 65],  # Saturday
    [45, 50, 35, 40, 55, 50, 45, 50, 55, 60, 50, 60, 45, 40, 60, 35, 45, 50, 45, 50]   # Sunday
]

# Define the standard deviation for each food item for each day of the week
std_deviation = [
    [5, 6, 4, 5, 8, 6, 5, 4, 6, 7, 9, 10, 8, 7, 10, 6, 7, 8, 7, 8],   # Monday
    [4, 5, 3, 4, 7, 5, 4, 5, 7, 8, 10, 11, 9, 8, 11, 7, 8, 9, 8, 9],   # Tuesday
    [6, 7, 5, 6, 9, 7, 6, 7, 9, 10, 8, 9, 7, 6, 9, 5, 6, 7, 6, 7],   # Wednesday
    [4, 5, 4, 5, 8, 6, 5, 6, 8, 9, 10, 11, 9, 8, 11, 7, 8, 9, 8, 9],   # Thursday
    [7, 8, 6, 7, 10, 8, 7, 8, 10, 11, 12, 14, 10, 9, 14, 8, 9, 10, 9, 10],  # Friday
    [9, 10, 8, 9, 12, 10, 9, 10, 12, 13, 11, 13, 11, 10, 13, 9, 10, 11, 10, 11], # Saturday
    [8, 9, 7, 8, 11, 9, 8, 9, 11, 12, 10, 11, 9, 8, 11, 7, 8, 9, 8, 9]   # Sunday
]

# Convert average_orders and std_deviation to NumPy arrays
average_orders = np.array(average_orders)
std_deviation = np.array(std_deviation)

# Simulate the number of orders for each food item for each day of the week
simulated_orders = np.random.normal(average_orders, std_deviation)

# Ensure that the simulated orders are non-negative
simulated_orders = np.maximum(simulated_orders, 0)

# Convert the simulated orders to integers
simulated_orders = np.round(simulated_orders).astype(int)

# Print the simulated orders for each food item for each day of the week
for day in range(len(average_orders)):
    print(f"Day {day+1}:")
    for i in range(len(food_items)):
        item = food_items[i]
        print(f"{item['sno']}: {item['name']} - {item['price']} | Orders: {simulated_orders[day][i]}")
    print()
