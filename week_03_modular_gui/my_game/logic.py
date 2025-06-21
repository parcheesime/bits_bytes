# logic.py
import pygame


def check_item_collisions(player, items, score, collected_items):
    for item in items[:]:  # Copy to avoid modification during loop
        if player.rect.colliderect(item.rect) and item not in collected_items:
            collected_items.add(item)
            items.remove(item)
            score += 1
    return score


def check_enemy_collisions(player, enemies, health, hit_enemies):
    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):
            if enemy not in hit_enemies:
                hit_enemies.add(enemy)
                health -= 1
        else:
            if enemy in hit_enemies:
                hit_enemies.remove(enemy)  # Reset for next possible hit
    return health
