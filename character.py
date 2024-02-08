import weapon


class Character:
    race = "Human"

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.hp_max = health
        self.health = health
        self.default_weapon = weapon.fists
        self.weapon = self.default_weapon

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        print(f"{self.name} dealt {self.weapon.damage} damage "
              f"with {self.weapon.name}")


class Hero(Character):
    def __init__(self, name, health):
        super().__init__(name=name, health=health)

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped with a(n) {self.weapon.name}")

    def drop(self, weapon) -> None:
        print(f"{self.name} dropped {self.weapon}")
        self.weapon = super(weapon.default_weapon)


class Enemy(Character):
    def __init__(self, name, health):
        super().__init__(name=name, health=health)


if __name__ == '__main__':
    pass
