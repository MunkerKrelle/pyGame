from abc import ABC, abstractmethod
import pygame
import os

class Component(ABC):

    def __init__(self) -> None:
        super().__init__()
        self._gameObject = None

    @property
    def gameObject(self):
        return self._gameObject
    
    @gameObject.setter
    def gameObject(self,value):
        self._gameObject = value

    @abstractmethod
    def awake(self, game_world):
        pass
    
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self, delta_time):
        pass

class Transform(Component):

    def __init__(self, position) -> None:
        super().__init__()
        self._position = position

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self,value):
        self._position = value

    def translate(self, direction):
        self._position += direction

    @property
    def flip(self):
        return self._flip

    def awake(self, game_world):
        pass

    def start(self):
        pass
   
    def update(self, delta_time):
        pass 

#SpriteRenderer
class SpriteRenderer(Component):

    def __init__(self, sprite_name) -> None:
        super().__init__()

        #self._sprite_image = pygame.image.load(f"Assets\\{sprite_name}")
        self._sprite_image = pygame.image.load(f"pygame\\Assets\\{sprite_name}") # Jeres version
        #self._sprite_image = pygame.image.load(f"C:/AxP/Githubrepositories/Semester4/pyGame/pyGame/Assets/{sprite_name}") # Sargons Version
        self._sprite = pygame.sprite.Sprite()
        self._sprite.rect = self._sprite_image.get_rect()
        self._sprite_mask = pygame.mask.from_surface(self.sprite_image)
        # self._sprite_flip = pygame.transform.flip(self._sprite_image, False, False)

    @property
    def sprite_image(self):
        return self._sprite_image
    
    @property
    def sprite_mask(self):
        return self._sprite_mask
    
    @sprite_image.setter
    def sprite_image(self, value):
        self._sprite_image= value

    @property
    def sprite(self):
        return self._sprite
    
    # @property
    # def sprite_flip(self):
    #     return self._sprite_flip
    
    # @sprite_flip.setter
    # def sprite_flip(self, flip_vertical, flip_horizontal):
    #     self._sprite_flip = pygame.transform.flip(self._sprite_image, flip_vertical, flip_horizontal)
    
    def awake(self, game_world, ):
      self._game_world = game_world
      self._sprite.rect.topleft = self.gameObject.transform.position

    def start(self):
        pass
   
    def update(self, delta_time):
        self._sprite.rect.topleft = self.gameObject.transform.position
        self._game_world.screen.blit(self._sprite_image,self._sprite.rect) 

class Animator(Component):

    def __init__(self) -> None:
        super().__init__()
        self._animations = {}
        self._current_animation = None
        self._animation_time = 0
        self._current_frame_index = 0

    def add_animation(self, name, *args):
        frames = []
        for arg in args:
            #sprite_image = pygame.image.load(f"Assets\\{arg}")
            sprite_image = pygame.image.load(f"pygame\\Assets\\{arg}") # Jeres version
            #sprite_image = pygame.image.load(f"C:/AxP/Githubrepositories/Semester4/pyGame/pyGame/Assets/{arg}") # SARGONS VERSION
            frames.append(sprite_image)
        
        self._animations[name] = frames

    def add_spritesheet_animation(self, name, spritesheet_path, frame_width, frame_height, frame_count):
        spritesheet = pygame.image.load(spritesheet_path)
        frames = []
        for i in range(frame_count):
            frame_rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame_image = spritesheet.subsurface(frame_rect)
            frames.append(frame_image)
        
        self._animations[name] = frames

    def play_animation(self, animation):
        self._current_animation = animation
        self._current_frame_index = 0  # Reset frame index when playing a new animation

    def awake(self, game_world):
        self._sprite_renderer = self._gameObject.get_component("SpriteRenderer")
    
    def start(self):
        pass

    def update(self, delta_time):
        frame_duration = 0.1
        self._animation_time += delta_time

        if self._animation_time >= frame_duration:
            self._animation_time = 0
            self._current_frame_index += 1
            
            animation_sequence = self._animations[self._current_animation]

            if self._current_frame_index >= len(animation_sequence):
                self._current_frame_index = 0  # Reset animation
            
            self._sprite_renderer.sprite_image = animation_sequence[self._current_frame_index]
            
    



