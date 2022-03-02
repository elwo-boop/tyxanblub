import pygame, sys

from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

screen_width = 1200
screen_height = 900

screen = pygame.display.set_mode((screen_width, screen_height))
bloo_sq = pygame.image.load("bloo_sq.png").convert()
gren_star = pygame.image.load("gren_star.png").convert()
orange_bolt = pygame.image.load("orange_bolt.png").convert()
pink_circ = pygame.image.load("pink_circ.png").convert()
purp_heart = pygame.image.load("purp_heart.png").convert()
red_tri = pygame.image.load("red_tri.png").convert()
yell_hex = pygame.image.load("yell_hex.png").convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    

