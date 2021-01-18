import sys, pygame, random

pygame.init()

size = width, height = 1080, 720
speed = [2, 2]
colors = {"black": [0,0,0], "red": [255, 0,0], "green": [0, 255, 0], "blue": [0,0,255], "white": [255, 255, 255]}
screen = pygame.display.set_mode(size)

screen.fill(colors["white"])

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pygame.display.flip()
