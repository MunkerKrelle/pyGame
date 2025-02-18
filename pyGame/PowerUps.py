import pygame
from Components import Component
from GameObject import GameObject


class BasePowerUp(Component):
    def __init__(self,player_pos, damage, proj_speed) -> None:
        self._gameObject = GameObject(pygame.math.Vector2(0, 0))
        self.player_pos = player_pos
        self.damage = damage
        self.proj_speed = proj_speed
        print("power up has been constructed")

    def awake(self, game_world):
        print("power up has awoken")
        # self.damage = 300
        # print(self.damage)

    def start(self):
        print("power up has started")

    def update(self, delta_time):
        # print("power up has updated")
        pass

    def power_change(self):
        # print("new power aqquired...")

        damage = 200
        print(damage)

        # Each power up needs its own shoot function

class FireballPowerUp(Component):
    pass