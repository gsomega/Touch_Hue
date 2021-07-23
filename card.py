import pygame
from pygame.sprite import Sprite


class Card(Sprite):
    def __init__(self, hue_settings, screen, location=(0, 0)):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(location[0], location[1], hue_settings.card_width, hue_settings.card_height)
        self.color = hue_settings.base_card_color

    def color_change(self, new_color):
        self.color = new_color

    def location_change(self, new_location):
        self.rect.left = new_location[0]
        self.rect.top = new_location[1]

    def get_location(self):
        return self.rect.left, self.rect.top

    def draw_card(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
