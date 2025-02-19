import pygame
from Button import Button
from GameWorld import GameWorld

class UIManager:
    def __init__(self):
        #LOAD A FONT FOR UI ELEMENTS
        self.font = pygame.font.Font(None,36)

        #CREATE A LIST OF UI ELEMENTS
        self.buttons = [
            Button(
                x = 150,
                y = 50,
                width  = 100,
                height = 50,
                text = "PLAY",
                color = (0, 200, 255),
                hover_color = (0, 200, 255),
                text_color = (255, 255, 255),
                font = self.font
            ),
            Button(
                x = 150,
                y = 150,
                width  = 100,
                height = 50,
                text = "OPTIONS",
                color = (0, 200, 255),
                hover_color = (0, 200, 255),
                text_color = (255, 255, 255),
                font = self.font
            ),
            Button(
                x = 150,
                y = 250,
                width  = 100,
                height = 50,
                text = "QUIT",
                color = (0, 200, 255),
                hover_color = (0, 200, 255),
                text_color = (255, 255, 255),
                font = self.font
            )
        ]

    
    def draw(self, screen):
        #DRAW ALL BUTTONS
        for button in self.buttons:
            button.draw(screen)

    def handle_event(self, event):
        #CHECK BUTTON CLICKS
        for button in self.buttons:
            if button.is_clicked(event):
                if button.text == "PLAY":
                    print("Starting Game")
                    game = GameWorld()
                    game.run()
                
                elif button.text == "OPTIONS":
                    print("Options are for pussies and color blind people")

                elif button.text == "QUIT":
                    pygame.quit()
