from Components import Component
import pygame
from GameObject import GameObject
from Components import Laser
from Components import Collider
from Components import SpriteRenderer
from PowerUps import FireballPowerUp
from PowerUps import MultiShot
from PowerUps import SpeedPowerUp
from PowerUps import MoreLivesPowerUp

class Player(Component):
    bullet_sprite = "blank"
    
    def awake(self, game_world): 
        self._lives = 3
        self.gameObject.tag = "Player" 

        self._time_since_last_shot = 1
        self._shoot_dealy = 0.1 
        self._game_world = game_world
        sr = self._gameObject.get_component("SpriteRenderer")
        self._screen_size = pygame.math.Vector2(game_world.screen.get_width(),game_world.screen.get_height())
        self._sprite_size = pygame.math.Vector2(sr.sprite_image.get_width(),sr.sprite_image.get_height())
        self._gameObject.transform.position.x = (self._screen_size.x/2) - (self._sprite_size.x/2)
        self._gameObject.transform.position.y = (self._screen_size.y) - (self._sprite_size.y)

        global name
        name = "BasePowerUp"

        global damage
        damage = 0
      
        global power
        power = self._gameObject.get_component(name)
        damage = power.power_change()
        print(damage)

        global speed
        # speed = self._gameObject.get_component(SpeedPowerUp.__name__)
        speed = 300 
        # print(speed) 

    def start(self):
        pass

    def update(self, delta_time): 
        keys = pygame.key.get_pressed()
        movement = pygame.math.Vector2(0,0)
        self._time_since_last_shot += delta_time
        
        if keys[pygame.K_a]:
            movement.x -= speed
        if keys[pygame.K_d]:
            movement.x += speed
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_g]:
            self.aqquire_fireball()
            # self.take_damage()
        if keys[pygame.K_h]:
            self.aqquire_multi_shot()
        if keys[pygame.K_f]:
            self.aqquire_speed_up()
        if keys[pygame.K_v]:
            # self.remove_colliders()
            self.aqquire_lives_up()

        self._gameObject.transform.translate(movement*delta_time)

        if self._gameObject.transform.position.x < -self._sprite_size.x:
            self._gameObject.transform.position.x = self._screen_size.x
        elif self._gameObject.transform.position.x > self._screen_size.x:
            self._gameObject.transform.position.x = -self._sprite_size.x

        bottom_limit = self._screen_size.y - self._sprite_size.y
        if self._gameObject.transform.position.y > bottom_limit:
            self._gameObject.transform.position.y = bottom_limit
        elif self._gameObject.transform.position.y < 0:
            self._gameObject.transform.position.y = 0
        
        # print(f" player pos is: {self.gameObject.transform.position}")
    
    @property
    def damage(self):
        return self.damage


    def shoot(self):
        # global bullet_sprite
        # global power
        if self._time_since_last_shot >= self._shoot_dealy:
            for i in range(power.proj_amount):
                projectile = GameObject(None)
                sr = projectile.add_component(SpriteRenderer(power.sprite))
                # print(power.damage)
                projectile.add_component(Laser(power.proj_speed))
                # print(power.proj_speed)
                projectile_position = power.unique_shoot(sr, self._sprite_size.x / 2, i, power.proj_amount, power.proj_spread_angle)
                projectile.transform.position = projectile_position
               
                projectile.add_component(Collider())

                # for component_name, component in projectile._components.items():
                #     print(f"{component_name}: {component}")
                #     self.gameObject.remove_component(component_name)

                projectile.tag = "PlayerProjectile" 
                projectile.damage = power.damage 
                # print(projectile.damage)
                self._game_world.instantiate(projectile)

            self._time_since_last_shot = 0
    
    def aqquire_fireball(self):     
        global power
        power = self._gameObject.get_component(FireballPowerUp.__name__)
        damage = power.power_change()
        # print(damage)

    def aqquire_multi_shot(self):
        global power
        power = self._gameObject.get_component(MultiShot.__name__)
        damage = power.power_change()
        # print(damage)

    def aqquire_speed_up(self):     
        global speed
        speed = self._gameObject.get_component(SpeedPowerUp.__name__)
        speed = speed.power_change() 
    
    def aqquire_lives_up(self): # more health    
        # global lives
        _lives = self._gameObject.get_component(MoreLivesPowerUp.__name__)
        temp = _lives.power_change()
        print(temp)
        self._lives += temp
        print(self._lives)

    def take_damage(self):
        self._lives -= 1
        print(f"Player hit! Lives left: {self._lives}")
        if self._lives <= 0:
            self.game_over()

    def game_over(self):
        print("Game Over!")
        # self._game_world.destroy(self._gameObject)  # Fjerner spilleren fra spillet
        self.gameObject.destroy()
