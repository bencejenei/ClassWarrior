class Character:
    race = "Human"

    def __init__(self, name: str, health: int, damage: int) -> None:
        self.name = name
        self.hp_max = health
        self.health = health
        self.damage = damage

    def attack(self, target) -> None:
        target.health -= self.damage
        target.health = max(target.health, 0)


if __name__ == '__main__':
    pass
