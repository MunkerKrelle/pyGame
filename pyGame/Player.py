from Components import Component
import pygame
from GameObject import GameObject
from Components import Laser
from Components import Collider
from Components import SpriteRenderer
from PowerUps import FireballPowerUp
from PowerUps import MultiShot

class Player(Component):
    bullet_sprite = "blank"

    def awake(self, game_world): 
        self._lives = 3  
        self.gameObject.add_component(Collider())

        
        self.gameObject.tag = "Player"

        self._time_since_last_shot = 1
        self._shoot_dealy = 1 
        self._game_world = game_world
        sr = self._gameObject.get_component("SpriteRenderer")
        self._screen_size = pygame.math.Vector2(game_world.screen.get_width(),game_world.screen.get_height())
        self._sprite_size = pygame.math.Vector2(sr.sprite_image.get_width(),sr.sprite_image.get_height())
        self._gameObject.transform.position.x = (self._screen_size.x/2) - (self._sprite_size.x/2)
        self._gameObject.transform.position.y = (self._screen_size.y) - (self._sprite_size.y)

        global name
        name = "BasePowerUp"

        global power
        power = self._gameObject.get_component(name)
        power.power_change()
        
        # global bullet_sprite
        # self.bullet_sprite = power.shoot_projectile_sprite()

    def start(self):
        pass

    def update(self, delta_time): 
        keys = pygame.key.get_pressed()
        speed = 300
        movement = pygame.math.Vector2(0,0)
        self._time_since_last_shot += delta_time

        
        if keys[pygame.K_a]:
            movement.x -= speed
        if keys[pygame.K_d]:
            movement.x += speed
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_g]:
            self.aqquire_power_up()
        if keys[pygame.K_h]:
            self.aqquire_multi_shot()

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
    
    def shoot(self):
        global bullet_sprite
        global power
        if self._time_since_last_shot >= self._shoot_dealy:
            # projectile = GameObject(None)
            # sr = projectile.add_component(SpriteRenderer(self.bullet_sprite))
            # projectile.add_component(Laser(power.proj_speed))
            # power.unique_shoot(sr)
            # projectile_position = pygame.math.Vector2(self._gameObject.transform.position.x+(self._sprite_size.x/2)-sr.sprite_image.get_width()/2
            #                                         ,self._gameObject.transform.position.y-40)
            # print(power.proj_spread_angle)

            for i in range(power.proj_amount):
                projectile = GameObject(None)
                # sr = projectile.add_component(SpriteRenderer(self.bullet_sprite))
                sr = projectile.add_component(SpriteRenderer(power.sprite))
                print(power.damage)
                projectile.add_component(Laser(power.proj_speed))
                print(power.proj_speed)
                projectile_position = power.unique_shoot(sr, self._sprite_size.x / 2, i, power.proj_amount, power.proj_spread_angle)
                projectile.transform.position = projectile_position

                self._game_world.instantiate(projectile)

            # projectile_position = power.unique_shoot(sr, self._sprite_size.x/2)

            # projectile.transform.position = projectile_position
            
            # self._game_world.instantiate(projectile)
            projectile = GameObject(None)
            sr = projectile.add_component(SpriteRenderer("laser.png"))
            projectile.add_component(Laser(power.proj_speed))

            projectile_position = pygame.math.Vector2(self._gameObject.transform.position.x+(self._sprite_size.x/2)-sr.sprite_image.get_width()/2
                                                    ,self._gameObject.transform.position.y-40)
            
            projectile.transform.position = projectile_position

            collider = projectile.add_component(Collider())
            projectile.tag = "PlayerProjectile"  

            self._game_world.instantiate(projectile)
            
            self._time_since_last_shot = 0
    
    def aqquire_power_up(self):
        # global name
        # name = "FireballPowerUp"
        
        global power
        power = self._gameObject.get_component(FireballPowerUp.__name__)
        power.power_change()

        # global bullet_sprite
        # self.bullet_sprite = power.shoot_projectile_sprite()

    def aqquire_multi_shot(self):
        # global name
        # name = "MultiShot"
        
        global power
        power = self._gameObject.get_component(MultiShot.__name__)
        power.power_change()

        # global bullet_sprite
        # self.bullet_sprite = power.shoot_projectile_sprite()
        
        
    def take_damage(self):
        self._lives -= 1
        print(f"Player hit! Lives left: {self._lives}")
        
        if self._lives <= 0:
            self.game_over()
    def game_over(self):
        print("Game Over!")
        self._game_world.destroy(self._gameObject)  # Fjerner spilleren fra spillet
