import pygame
import random
import time

from grid import Grid
from box import Box
from player import Player
from bomb import Bomb
#from ui import Ui

SCREEN_WIDTH=600
SCREEN_HEIGHT=600
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

font25 = pygame.font.Font(None, 25)

main_imagine = pygame.image.load("C:/Users/Nitro/Desktop/BomberMan3/pictures/main2.png")
main_scaled_image = pygame.transform.scale(main_imagine, (600, 600))

winner=None
running = True

enter_event_for_toggle=False

while running:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False

    keys= pygame.key.get_pressed()

    #main menu
    if enter_event_for_toggle==False:
        screen.fill("black")
        screen.blit(main_scaled_image, (5,100))
        enemy_text =font25.render(f"PRESS G", True, "white")
        screen.blit(enemy_text, (250, 500))
        
    if keys[pygame.K_g]:                                
        enter_event_for_toggle=True   
        
    if enter_event_for_toggle and not keys[pygame.K_g]:
             
        screen.fill("white")
        box.draw_box(screen)
        grid.draw_grid(screen)

        player.move(keys,screen)

        #players died check board
        player1_live_event,player2_live_event=bomb.live_event()

        if player1_live_event==3:                     
            winner="PLAYER 1"
        if player2_live_event==3:
            winner="PLAYER 2"

        p1_text =font25.render(f"SCORE: {player1_live_event}", True, "black")
        screen.blit(p1_text, (20, 20))

        p2_text =font25.render(f"SCORE: {player2_live_event}", True, "black")
        screen.blit(p2_text, (500, 20))

    pygame.display.flip()
    dt=clock.tick(FPS)/1000

pygame.quit()  

#####################################################################################################################
#                                                                                                                   #
#                                                                                                                   #
#        #to do:     #COMPLETED#                                                                                    #
#                                                                                                                   #
#       +    # if any plyayer close to default bomb(and turn is it 0 ?), the player will be died.                   #
#                                                                                                                   #
#       +    # if any player close to enemy player's first bomb or chain reaction bomb, the player will be died.    #
#                                                                                                                   #
#       +    # add score board.                                                                                     #
#                                                                                                                   #
#                                                                                                                   #
#####################################################################################################################
  