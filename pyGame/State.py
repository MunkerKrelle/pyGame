from Components import Component
import pygame
class State(Component):
    def __init__(self) -> None:
        super().__init__()

    def awake(self, game_world):
        pass

    def start(self):
        pass
   
    def update(self, delta_time):
        pass 

    def attack(self):
            pass
    def move(self):
            pass
    def die(self):
            pass

class Battlecruiser(State):
    def attack(self):
        print("Battlecruiser attack")
    def move(self):
        print("Battlecruiser move")
    def die(self):
        print("Battlecruiser die")

class Dreadnought(State):
    def attack(self):
        print("Dreadnought attack")
    def move(self):
        print("Dreadnought move")
    def die(self):
        print("Dreadnought die")

class Bomber(State):
    def attack(self):
        print("Bomber attack")
    def move(self):
        print("Bomber move")
    def die(self):
        print("Bomber die")

class Fighter(State):
    def attack(self):
        print("Fighter attack")
    def move(self):
        print("Fighter move")
    def die(self):
        print("Fighter die")

class Torpedo_Ship(State):
    def attack(self):
        print("Torpedo_Ship attack")
    def move(self):
        print("Torpedo_Ship move")
    def die(self):
        print("Torpedo_Ship die")

class Frigate(State):
    def attack(self):
        print("Frigate attack")
    def move(self):
        print("Frigate move")
    def die(self):
        print("Frigate die")

class Scout(State):
    def attack(self):
        print("Scout attack")
    def move(self):
        print("Scout move")
    def die(self):
        print("Scout die")