from abc import ABC, abstractmethod
from GameObject import GameObject
from Components import Animator
from Components import SpriteRenderer
from Player import Player
from Enemy import Enemy
from PowerUps import BasePowerUp
from PowerUps import FireballPowerUp
from PowerUps import MultiShot
from PowerUps import SpeedPowerUp
from PowerUps import MoreLivesPowerUp
from Components import Collider
from Strategy import Battlecruiser, Bomber, Dreadnought, Fighter, Frigate, Scout, Strategy, Torpedo_Ship
import pygame
import random
from Boss import Boss

class Builder(ABC):
    
    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def get_gameObject(self) -> GameObject:
        pass

class PlayerBuilder(Builder):
    
    def build(self):
        self._gameObject = GameObject(pygame.math.Vector2(0, 0))
        self._gameObject.add_component(Player())
        self._gameObject.add_component(Collider())
        self._gameObject.add_component(BasePowerUp(pygame.math.Vector2(0, 0), 1, 1, 500, 0, "laser.png"))
        self._gameObject.add_component(FireballPowerUp(pygame.math.Vector2(0, 0), 4, 1, 1501, 0, "shield.png"))
        self._gameObject.add_component(MultiShot(pygame.math.Vector2(0, 0), 1, 6, 1200, 30, "player_fire-spaceship.png"))
        self._gameObject.add_component(SpeedPowerUp(pygame.math.Vector2(0, 0),800))
        self._gameObject.add_component(MoreLivesPowerUp(pygame.math.Vector2(0, 0),5))
        self._gameObject.add_component(SpriteRenderer("player08.png"))
        animator = self._gameObject.add_component(Animator())
        animator.add_animation("Idle","player02.png",
                            "player03.png",
                            "player04.png",
                            "player05.png",
                            "player06.png",
                            "player07.png",
                            "player08.png",
                            "player07.png",
                            "player06.png",
                            "player05.png",
                            "player04.png",
                            "player03.png",)
        
        animator.play_animation("Idle")


    def get_gameObject(self):
        return self._gameObject

