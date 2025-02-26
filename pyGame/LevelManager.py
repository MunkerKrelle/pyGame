import pygame
from Builder import EnemyBuilder


class LevelManager:
    def __init__(self, game_world):
        self._game_world = game_world
        self._current_level = 1  
        self._enemies_per_level = 3  
        self._enemy_health_multiplier = 1  
        self.spawn_enemies()

    def spawn_enemies(self):
        """Spawner fjender baseret på level"""
        builder = EnemyBuilder()
        enemy_types = ["Dreadnought", "Scout", "Frigate", "Bomber", "Battlecruiser", "Fighter", "Torpedo_Ship"]

        print(f"Spawning {self._enemies_per_level} enemies for Level {self._current_level}")  # 🔍 Debugging

        for _ in range(self._enemies_per_level):
            enemy_type = enemy_types[_ % len(enemy_types)]  
            builder.build(enemy_type)
            enemy = builder.get_gameObject()

            enemy_component = enemy.get_component("Enemy")
            if enemy_component:
                # 🚀 Få fjendens BASE health
                base_health = enemy_component.get_base_health(enemy_type)  # ✅ Henter original HP
                enemy_component._lives = int(base_health * self._enemy_health_multiplier)  # 🔥 Skalerer liv
                print(f"Enemy {enemy_type} spawned with {enemy_component._lives} HP")  # Debugging

            self._game_world.instantiate(enemy)


    def update(self):
        """Tjekker om alle fjender er døde og går til næste level"""
        enemies_left = any(obj.tag == "Enemy" for obj in self._game_world._gameObjects)
        if not enemies_left:
            print("No enemies left, advancing to next level...")
            # set extra condition for power up selected
            self.next_level()

    def clear_enemies(self):
        """Fjerner alle fjender fra spillet før næste level starter"""
        enemies_before = len([obj for obj in self._game_world._gameObjects if obj.tag == "Enemy"])
        self._game_world._gameObjects = [obj for obj in self._game_world._gameObjects if obj.tag != "Enemy"]
        self._game_world._colliders = [col for col in self._game_world._colliders if col.gameObject.tag != "Enemy"]
        enemies_after = len([obj for obj in self._game_world._gameObjects if obj.tag == "Enemy"])
        print(f"Cleared {enemies_before - enemies_after} enemies before next level.")

    def next_level(self):
        """Skifter til næste level"""
        print(f"Level {self._current_level} complete! Starting Level {self._current_level + 1}...")

        self.clear_enemies()  

        self._current_level += 1
        self._enemies_per_level += 1  
        self._enemy_health_multiplier += 0.2  
    
        self.spawn_enemies()
