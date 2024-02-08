
class Weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int ) -> None:
        self.name = name
        self.weapon_type =weapon_type
        self.damage = damage
        self.value = value


iron_sword = Weapon(name= "Iron Sword",
                    weapon_type="melee" ,
                    damage= 5,
                    value= 10)

long_bow = Weapon(name= "Long Bow",
                  weapon_type= "range",
                  damage= 4,
                  value= 8)

fists = Weapon(name= "Fist",
               weapon_type= "hands",
               damage= 2,
               value= 0)


if __name__ == '__main__':
    pass
