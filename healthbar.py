import typing
from character import Character


class HealthBar:
    symbol_remaining: str = "x"
    symbol_lost: str = "_"
    symbol_barrier: str = 'I'

    def __init__(self, entity: Character, length: int) -> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.hp_max
        self.current_value = entity.health

    def update(self) -> None:
        self.current_value = self.entity.health

    def draw_hp_bar(self) -> str:
        remaining_bar = round(self.current_value/self.max_value * self.length)
        lost_bar = self.length - remaining_bar
        return (f"    "
                f"{self.symbol_barrier}"
                f"{remaining_bar * self.symbol_remaining}"
                f"{lost_bar * self.symbol_lost}"
                f"{self.symbol_barrier}")