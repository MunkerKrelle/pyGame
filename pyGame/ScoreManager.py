import pygame

class ScoreManager:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)  # Font for displaying score

    def increase_score(self):
        self.score += 1

    def decrease_score(self):
        self.score = max(0, self.score - 1)  # Prevent negative score

    def draw(self, screen):
        score_text = f"Score: {self.score}"
        text_surface = self.font.render(score_text, True, (255, 255, 255))  # White text
        screen.blit(text_surface, (10, 10))  # Draw in top-left corner
