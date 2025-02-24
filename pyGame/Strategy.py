import pygame
import random
import math

class Strategy():
    def __init__(self) -> None:
        super().__init__()
        self.horizontal_movement = 0  # Initialize horizontal movement

    def attack(self):
        pass

    def move(self, game_object, delta_time, game_world):
        pass

    def die(self):
        pass

    def _keep_within_bounds(self, game_object, screen_width):
        # Ensure the game object stays within the screen bounds on the x-axis and change direction if needed
        if game_object.transform.position.x < 0:
            game_object.transform.position.x = 0
            self.horizontal_movement = abs(self.horizontal_movement)  # Change direction to right
        elif game_object.transform.position.x > screen_width - game_object.get_component("SpriteRenderer").sprite_image.get_width():
            game_object.transform.position.x = screen_width - game_object.get_component("SpriteRenderer").sprite_image.get_width()
            self.horizontal_movement = -abs(self.horizontal_movement)  # Change direction to left

class Battlecruiser(Strategy):
    def move(self, game_object, delta_time, game_world):
        # Battlecruisers move straight down
        speed = 50
        movement = pygame.math.Vector2(0, speed * delta_time)
        game_object.transform.translate(movement)
        self._keep_within_bounds(game_object, game_world.screen.get_width())

class Dreadnought(Strategy):
    def move(self, game_object, delta_time, game_world):
        # Dreadnoughts move straight down, faster
        speed = 75
        movement = pygame.math.Vector2(0, speed * delta_time)
        game_object.transform.translate(movement)
        self._keep_within_bounds(game_object, game_world.screen.get_width())

class Bomber(Strategy):
    def move(self, game_object, delta_time, game_world):
        # Bombers move in a zig-zag pattern
        speed = 60
        movement = pygame.math.Vector2(0, speed * delta_time)

        # Change direction more frequently (every 0.2 seconds)
        if random.randint(0, 30) == 0:  # 30 frames per second = 0.2 seconds
            self.horizontal_movement = random.choice([-1, 1]) * speed * delta_time

        movement.x = self.horizontal_movement  # Apply horizontal movement
        game_object.transform.translate(movement)
        self._keep_within_bounds(game_object, game_world.screen.get_width())

class Fighter(Strategy):
    def __init__(self):
        self.change_direction_timer = 0
        self.change_direction_interval = 2  # Change direction every 2 seconds
        self.current_movement = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.descent_speed = 50  # Adjust this value for desired downward speed
        self.horizontal_movement = 0  # Initialize horizontal movement

    def move(self, game_object, delta_time, game_world):
        # Fighters move randomly with a downward bias
        speed = 100

        # Update change direction timer
        self.change_direction_timer += delta_time

        # Check if it's time to change direction
        if self.change_direction_timer >= self.change_direction_interval:
            # Reset timer
            self.change_direction_timer = 0
            # Change direction (with a downward bias)
            self.current_movement = pygame.math.Vector2(
                random.uniform(-1, 1), random.uniform(0, 1)  # Y component is always positive
            )

        # Apply the current movement vector
        movement = self.current_movement * speed * delta_time
        movement.y += self.descent_speed * delta_time  # Add downward movement

        game_object.transform.translate(movement)
        self._keep_within_bounds(game_object, game_world.screen.get_width())


class Torpedo_Ship(Strategy):
    def move(self, game_object, delta_time, game_world):
        # Torpedo ships move straight down, with occasional turns
        speed = 80
        movement = pygame.math.Vector2(0, speed * delta_time)

        # Turn randomly
        if random.randint(0, 20) == 0:
            self.horizontal_movement = random.choice([-1, 1]) * speed * delta_time

        movement.x = self.horizontal_movement  # Apply horizontal movement
        game_object.transform.translate(movement)
        self._keep_within_bounds(game_object, game_world.screen.get_width())

class Frigate(Strategy):
    def __init__(self):
        self.wave_amplitude = 10  # Reduced amplitude for smoother movement
        self.wave_frequency = 0.05
        self.initial_y = 0  # Store the initial y position
        self.horizontal_movement = 0  # Initialize horizontal movement

    def move(self, game_object, delta_time, game_world):
        # Frigates move in a wave-like pattern
        speed = 60  # Reduced speed for slower movement
        movement = pygame.math.Vector2(0, speed * delta_time)

        # Calculate the wave movement based on the initial y position
        wave_offset = self.wave_amplitude * math.sin(self.initial_y * self.wave_frequency)
        movement.x = wave_offset  # Apply wave movement to x

        # Apply the calculated movement
        game_object.transform.translate(movement)
        self._keep_within_bounds(game_object, game_world.screen.get_width())

        # Update the initial y position for the next frame
        self.initial_y += speed * delta_time

class Scout(Strategy):
    def __init__(self):
        self.loop_radius = 2  # Radius of the loop
        self.loop_speed = 1  # Speed of the loop rotation (radians per frame)
        self.loop_angle = 0  # Current angle of the loop
        self.descent_speed = 40  # Vertical descent speed

    def move(self, game_object, delta_time, game_world):
        # Calculate the position on the loop
        loop_x = self.loop_radius * math.cos(self.loop_angle)
        loop_y = self.loop_radius * math.sin(self.loop_angle)

        # Update the loop angle
        self.loop_angle += self.loop_speed * delta_time

        # Create the movement vector
        movement = pygame.math.Vector2(loop_x, loop_y)
        movement.y += self.descent_speed * delta_time  # Add vertical descent

        # Apply the movement
        game_object.transform.translate(movement)
        # self._keep_within_bounds(game_object, game_world.screen.get_width())