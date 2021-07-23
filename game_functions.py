import sys
import pygame
from card import Card
from settings import Settings
from random import randint
from time import sleep


def check_events(hue_settings, cards, sel_card_indexes):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            select_card(hue_settings, cards, sel_card_indexes)


def select_card(hue_settings, cards, sel_card_indexes):
    pos = pygame.mouse.get_pos()
    selected = [cards.index(card) for card in cards if card.rect.collidepoint(pos)]
    if selected[0] not in hue_settings.locked_card_indexes:
        sel_card_indexes.append(selected[0])
        if len(sel_card_indexes) == 2:
            card_swap(cards, sel_card_indexes)
            sel_card_indexes.clear()
        elif len(sel_card_indexes) > 2:
            sel_card_indexes.clear()


def card_swap(cards, card_indexes):
    # swap location information
    pos1 = cards[card_indexes[0]].get_location()
    pos2 = cards[card_indexes[1]].get_location()
    cards[card_indexes[0]].location_change(pos2)
    cards[card_indexes[1]].location_change(pos1)
    # swap list information
    cards[card_indexes[0]], cards[card_indexes[1]] = cards[card_indexes[1]], cards[card_indexes[0]]


def create_board(hue_settings: Settings, screen, cards):
    for row_number in range(hue_settings.cards_in_height):
        for column_number in range(hue_settings.cards_in_width):
            card_left = column_number*hue_settings.card_width
            card_top = row_number*hue_settings.card_height
            location = (card_left, card_top)
            create_card(hue_settings, screen, cards, location, find_color_at_location(hue_settings, location))


def find_color_at_location(hue_settings, location):
    x = location[0]/hue_settings.screen_width
    y = location[1]/hue_settings.screen_height
    f1 = [(1 - x) * (1 - y) * i for i in hue_settings.TL_color]
    f2 = [x * (1 - y) * i for i in hue_settings.TR_color]
    f3 = [(1 - x) * y * i for i in hue_settings.BL_color]
    f4 = [x * y * i for i in hue_settings.BR_color]
    return tuple([f1[i] + f2[i] + f3[i] + f4[i] for i in range(3)])


def create_card(hue_settings, screen, cards, location, color):
    card = Card(hue_settings, screen, location)
    card.color_change(color)
    cards.append(card)


def update_screen(hue_settings: Settings, screen, cards):
    screen.fill(hue_settings.bg_color)

    # Redraw all cards
    for card in cards:
        card.draw_card()


def shuffle_board(cards, locked_card_indexes):
    number_of_cards = len(cards)
    for _ in range(200):
        index1 = randint(0, number_of_cards-1)
        index2 = randint(0,number_of_cards-1)
        if index1 != index2 and (index1 not in locked_card_indexes) and (index2 not in locked_card_indexes):
            card_swap(cards, [index1, index2])


def start_animation(screen):
    image = pygame.image.load('images/Title_Screen.bmp')
    rect = image.get_rect()
    screen_rect = screen.get_rect()
    rect.centerx = screen_rect.centerx
    rect.centery = screen_rect.centery
    for i in range(256):
        image.set_alpha(i)
        screen.blit(image,rect)
        pygame.display.flip()
    sleep(2)

def win_animation(screen):
    image = pygame.image.load('images/great_job.bmp')
    rect = image.get_rect()
    screen_rect = screen.get_rect()
    rect.centerx = screen_rect.centerx
    rect.centery = screen_rect.centery
    for i in range(256):
        image.set_alpha(i)
        screen.blit(image,rect)
        pygame.display.flip()
    sleep(2)


def randomize_colors(hs: Settings):
    hs.BR_color = randint(0, 100), randint(0, 100), randint(0, 255)
    hs.TR_color = randint(0, 100), randint(0, 255), randint(0, 100)
    hs.TL_color = randint(0, 255), randint(0, 100), randint(0, 100)
    hs.BL_color = randint(200, 255), randint(200, 255), randint(200, 255)


def restart_game(hue_settings, screen, cards):
    cards.clear()
    randomize_colors(hue_settings)
    create_board(hue_settings, screen, cards)

