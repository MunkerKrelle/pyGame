import pygame
from GameObject import GameObject
from Components import Animator
from Components import SpriteRenderer
from Player import Player
from Builder import BossBuilder, PlayerBuilder, EnemyBuilder
from Background import Background
from Builder import PlayerBuilder
from Builder import EnemyBuilder
from LevelManager import LevelManager
class GameWorld:

    def __init__(self) -> None:
        
        pygame.mixer.init()
        pygame.init()

        pygame.mixer.music.load("Pygame//assets/BackGroundMusic.mp3")
        
        pygame.mixer.music.play(-1)
        self._screen = pygame.display.set_mode((1280,720))
        self._gameObjects = []
        self._colliders = []
        builder = PlayerBuilder()
        builder.build()

        self._gameObjects.append(builder.get_gameObject())

        
        # builder = EnemyBuilder()
        # builder.build("Dreadnought")
        # self._gameObjects.append(builder.get_gameObject())        
        # builder.build("Scout")
        # self._gameObjects.append(builder.get_gameObject())
        # builder.build("Frigate")
        # self._gameObjects.append(builder.get_gameObject())
        # builder.build("Bomber")
        # self._gameObjects.append(builder.get_gameObject())
        # builder.build("Battlecruiser")
        # self._gameObjects.append(builder.get_gameObject())
        # builder.build("Fighter")
        # self._gameObjects.append(builder.get_gameObject())
        # builder.build("Torpedo_Ship")
        # self._gameObjects.append(builder.get_gameObject())

        builder = BossBuilder()
        builder.build()
        self._gameObjects.append(builder.get_gameObject())
        
        self._background = Background("pygame\\Assets\\Space1.jpg", self._screen, speed=2)

        #builder = EnemyBuilder()
        #builder.build("Dreadnought") 
        #self._gameObjects.append(builder.get_gameObject())        
        #builder.build("Scout")
        #self._gameObjects.append(builder.get_gameObject())
        #builder.build("Frigate")
        #self._gameObjects.append(builder.get_gameObject())
        #builder.build("Bomber")
        #self._gameObjects.append(builder.get_gameObject())
        #builder.build("Battlecruiser")
        #self._gameObjects.append(builder.get_gameObject())
        #builder.build("Fighter")
        #self._gameObjects.append(builder.get_gameObject())
        #builder.build("Torpedo_Ship")
        #self._gameObjects.append(builder.get_gameObject())

        self._level_manager = LevelManager(self)

        self._running = True
        self._clock = pygame.time.Clock()

    @property
    def screen(self):
        return self._screen
    
    @property
    def colliders(self):
        return self._colliders
    
    def instantiate(self, gameObject):
        gameObject.awake(self)
        gameObject.start()
        self._gameObjects.append(gameObject)


    def Awake(self): 
        for gameObject in self._gameObjects[:]:
            gameObject.awake(self)
    
    def Start(self): 
        for gameObject in self._gameObjects[:]:
            gameObject.start()

    def update(self):

        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running =False

            self._background.update()

            
            self._screen.fill("black")
            self._background.draw()

            self._level_manager.update()

            delta_time = self._clock.tick(60) / 1000.0

            
            for gameObject in self._gameObjects[:]:
                gameObject.update(delta_time)

            for i, collider1 in enumerate(self._colliders):
                for j in range(i + 1, len(self._colliders)):
                    collider2 = self._colliders[j]
                    collider1.collision_check(collider2)

            self._gameObjects = [obj for obj in self._gameObjects if not obj.is_destroyed]
            self._colliders = [col for col in self._colliders if not col.gameObject.is_destroyed]

            pygame.display.flip()
            self._clock.tick(60)

        pygame.quit()
    
    def get_player_position(self):
        for gameObject in self._gameObjects:
            if gameObject.tag == "Player":
                return gameObject.transform.position

gw = GameWorld()

gw.Awake()
gw.Start()
gw.update()

        