# Superhero Base Class
class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.level = level

    def display_info(self):
        print(f"{self.name} ⚡️ | Power: {self.power} | Level: {self.level}")

    def attack(self):
        print(f"{self.name} uses {self.power}!")


class FlyingHero(Superhero):
    def attack(self):
        print(f"{self.name} swoops from the sky with {self.power}!")

class StrongHero(Superhero):
    def attack(self):
        print(f"{self.name} smashes with super strength of level {self.level}!")

hero1 = FlyingHero("SkyBolt", "Wind Slash", 5)
hero2 = StrongHero("Titan", "Super Strength", 8)

hero1.display_info()
hero1.attack()
hero2.display_info()
hero2.attack()

print("\n--- Polymorphism Challenge ---")


# Polymorphism Challenge: Vehicles with different move() methods
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    # def move(self):
    #     print("Sailing 🚤")


# Test polymorphism
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
