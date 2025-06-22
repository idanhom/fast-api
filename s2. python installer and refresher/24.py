# list of 5 animals
zoo = ["bear", "dog", "cat", "elephant", "kangaroo"]
print(zoo)
print(len(zoo))

# deleting third index (cat)
print(zoo.pop(2))
print(zoo)

# append new animal at end
zoo.append("pig")

print(zoo)

# delete animal at beginning (bear)
zoo.remove("bear")

# print all animals
print(zoo)

# print first three animals
print(zoo[:3])
