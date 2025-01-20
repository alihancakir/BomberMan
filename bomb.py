import pygame
from box import Box
TILE_SIZE=40
box=Box()

flag=False


class Bomb():
    
    def drop_bomb_player1(self,screen,player1_bomb_info,player1_bomb_location_size):
        self.screen=screen
        self.player1_bomb_info=player1_bomb_info
        self.player1_bomb_location_size=player1_bomb_location_size

        global flag

        font = pygame.font.Font(None, 25)

        bomb_info_text = font.render(f"Bomb: {self.player1_bomb_info}, array size. {len(self.player1_bomb_info)}", True, "black")
        self.screen.blit(bomb_info_text, (10, 50))

        if  len(self.player1_bomb_info)==3:
            
            self.player1_bomb_info.remove((self.player1_bomb_info[0]))


        """bomb_directions = { #if the bomb, near to other bombs                                            

                    "going right":  (bomb_x_0 + 20, bomb_y_0     ),
                    "going left":   (bomb_x_0 - 40, bomb_y_0     ),
                    "going up":     (bomb_x_0     , bomb_y_0 - 40),
                    "going down":   (bomb_x_0     , bomb_y_0 + 40)

                }"""
        
            

       
    def drop_bomb_player2(self,player2_bomb_info):
        self.player2_bomb_info=player2_bomb_info

        for bomb_x, bomb_y in self.player2_bomb_info:
            pygame.draw.circle(self.screen, "green", (bomb_x, bomb_y), 10)
    
        
        

        
  
    def explode_bomb_player2(self,player2_bomb_location_size):
        
        font = pygame.font.Font(None, 25)
        bomb_info_text = font.render(f"bomb count: {player2_bomb_location_size} " ,True, "green")  
        self.screen.blit(bomb_info_text, (400,0))
        