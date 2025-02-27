import pygame

#ScoreManager holder styr på score. Det er en singleton, så samme instans af score kan tilgås fra hele programmet.
#Dette bruges også til at resette score mellem runs
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

#Øg scoren ved dræbt fjende eller ramt boss
    def increase_score(self):
        self.score += 10

#- score hvis man rammer en fjende eller bliver ramt af et skud
    def decrease_score(self):
        self.score = max(0, self.score - 10)

    def draw(self, screen):
        score_text = f"Score: {self.score}"
        text_surface = self.font.render(score_text, True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))