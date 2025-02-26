import pygame

class ScoreManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ScoreManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.score = 0
            self.font = pygame.font.Font(None, 36)
            self._initialized = True

    def increase_score(self):
        self.score += 10

    def decrease_score(self):
        self.score = max(0, self.score - 10)

    def draw(self, screen):
        score_text = f"Score: {self.score}"
        text_surface = self.font.render(score_text, True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))