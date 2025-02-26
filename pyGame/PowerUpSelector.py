import pygame
from Components import Component, SpriteRenderer

# click or keyboard press for a power up.
class PowerUpSelector(Component):
    def __init__(self) -> None:
        super().__init__()

    def awake(self, game_world) -> None:
        pass

    def start(self) -> None:
        pass

    def update(self, delta_time) -> None:
        keys = pygame.key.get_pressed()
       
        if keys[pygame.K_1]:
            print("1 was pressed")