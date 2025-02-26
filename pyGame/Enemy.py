from Components import Component
import random
import pygame
from Components import Laser  
from Components import SpriteRenderer
from Components import Collider
from GameObject import GameObject

class Enemy(Component):
    def __init__(self, strategy) -> None:
        super().__init__()

        self._strategy = strategy


    def awake(self, game_world) -> None:
        self._game_world = game_world
        sr = self.gameObject.get_component("SpriteRenderer")
        
        self.set_enemy_health(sr)
        # print(sr.sprite_name)  

        random_x = random.randint(0, game_world.screen.get_width() - sr.sprite_image.get_width())
        self._screen_size = pygame.math.Vector2(game_world.screen.get_width(), game_world.screen.get_height())
        self.gameObject.transform.position = pygame.math.Vector2(random_x, 0)
        
        self.gameObject.add_component(Collider())
        self.gameObject.tag = "Enemy"
        
        self._time_since_last_shot = 0
        self._shoot_delay = 2  # Seconds between shots

         
        self._explosion_sound = pygame.mixer.Sound("pygame\\Assets\\Explode.mp3")
        self._laser_sound = pygame.mixer.Sound("pygame\\Assets\\LaserSound.mp3")
        self._explosion_sound = pygame.mixer.Sound("pygame\\Assets\\Explode.mp3")
        self._laser_sound = pygame.mixer.Sound("pygame\\Assets\\LaserSound.mp3")


    def start(self) -> None:
        pass

    def update(self, delta_time: float) -> None:
        self._strategy.move(self.gameObject, delta_time, self._game_world)


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

            
        # self._laser_sound.play()

            
        self._game_world.instantiate(self.projectile)
    
    def take_damage(self, damage_taken):
        self._lives -= damage_taken
        print(f"Enemy was hit! Lives left: {self._lives}")
        
        if self._lives <= 0:
            self.game_over()

    def game_over(self):
        print("Game Over!")
        # self._game_world.destroy(self._gameObject)  # Fjerner spilleren fra spillet
        self.gameObject.destroy()
    
    def set_enemy_health(self, sr):
        if sr.sprite_name == "/EnemyShips/Designs - Base/pngs/Nairan - Dreadnought - Base.png":
            self._lives = 5

        elif sr.sprite_name == "/EnemyShips/Designs - Base/pngs/Nairan - Scout - Base.png":
            self._lives = 1

        elif sr.sprite_name == "/EnemyShips/Designs - Base/pngs/Nairan - Frigate - Base.png":
            self._lives = 1

        elif sr.sprite_name == "/EnemyShips/Designs - Base/pngs/Nairan - Bomber - Base.png":
            self._lives = 2

        elif sr.sprite_name == "/EnemyShips/Designs - Base/pngs/Nairan - Battlecruiser - Base.png":
            self._lives = 3

        elif sr.sprite_name == "/EnemyShips/Designs - Base/pngs/Nairan - Fighter - Base.png":
            self._lives = 2

        elif sr.sprite_name == "/EnemyShips/Designs - Base/pngs/Nairan - Torpedo Ship - Base.png":
            self._lives = 1

    def destroy(self):
        """Spil eksplosionseffekten, når fjenden dør"""
        # self._explosion_sound.play()
        self.gameObject.destroy()
