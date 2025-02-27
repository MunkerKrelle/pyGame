import pygame
from Builder import BossBuilder, PlayerBuilder
from Background import Background
from Builder import PlayerBuilder
from LevelManager import LevelManager
from PowerUpSelector import PowerUpSelector
from Builder import UIElementBuilder
from UIManager import UIManager
from ScoreManager import ScoreManager
from Menu import Menu, EndGameMenu

# Gameworld handles early initialization for things such as list of objects and colliders, instantiation of manager classes etc,
# whilst also retaining the core gameplay loop in update.
class GameWorld:

    def __init__(self) -> None:
        
        pygame.mixer.init()
        pygame.init()

        #pygame.mixer.music.load("Pygame//assets/BackGroundMusic.mp3")
        pygame.mixer.music.load("assets/BackGroundMusic.mp3")
        
        pygame.mixer.music.play(-1)
        self._screen = pygame.display.set_mode((1280,720))
        self._gameObjects = []
        self._colliders = []
        builder = PlayerBuilder()
        builder.build()
      
        self._gameObjects.append(builder.get_gameObject())
        self.stored_player = builder.get_gameObject()



        self._UI_element = UIElementBuilder()
        self._UI_element.build("shield.png", pygame.math.Vector2(100, 100), builder.get_gameObject())
        self._gameObjects.append(self._UI_element.get_gameObject())
        
        
        #self._background = Background("pygame\\Assets\\Space1.jpg", self._screen, speed=2)
        self._background = Background("Assets\\Space1.jpg", self._screen, speed=2)

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
    
    # Runs the core loop of the game, calls update on all gameobjects in the list, sets tick rate for fps, checks input for quitting the game,
    # draws the screen, checks collisions etc.
    def update(self):

        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running =False

            self._background.update()

            self._screen.fill("black")
            self._background.draw()
            
            ScoreManager().draw(self._screen)
            self._level_manager.draw(self._screen)

            self._level_manager.update()
        
            delta_time = self._clock.tick(60) / 1000.0
            
            for gameObject in self._gameObjects[:]:
                gameObject.update(delta_time)

            #checks collisions of objects.
            for i, collider1 in enumerate(self._colliders):
                for j in range(i + 1, len(self._colliders)):
                    collider2 = self._colliders[j]
                    collider1.collision_check(collider2)
            #removes objects and colliders from the list of active objects and colliders.
            self._gameObjects = [obj for obj in self._gameObjects if not obj.is_destroyed]
            self._colliders = [col for col in self._colliders if not col.gameObject.is_destroyed]

            pygame.display.flip()
            self._clock.tick(60)

        pygame.quit()
    
    def get_player_position(self):
        for gameObject in self._gameObjects:
            if gameObject.tag == "Player":
                return gameObject.transform.position
    
    def get_player(self):
        self.stored_player
        return self.stored_player
    
# runs the menu which the player can press play, options or quit 
Menu().run()

        