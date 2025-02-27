import pygame
from Builder import EnemyBuilder, BossBuilder
from PowerUpSelector import PowerUpSelector
from Menu import EndGameMenu

class LevelManager:
    
    #The LevelManager class controls game progression, enemy spawning, and power-up selection.
    
    #Features:
    #- Keeps track of the current level.
    #- Spawns enemies dynamically based on level progression.
    #- Increases enemy difficulty with each level.
    #- Allows the player to select power-ups between levels.
    #- Spawns a boss at a specific level.
    #- Ends the game when the final level is reached.
    

    def __init__(self, game_world):
        
        #Initializes the LevelManager.
        #- Sets starting level to 1.
        #- Starts with 3 enemies per level.
        #- Health multiplier increases enemy difficulty over time.
        #- Power-up system allows players to choose upgrades.
        
        self._game_world = game_world
        self._current_level = 1  # Start level
        self._enemies_per_level = 3  # Number of enemies per level
        self._enemy_health_multiplier = 0  # Multiplier for enemy HP
        self.power_up = PowerUpSelector(self._game_world.get_player())  # Handles power-up selection
        self.spawn_enemies()
        self.font = pygame.font.Font(None, 36)  # Font for displaying level UI

    #Property som bruges til at returnere level, som hjælper med at holde styr på game loop
    #Hvornår bosser skal spawnes, hvor mange levels før end game screen etc.
    @property
    def level(self):
        return self._current_level

    def spawn_enemies(self):
        
        #Spawns enemies based on the current level.
        #- Uses different enemy types to increase difficulty.
        #- The number of enemies increases as levels progress.
        
        builder = EnemyBuilder()
        enemy_types = ["Dreadnought", "Scout", "Frigate", "Bomber", "Battlecruiser", "Fighter", "Torpedo_Ship"]

        print(f"Spawning {self._enemies_per_level} enemies for Level {self._current_level}")  # 🔍 Debugging

        for _ in range(self._enemies_per_level):
            enemy_type = enemy_types[_ % len(enemy_types)]  # Cycle through enemy types
            builder.build(enemy_type, 1)
            enemy = builder.get_gameObject()

            enemy_component = enemy.get_component(enemy_type)

            self._game_world.instantiate(enemy)  # Add enemy to the game world

    def update(self):
        
        #Checks if all enemies are defeated to progress to the next level.
        #- Calls the power-up selection system before starting the next level.
        #- If power-up selection is confirmed, moves to the next level.
        
        enemies_left = any(obj.tag == "Enemy" for obj in self._game_world._gameObjects)
        if not enemies_left:
            print("No enemies left, advancing to next level...")

            # Activate power-up selection
            self.power_up.select_power()

            # Ensure power-up selection is completed before progressing
            if self.power_up.get_power_picker == True:
                self.power_up.set_power_picker
                self.next_level()

    def clear_enemies(self):
        
        #Clears all enemies from the game before progressing to the next level.
        #- Removes enemy objects from the game world.
        #- Also removes associated colliders to prevent lingering hitboxes.
        
        enemies_before = len([obj for obj in self._game_world._gameObjects if obj.tag == "Enemy"])
        self._game_world._gameObjects = [obj for obj in self._game_world._gameObjects if obj.tag != "Enemy"]
        self._game_world._colliders = [col for col in self._game_world._colliders if col.gameObject.tag != "Enemy"]
        enemies_after = len([obj for obj in self._game_world._gameObjects if obj.tag == "Enemy"])
        print(f"Cleared {enemies_before - enemies_after} enemies before next level.")

    def spawn_boss(self):
        
        #Spawns a boss at a specific level.
        #- Bosses are stronger than regular enemies.
        #- Only appears when the level requirement is met.
        
        builder = BossBuilder()
        builder.build()
        self._game_world.instantiate(builder.get_gameObject())

    def next_level(self):
        
        #Advances the game to the next level.
        #- Clears existing enemies.
        #- Increases the number of enemies per level.
        #- Increases enemy health using a multiplier.
        #- Spawns a boss at level 4.
        #- Ends the game at level 5.
        
        print(f"Level {self._current_level} complete! Starting Level {self._current_level + 1}...")

        self.clear_enemies()  # Remove all enemies before starting next level

        self._current_level += 1  # Increase level
        self._enemies_per_level += 1  # Increase enemy count
        self._enemy_health_multiplier += 0.2  # Enemies get stronger

        if self._current_level < 2:
            self.spawn_enemies()  # Spawn regular enemies

        if self._current_level == 2:
            self.spawn_boss()  # Spawn a boss

        if self._current_level == 5:
            EndGameMenu().run()  # Trigger the end game screen

    def draw(self, screen):
        
        #Displays the current level on the screen.
        #- Helps the player track game progress.
        
        level_text = f"Level: {self._current_level}"
        text_surface = self.font.render(level_text, True, (255, 255, 255))
        screen.blit(text_surface, (10, 40))
