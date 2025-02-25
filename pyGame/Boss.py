from Components import Animator, Component
import random
import pygame
from Components import Laser  
from Components import SpriteRenderer
from Components import Collider
from GameObject import GameObject

class Boss(Component):
    def __init__(self) -> None:
        super().__init__()
        self.bullet_offset = [(208, 0), (218, 0), (228, 0), (326, 0), (336, 0), (346, 0)]  # Define bullet offsets relative to the Boss

    def awake(self, game_world) -> None:
        self.horizontal_movement = 100  # Initialize horizontal movement
        self._game_world = game_world
        sr = self.gameObject.get_component("SpriteRenderer")
        self.shoot = False
        self.nextShot = 0
        self.bulletIndex = 0

        # Initialize bullet positions based on the Boss's initial position
        self.update_bullet_positions()

        self._screen_size = pygame.math.Vector2(game_world.screen.get_width(), game_world.screen.get_height())
        self.gameObject.transform.position = pygame.math.Vector2((game_world.screen.get_width()/2)-sr.sprite_image.get_width() / 2 , -208)
        
        self.gameObject.tag = "Boss"
        
        self._time_since_last_shot = 0
        self._shoot_delay = 2  # Seconds between shots


    def start(self) -> None:
        pass

    def update(self, delta_time: float) -> None:
        speed = 100

        if self.gameObject.transform.position.y < 0:
            movement = pygame.math.Vector2(0, speed * delta_time)
            self.gameObject.transform.translate(movement)
        else:
            self.shoot = True
            movement = pygame.math.Vector2(self.horizontal_movement * delta_time, 0)
            self.gameObject.transform.translate(movement)

        self._keep_within_bounds(self.gameObject, self._game_world.screen.get_width())

        bottom_limit = self._screen_size.y
        if self.gameObject.transform.position.y > bottom_limit:
            self.gameObject.destroy()
        
        self._time_since_last_shot += delta_time
        self.nextShot += delta_time
        if self._time_since_last_shot >= self._shoot_delay and self.shoot:
            if self.nextShot >= 0.1:
                self.shoot_bullet(self.bulletList[self.bulletIndex])
                print("Shooting Bullet")
                self.bulletIndex += 1
                self.nextShot = 0
                if self.bulletIndex == 6:
                    self.bulletIndex = 0
                    self._time_since_last_shot = 0

        # Update bullet positions whenever the Boss moves
        self.update_bullet_positions()

    def shoot_bullet(self, pos):
                self.projectile = GameObject(None)
                self.projectile.add_component(SpriteRenderer("/BossShip/bulletStart.png"))
                self.projectile.add_component(Laser(500))
                animator = self.projectile.add_component(Animator())
                animator.add_spritesheet_animation("Bullet", "pyGame/Assets/BossShip/bullet.png", 8, 32, 4)
            
                animator.play_animation("Bullet")
                # self.projectile.add_component(Collider())
                self.projectile.tag = "EnemyProjectile" 
                self.projectile.transform.position = pos

                self._game_world.instantiate(self.projectile)

    def shoot_missile(self):
        pass

    def shoot_bomb(self):
        pass

    def _keep_within_bounds(self, game_object, screen_width):
        # Ensure the game object stays within the screen bounds on the x-axis and change direction if needed
        if game_object.transform.position.x < 0:
            game_object.transform.position.x = 0
            self.horizontal_movement = abs(self.horizontal_movement)  # Change direction to right
        elif game_object.transform.position.x > screen_width - game_object.get_component("SpriteRenderer").sprite_image.get_width():
            game_object.transform.position.x = screen_width - game_object.get_component("SpriteRenderer").sprite_image.get_width()
            self.horizontal_movement = -abs(self.horizontal_movement)  # Change direction to left

    def update_bullet_positions(self):
        # Calculate bullet positions relative to the Boss's current position
        self.bulletList = [
            (self.gameObject.transform.position.x + offset[0], self.gameObject.transform.position.y + offset[1] + 158)
            for offset in self.bullet_offset
        ]
        print(f"{self.gameObject.transform.position}")
