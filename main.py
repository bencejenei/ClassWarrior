from character import Hero, Enemy
import weapon
from time import sleep

hero = Hero(name="Hero", health=100)
enemy = Enemy(name="Enemy", health=95)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"{hero.name}'s health: {hero.health} \n"
          f"{enemy.name}'s health: {enemy.health} \n")

    sleep(3)
    hero.equip(weapon.long_bow)
