import pygame
from Builder import EnemyBuilder, BossBuilder
from PowerUpSelector import PowerUpSelector

class LevelManager:
    def __init__(self, game_world):
        self._game_world = game_world
        self._current_level = 1  
        self._enemies_per_level = 3  
        self._enemy_health_multiplier = 0 
        self.power_up = PowerUpSelector(self._game_world.get_player())
        self.spawn_enemies()
        # self.available_powers = PowerUpSelector()

    def spawn_enemies(self):
        """Spawner fjender baseret på level"""
        builder = EnemyBuilder()
        enemy_types = ["Dreadnought", "Scout", "Frigate", "Bomber", "Battlecruiser", "Fighter", "Torpedo_Ship"]

        print(f"Spawning {self._enemies_per_level} enemies for Level {self._current_level}")  # 🔍 Debugging

        for _ in range(self._enemies_per_level):
            enemy_type = enemy_types[_ % len(enemy_types)]  
            builder.build(enemy_type, 1)
            enemy = builder.get_gameObject()

            enemy_component = enemy.get_component(enemy_type)
            
                
                

            self._game_world.instantiate(enemy)



    def update(self):
        """Tjekker om alle fjender er døde og går til næste level"""
        enemies_left = any(obj.tag == "Enemy" for obj in self._game_world._gameObjects)
        if not enemies_left:
            print("No enemies left, advancing to next level...")
            # set extra condition for power up selected

            self.power_up.select_power()
            if self.power_up.get_power_picker == True:
                self.power_up.set_power_picker
                self.next_level()

    def clear_enemies(self):
        """Fjerner alle fjender fra spillet før næste level starter"""
        enemies_before = len([obj for obj in self._game_world._gameObjects if obj.tag == "Enemy"])
        self._game_world._gameObjects = [obj for obj in self._game_world._gameObjects if obj.tag != "Enemy"]
        self._game_world._colliders = [col for col in self._game_world._colliders if col.gameObject.tag != "Enemy"]
        enemies_after = len([obj for obj in self._game_world._gameObjects if obj.tag == "Enemy"])
        print(f"Cleared {enemies_before - enemies_after} enemies before next level.")

    def spawn_boss(self):
        builder = BossBuilder()
        builder.build()
        self._game_world.instantiate(builder.get_gameObject())   

    def next_level(self):
        """Skifter til næste level"""
        print(f"Level {self._current_level} complete! Starting Level {self._current_level + 1}...")

        self.clear_enemies()  

        self._current_level += 1
        self._enemies_per_level += 1  
        self._enemy_health_multiplier += 0.2  

        if self._current_level < 4:
            self.spawn_enemies()

        if self._current_level == 4:
            self.spawn_boss()
        
        # ADD END SCREEN AFTER BOSS
