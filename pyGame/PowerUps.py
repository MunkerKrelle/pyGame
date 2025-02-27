import pygame
from Components import Component
from GameObject import GameObject

# This class handles the component based power ups that the player aqquires over the duration of the game. 
# The basepowerup class is the default power the player starts with.
class BasePowerUp(Component):
    def __init__(self,player_pos, damage, proj_amount, proj_speed, proj_spread_angle, sprite) -> None:
        self._gameObject = GameObject(pygame.math.Vector2(0, 0))
        self.player_pos = player_pos
        self.damage = damage
        self.proj_speed = proj_speed
        self.proj_amount = proj_amount
        self.proj_spread_angle = proj_spread_angle
        self.sprite = sprite

    def awake(self, game_world):
        pass

    def start(self):
        pass

    def update(self, delta_time):
        pass

    def power_change(self):
        return self.damage
    
    def shoot_projectile_sprite(self):
        sprite = "laser.png"
        return sprite
    
    # Method for handling multiple projectiles so they are centered on the player at the time of shooting. 
    # This method is called inside a for loop, based on the amount of projectiles the attack type has.
    def unique_shoot(self, sr, proj_center, shot_index, total_projectiles, spread):
        # Calculate X offset based on shot index and spread
        offset = (shot_index - (total_projectiles - 1) / 2) * spread  # Center shot at index 1 if 3 shots (0,1,2)
        
        projectile_position = pygame.math.Vector2(
            self._gameObject.transform.position.x + proj_center - sr.sprite_image.get_width() / 2 + offset,
            self._gameObject.transform.position.y - 40
        )
        
        return projectile_position

# attack type power up, hits hard pr shot.
class FireballPowerUp(Component):
    def __init__(self,player_pos, damage, proj_amount, proj_speed, proj_spread_angle, sprite) -> None:
        self._gameObject = GameObject(pygame.math.Vector2(0, 0))
        self.player_pos = player_pos
        self.damage = damage
        self.proj_speed = proj_speed
        self.proj_amount = proj_amount
        self.proj_spread_angle = proj_spread_angle
        self.sprite = sprite

    def awake(self, game_world):
        print("fireball up has awoken")

    def start(self):
        print("fireball up has started")

    def update(self, delta_time):
        pass

    def power_change(self):
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
        
        return projectile_position

# Attack type power up, shots multiple projectiles.
class MultiShot(Component):
    def __init__(self,player_pos, damage, proj_amount, proj_speed, proj_spread_angle, sprite) -> None:
        self._gameObject = GameObject(pygame.math.Vector2(0, 0))
        self.player_pos = player_pos
        self.damage = damage
        self.proj_speed = proj_speed
        self.proj_amount = proj_amount
        self.proj_spread_angle = proj_spread_angle
        self.sprite = sprite

    def awake(self, game_world):
        pass

    def start(self):
        pass

    def update(self, delta_time):
        pass

    def power_change(self):
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
        
        return projectile_position

# Utility type power up, increase player movement speed.
class SpeedPowerUp(Component):
    def __init__(self,player_pos, speed) -> None:
        self._gameObject = GameObject(pygame.math.Vector2(0, 0))
        self.player_pos = player_pos
        self.speed = speed

    def awake(self, game_world):
        pass

    def start(self):
        pass

    def update(self, delta_time):
        pass

    def power_change(self):
        return self.speed

# Defence type power up, gives the player more lives.
class MoreLivesPowerUp(Component):
    def __init__(self,player_pos, lives) -> None:
        self._gameObject = GameObject(pygame.math.Vector2(0, 0))
        self.player_pos = player_pos
        self.lives = lives

    def awake(self, game_world):
        pass

    def start(self):
        pass

    def update(self, delta_time):
        pass

    def power_change(self):
        return self.lives