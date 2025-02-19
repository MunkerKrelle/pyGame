import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, font):
        # Initialize button properties
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.text_color = text_color
        self.font = font

    def draw(self, screen):
        # Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Check if the mouse is hovering over the button
        if self.rect.collidepoint(mouse_pos):
            color = self.hover_color
        else:
            color = self.color

        # Draw the button rectangle
        pygame.draw.rect(screen, color, self.rect)

        # Render the button text
        text_surface = self.font.render(self.text, True, self.text_color)

        # Get the text rectangle and center it inside the button
        text_rect = text_surface.get_rect(center=self.rect.center)

        # Draw the text on the button
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        # Check if the event is a mouse button press
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click was inside the button
            if self.rect.collidepoint(event.pos):
                return True

        return False
