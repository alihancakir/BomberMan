import pygame

SCREEN_WIDTH=600
SCREEN_HEIGHT=600
TILE_SIZE=40

class Grid():
    def draw_grid(self,screen):
        self.secreen= screen
        for x in range(0,SCREEN_WIDTH,TILE_SIZE):
            for y in range(0,SCREEN_HEIGHT,TILE_SIZE):
                rect= pygame.Rect(x,y,TILE_SIZE,TILE_SIZE)
                pygame.draw.rect(self.secreen,"black",rect,1)