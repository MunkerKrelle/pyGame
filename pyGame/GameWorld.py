import pygame
from GameObject import GameObject
from Components import Animator
from Components import SpriteRenderer
from Player import Player
from Builder import PlayerBuilder
from Builder import EnemyBuilder
from ScoreManager import ScoreManager


class GameWorld:

    def __init__(self) -> None:
        pygame.init()

        self._gameObjects = []
        self._colliders = []
        builder = PlayerBuilder()
        builder.build()

        self._gameObjects.append(builder.get_gameObject())

        builder = EnemyBuilder()
        builder.build()
        self._gameObjects.append(builder.get_gameObject())


        self._screen = pygame.display.set_mode((1280,720))
        self._running = True
        self._clock = pygame.time.Clock()

        self.score_manager = ScoreManager()
        self.player = Player()
        self.font = pygame.font.SysFont("Arial", 30)

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
    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_o:
                        self.score_manager.increase_score()

                    if event.key == pygame.K_p:
                        self.score_manager.decrease_score()

                    if self.score_manager.score >= 10:
                        self.show_endgame_screens()
                        #Virker ikke, but who cares? --> self.score_manager.score = 0

                    if event.key == pygame.K_q:
                        self.player._lives -= 1

                    if self.player._lives <= 0:
                        self.show_gameover_screen()

            


            self._screen.fill("cornflowerblue")

            self.draw_lives()

            delta_time = self._clock.tick(60) / 1000.0
            
            #draw your game
            for gameObject in self._gameObjects[:]:
                gameObject.update(delta_time)

            for i, collider1 in enumerate(self._colliders):
                for j in range(i + 1, len(self._colliders)):
                    collider2 = self._colliders[j]
                    collider1.collision_check(collider2)

            self._gameObjects = [obj for obj in self._gameObjects if not obj.is_destroyed]


            self.score_manager.draw(self._screen)

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

    def run(self):
        gw.Awake()
        gw.Start()



        while self._running:
            gw.update()
            
        pygame.quit()
    

gw = GameWorld()



        