import pygame
from GameObject import GameObject
from Components import Animator
from Components import SpriteRenderer
from Player import Player
from Background import Background
from Builder import PlayerBuilder
from Builder import EnemyBuilder
from ScoreManager import ScoreManager
from UIManager import UIManager
from Menu import Menu


class GameWorld:

    def __init__(self) -> None:
        
        pygame.mixer.init()
        pygame.init()

        # self.player = Player()
        self.font = pygame.font.SysFont("Arial", 30)
        print("test")
        # pygame.mixer.music.load("Pygame//assets/BackGroundMusic.mp3")
        pygame.mixer.music.load("assets/BackGroundMusic.mp3")

        # self.gamestate = 1
        # pygame.mixer.music.play(-1)
        self._screen = pygame.display.set_mode((1280,720))
        self._gameObjects = []
        self._colliders = []
        builder = PlayerBuilder()
        builder.build()

        self._gameObjects.append(builder.get_gameObject())

        
        # self._background = Background("pygame\\Assets\\Space1.jpg", self._screen, speed=2)
        self._background = Background("Assets\\Space1.jpg", self._screen, speed=2)

        builder = EnemyBuilder()
        builder.build("Dreadnought") 
        self._gameObjects.append(builder.get_gameObject())        
        builder.build("Scout")
        self._gameObjects.append(builder.get_gameObject())
        builder.build("Frigate")
        self._gameObjects.append(builder.get_gameObject())
        builder.build("Bomber")
        self._gameObjects.append(builder.get_gameObject())
        builder.build("Battlecruiser")
        self._gameObjects.append(builder.get_gameObject())
        builder.build("Fighter")
        self._gameObjects.append(builder.get_gameObject())
        builder.build("Torpedo_Ship")
        self._gameObjects.append(builder.get_gameObject())

        self._running = True
        self._clock = pygame.time.Clock()
        # self.Awake()
        # self.Start()
     

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

    def get_player(self):
        for gameObject in self._gameObjects:
            if gameObject.tag == "Player":
                # print(gameObject)
                return gameObject

    def Awake(self): 
        for gameObject in self._gameObjects[:]:
            gameObject.awake(self)
    
    def Start(self): 
        for gameObject in self._gameObjects[:]:
            gameObject.start()

        # self.get_player()
        
      

    def update(self):
        # while self.gamestate == 1:
     


        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running =False
           
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_o:
                        ScoreManager().increase_score()

                    if event.key == pygame.K_p:
                        ScoreManager().decrease_score()

                    if ScoreManager().score >= 10:
                        self.show_endgame_screens()
                        #Virker ikke, but who cares? --> self.score_manager.score = 0

                    # if event.key == pygame.K_q:
                    #     self.player._lives -= 1

                    # if self.player._lives <= 0:
                    #     self.show_gameover_screen()

            self._background.update()

            
            self._screen.fill("black")


            self._background.draw()

            ScoreManager().draw(self._screen)

            # self.player.draw(self._screen)


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

        
    def show_endgame_screens(self):
        from EndGameScreen import CompletedLevelScreen
        self.completed_screen = CompletedLevelScreen()
        self.completed_screen.run()

    def show_gameover_screen(self):
        from EndGameScreen import GameOverScreen
        self.gameover_screen = GameOverScreen()
        self.gameover_screen.run()


    def draw_lives(self):
        x_pos = 10
        y_pos = 30

        lives_text = self.font.render(f"Lives: {self.player.lives}", True, (255,255,255))
        self._screen.blit(lives_text, (x_pos, y_pos))

    # def run(self):
    #     pass
        # gw.Awake()
        # gw.Start()

        # while self._running:
        #     gw.update()

        # pygame.quit()
# gw = GameWorld()
# gw.Awake()
# gw.Start()

# gw.run()
menu = Menu()
menu.run()
# UI_manager = UIManager()
# UI_manager.handle_event()       