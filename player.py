import pygame
import os
from enum import Enum


class State(Enum):
    NORMAL_FLAP = 1
    FLYING_FLAP = 2


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        path = os.path.join(os.getcwd(), "assets/Regular_flap.png")
        self.sprite_sheet = pygame.image.load(path).convert_alpha()

        # one block of the sprite sheet
        self.rect = (0, 0, 115, 80)

        self.curr_frame = 0
        self.total_time = 0

        self.x = 80
        self.y = 250

    def move(self):
        self.y -= 20

        # self.image = pygame.transform.rotate(self.sprite_sheet, 5)

    def update(self, dt):
        self.total_time += dt
        if self.total_time > 100000:
            self.total_time = 0

        # 2 is the number of flap animations
        self.curr_frame = (self.total_time // 85) % 2

        if self.curr_frame == 0:
            self.rect = (115, 0, 115, 80)
        else:
            self.rect = (0, 0, 115, 80)

    def draw(self, screen):
        screen.blit(self.sprite_sheet, (self.x, self.y), self.rect)
