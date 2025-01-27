import pygame
from box import Box
#TILE_SIZE=40
box=Box()

first_added_bomb_from_player1=[]

index_handle=0



flag_first_added_from_player1=False

class Bomb():
    #def __init__(self):
              

    def add_bomb_location(self,screen,bomb_info_from_player,player1_bomb_count,player2_bomb_count):

        self.player1_bomb_count=player1_bomb_count    
        self.player2_bomb_count=player2_bomb_count 

        self.font25 = pygame.font.Font(None, 25)      
        self.font15 = pygame.font.Font(None, 25)    

        bomb_info_text =self.font25.render(f"bomb_location:{bomb_info_from_player}", True, "black")
        screen.blit(bomb_info_text, (20, 50))

        bomb_info_text_count = self.font15.render(f"p1:{self.player1_bomb_count} p2:{self.player2_bomb_count} size_of_bomb_array: {len(bomb_info_from_player)}", True, "black")
        screen.blit(bomb_info_text_count, (20, 500))        

        global first_added_bomb_from_player1
        global index_handle
        global flag_first_added_from_player1
        

        ##drop bomb from player events
        for index, bomb_info in enumerate(bomb_info_from_player):

            #(bomb X    ,bomb Y  ,bomb TURN COUNT   ,PLAYER ID)
            #(bomb_x,   bomb_y   ,bomb_turn         ,bomb_by)
            bomb_x,bomb_y,bomb_turn,bomb_by=bomb_info

        
            if bomb_by==0:  ##default bombs      
                pygame.draw.circle(screen,"black",(bomb_x,bomb_y),15)        
                bomb_info_text_default = self.font15.render(f"{bomb_turn}", True, "white")
                screen.blit(bomb_info_text_default, (bomb_x-5, bomb_y-6))

            if bomb_by==1: ##added bomb by player1
                pygame.draw.circle(screen,"red",(bomb_x,bomb_y),15) 
                bomb_info_text_default = self.font15.render(f"{bomb_turn}", True, "white")
                screen.blit(bomb_info_text_default, (bomb_x-5, bomb_y-6))


                if player1_bomb_count==1:
                    bomb_info_text_ = self.font15.render(f"{bomb_info} {index}", True, "black")
                    screen.blit(bomb_info_text_, (100,400))

                    bomb_info_text_a = self.font15.render(f"{first_added_bomb_from_player1} {index_handle}", True, "black")
                    screen.blit(bomb_info_text_a, (100,450))


            
            if bomb_by==2: ##added bomb by player1
                pygame.draw.circle(screen,"blue",(bomb_x,bomb_y),15) 
                bomb_info_text_default = self.font15.render(f"{bomb_turn}", True, "white")
                screen.blit(bomb_info_text_default, (bomb_x-5, bomb_y-6))

                        

            if len(bomb_info_from_player)==13:


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

                                    bomb_info_from_player.remove(bomb_info)     #removed player's bomb                             

                                    bomb_info_text = self.font25.render(f"yakinda default bomba var", True, "blue")
                                    screen.blit(bomb_info_text, (300, 10))

                                    if bomb[2]==0:
                                        bomb_info_from_player.remove(bomb)      #removed default bomb, when turn is 0

                                        #bomb_info_from_player.remove(bomb_info)
                                        del bomb_info_from_player[(len(bomb_info_from_player))-3]
                            
                            
                            


           
                

                






















        #to do:
        # 
        # if there is a player1's bomb close to the default bomb, explode or decrease the turn 
        #
        # explode added first bomb and maybe close other bomb when player's bomb count is 3
        # meabwhile decrease related default bomb turn if the turn is 0, explode it                       
                                


                               

                            
                            
                

                                                                                                


