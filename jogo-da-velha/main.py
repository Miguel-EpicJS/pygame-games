import sys, pygame, random
from draw_game_board import draw_game_board
from verify_if_click_is_inside_the_square_and_return_the_center import verify_if_click_is_inside_the_square_and_return_the_center

#Python
game = ['','','','','','','','','']
player = 0
#Pygame 
pygame.init()

size = width, height = 1080, 720 # WARNING DON'T CHANGE THIS!!!
speed = [2, 2]
colors = {"black": [0,0,0], "red": [255, 0,0], "green": [0, 255, 0], "blue": [0,0,255], "white": [255, 255, 255]}
screen = pygame.display.set_mode(size)

screen.fill(colors["white"])

draw_game_board(screen, colors["black"], 2)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if player % 2 == 0: 
                game[verify_if_click_is_inside_the_square_and_return_the_center(pygame.mouse.get_pos())[1]] = 'x'
                print(game)
                player += 1 
            else:
                game[verify_if_click_is_inside_the_square_and_return_the_center(pygame.mouse.get_pos())[1]] = 'o'
                print(game)
                player += 1 
    pygame.display.flip()
