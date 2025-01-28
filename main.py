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
running = True
dt=0

grid=Grid()
box= Box()  
player=Player()
bomb=Bomb()
#ui=Ui()

font15 = pygame.font.Font(None, 25)

while running:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False   
    screen.fill("white")

    box.draw_box(screen)
    grid.draw_grid(screen)


     
    
    keys= pygame.key.get_pressed()
    player.move(keys,screen)

    #players died check board
    player1_live_event,player2_live_event=bomb.live_event()
    enemy_text =font15.render(f"p1 live:{player1_live_event}, p2 live: {player2_live_event}", True, "red")
    screen.blit(enemy_text, (20, 20))

    pygame.display.flip()
    dt=clock.tick(FPS)/1000

pygame.quit()  



#####################################################################################################################
#                                                                                                                   #
#                                                                                                                   #
#        #to do:                                                                                                    #
#                                                                                                                   #
#            # if any plyayer close to default bomb(and turn is it 0 ?), the player will be died.
#                    #(currently i reached the player2 died algoritm)
#                                                                                                                   #
#            # if any player close to enemy player's first bomb or chain reaction bomb, the player will be died.    #
#                                                                                                                   #
#            # add score board.                                                                                     #
#                                                                                                                   #
#                                                                                                                   #
#                                                                                                                   #
#####################################################################################################################
  