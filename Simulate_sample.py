import numpy as np
import datetime

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
    [70, 62, 200, 210, 300, 100, 80, 50, 55, 80, 50, 57, 40, 75, 76, 90, 315, 48, 74, 70],  # Monday
    [75, 63, 204, 212, 302, 102, 82, 51, 54, 81, 50, 57, 42, 76, 77, 92, 316, 49, 75, 72],  # Tuesday
    [78, 64, 205, 213, 303, 102, 83, 52, 54, 82, 51, 58, 42, 79, 77, 93, 316, 49, 78, 73],  # Wednesday
    [72, 63, 206, 213, 303, 103, 85, 51, 53, 81, 52, 57, 43, 79, 78, 93, 317, 50, 79, 73],  # Thursday
    [80, 65, 200, 208, 315, 104, 89, 51, 54, 79, 48, 59, 45, 85, 89, 90, 320, 42, 83, 71],  # Friday
    [110, 67, 188, 205, 340, 96, 94, 45, 49, 74, 42, 58, 47, 90, 96, 80, 340, 32, 90, 70],  # Saturday
    [125, 68, 182, 200, 350, 86, 98, 36, 49, 60, 38, 58, 49, 100, 109, 68, 350, 28, 100, 72],  # Sunday
]

# Define the standard deviation for each food item for each day of the week
std_deviation = [
    [5, 6, 4, 5, 8, 6, 5, 4, 6, 7, 9, 10, 8, 7, 10, 6, 7, 8, 7, 8],  # Monday
    [4, 5, 3, 4, 7, 5, 4, 5, 7, 8, 10, 11, 9, 8, 11, 7, 8, 9, 8, 9],  # Tuesday
    [6, 7, 5, 6, 9, 7, 6, 7, 9, 10, 8, 9, 7, 6, 9, 5, 6, 7, 6, 7],  # Wednesday
    [4, 5, 4, 5, 8, 6, 5, 6, 8, 9, 10, 11, 9, 8, 11, 7, 8, 9, 8, 9],  # Thursday
    [7, 8, 6, 7, 10, 8, 7, 8, 10, 11, 12, 14, 10, 9, 14, 8, 9, 10, 9, 10],  # Friday
    [9, 10, 8, 9, 12, 10, 9, 10, 12, 13, 11, 13, 11, 10, 13, 9, 10, 11, 10, 11],  # Saturday
    [8, 9, 7, 8, 11, 9, 8, 9, 11, 12, 10, 11, 9, 8, 11, 7, 8, 9, 8, 9]  # Sunday
]

# Convert average_orders and std_deviation to NumPy arrays
average_orders = np.array(average_orders)
std_deviation = np.array(std_deviation)

# Define the start date
start_date = datetime.date(2023, 5, 8)

# Simulate the number of orders for each food item for each day of the week
simulated_orders = np.random.normal(average_orders, std_deviation)

# Ensure that the simulated orders are non-negative
simulated_orders = np.maximum(simulated_orders, 0)

# Convert the simulated orders to integers
simulated_orders = np.round(simulated_orders).astype(int)

# Print the simulated orders for each food item for each day of the week
for day in range(len(average_orders)):
    date = start_date + datetime.timedelta(days=day)

    for i in range(len(food_items)):
        item = food_items[i]
        print(f"{item['sno']},{item['name']},{item['price']},{simulated_orders[day][i]},{date}")
    print()
