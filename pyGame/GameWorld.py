import pygame
from GameObject import GameObject
from Components import Animator
from Components import SpriteRenderer
from Player import Player
from Builder import PlayerBuilder
from Builder import EnemyBuilder
from Background import Background  # Importér baggrundsklassen

class GameWorld:

    def __init__(self) -> None:
        # 🎵 Initialiser lydsystemet
        pygame.mixer.init()
        pygame.init()



        # 🎶 Indlæs baggrundsmusik (MP3 eller OGG)
        pygame.mixer.music.load("assets/BackGroundMusic.mp3")

        # 🔁 Afspil musikken i et uendeligt loop (-1 betyder "loop for evigt")
        pygame.mixer.music.play(-1)
        self._screen = pygame.display.set_mode((1280, 720))
        self._gameObjects = []
        self._colliders = []
        self._running = True
        self._clock = pygame.time.Clock()

        # Tilføj en scrollende baggrund
        self._background = Background("assets/Space1.jpg", self._screen, speed=2)

        # Byg spilleren
        builder = PlayerBuilder()
        builder.build()
        self._gameObjects.append(builder.get_gameObject())

        # Byg fjender
        builder = EnemyBuilder()
        builder.build("Dreadnought")
        self._gameObjects.append(builder.get_gameObject())        
        builder.build("Scout")
        self._gameObjects.append(builder.get_gameObject())
        builder.build("Frigate")
        self._gameObjects.append(builder.get_gameObject())
        builder.build("Bomber")
        self._gameObjects.append(builder.get_gameObject())

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
                    self._running = False

            # Opdater baggrunden
            #python GameWorld.py
            self._background.update()

            # Tegn baggrunden først
            self._screen.fill("black")
            self._background.draw()

            delta_time = self._clock.tick(60) / 1000.0

            # Opdater og tegn spilobjekter
            for gameObject in self._gameObjects[:]:
                gameObject.update(delta_time)

            # Tjek kollisioner
            for i, collider1 in enumerate(self._colliders):
                for j in range(i + 1, len(self._colliders)):
                    collider2 = self._colliders[j]
                    collider1.collision_check(collider2)

            # Fjern ødelagte objekter
            self._gameObjects = [obj for obj in self._gameObjects if not obj.is_destroyed]
            self._colliders = [col for col in self._colliders if not col.gameObject.is_destroyed]

            pygame.display.flip()
            self._clock.tick(60)

        pygame.quit()
    

gw = GameWorld()

gw.Awake()
gw.Start()
gw.update()
