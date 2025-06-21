# This is where we run the game

# import necessary modules
import pygame
from settings import WIDTH, HEIGHT, FPS, BG_COLOR

from player import Player
from enemy import Enemy
from items import Item
from logic import check_item_collisions, check_enemy_collisions


# initialize pygame and create game window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# initialize player, enemy, and item
player = Player(100, 100)
enemy = Enemy(300, 200)
items = [
    Item(200, 100),
    Item(400, 150),
    Item(150, 300),
    Item(500, 250)
]


# initialize score and health
score = 0
health = 3
collected_items = set()
hit_enemies = set()

running = True
while running:
    # REORDER score text and draw images

    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    # update score and health
    score = check_item_collisions(player, items, score, collected_items)
    health = check_enemy_collisions(player, [enemy], health, hit_enemies)

    # draw the objects
    player.draw(screen)
    enemy.move(player)
    enemy.draw(screen)
    for item in items:
        item.draw(screen)

    # display score and health LAST so it stays visible
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    health_text = font.render(f"Health: {health}", True, (255, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(health_text, (10, 50))

    pygame.display.flip()
    clock.tick(FPS)


# quite pygame
pygame.quit()