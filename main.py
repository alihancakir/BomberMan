import pygame
import random
import time

from grid import Grid
from box import Box
from player import Player
from bomb import Bomb

SCREEN_WIDTH=600
SCREEN_HEIGHT=640
TILE_SIZE=40
FPS=100

pygame.init()
font = pygame.font.Font(None, 25)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("BomberMan")
dt=0

grid=Grid()
box= Box()  
player=Player()
bomb=Bomb()

font20 = pygame.font.Font(None, 20)
font25 = pygame.font.Font(None, 25)
font100= pygame.font.Font(None, 100)

main_imagine = pygame.image.load("C:/Users/Nitro/Desktop/BomberMan3/pictures/main2.png")
main_scaled_image = pygame.transform.scale(main_imagine, (600, 600))

running = True

enter_event_for_toggle=False

restart_event_toggle=False

game_finished=False

winner=None


main_default_bomb_location=[
                                ##theese bomb could be random location add in here
                                [20, 580, 1], [20, 380, 1], [20, 100, 3], [100, 60, 1], [100, 220, 2],
                                [300, 180, 2], [420, 140, 1], [420, 60, 1], [540, 260, 1], [540, 500, 3],
                                [300, 580, 2], [420, 540, 3], [460, 500, 1], [540, 380, 1], [540, 580, 3]
                            ]

while running:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False

    keys= pygame.key.get_pressed()

    #main menu
    if enter_event_for_toggle == False:
        screen.fill("black")
        screen.blit(main_scaled_image, (5,10))
        enemy_text =font25.render(f"PRESS G FOR GO", True, "white")
        screen.blit(enemy_text, (450, 620))
        
    #run game
    if keys[pygame.K_g]:
        enter_event_for_toggle=True
 
    if enter_event_for_toggle and not keys[pygame.K_g]:
        screen.fill("white")
        box.draw_box(screen)
        grid.draw_grid(screen)

        player.move(keys,screen,main_default_bomb_location)

        #players died board
        player1_live_event,player2_live_event=bomb.live_event()

        p1_text =font25.render(f"P1 SCORE: {(player1_live_event)}", True, "red")
        screen.blit(p1_text, (10, 15))

        p2_text =font25.render(f"P2 SCORE: {player2_live_event}", True, "blue")
        screen.blit(p2_text, (490, 15))

        if player1_live_event==3:
            winner="PLAYER 1"
            game_finished=True

        if player2_live_event==3:
            winner="PLAYER 2"
            game_finished=True

        if game_finished==True:

            screen.fill("black")
            winner_text =font100.render(f" {winner} WON", True, "red")
            screen.blit(winner_text, (20, 300))

    pygame.display.flip()
    dt=clock.tick(FPS)/1000

pygame.quit()  

#to do:
#
# start AI

  