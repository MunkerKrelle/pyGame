import pygame
from UIManager import UIManager
from Button import Button
from GameWorld import GameWorld

class Menu():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        self.running = True

    def run(self):
        while self.running:
            self.screen.fill((30, 30, 30))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                UIManager().handle_event(event)

            UIManager().draw(self.screen)

            pygame.display.flip()

        pygame.quit()

    def start_game(self):
        print("Starter spillet")
        self.running = False
        

if __name__ == "__main__":  
    Menu().run()
