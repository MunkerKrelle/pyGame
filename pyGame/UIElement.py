import pygame
from Components import Component

# This class was supposed to create UI elements, but was not completed 
class UIElement(Component):
    def __init__(self) -> None:
        super().__init__()

    def awake(self, game_world) -> None:
        self._game_world = game_world

    def start(self) -> None:
        pass

    def update(self, delta_time: float) -> None:
        pass