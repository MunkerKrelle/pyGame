from Components import Component
import pygame
from GameObject import GameObject
from Components import Projectile
from Components import Collider
from Components import SpriteRenderer
from PowerUps import FireballPowerUp
from PowerUps import MultiShot
from PowerUps import SpeedPowerUp
from PowerUps import MoreLivesPowerUp
from Menu import EndGameMenu

class Player(Component):
    
    #The Player class controls the player character in the game.
    
    #Features:
    #- Movement and screen wrapping
    #- Shooting with cooldown and power-ups
    #- Taking damage and losing lives
    #- Power-ups to enhance abilities
    #- UI display for remaining lives
    

    def __init__(self):
        
        #Initialize the player with default values.
        #- Starts with 3 lives.
        #- Initializes font for displaying UI.
        
        self._lives = 3  # Player starts with 3 lives
        self.font = pygame.font.Font(None, 36)  # Font for displaying lives on screen

    bullet_sprite = "blank"  # Default bullet sprite (can be changed with power-ups)

    def awake(self, game_world):
        
        #Set up player properties when the game starts.
        #- Resets lives.
        #- Loads shooting and explosion sound effects.
        #- Determines screen size and initial position.
        #- Initializes power-up attributes (damage, speed, projectile type).
        
        self._lives = 3  # Reset lives when the player spawns
        self.gameObject.tag = "Player"  # Assign player tag for collision detection

        self._time_since_last_shot = 1  # Timer to handle shooting cooldown
        self._shoot_dealy = 0.1  # Time delay between shots
        self._game_world = game_world  # Store reference to game world

        # Load sound effects for shooting and explosions
        self._shoot_sound = pygame.mixer.Sound("Assets\\LaserSound.mp3")
        self._explosion_sound = pygame.mixer.Sound("Assets\\Explode.mp3")

        # Get sprite details for positioning
        sr = self._gameObject.get_component("SpriteRenderer")
        self._screen_size = pygame.math.Vector2(game_world.screen.get_width(), game_world.screen.get_height())
        self._sprite_size = pygame.math.Vector2(sr.sprite_image.get_width(), sr.sprite_image.get_height())

        # Set initial position of the player at the bottom center of the screen
        self._gameObject.transform.position.x = (self._screen_size.x / 2) - (self._sprite_size.x / 2)
        self._gameObject.transform.position.y = (self._screen_size.y) - (self._sprite_size.y * 2)

        # Power-up system
        global name
        name = "BasePowerUp"

        global damage
        damage = 0  # Default damage value

        global power
        power = self._gameObject.get_component(name)  # Get the power-up component
        damage = power.power_change()  # Update damage based on power-up
        print(damage)

        global speed
        speed = 300  # Default movement speed

    def start(self):
        """Runs once when the game starts."""
        pass

    def update(self, delta_time):
        
        #Handles player movement, shooting, and power-ups every frame.
        #- Movement: A (left), D (right), Screen Wrapping.
        #- Shooting: SPACE key.
        #- Power-ups: Activate with G, H, F, V keys.
        
        keys = pygame.key.get_pressed()
        movement = pygame.math.Vector2(0, 0)
        self._time_since_last_shot += delta_time  # Increment shot cooldown timer

        # Movement controls
        if keys[pygame.K_a]:
            movement.x -= speed  # Move left
        if keys[pygame.K_d]:
            movement.x += speed  # Move right

        # Shooting
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Power-ups activation
        if keys[pygame.K_g]:
            self.aqquire_fireball()
        if keys[pygame.K_h]:
            self.aqquire_multi_shot()
        if keys[pygame.K_f]:
            self.aqquire_speed_up()
        if keys[pygame.K_v]:
            self.aqquire_lives_up()

        # Apply movement
        self._gameObject.transform.translate(movement * delta_time)

        # Screen wrapping (player appears on the other side if moving off-screen)
        if self._gameObject.transform.position.x < -self._sprite_size.x:
            self._gameObject.transform.position.x = self._screen_size.x
        elif self._gameObject.transform.position.x > self._screen_size.x:
            self._gameObject.transform.position.x = -self._sprite_size.x

    @property
    def damage(self):
        """Returns the player's current damage value."""
        return self.damage

    def shoot(self):
        
        #Fires projectiles when SPACE is pressed.
        #- Uses power-up settings for damage, projectile amount, and spread.
        #- Plays a shooting sound effect.
        
        if self._time_since_last_shot >= self._shoot_dealy:
            for i in range(power.proj_amount):
                projectile = GameObject(None)
                sr = projectile.add_component(SpriteRenderer(power.sprite))

                # Create projectile with speed and damage from power-up
                projectile_component = projectile.add_component(Projectile(power.proj_speed, None, power.damage))

                # Set projectile position based on power-up shooting pattern
                projectile_position = power.unique_shoot(sr, self._sprite_size.x / 2, i, power.proj_amount, power.proj_spread_angle)
                projectile.transform.position = projectile_position

                projectile.add_component(Collider())  # Add collision component
                projectile.tag = "PlayerProjectile"  # Mark projectile for collision detection

                self._game_world.instantiate(projectile)

            self._shoot_sound.play()  # Play shooting sound effect
            self._time_since_last_shot = 0  # Reset cooldown

    # Power-up functions
    def aqquire_fireball(self):
        """Changes the player's projectiles to fireballs."""
        global power
        power = self._gameObject.get_component(FireballPowerUp.__name__)
        damage = power.power_change()

    def aqquire_multi_shot(self):
        """Enables the player to fire multiple projectiles at once."""
        global power
        power = self._gameObject.get_component(MultiShot.__name__)
        damage = power.power_change()

    def aqquire_speed_up(self):
        """Increases the player's movement speed."""
        global speed
        speed = self._gameObject.get_component(SpeedPowerUp.__name__)
        speed = speed.power_change()

    def aqquire_lives_up(self):
        """Grants the player extra lives when picking up a health power-up."""
        _lives = self._gameObject.get_component(MoreLivesPowerUp.__name__)
        temp = _lives.power_change()
        print(temp)
        self._lives += temp  # Increase player lives
        print(self._lives)

    # Damage and Game Over Functions
    def take_damage(self):
        
        #Handles damage when the player is hit.
        #- Reduces lives.
        #- Plays explosion sound.
        #- Calls game_over() if lives reach zero.
        
        self._lives -= 1
        self._explosion_sound.play()
        print(f"Player hit! Lives left: {self._lives}")
        if self._lives <= 0:
            self.game_over()

    def game_over(self):
        
        #Handles game over conditions.
        #- Removes the player from the game.
        #- Displays the end screen.
        
        print("Game Over!")
        self.gameObject.destroy()
        EndGameMenu().run()  # Call the end game menu

    # UI Functions
    def draw(self, screen):
        
        #Displays the player's remaining lives on the screen.
        
        score_text = f"Lives: {self._lives}"
        text_surface = self.font.render(score_text, True, (255, 255, 255))
        screen.blit(text_surface, (10, 40))
