class BeeEleph:
    def __init__(self, bee, elephant):
        self.bee_part = max(0, min(100, bee))
        self.elephant_part = max(0, min(100, elephant))

    def fly(self):
        return self.bee_part >= self.elephant_part

    def trumpet(self):
        return "tu-tu-doo-doo" if self.elephant_part >= self.bee_part else "wzzzz"

    def eat(self, meal, value):
        if meal not in ["nectar", "grass"]:
            raise ValueError("Есть только 'nectar' или 'grass'")

        if meal == "nectar":
            self.bee_part = max(0, min(100, self.bee_part + value))
            self.elephant_part = max(0, min(100, self.elephant_part - value))
        else:
            self.bee_part = max(0, min(100, self.bee_part - value))
            self.elephant_part = max(0, min(100, self.elephant_part + value))

creature = BeeEleph(30, 70)
print(creature.fly())
print(creature.trumpet())

creature.eat("nectar", 20)
print(creature.fly())
print(creature.trumpet())

creature.eat("grass", 50)
print(creature.fly())
print(creature.trumpet())

