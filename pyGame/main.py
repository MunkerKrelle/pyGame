import pygame
import sys
from menu_scene import MenuScene
from game_world_scene import GameWorldScene

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scene-Based Game")

# Global scene manager
class SceneManager:
    def __init__(self):
        self.current_scene = MenuScene(self)

    def go_to(self, scene):
        self.current_scene = scene

scene_manager = SceneManager()

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        scene_manager.current_scene.handle_event(event)

    scene_manager.current_scene.update()
    scene_manager.current_scene.render(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
