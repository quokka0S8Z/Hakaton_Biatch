import pygame
class HealthBar:
    def __init__(self, player):
        self.player = player
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (20, 20, 200, 20))
        pygame.draw.rect(screen, (0, 255, 0), (20, 20, 2 * self.player.health, 20))
