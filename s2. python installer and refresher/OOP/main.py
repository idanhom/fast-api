from enemy import Enemy

zombie = Enemy()
zombie.type_of_enemy = "Zombie"

print(zombie.talk())
print(zombie.walk_forward())
print(zombie.attack())

print(zombie.summary())