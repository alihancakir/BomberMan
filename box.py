import pygame
import random
import time

SCREEN_WIDTH=600
SCREEN_HEIGHT=600
TILE_SIZE=40

box_location_handle= []

box_imagine = pygame.image.load("C:/Users/Nitro/Desktop/BomberMan3/pictures/box.png")
box_scaled_image = pygame.transform.scale(box_imagine, (40, 40))

explode_bomb_imagine = pygame.image.load("C:/Users/Nitro/Desktop/BomberMan3/pictures/blast.png")
explode_bomb_scaled_image = pygame.transform.scale(explode_bomb_imagine, (60, 60))

class Box():

    def draw_box(self,screen):
        self.screen= screen

        for index in range(0,len(box_location_handle)):
                x_location_start_box,y_location_start_box=box_location_handle[index]           
                for x in range(x_location_start_box,x_location_start_box+TILE_SIZE,TILE_SIZE):
                    for y in range(y_location_start_box,y_location_start_box+TILE_SIZE,TILE_SIZE):
                        screen.blit(box_scaled_image, (x, y)) 

    def add_box(self):
        added_random_box_location_x=random.randrange(0, 600, 40)  
        added_random_box_location_y=random.randrange(0, 640, 40)
        box_location_handle.append(((added_random_box_location_x),(added_random_box_location_y)))

                                                                 
############################################################################
#                                                                          #
#  # first in first out. First bomb will explode when bombs count is 3. #  #
#  # if the bomb near other bombs in PLUS(+) way, they are will explode.#  # 
#                                                                          #
############################################################################

    def remove_box(self,screen,player_bomb_info):

        self.screen=screen
        bomb_x,bomb_y=player_bomb_info
        
            
        delete_box_directions = {

            "going right":  (bomb_x + 20, bomb_y - 20),
            "going left":   (bomb_x - 60, bomb_y - 20),
            "going up":     (bomb_x - 20, bomb_y - 60),
            "going down":   (bomb_x - 20, bomb_y + 20)

        }

        for direction, (x, y) in delete_box_directions.items():
                   
                screen.blit(explode_bomb_scaled_image, (x, y))

                if (x, y) in box_location_handle:
                    box_location_handle.remove((x, y))

    def remove_box_default_bomb_location_event_check(self,screen,default_bomb_info):

        #self.font15 = pygame.font.Font(None, 25)
        for box_location_info in box_location_handle:
            box_x,box_y=box_location_info
            for def_bomb_info in default_bomb_info:
                if ((def_bomb_info[0])-20,(def_bomb_info[1])-20) == (box_x,box_y):
                    box_location_handle.remove((def_bomb_info[0]-20,def_bomb_info[1]-20))
                else:
                     print(f"LOGE:** no match between box and default bomb, on the same grid  **")

    def add_random_box(self,random_box_flag):

        global box_location_handle
         
        if random_box_flag == True:
            for index in range(0,5):

                added_random_box_location_x=random.randrange(40, 600, 40)  
                added_random_box_location_y=random.randrange(80, 640, 40)
                box_location_handle.append(((added_random_box_location_x),(added_random_box_location_y)))
                
        elif random_box_flag==False:
             box_location_handle= [
                
                                (40, 440),  (160, 120), (280, 80),  (40, 160),  (120, 240), (280, 440),
                                (40, 320),  (120, 480), (160, 400), (240, 200), (320, 160), (240, 320),
                                (360, 280), (440, 360), (480, 80),  (360, 320), (440, 160), (320, 520),
                                (160, 520), (120, 200), (40, 400),  (160, 360), (480, 320), (360, 240),
                                (40, 80),   (280, 200), (120, 40),  (440, 240), (120, 80),  (480, 200),
                                (320, 360), (280, 400), (360, 360), (400, 440)
            ]

            
              
            
         
                     
    def box_event(self):
        return box_location_handle
        