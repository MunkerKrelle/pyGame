import pygame
from UIManager import UIManager
from Button import Button

class Menu:
    _instance = None  # Class-level variable to hold the single instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  # Only create an instance if one doesn't exist
            cls._instance = super(Menu, cls).__new__(cls)
        return cls._instance  # Always return the same instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # Prevent multiple initializations
            pygame.init()
            self.screen = pygame.display.set_mode((400, 300))
            self.running = True
            self.initialized = True  # Mark as initialized

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
        print("Starting game")
        self.running = False

# if __name__ == "__main__":
#     Menu().run()


class EndGameMenu:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(EndGameMenu, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            pygame.init()
            self.screen = pygame.display.set_mode((400,300))
            self.font = pygame.font.Font(None, 36)
            self.running = True
            self._initialized = True

    def run(self):
        while self.running:
                self.screen.fill((30, 30, 30))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    UIManager().handle_endgame(event)

                UIManager().draw_end_screen(self.screen)
                pygame.display.flip()
