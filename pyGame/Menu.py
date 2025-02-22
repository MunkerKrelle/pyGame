import pygame
from UIManager import UIManager
from Button import Button
from GameWorld import GameWorld

class Menu():
    def __init__(self):
        pygame.init()

        #CREATE GAME WINDOW
        self.screen = pygame.display.set_mode((400, 300))

        #CREATE UIMANAGER INSTANCE
        self.ui_manager = UIManager()

        #CONTROL GAME LOOP
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
                self.ui_manager.handle_event(event)

            #DRAW ALL UI ELEMENTS
            self.ui_manager.draw(self.screen)

            #UPDATE DISPLAY
            pygame.display.flip()

        #QUIT PYGAME WHEN LOOP ENDS
        pygame.quit()

    def start_game(self):
        print("Starter spillet")
        self.running = False
        

if __name__ == "__main__":  
    Menu().run()
