# ---------- imports ----------
from character import Hero, Enemy
import weapon
from weapon import long_bow
from healthbar import HealthBar

from time import sleep
import os

# ---------- setup ----------
hero = Hero(name="Hero", health=20)
hero.equip(weapon.long_bow)
enemy = Enemy(name="Enemy", health=15, weapon=weapon.fists)

# ---------- game loop ----------
while True:
    os.system("clear")
    if hero.is_alive:
        hero.attack(enemy)
    else:
        hero.health_bar.draw_hp_bar()
        enemy.health_bar.draw_hp_bar()
        break

    if enemy.is_alive:
        enemy.attack(hero)
    else:
        hero.health_bar.draw_hp_bar()
        enemy.health_bar.draw_hp_bar()
        break

    hero.health_bar.draw_hp_bar()
    enemy.health_bar.draw_hp_bar()


    # print(f"{hero.name}'s health: {hero.health} \n"
    #       f"{HealthBar(color='green',entity=hero, length=20).draw_hp_bar()} \n"
    #       f"{enemy.name}'s health: {enemy.health} \n"
    #       f"{HealthBar(color='red', entity=enemy, length=20).draw_hp_bar()}\n")

    sleep(1)
