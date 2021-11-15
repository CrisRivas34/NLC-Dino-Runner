import pygame.time

from nlc_dino_runner.utils.constants import SMALL_CACTUS, LIFES
from nlc_dino_runner.Components.obstacles.cactus import Cactus


class ObstacleManager:

    def __init__(self):
        self.obstacles = []
        self.lifes = LIFES

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles.remove(obstacle)
                elif self.lifes > 0:
                    self.lifes -= 1
                    self.obstacles.remove(obstacle)
                else:
                    pygame.mixer.music.load("death_sound.mp3")
                    pygame.mixer.music.play(1)
                    pygame.mixer.music.set_volume(0.5)
                    pygame.time.delay(1000)
                    game.playing = False
                    game.death_count += 1
                    break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
