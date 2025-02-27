from Components import Animator, Component
import random
import pygame
from Components import Projectile  
from Components import SpriteRenderer
from Components import Collider
from GameObject import GameObject
from PowerUpSelector import PowerUpSelector

class Boss(Component):
    def __init__(self) -> None:
        super().__init__()
        self.bullet_offset = [(208, 0), (218, 0), (228, 0), (326, 0), (336, 0), (346, 0), (166,0), (388,0), (102,0), (452,0)]  # Define bullet offsets relative to the Boss
        self._lives = 100

    def awake(self, game_world) -> None:
        self.horizontal_movement = 100  # Initialize horizontal movement
        self._game_world = game_world
        sr = self.gameObject.get_component("SpriteRenderer")
        self.shoot = False
        self.nextShot = 0
        self.bulletIndex = 0
        self.nextBomb = 0
        
        #pygame.mixer.music.load("pyGame\Assets\BossShip/dangerSound.mp3")
        pygame.mixer.music.load("Assets\BossShip/dangerSound.mp3")
        # pygame.mixer.music.play(-1)

        # Initialize bullet positions based on the Boss's initial position
        self.update_bullet_positions()
        self.createDangerSign()

        self._screen_size = pygame.math.Vector2(game_world.screen.get_width(), game_world.screen.get_height())
        self.gameObject.transform.position = pygame.math.Vector2((game_world.screen.get_width()/2)-sr.sprite_image.get_width() / 2 , -208)
        
        self.gameObject.tag = "Enemy"
        
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
            self.dangerSign.destroy()
            self.shoot = True
            movement = pygame.math.Vector2(self.horizontal_movement * delta_time, 0)
            self.gameObject.transform.translate(movement)
            self.update_bullet_positions()

        self._keep_within_bounds(self.gameObject, self._game_world.screen.get_width())

        bottom_limit = self._screen_size.y
        if self.gameObject.transform.position.y > bottom_limit:
            self.gameObject.destroy()
        
        self._time_since_last_shot += delta_time
        self.nextShot += delta_time
        self.nextBomb += delta_time
        if self._time_since_last_shot >= self._shoot_delay and self.shoot:
            if self.nextShot >= 0.1:
                self.shoot_bullet()
                self.bulletIndex += 1
                self.nextShot = 0 
                if self.bulletIndex == 6:
                    self.bulletIndex = 0
                    self._time_since_last_shot = 0
                    self.shoot_missile(self.bulletList[6])    
                    self.shoot_missile(self.bulletList[7])   

        # if self.nextBomb >= 2:
        #     print("Shooting Bombs")
        #     self.shoot_bomb(self.bulletList[8])
        #     self.shoot_bomb(self.bulletList[9])
        #     self.nextBomb = 0

    def take_damage(self, damage_taken=1):  # ✅ Gør `damage_taken` valgfri, default = 1
        self._lives -= damage_taken
        print(f"Enemy was hit! Lives left: {self._lives}")

        if self._lives <= 0:
            self.destroy()
        
    def destroy(self):
        """Spil eksplosionseffekten, når fjenden dør"""
        # self._explosion_sound.play()
        self.gameObject.destroy()


    def shoot_bullet(self):
        self.projectile = GameObject(None)
        self.projectile.add_component(SpriteRenderer("/BossShip/bulletStart.png"))
        self.projectile.add_component(Projectile(500, None))
        animator = self.projectile.add_component(Animator())
        # animator.add_spritesheet_animation("Bullet", "pyGame/Assets/BossShip/bullet.png", 8, 32, 4)
        animator.add_spritesheet_animation("Bullet", "Assets/BossShip/bullet.png", 8, 32, 4)
        
        animator.play_animation("Bullet")
        self.projectile.add_component(Collider())
        self.projectile.tag = "EnemyProjectile" 
        self.projectile.transform.position = self.bulletList[self.bulletIndex]

        self._game_world.instantiate(self.projectile)

    def shoot_missile(self, pos):
        self.projectile = GameObject(None)
        self.projectile.add_component(SpriteRenderer("/BossShip/missileStart.png"))
        self.projectile.add_component(Projectile(500, self._game_world.get_player_position()))
        animator = self.projectile.add_component(Animator())
        # animator.add_spritesheet_animation("Missile", "pyGame/Assets/BossShip/missile.png", 22, 64, 3)
        animator.add_spritesheet_animation("Missile", "Assets/BossShip/missile.png", 22, 64, 3)

        animator.play_animation("Missile")
        self.projectile.add_component(Collider())
        self.projectile.tag = "MissileProjectile" 
        self.projectile.transform.position = pos

        self._game_world.instantiate(self.projectile)

    def shoot_bomb(self, pos):
        self.projectile = GameObject(None)
        self.projectile.add_component(SpriteRenderer("/BossShip/bomb animation/shot6_asset.png"))
        self.projectile.add_component(Projectile(250, None))
        animator = self.projectile.add_component(Animator())
        animator.add_animation("BombShot","/BossShip/bomb animation/shot6_1.png",
                               "/BossShip/bomb animation/shot6_2.png",
                               "/BossShip/bomb animation/shot6_3.png",
                               "/BossShip/bomb animation/shot6_4.png"
        )

        animator.add_animation("BombExp","/BossShip/bomb animation/shot6_exp1.png",
                               "/BossShip/bomb animation/shot6_exp2.png",
                               "/BossShip/bomb animation/shot6_exp3.png",
                               "/BossShip/bomb animation/shot6_exp4.png",
                               "/BossShip/bomb animation/shot6_exp5.png",
                               "/BossShip/bomb animation/shot6_exp6.png",
                               "/BossShip/bomb animation/shot6_exp7.png",
                               "/BossShip/bomb animation/shot6_exp8.png",
                               "/BossShip/bomb animation/shot6_exp9.png",
                               "/BossShip/bomb animation/shot6_exp10.png"          
        )
        
        animator.play_animation("BombShot")
            
        self.projectile.add_component(Collider())
        self.projectile.tag = "BombProjectile" 
        self.projectile.transform.position = pos

        self._game_world.instantiate(self.projectile)


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
    
    def createDangerSign(self):
        self.dangerSign = GameObject(None)
        sr = self.dangerSign.add_component(SpriteRenderer("/BossShip/danger.png"))
        animator = self.dangerSign.add_component(Animator())
        animator.add_animation("FlashDanger","/BossShip/danger.png", "/BossShip/danger.png","/BossShip/dangerEmpty.png","/BossShip/dangerEmpty.png")
        animator.play_animation("FlashDanger")
        self.dangerSign.tag = "UIElement" 
        self.dangerSign.transform.position = pygame.math.Vector2((self._game_world.screen.get_width()/2 - sr.sprite_image.get_width()/2) , 0)

        self._game_world.instantiate(self.dangerSign)