class Laser(Component):
    def init(self, speed):
        self.speed = speed

    def awake(self, game_world):
        pass

    def start(self):
        pass

    def update(self, delta_time):
        movement = pygame.math.Vector2(0, - self.speed)
        self._gameObject.transform.translate(movement * delta_time)

        if self.gameObject.tag == "EnemyProjectile":
            movement.y = self.speed * 2 # Fjendens skud skal bevæge sig nedad

        self._gameObject.transform.translate(movement * delta_time)

        if self._gameObject.transform.position.y < 0:
            self._gameObject.destroy()


class Collider(Component):  
    def __init__(self) -> None:
        super().__init__()  
        self._other_colliders = []
        self._other_masks = []
        self._listeners = {}


    def awake(self, game_world):
        sr = self.gameObject.get_component("SpriteRenderer")
        self._collision_box = sr.sprite.rect
        self._sprite_mask = sr.sprite_mask
        print(self._collision_box)
        game_world.colliders.append(self)
        
    @property
    def collision_box(self):
        return self._collision_box
    
    @property 
    def sprite_mask(self):
        return self._sprite_mask

    def subscribe(self, service, method):
        self._listeners[service] = method
    
    def collision_check(self, other):
        is_rect_colliding = self._collision_box.colliderect(other.collision_box)
        is_already_colliding = other in self._other_colliders
            
        if is_rect_colliding:
            
            if not is_already_colliding:
                self.collision_enter(other)
                other.collision_enter(self)

            if self.check_pixel_collision(self._collision_box, other.collision_box, self._sprite_mask, other.sprite_mask):
                if other not in self._other_masks:
                    self.pixel_collision_enter(other)
                    other.pixel_collision_enter(self)
            else:
                if other in self._other_masks:
                    self.pixel_collision_exit(other)
                    other.pixel_collision_exit(self)
        else:
            if is_already_colliding:
                self.collision_exit(other)
                other.collision_exit(self)


    def check_pixel_collision(self, collision_box1, collision_box2, mask1, mask2):
        offset_x = collision_box2.x - collision_box1.x
        offset_y = collision_box2.y - collision_box1.y
        return mask1.overlap(mask2, (offset_x, offset_y)) is not None

    def start(self):
        pass

    def update(self, delta_time):
        pass

    def collision_enter(self, other):
        self._other_colliders.append(other)
        
        if self.gameObject.tag == "Player" and other.gameObject.tag == "EnemyProjectile":
            # print("player is hit")
            player = self.gameObject.get_component("Player")  
            if player:
                player.take_damage()  
                other.gameObject.destroy()
                print("player is hit")
        
        if self.gameObject.tag == "Enemy" and other.gameObject.tag == "PlayerProjectile":
            other.gameObject.destroy()
            self.gameObject.destroy()

            # for component_name, component in self.gameObject._components.items():
            #     print(f"{component_name}: {component}")         

        if self.gameObject.tag == "Player" and other.gameObject.tag == "Enemy":
            print("player flew into enemy")
            # player = self.gameObject.get_component("Player")  
            # if player:
            #     player.take_damage()  
            #     other.gameObject.destroy()
            #     print("player flew into enemy")
        

        if "collision_enter" in self._listeners:
            self._listeners["collision_enter"](other)

    def collision_exit(self, other):
        # print(other)
        self._other_colliders.remove(other)
        if "collision_exit" in self._listeners:
            self._listeners["collision_exit"](other)

    def pixel_collision_enter(self, other):
        # print(other)
        self._other_masks.append(other)
        if "pixel_collision_enter" in self._listeners:
            self._listeners["pixel_collision_enter"](other)

    def pixel_collision_exit(self, other):
        # print(other)
        self._other_masks.remove(other)
        if "pixel_collision_exit" in self._listeners:
            self._listeners["pixel_collision_exit"](other)
            
