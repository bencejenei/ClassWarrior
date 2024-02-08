from character import Hero, Enemy
import weapon
from healthbar import HealthBar

from time import sleep
import os

hero = Hero(name="Hero", health=100)
hero.equip(weapon.long_bow)
enemy = Enemy(name="Enemy", health=95)

while True:
    os.system("clear")
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"{hero.name}'s health: {hero.health} \n"
          f"{HealthBar(entity=hero, length=20).draw_hp_bar()} \n"    
          f"{enemy.name}'s health: {enemy.health} \n"
          f"{HealthBar(entity=enemy, length=20).draw_hp_bar()}\n")

    sleep(1)
