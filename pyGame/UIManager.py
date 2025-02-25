import pygame
from Button import Button
# from GameWorld import GameWorld
from Player import Player

class UIManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UIManager, cls).__new__(cls)
            cls._instance._initialized = False  # Prevent re-initialization
        return cls._instance




    def __init__(self):
        #LOAD A FONT FOR UI ELEMENTS
        if not self._initialized:
            self._initialized = True
            self.font = pygame.font.Font(None,36)
            self.player = Player()

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

        self.completed_level_buttons = [
            Button(
                x = 150,
                y = 50,
                width  = 100,
                height = 50,
                text = "NEXT LEVEL",
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
        self.game_over_buttons = [
            Button(
                x = 150,
                y = 50,
                width  = 100,
                height = 50,
                text = "START OVER",
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

    def draw_gameover_buttons(self, screen):
        for button in self.game_over_buttons:
            button.draw(screen)

    def draw_completedlevel_buttons(self, screen):
        for button in self.completed_level_buttons:
            button.draw(screen)

    def handle_event(self, event):
        #CHECK BUTTON CLICKS
        for button in self.buttons + self.completed_level_buttons + self.game_over_buttons :
            if button.is_clicked(event):
                if button.text == "PLAY":
                    print("Starting Game")
                    from GameWorld import GameWorld 
                    game = GameWorld()
                    # game.run()
                    # game.Awake()
                    # game.Start()
                    game.update()
                    break
                
                elif button.text == "OPTIONS":
                    print("Options are for pussies and color blind people")
                    break
                #Break for at undgå dobbelt metode

                elif button.text == "QUIT":
                    pygame.quit()
                    break
                #Break for at undgå dobbelt metode

                elif button.text == "NEXT LEVEL":
                    #Still Need Method for this
                    
                    game = GameWorld()
                    # game.run()
                    # game.Awake()
                    # game.Start()
                    game.update()
                    break

                elif button.text == "START OVER":
                    print("Restarting...")
                    from GameWorld import GameWorld 
                    # game = GameWorld()
                    # game.run()
                    
