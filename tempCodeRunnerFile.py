<<<<<<< HEAD
import pygame
import random
import time

from grid import Grid
from box import Box
from player import Player
from bomb import Bomb

SCREEN_WIDTH=600
SCREEN_HEIGHT=600
TILE_SIZE=40
FPS=60

pygame.init()
font = pygame.font.Font(None, 25)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt=0


grid=Grid()
box= Box()
player=Player()
bomb=Bomb()

while running:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False   
    screen.fill("white")


    box.draw_box(screen)
    grid.draw_grid(screen)
    
       

    keys= pygame.key.get_pressed()
    player.move(keys,screen)
    
    pygame.display.flip()
    dt=clock.tick(FPS)/1000

=======
import pygame
import random
import time

from grid import Grid
from box import Box
from player import Player
from bomb import Bomb

SCREEN_WIDTH=600
SCREEN_HEIGHT=600
TILE_SIZE=40
FPS=60

pygame.init()
font = pygame.font.Font(None, 25)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt=0


grid=Grid()
box= Box()
player=Player()
bomb=Bomb()

while running:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False   
    screen.fill("white")


    box.draw_box(screen)
    grid.draw_grid(screen)
    
       

    keys= pygame.key.get_pressed()
    player.move(keys,screen)
    
    pygame.display.flip()
    dt=clock.tick(FPS)/1000

>>>>>>> 7677db1 (stage4)
pygame.quit()