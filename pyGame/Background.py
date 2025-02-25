import pygame

class Background:
    def __init__(self, image_path, screen, speed):
        self.image = pygame.image.load(image_path).convert()
        self.screen = screen
        self.speed = speed
        self.y = 0  # Startposition for baggrunden

    def update(self):
        """Flytter baggrunden nedad og looper den"""
        self.y += self.speed
        if self.y >= self.screen.get_height():
            self.y = 0  # Reset når baggrunden er scrollet helt ned

    def draw(self):
        """Tegner baggrunden to gange for en sømløs loop-effekt"""
        self.screen.blit(self.image, (0, self.y))
        self.screen.blit(self.image, (0, self.y - self.screen.get_height()))