import pygame
import os

class Player:
    def __init__(self, x, y):
        # Use file-relative path to avoid my_game/my_game issues
        image_path = os.path.join(os.path.dirname(__file__), "assets", "Players", "bunny2_ready.png")

        if os.path.exists(image_path):
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (50, 50))
        else:
            print(f"⚠️ Image not found at {image_path}, using fallback.")
            self.image = pygame.Surface((50, 50))
            self.image.fill((255, 0, 0))  # red square fallback

        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
