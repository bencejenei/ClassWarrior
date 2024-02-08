import weapon


class Character:
    race = "Human"

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.hp_max = health
        self.health = health
        self.weapon = weapon.fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)


class Hero(Character):
    def __init__(self, name, healt):
        super().__init__(name=name, health=healt)


class Enemy(Character):
    def __init__(self, name, healt):
        super().__init__(name=name, health=healt)


if __name__ == '__main__':
    pass