class EnemyBuilder(Builder):

    def build(self, shipType, lives_multiplier):
        # Load the spritesheet

        # Create the GameObject
        self._gameObject = GameObject(pygame.math.Vector2(0, 0))

        # Add an Animator component
        animator = Animator()
        self._gameObject.add_component(animator)

        if shipType == "Dreadnought":
            self._gameObject.add_component(SpriteRenderer("/EnemyShips/Designs - Base/pngs/Nairan - Dreadnought - Base.png"))
            spritesheet = ("pyGame/Assets/EnemyShips/Weapons/pngs/Nairan - Dreadnought - Weapons.png")
            #spritesheet = ("Assets/EnemyShips/Weapons/pngs/Nairan - Dreadnought - Weapons.png")
            strategy = Dreadnought()
            lives = 2
            frame_width = 128  # Adjust based on your spritesheet
            frame_height = 128  # Adjust based on your spritesheet
            frame_count = 34  # Adjust based on your spritesheet
        elif shipType == "Battlecruiser":
            self._gameObject.add_component(SpriteRenderer("/EnemyShips/Designs - Base/pngs/Nairan - Battlecruiser - Base.png"))
            spritesheet = ("pyGame/Assets/EnemyShips/Weapons/pngs/Nairan - Battlecruiser - Weapons.png")
            #spritesheet = ("Assets/EnemyShips/Weapons/pngs/Nairan - Battlecruiser - Weapons.png")
            state = Battlecruiser()
            strategy = Battlecruiser()
            lives = 2
            frame_width = 128  # Adjust based on your spritesheet
            frame_height = 128  # Adjust based on your spritesheet
            frame_count = 9  # Adjust based on your spritesheet
        elif shipType == "Frigate":
            self._gameObject.add_component(SpriteRenderer("/EnemyShips/Designs - Base/pngs/Nairan - Frigate - Base.png"))
            spritesheet = ("pyGame/Assets/EnemyShips/Weapons/pngs/Nairan - Frigate - Weapons.png")
            #spritesheet = ("Assets/EnemyShips/Weapons/pngs/Nairan - Frigate - Weapons.png")
            strategy = Frigate()
            lives = 3
            frame_width = 64  # Adjust based on your spritesheet
            frame_height = 64  # Adjust based on your spritesheet
            frame_count = 5  # Adjust based on your spritesheet
        elif shipType == "Fighter":
            self._gameObject.add_component(SpriteRenderer("/EnemyShips/Designs - Base/pngs/Nairan - Fighter - Base.png"))
            spritesheet = ("pyGame/Assets/EnemyShips/Weapons/pngs/Nairan - Fighter - Weapons.png")
            #spritesheet = ("Assets/EnemyShips/Weapons/pngs/Nairan - Fighter - Weapons.png")
            strategy = Fighter()
            lives = 2
            frame_width = 64  # Adjust based on your spritesheet
            frame_height = 64  # Adjust based on your spritesheet
            frame_count = 28  # Adjust based on your spritesheet
        elif shipType == "Bomber":
            self._gameObject.add_component(SpriteRenderer("/EnemyShips/Designs - Base/pngs/Nairan - Bomber - Base.png"))
            spritesheet = ("pyGame/Assets/EnemyShips/Designs - Base/pngs/Nairan - Bomber - Base.png")
            #spritesheet = ("Assets/EnemyShips/Designs - Base/pngs/Nairan - Bomber - Base.png")
            strategy = Bomber()
            lives = 2
            frame_width = 64  # Adjust based on your spritesheet
            frame_height = 64  # Adjust based on your spritesheet
            frame_count = 1  # Adjust based on your spritesheet
        elif shipType == "Scout":
            self._gameObject.add_component(SpriteRenderer("/EnemyShips/Designs - Base/pngs/Nairan - Scout - Base.png"))
            spritesheet = ("pyGame/Assets/EnemyShips/Weapons/pngs/Nairan - Scout - Weapons.png")
            #spritesheet = ("Assets/EnemyShips/Weapons/pngs/Nairan - Scout - Weapons.png")
            strategy = Scout()
            lives = 2
            frame_width = 64  # Adjust based on your spritesheet
            frame_height = 64  # Adjust based on your spritesheet
            frame_count = 6  # Adjust based on your spritesheet
        elif shipType == "Torpedo_Ship":
            self._gameObject.add_component(SpriteRenderer("/EnemyShips/Designs - Base/pngs/Nairan - Torpedo Ship - Base.png"))
            spritesheet = ("pyGame/Assets/EnemyShips/Weapons/pngs/Nairan - Torpedo Ship - Weapons.png")
            #spritesheet = ("Assets/EnemyShips/Weapons/pngs/Nairan - Torpedo Ship - Weapons.png")
            strategy = Torpedo_Ship()
            lives = 2
            frame_width = 64  # Adjust based on your spritesheet
            frame_height = 64  # Adjust based on your spritesheet
            frame_count = 6  # Adjust based on your spritesheet

        self._gameObject.add_component(Collider())
        self._gameObject.add_component(Enemy(strategy, lives + lives_multiplier))


        # Add the animation to the animator
        animator.add_spritesheet_animation("WeaponFire", spritesheet, frame_width, frame_height, frame_count)

        animator.play_animation("WeaponFire")
        # self._gameObject.get_component(SpriteRenderer()).flip(True, False)

    def get_gameObject(self) -> GameObject:
        return self._gameObject
    

        #     animator = self._gameObject.add_component(Animator())
        # animator.add_spritesheet_animation("Attack", "Assets/EnemyShips/Weapons/Nairan - Dreadnought - Weapons.png", 64, 64, 4)

class BossBuilder(Builder):

    def build(self):
        self._gameObject = GameObject(pygame.math.Vector2(0, 0))
        self._gameObject.add_component(Collider())
        self._gameObject.add_component(SpriteRenderer("/BossShip/BossBase.png"))
        self._gameObject.add_component(Boss())
        animator = self._gameObject.add_component(Animator())
        animator.add_spritesheet_animation("Attack", "pyGame/Assets/BossShip/Boss.png", 560, 208, 4)
        animator.play_animation("Attack")
    
    def get_gameObject(self) -> GameObject:
        return self._gameObject