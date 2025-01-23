import pygame
from box import Box
TILE_SIZE=40
box=Box()

turn_reduced=False
turn_reduced_toggle=False


class Bomb():

    def add_bomb_location(self,screen,bomb_info_from_player):

        font25 = pygame.font.Font(None, 25)
        font15 = pygame.font.Font(None, 25)

        bomb_info_text =font25.render(f"bomb_location:{bomb_info_from_player}", True, "black")
        screen.blit(bomb_info_text, (20, 50))   

        global turn_reduced
        global turn_reduced_toggle


        ##drop bomb from player events
        for bomb_info in bomb_info_from_player:
            bomb_x,bomb_y,bomb_turn,bomb_by=bomb_info

            if bomb_by>0: ##added bombs
                pygame.draw.circle(screen,"black",(bomb_x,bomb_y),10) 
            else:  ##default bombs      
                pygame.draw.circle(screen,"black",(bomb_x,bomb_y),15)        
                bomb_info_text_default = font15.render(f"{bomb_turn}", True, "white")
                screen.blit(bomb_info_text_default, (bomb_x-5, bomb_y-6))
                

            bomb_directions = { #if the bomb, near to other bombs                                            

                        "going right":  (bomb_x + 40, bomb_y     ),
                        "going left":   (bomb_x - 40, bomb_y     ),
                        "going up":     (bomb_x     , bomb_y - 40),
                        "going down":   (bomb_x     , bomb_y + 40)

                    }     
            
            for direction, (x, y) in bomb_directions.items():                        
                    for bomb in bomb_info_from_player:
                        if (x, y) == (bomb[0], bomb[1]):
                            if bomb[3]==0:  ## check for able reduce. its mean, is it default bomb?...

                                bomb[2]-=1

                                bomb_info_from_player.remove(bomb_info)

                                bomb_info_text = font25.render(f"yakinda default bomba var", True, "blue")
                                screen.blit(bomb_info_text, (300, 10))

                                if bomb[2]==0:
                                    bomb_info_from_player.remove(bomb)

                      

                             
        #to do:
        # 
        # explode added first bomb and maybe close other bomb when palyer's bomb count is 3
        # meabwhile decrease related defauşt bomb turn and maybe explode it                       
                                


                               

                            
                            
                

                                                                                                


