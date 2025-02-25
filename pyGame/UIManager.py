import pygame
from Button import Button
from GameWorld import GameWorld
from Player import Player

class UIManager:
    def __init__(self):
        #LOAD A FONT FOR UI ELEMENTS
        self.font = pygame.font.Font(None,36)
        self.player = Player()
        global test
        test = 14
        global game
        # game = GameWorld()
        # global my_player
        # my_player = None
        # global component
        # component = None
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
            # Button(
            #     x = 150,
            #     y = 150,
            #     width  = 100,
            #     height = 50,
            #     text = "OPTIONS",
            #     color = (0, 200, 255),
            #     hover_color = (0, 200, 255),
            #     text_color = (255, 255, 255),
            #     font = self.font
            # ),
            # Button(
            #     x = 150,
            #     y = 250,
            #     width  = 100,
            #     height = 50,
            #     text = "QUIT",
            #     color = (0, 200, 255),
            #     hover_color = (0, 200, 255),
            #     text_color = (255, 255, 255),
            #     font = self.font
            # )
        ]

        self.completed_level_buttons = [
            Button(
                x = 50,
                y = 250,
                width  = 100,
                height = 50,
                text = "NEXT LEVEL",
                color = (0, 200, 255),
                hover_color = (0, 200, 255),
                text_color = (255, 255, 255),
                font = self.font
            ),
            # Button(
            #     x = 150,
            #     y = 150,
            #     width  = 100,
            #     height = 50,
            #     text = "OPTIONS",
            #     color = (0, 200, 255),
            #     hover_color = (0, 200, 255),
            #     text_color = (255, 255, 255),
            #     font = self.font
            # ),
            # Button(
            #     x = 150,
            #     y = 250,
            #     width  = 100,
            #     height = 50,
            #     text = "QUIT",
            #     color = (0, 200, 255),
            #     hover_color = (0, 200, 255),
            #     text_color = (255, 255, 255),
            #     font = self.font
            # ),
            Button( # sargons buttons for power up
                x = 300,
                y = 50,
                width  = 100,
                height = 50,
                text = "FIREBALL",
                color = (0, 200, 255),
                hover_color = (0, 200, 255),
                text_color = (255, 255, 255),
                font = self.font
            ),
        ]
        self.game_over_buttons = [
            # Button(
            #     x = 150,
            #     y = 50,
            #     width  = 100,
            #     height = 50,
            #     text = "START OVER",
            #     color = (0, 200, 255),
            #     hover_color = (0, 200, 255),
            #     text_color = (255, 255, 255),
            #     font = self.font
            # ),
            # Button(
            #     x = 150,
            #     y = 150,
            #     width  = 100,
            #     height = 50,
            #     text = "OPTIONS",
            #     color = (0, 200, 255),
            #     hover_color = (0, 200, 255),
            #     text_color = (255, 255, 255),
            #     font = self.font
            # ),
            # Button(
            #     x = 150,
            #     y = 250,
            #     width  = 100,
            #     height = 50,
            #     text = "QUIT",
            #     color = (0, 200, 255),
            #     hover_color = (0, 200, 255),
            #     text_color = (255, 255, 255),
            #     font = self.font
            # )
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
                    global game
                    game = GameWorld()
                    # global test
                    # test = test * 10
                    # print(test)
                    
                    game.run()
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
                    print("you didnt click on me, but im here")
                    game.run2()
                    
                    break

                # elif button.text == "START OVER":
                #     print("Restarting...")
                #     game = GameWorld()
                #     game.run()
                #     pass
                    
                
                elif button.text == "FIREBALL":
                    # test = test * 3
                    # print(mybob)
                    # self.player.aqquire_fireball()

                    my_player = game.test_returner()
                    component = my_player.get_component("Player")
                    print("fireball component was called.....")
                    component.aqquire_fireball()
                    # print(my_player)
                    # for component_name, component in my_player._components.items():
                        # print(f"{component_name}: {component}")


                    # print("you have been granted the power of balls of great fire!")
                    break
