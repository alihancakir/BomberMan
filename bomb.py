import pygame
from box import Box
TILE_SIZE=40
box=Box()

turn_reduced=False     #add __init__
turn_reduced_toggle=False     #add __init__


class Bomb():

    def add_bomb_location(self,screen,bomb_info_from_player,player1_bomb_count,player2_bomb_count):

        self.player1_bomb_count=player1_bomb_count     #add __init__
        self.player2_bomb_count=player2_bomb_count     #add __init__

        font25 = pygame.font.Font(None, 25)     #add __init__
        font15 = pygame.font.Font(None, 25)     #add __init__

        bomb_info_text =font25.render(f"bomb_location:{bomb_info_from_player}", True, "black")
        screen.blit(bomb_info_text, (20, 50))

        bomb_info_text_count = font15.render(f"p1:{self.player1_bomb_count} p2:{self.player2_bomb_count}", True, "black")
        screen.blit(bomb_info_text_count, (20, 500))        

        global turn_reduced     #add __init__
        global turn_reduced_toggle     #add __init__


        ##drop bomb from player events
        for bomb_info in bomb_info_from_player:
            bomb_x,bomb_y,bomb_turn,bomb_by=bomb_info

            if bomb_by==1: ##added bomb by player1
                pygame.draw.circle(screen,"red",(bomb_x,bomb_y),15) 
                bomb_info_text_default = font15.render(f"{bomb_turn}", True, "white")
                screen.blit(bomb_info_text_default, (bomb_x-5, bomb_y-6))
            
            if bomb_by==2: ##added bomb by player1
                pygame.draw.circle(screen,"blue",(bomb_x,bomb_y),15) 
                bomb_info_text_default = font15.render(f"{bomb_turn}", True, "white")
                screen.blit(bomb_info_text_default, (bomb_x-5, bomb_y-6))

            if bomb_by==0:  ##default bombs      
                pygame.draw.circle(screen,"black",(bomb_x,bomb_y),15)        
                bomb_info_text_default = font15.render(f"{bomb_turn}", True, "white")
                screen.blit(bomb_info_text_default, (bomb_x-5, bomb_y-6))

                
                

            bomb_directions = { #if the bomb, near to other bombs                                            

                        "going right":  (bomb_x + 40, bomb_y     ),
                        "going left":   (bomb_x - 40, bomb_y     ),
                        "going up":     (bomb_x     , bomb_y - 40),
                        "going down":   (bomb_x     , bomb_y + 40)

                    }     
            #if player1_bomb_count==3:

            for direction, (x, y) in bomb_directions.items():                        
                    for bomb in bomb_info_from_player:
                        if (x, y) == (bomb[0], bomb[1]):
                            if bomb[3]==0:  ## check for able reduce. its mean, is it default bomb?...

                                bomb[2]-=1   

                                bomb_info_from_player.remove(bomb_info)     #removed player's bomb

                                bomb_info_text = font25.render(f"yakinda default bomba var", True, "blue")
                                screen.blit(bomb_info_text, (300, 10))

                                if bomb[2]==0:
                                    bomb_info_from_player.remove(bomb)      #removed default bomb, when turn is 0

                               
                                                                 
            

                        
                            


                             
        #to do:
        # 
        # explode added first bomb and maybe close other bomb when player's bomb count is 3
        # meabwhile decrease related default bomb turn if the turn is 0, explode it                       
                                


                               

                            
                            
                

                                                                                                


