import os
# from character import Character

os.system("")


class HealthBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    symbol_barrier: str = '|'
    colors: dict = {"red": "\033[91m",
                    "purple": "\33[95m",
                    "blue": "\33[34m",
                    "blue2": "\33[36m",
                    "blue3": "\33[96m",
                    "green": "\033[92m",
                    "green2": "\033[32m",
                    "brown": "\33[33m",
                    "yellow": "\33[93m",
                    "grey": "\33[37m",
                    "default": "\033[0m"
                    }

    def __init__(self,
                 entity,
                 length: int = 20,
                 is_colored: bool = True,
                 color: str = ""
                 ) -> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.hp_max
        self.current_value = entity.health
        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]

    def update(self) -> None:
        self.current_value = self.entity.health

    def draw_hp_bar(self) -> None:
        remaining_bar = round(self.current_value / self.max_value * self.length)
        lost_bar = self.length - remaining_bar

        print(f"{self.entity.name}'s health: {self.entity.health}")
        print(f"    "
              f"{self.color if self.is_colored else ''}"
              f"{self.symbol_barrier}"
              f"{remaining_bar * self.symbol_remaining}"
              f"{lost_bar * self.symbol_lost}"
              f"{self.symbol_barrier}"
              f"{self.colors['default'] if self.is_colored else ''}")
