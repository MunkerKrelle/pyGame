import pygame
from Button import Button
from ScoreManager import ScoreManager

#Klassen er en singleton
#Denne klasse opretter knapper samt kalder buttons draw metode
#Den tegner også alle skærme samt håndterer tryk på de forskellige knapper
#Med dette tænkes der på de forskellige klassers run metode, fx menu, options og endgame
class UIManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UIManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

#Constructoren opretter de forskellige lister af knapper, som skal vises alt efter hvilken skærm der vises
    def __init__(self):
        if not self._initialized:
            self._initialized = True
            self.font = pygame.font.Font(None, 36)

            self.buttons = [
                Button(
                    x=150,
                    y=50,
                    width=100,
                    height=50,
                    text="PLAY",
                    color=(0, 200, 255),
                    hover_color=(0, 200, 255),
                    text_color=(255, 255, 255),
                    font=self.font
                ),
                Button(
                    x=150,
                    y=150,
                    width=100,
                    height=50,
                    text="OPTIONS",
                    color=(0, 200, 255),
                    hover_color=(0, 200, 255),
                    text_color=(255, 255, 255),
                    font=self.font
                ),
                Button(
                    x=150,
                    y=250,
                    width=100,
                    height=50,
                    text="QUIT",
                    color=(0, 200, 255),
                    hover_color=(0, 200, 255),
                    text_color=(255, 255, 255),
                    font=self.font
                )
            ]
            self.end_buttons = [
                Button(
                    x=150,
                    y=50,
                    width=100,
                    height=50,
                    text="GO AGAIN",
                    color=(0, 200, 255),
                    hover_color=(0, 200, 255),
                    text_color=(255, 255, 255),
                    font=self.font
                ),
                Button(
                    x=150,
                    y=150,
                    width=100,
                    height=50,
                    text="OPTIONS",
                    color=(0, 200, 255),
                    hover_color=(0, 200, 255),
                    text_color=(255, 255, 255),
                    font=self.font
                ),
                Button(
                    x=150,
                    y=250,
                    width=100,
                    height=50,
                    text="QUIT",
                    color=(0, 200, 255),
                    hover_color=(0, 200, 255),
                    text_color=(255, 255, 255),
                    font=self.font
                )
            ]
            self.options_buttons = [
                Button(
                    x=150,
                    y=50,
                    width=100,
                    height=50,
                    text="PLAY",
                    color=(0, 200, 255),
                    hover_color=(0, 200, 255),
                    text_color=(255, 255, 255),
                    font=self.font
                ),
                Button(
                    x=150,
                    y=250,
                    width=100,
                    height=50,
                    text="QUIT",
                    color=(0, 200, 255),
                    hover_color=(0, 200, 255),
                    text_color=(255, 255, 255),
                    font=self.font
                )
            ]
    
    def draw(self, screen):
        #DRAW ALL BUTTONS
        for button in self.buttons:
            button.draw(screen)

    def draw_end_screen(self, screen):
        for button in self.end_buttons:
            button.draw(screen)
        score_text = self.font.render(f"Final Score: {ScoreManager().score}", True, (255, 255, 255))
        text_rect = score_text.get_rect(topleft=(10, 10))
        screen.blit(score_text, text_rect)

    def draw_options(self, screen):
        for button in self.options_buttons:
            button.draw(screen)

        options_lines =[
            "These are the options",
            "Change your gamma and whatever",
            "You can also change volume",
            "When we feel like adding it"
        ]
        y = 350

        for line in options_lines:
            options_text = self.font.render(line, True, (255,255,255))
            text_rect = options_text.get_rect(topleft=(10, y))
            screen.blit(options_text, text_rect)
            y += 30

#Alle handle_event metoder står for at køre relevante funktioner alt efter hvilke knapper der trykkes på
    def handle_event(self, event):
        for button in self.buttons:
            if button.is_clicked(event):
                if button.text == "PLAY":
                    print("Starting Game")
                    from GameWorld import GameWorld 
                    game = GameWorld()
                    game.Awake()
                    game.Start()
                    game.update()
                    break
                
                elif button.text == "OPTIONS":
                    from Menu import Options
                    Options().run()
                    break
                #Break for at undgå dobbelt metode

                elif button.text == "QUIT":
                    pygame.quit()
                    break
                #Break for at undgå dobbelt metode

    def handle_endgame(self, event):
        for button in self.end_buttons:
            if button.is_clicked(event):
                if button.text == "GO AGAIN":
                    print("Starting Game")
                    from GameWorld import GameWorld 
                    game = GameWorld()
                    ScoreManager().score = 0
                    game.Awake()
                    game.Start()
                    game.update()
                    break

                elif button.text == "OPTIONS":
                        from Menu import Options
                        Options().run()
                        break
                    #Break for at undgå dobbelt metode

                elif button.text == "QUIT":
                    pygame.quit()
                    break
                    #Break for at undgå dobbelt metode

    def handle_options(self, event):
        for button in self.options_buttons:
            if button.is_clicked(event):
                if button.text == "PLAY":
                    from GameWorld import GameWorld 
                    game = GameWorld()
                    ScoreManager().score = 0
                    game.Awake()
                    game.Start()
                    game.update()
                    break
                if button.text == "QUIT":
                    pygame.quit()
                    break
