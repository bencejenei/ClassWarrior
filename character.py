# ---------- imports ----------
import weapon
from healthbar import HealthBar

# ---------- Parent Class ----------


class Character:
    race = "Human"

    def __init__(self,
                 name: str,
                 health: int
                 ) -> None:
        self.name = name
        self.hp_max = health
        self.health = health
        self.default_weapon = weapon.fists
        self.weapon = self.default_weapon
        self.is_alive: bool = True

    def is_alive(self):
        if self.health > 0:
            pass
        else:
            self.is_alive = False
            print(f"{self.name} is dead!")

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} dealt {self.weapon.damage} damage to "
              f"{target.name} with {self.weapon.name}")

        if target.health <= 0:
            print(f"{target.name} is dead!")
            target.is_alive = False

# ---------- Child Classes ----------

class Hero(Character):
    def __init__(self,
                 name: str,
                 health: int
                 ) -> None:
        super().__init__(name=name, health=health)
        self.health_bar = HealthBar(entity=self,color="green")

    def equip(self,
              weapon:weapon
              ) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped with a(n) {self.weapon.name}")

    def drop(self, weapon) -> None:
        print(f"{self.name} dropped {self.weapon}")
        self.weapon = super(weapon.default_weapon)


class Enemy(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 weapon: object
                 ) -> None:
        super().__init__(name=name, health=health)
        self.health_bar = HealthBar(self, color="purple")
        self.weapon = weapon


if __name__ == '__main__':
    pass
