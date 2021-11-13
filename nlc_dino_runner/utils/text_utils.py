import pygame
from nlc_dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = "freesansbold.ttf"
black_color = (0, 0, 0)

def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 22)
    text = font.render("Points : " + str(points), True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (1000, 20)
    return text, text_rect

def get_centred_message(message, width = SCREEN_WIDTH // 2, height = SCREEN_HEIGHT // 2):
    font = pygame.font.Font("freesansbold.ttf", 30)
    black_color = (0, 0, 0)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect
