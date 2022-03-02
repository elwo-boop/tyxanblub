import pygame, sys
import random


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


white = (255, 255, 255)
black = (0, 0, 0)

def show_shape(shape):
    screen.blit(shape, (random.randint(200, 800), random.randint(100, 600)))
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    

    screen.fill(black)
    show_shape(orange_bolt)
    show_shape(red_tri)

    pygame.time.wait(1000)

