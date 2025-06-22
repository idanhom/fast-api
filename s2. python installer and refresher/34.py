my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

# Print all keys and values
for key, value in my_vehicle.items():
    print(f"{key}: {value}")

# Create a copy
vehicle2 = my_vehicle.copy()

# Add new key
vehicle2['number_of_tires'] = 4

# Remove mileage
vehicle2.pop('mileage')

# Print keys only
print(vehicle2.keys())
