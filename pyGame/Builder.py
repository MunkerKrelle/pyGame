from abc import ABC, abstractmethod
from GameObject import GameObject
from Components import Animator
from Components import SpriteRenderer
from Player import Player
from Enemy import Enemy
from Components import Collider
import pygame
import random

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

    def build(self):
        # Load the spritesheet
        spritesheet = pygame.image.load("Assets/Nairan - Dreadnought - Weapons.aseprite").convert_alpha()

        # Create the GameObject
        self._gameObject = GameObject(pygame.math.Vector2(0, 0))

        # Add components
        self._gameObject.add_component(SpriteRenderer("Nairan - Dreadnought - Base.png"))
        self._gameObject.add_component(Collider())
        self._gameObject.add_component(Enemy())
        
        # Add an Animator component
        animator = Animator()
        self._gameObject.add_component(animator)

        # Define animation parameters
        frame_width = 128  # Adjust based on your spritesheet
        frame_height = 128  # Adjust based on your spritesheet
        frame_count = 8  # Adjust based on your spritesheet

        # Add the animation to the animator
        animator.add_spritesheet_animation("WeaponFire", spritesheet, spritesheet.get_width(), spritesheet.get_height(), frame_count)

        animator.play_animation("WeaponFire")
        
    def get_gameObject(self) -> GameObject:
        return self._gameObject
    

        #     animator = self._gameObject.add_component(Animator())
        # animator.add_spritesheet_animation("Attack", "Assets/EnemyShips/Weapons/Nairan - Dreadnought - Weapons.png", 64, 64, 4)