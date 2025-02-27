import pygame
from Components import Component, SpriteRenderer

# click or keyboard press for a power up.
class PowerUpSelector(Component):
    _instance = None  

    def __new__(cls, player, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(PowerUpSelector, cls).__new__(cls)
            cls._instance.initialize(player)  # Ensure it's only initialized once
        return cls._instance

    def __init__(self, player):
        super().__init__()  
        self.player = player

    def initialize(self, player):
        self.player = player
        print(player)
        print("PowerUpSelector was constructed")

    def awake(self, game_world) -> None:
        self.power_picked = False

    @property
    def get_power_picker(self):
        return self.power_picked

    @property
    def set_power_picker(self):
        self.power_picked = False

    def start(self) -> None:
        print("player aqquired")
        print(self.player)
        
    def update(self, delta_time) -> None:
        # self.select_power()
        pass

    def select_power(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            print("1 was pressed")
            print(self.player)
            bob = self.player.get_component("Player")
            print(bob)
            bob.aqquire_fireball()
            self.power_picked = True
            # bob.aqquire_multi_shot()
        
        if keys[pygame.K_2]:
            print("2 was pressed")
            bob = self.player.get_component("Player")
            print(bob)
            # bob.aqquire_fireball()
            bob.aqquire_multi_shot()
            self.power_picked = True

        if keys[pygame.K_3]:
            print("3 was pressed")
            bob = self.player.get_component("Player")
            print(bob)
            # bob.aqquire_fireball()
            bob.aqquire_speed_up()
            self.power_picked = True
        
        if keys[pygame.K_4]:
            print("3 was pressed")
            bob = self.player.get_component("Player")
            print(bob)
            # bob.aqquire_fireball()
            bob.aqquire_lives_up()
            self.power_picked = True
    
    def test_method(self):
        print("this test was successful")

    # def get_player(self, obj_list):
    #     for gameObject in obj_list:
    #         if gameObject.tag == "Player":
    #             # print("player found... :")
    #             # print(gameObject)
    #             self.player = gameObject
    
    def get_player(self, obj):
            if obj.tag == "Player":
                print("player found... :")
                print(obj)
                self.player = obj