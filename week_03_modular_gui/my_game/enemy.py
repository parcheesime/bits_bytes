import pygame
import os
from settings import ENEMY_COLOR

class Enemy:
    def __init__(self, x, y):
        image_path = os.path.join(os.path.dirname(__file__), "assets", "Enemies", "spikeMan_jump.png")

        if os.path.exists(image_path):
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (50, 50))
        else:
            print(f"⚠️ Image not found at {image_path}, using fallback rectangle.")
            self.image = None

        self.rect = pygame.Rect(x, y, 50, 50)
        self.speed = 2

    def move(self, player):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        distance = max(1, (dx**2 + dy**2) ** 0.5)
        self.rect.x += int(self.speed * dx / distance)
        self.rect.y += int(self.speed * dy / distance)

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(screen, ENEMY_COLOR, self.rect)
