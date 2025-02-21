import pygame
from Components import Component
from GameObject import GameObject
from Components import SpriteRenderer
from Components import Laser


class BasePowerUp(Component):
    def __init__(self,player_pos, damage, proj_amount, proj_speed, proj_spread_angle, sprite) -> None:
        self._gameObject = GameObject(pygame.math.Vector2(0, 0))
        self.player_pos = player_pos
        self.damage = damage
        self.proj_speed = proj_speed
        self.proj_amount = proj_amount
        self.proj_spread_angle = proj_spread_angle
        self.sprite = sprite
        # print("power up has been constructed")

    def awake(self, game_world):
        pass
        # print("power up has awoken")

    def start(self):
        pass
        # print("power up has started")

    def update(self, delta_time):
        pass

    def power_change(self):
        # print("new power aqquired...")
        # self.damage = 200
        return self.damage
    
    def shoot_projectile_sprite(self):
        sprite = "laser.png"
        return sprite
    
    # def unique_shoot(self, sr, proj_center):
    #     projectile_position = pygame.math.Vector2(self._gameObject.transform.position.x+(proj_center)-sr.sprite_image.get_width()/2
    #                                                 ,self._gameObject.transform.position.y-40)
    #     print("a unique shot was fired")
    #     return projectile_position
    
    def unique_shoot(self, sr, proj_center, shot_index, total_projectiles, spread):
        # Calculate X offset based on shot index and spread
        offset = (shot_index - (total_projectiles - 1) / 2) * spread  # Center shot at index 1 if 3 shots (0,1,2)
        
        projectile_position = pygame.math.Vector2(
            self._gameObject.transform.position.x + proj_center - sr.sprite_image.get_width() / 2 + offset,
            self._gameObject.transform.position.y - 40
        )
        
        # print(f"A unique shot was fired at position {projectile_position}")
        return projectile_position

class FireballPowerUp(Component):
    def __init__(self,player_pos, damage, proj_amount, proj_speed, proj_spread_angle, sprite) -> None:
        self._gameObject = GameObject(pygame.math.Vector2(0, 0))
        self.player_pos = player_pos
        self.damage = damage
        self.proj_speed = proj_speed
        self.proj_amount = proj_amount
        self.proj_spread_angle = proj_spread_angle
        self.sprite = sprite
        # print("fireball has been constructed")

    def awake(self, game_world):
        pass
        # print("fireball up has awoken")

    def start(self):
        pass
        # print("fireball up has started")

    def update(self, delta_time):
        pass

    def power_change(self):
        # print("new power aqquired...")
        # self.damage = 333
        return self.damage

    def shoot_projectile_sprite(self):
        sprite = "shield.png"
        return sprite
    
    def unique_shoot(self, sr, proj_center, shot_index, total_projectiles, spread):
        offset = (shot_index - (total_projectiles - 1) / 2) * spread  # centers the projectiles
        
        projectile_position = pygame.math.Vector2(
            self._gameObject.transform.position.x + proj_center - sr.sprite_image.get_width() / 2 + offset,
            self._gameObject.transform.position.y - 40
        )
        
        # print(f"A unique fireball was fired at position {projectile_position}")
        return projectile_position

class MultiShot(Component):
    def __init__(self,player_pos, damage, proj_amount, proj_speed, proj_spread_angle, sprite) -> None:
        self._gameObject = GameObject(pygame.math.Vector2(0, 0))
        self.player_pos = player_pos
        self.damage = damage
        self.proj_speed = proj_speed
        self.proj_amount = proj_amount
        self.proj_spread_angle = proj_spread_angle
        self.sprite = sprite
        
        # print("multishot has been constructed")

    def awake(self, game_world):
        pass
        # print("multishot has awoken")

    def start(self):
        pass
        # print("multishot has started")

    def update(self, delta_time):
        pass

    def power_change(self):
        # print("new power aqquired...")
        # self.damage = 200
        return self.damage
    
    def shoot_projectile_sprite(self):
        sprite = "player_fire-spaceship.png"
        return sprite
    
    def unique_shoot(self, sr, proj_center, shot_index, total_projectiles, spread):
        offset = (shot_index - (total_projectiles - 1) / 2) * spread # centers the projectiles
        
        projectile_position = pygame.math.Vector2(
            self._gameObject.transform.position.x + proj_center - sr.sprite_image.get_width() / 2 + offset,
            self._gameObject.transform.position.y - 40
        )
        
        # print(f"A unique multi shot was fired at position {projectile_position}")
        return projectile_position

class SpeedPowerUp(Component):
    def __init__(self,player_pos, speed) -> None:
        self._gameObject = GameObject(pygame.math.Vector2(0, 0))
        self.player_pos = player_pos
        self.speed = speed
        # print("speed up has been constructed")

    def awake(self, game_world):
        pass
        # print("speed up has awoken")

    def start(self):
        pass
        # print("speed up has started")

    def update(self, delta_time):
        pass

    def power_change(self):
        # print("speed has been buffed..")
        # print(self.speed)
        return self.speed
    
class MoreLivesPowerUp(Component):
    def __init__(self,player_pos, lives) -> None:
        self._gameObject = GameObject(pygame.math.Vector2(0, 0))
        self.player_pos = player_pos
        self.lives = lives
        print("lives up has been constructed")

    def awake(self, game_world):
        print("lives up has awoken")

    def start(self):
        print("lives up has started")

    def update(self, delta_time):
        pass

    def power_change(self):
        print("lives has been buffed..")
        # print(self.lives)
        return self.lives