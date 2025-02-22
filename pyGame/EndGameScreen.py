import pygame
from UIManager import UIManager

class CompletedLevelScreen():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        self.UIManager = UIManager()
        self.running = True
    
    def run(self):
        while self.running:
            #FILL SCREEN WITH BACKGROUND COLOR
            self.screen.fill((30, 30, 30))
            #HANDLE EVENTS
            for event in pygame.event.get():
                #CHECK IF USER CLOSES THE WINDOW
                if event.type == pygame.QUIT:
                    self.running = False

                #HANDLE UI EVENTS
                self.UIManager.handle_event(event)

            #self.UIManager.dra(self.screen)

            pygame.display.flip()

        pygame.quit()


    def next_level(self):
        print("Loader næste level")
        self.running = False

############################################################


class GameOverScreen():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        self.UIManager = UIManager()
        self.running = True

    def run(self):
        while self.running:
            #FILL SCREEN WITH BACKGROUND COLOR
            self.screen.fill((30, 30, 30))
            #HANDLE EVENTS
            for event in pygame.event.get():
                #CHECK IF USER CLOSES THE WINDOW
                if event.type == pygame.QUIT:
                    self.running = False

                #HANDLE UI EVENTS
                self.UIManager.handle_event(event)

            self.UIManager.draw_gameover_buttons(self.screen)

            pygame.display.flip()

        pygame.quit()
    
    def start_over(self):
        print("Genstarter")
        self.running = False

if __name__ == "__main__":  
    GameOverScreen().run()


