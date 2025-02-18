import pygame
from GameObject import GameObject
class GameWorld:
    
    def __init__(self) -> None:
        pygame.init()
        self._gameObjects =[]

        self._gameObjects.append(GameObject(self))


        self._screen = pygame.display.set_mode((1280, 720))
        self._running = True
        self._clock = pygame.time.Clock()

    @property 
    def screen(self):
        return self._screen


    def Awake(self):
        pass

    def Start(self):
        pass

    def Update(self):

        while self._running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

            # fill the screen with a color to wipe away anything from last frame
            self._screen.fill("cornflowerblue")
            delta_time = self._clock.tick(60) / 1000.0
            
            #render your game here
            for gameObject in self._gameObjects:
                gameObject.update(delta_time)


            # flip() the display to put your work on screen
            pygame.display.flip()

            self._clock.tick(60)  # limits FPS to 60

        pygame.quit()

gw = GameWorld()

gw.Awake()
gw.Start()
gw.Update()