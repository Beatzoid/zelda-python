import enum
import pygame

from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):
        # Get the display surface
        self.display_surface = pygame.display.get_surface()

        # Sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # Sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if col == "x":
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])

                if col == "p":
                    Player((x, y), [self.visible_sprites])

    def run(self):
        # Update and draw the game
        self.visible_sprites.draw(self.display_surface)
