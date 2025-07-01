class Enemy:
    type_of_enemy: str = ""
    health_points: int = 10
    attack_damage: int = 1

    def talk(self):
        return f"I'm a {self.type_of_enemy}. Be prepared to fight."
    
    def walk_forward(self):
        return f"{self.type_of_enemy} moves closer to you."
    
    def attack(self):
        return f"{self.type_of_enemy} attacks for {self.attack_damage} damage."

    def summary(self):
        return f"{self.type_of_enemy} has {self.health_points} health points and can do an attack of {self.attack_damage}."

from enemy import Enemy

