from Components import Component
import random
import pygame
from Components import Laser  
from Components import SpriteRenderer
from Components import Collider
from GameObject import GameObject

class Enemy(Component):

    def __init__(self,state) -> None:
        super().__init__()
        self._state = state
        # self.projectile = None # jsut for debugging, remove projectile fix

    def awake(self, game_world):
        self._game_world = game_world
        sr = self.gameObject.get_component("SpriteRenderer")

        
        random_x = random.randint(0, game_world.screen.get_width() - sr.sprite_image.get_width())
        self._screen_size = pygame.math.Vector2(game_world.screen.get_width(), game_world.screen.get_height())
        self.gameObject.transform.position = pygame.math.Vector2(random_x, 0)

        
        self.gameObject.add_component(Collider())

        
        self.gameObject.tag = "Enemy"

        
        self._time_since_last_shot = 0
        self._shoot_delay = 2  

    def start(self):
        pass     

    def update(self, delta_time):
        speed = 50
        movement = pygame.math.Vector2(0,speed)
        self.gameObject.transform.translate(movement * delta_time)
        
        # if self.projectile: #### debugging collider position, remove after fix
        #     collider = self.projectile.get_component("Collider")
        #     print(f"Collider position: {collider.collision_box.topleft}")

            

        bottom_limit = self._screen_size.y
        if self.gameObject.transform.position.y > bottom_limit:
            self.gameObject.destroy()

        
        self._time_since_last_shot += delta_time
        if self._time_since_last_shot >= self._shoot_delay:
            self.shoot()
            self._time_since_last_shot = 0

    def shoot(self):
        """Fjenden skyder et projektil mod spilleren."""
        self.projectile = GameObject(None)
        sr = self.projectile.add_component(SpriteRenderer("laser.png"))  
        self.projectile.add_component(Laser(500))  

        projectile_position = pygame.math.Vector2(
            self.gameObject.transform.position.x + (self.gameObject.get_component("SpriteRenderer").sprite_image.get_width() / 2) - (sr.sprite_image.get_width() / 2),
            self.gameObject.transform.position.y + 40
        )
        self.projectile.add_component(Collider())
        self.projectile.tag = "EnemyProjectile" 
        self.projectile.transform.position = projectile_position

               

        self._game_world.instantiate(self.projectile)

    
