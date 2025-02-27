from Components import Component
import random
import pygame
from Components import Projectile  
from Components import SpriteRenderer
from Components import Collider
from GameObject import GameObject
from ScoreManager import ScoreManager

# The enemy class handles the enemy logic, such as which strategy pattern they use, or what happens when they run out of lives etc.
class Enemy(Component):
    def __init__(self, strategy, lives) -> None:
        super().__init__()

        self._strategy = strategy
        self._lives = lives

    # Spawn the enemy randomly in the world along the X axis.
    def awake(self, game_world) -> None:
        
        self._game_world = game_world
        
        sr = self.gameObject.get_component("SpriteRenderer")

        random_x = random.randint(0, game_world.screen.get_width() - sr.sprite_image.get_width())
        self._screen_size = pygame.math.Vector2(game_world.screen.get_width(), game_world.screen.get_height())
        self.gameObject.transform.position = pygame.math.Vector2(random_x, -100)
        
        self.gameObject.tag = "Enemy"
        
        self._time_since_last_shot = 0
        self._shoot_delay = 2  # Seconds between shots

         
        self._explosion_sound = pygame.mixer.Sound("pygame\\Assets\\Explode.mp3")
        self._laser_sound = pygame.mixer.Sound("pygame\\Assets\\LaserSound.mp3")
        #self._explosion_sound = pygame.mixer.Sound("Assets\\Explode.mp3")
        #self._laser_sound = pygame.mixer.Sound("Assets\\LaserSound.mp3")


    def start(self) -> None:
        pass

    # Dictates movement stratety and what happens when the enemy reaches the buttom of the screen
    def update(self, delta_time: float) -> None:
        self._strategy.move(self.gameObject, delta_time, self._game_world)


        bottom_limit = self._screen_size.y
        if self.gameObject.transform.position.y > bottom_limit:
            self.gameObject.destroy()
        
        self._time_since_last_shot += delta_time
        if self._time_since_last_shot >= self._shoot_delay:
            self.shoot()
            self._time_since_last_shot = 0

    # The enemy can shoot projectiles which can hit the player, here we pass along things like sprites, damage amount, tags etc
    def shoot(self):
        """Fjenden skyder et projektil mod spilleren."""
        self.projectile = GameObject(None)
        sr = self.projectile.add_component(SpriteRenderer("laser.png"))

        projectile_component = self.projectile.add_component(Projectile(500, None, damage=1))  

        projectile_position = pygame.math.Vector2(
            self.gameObject.transform.position.x + (self.gameObject.get_component("SpriteRenderer").sprite_image.get_width() / 2) - (sr.sprite_image.get_width() / 2),
            self.gameObject.transform.position.y + 40
        )

        self.projectile.add_component(Collider())
        self.projectile.tag = "EnemyProjectile"  
        self.projectile.transform.position = projectile_position

            
        self._laser_sound.play()

            
        self._game_world.instantiate(self.projectile)

    def take_damage(self, damage_taken=1):
        self._lives -= damage_taken
        print(f"Enemy was hit! Lives left: {self._lives}")

        if self._lives <= 0:
            self.destroy()


    def game_over(self):
        print("Game Over!")
        self.gameObject.destroy()


    def destroy(self):
        """Spil eksplosionseffekten, når fjenden dør"""
        self._explosion_sound.play()
        self.gameObject.destroy()
        ScoreManager().increase_score()
        

