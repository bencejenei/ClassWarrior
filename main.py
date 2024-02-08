from character import Character
from time import sleep

hero = Character(name="Hero", health=100, damage=10)
enemy = Character(name="Enemy", health=95, damage=8)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"{hero.name}'s health: {hero.health} \n"
          f"{enemy.name}'s health: {enemy.health} \n")

    sleep(1)
