import pygame
from settings import Settings
import game_functions as gf
from time import sleep


def run_game():
    pygame.init()
    hue_settings = Settings()
    screen = pygame.display.set_mode((hue_settings.screen_width, hue_settings.screen_height))
    cards = []
    selected_cards = []

    pygame.display.set_caption("Touch Hue")

    gf.create_board(hue_settings, screen, cards)
    board_solution = cards.copy()

    start = True

    while True:

        gf.check_events(hue_settings, cards, selected_cards)

        gf.update_screen(hue_settings, screen, cards)

        pygame.display.flip()

        if start:
            sleep(2)
            gf.shuffle_board(cards, hue_settings.locked_card_indexes)
            start = False

        if cards == board_solution:
            print("You win!!")


run_game()
