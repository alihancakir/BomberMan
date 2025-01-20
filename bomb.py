import pygame
from box import Box
TILE_SIZE=40
box=Box()



class Bomb():
    
    def drop_bomb_player1(self,screen,player1_bomb_info,player1_bomb_location_size):
        self.screen=screen
        self.player1_bomb_info=player1_bomb_info
        self.player1_bomb_location_size=player1_bomb_location_size
        font = pygame.font.Font(None, 25)

        if self.player1_bomb_location_size==3:
                #count+=1
                box.remove_box(screen,self.player1_bomb_info,self.player1_bomb_location_size)
    
                bomb_x_0,bomb_y_0=player1_bomb_info[0]
                
                bomb_directions = { #if the bomb, near to other bombs                                            

                            "going right":  (bomb_x_0 + 20, bomb_y_0     ),
                            "going left":   (bomb_x_0 - 40, bomb_y_0     ),
                            "going up":     (bomb_x_0     , bomb_y_0 - 40),
                            "going down":   (bomb_x_0     , bomb_y_0 + 40)

                        }

                for direction, (x, y) in bomb_directions.items():
                    if (x, y) in player1_bomb_info:

                        player1_bomb_info.remove((x, y))
                        rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                        
                        pygame.draw.rect(self.screen, "white", rect, 0)
                        self.player1_bomb_location_size-=1

                rect = pygame.Rect(bomb_x_0, bomb_y_0, TILE_SIZE, TILE_SIZE)                      
                pygame.draw.rect(self.screen, "white", rect, 0)               
                del self.player1_bomb_info[0]
                self.player1_bomb_location_size-=1
                


        else:
            for index, bomb_info in enumerate (self.player1_bomb_info):

                bomb_x,bomb_y=bomb_info
                pygame.draw.circle(screen, "black", (bomb_x,bomb_y), 10)

                bomb_info_text = font.render(f"Bomb {index}: {bomb_info}", True, "black")
                self.screen.blit(bomb_info_text, (10, 50 + index * 20))

            





        


        

        

       
    def drop_bomb_player2(self,player2_bomb_info):
        self.player2_bomb_info=player2_bomb_info

        for bomb_x, bomb_y in self.player2_bomb_info:
            pygame.draw.circle(self.screen, "green", (bomb_x, bomb_y), 10)
    
        
        

        
  
    def explode_bomb_player2(self,player2_bomb_location_size):
        
        font = pygame.font.Font(None, 25)
        bomb_info_text = font.render(f"bomb count: {player2_bomb_location_size} " ,True, "green")  
        self.screen.blit(bomb_info_text, (400,0))
        

