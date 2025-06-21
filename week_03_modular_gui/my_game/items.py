import pygame
import os


class Item:
    def __init__(self, x, y):
        # Safe and correct image path
        image_path = os.path.join(os.path.dirname(__file__), "assets", "Items", "carrot_gold.png")

        if os.path.exists(image_path):
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (30, 30))  # resize if needed
        else:
            print(f"⚠️ Image not found at {image_path}, using fallback rectangle.")
            self.image = None

        self.rect = pygame.Rect(x, y, 30, 30)

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(screen, (255, 255, 0), self.rect)  # fallback yellow square
