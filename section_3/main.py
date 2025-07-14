import json

food_ratings = {1: True, 2: True, 3: False}
dumping = json.dumps(food_ratings)
print(dumping)


