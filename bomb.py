import pygame
from box import Box
TILE_SIZE=40
box=Box()

class Bomb():
    
    def drop_bomb_player1(self,screen,player1_bomb_info):
        self.screen=screen
        self.player1_bomb_info=player1_bomb_info
        
        font = pygame.font.Font(None, 25)

        for bomb_info in self.player1_bomb_info:
            bomb_x,bomb_y=bomb_info

            pygame.draw.circle(screen,"black",(bomb_x,bomb_y),10)

            if  len(self.player1_bomb_info)==3:

                bomb_x_0,bomb_y_0=self.player1_bomb_info[0]

                box.remove_box(screen,self.player1_bomb_info[0])
                
                bomb_directions = { #if the bomb, near to other bombs                                            

                            "going right":  (bomb_x_0 + 40, bomb_y_0     ),
                            "going left":   (bomb_x_0 - 40, bomb_y_0     ),
                            "going up":     (bomb_x_0     , bomb_y_0 - 40),
                            "going down":   (bomb_x_0     , bomb_y_0 + 40)

                        }

                for direction, (x, y) in bomb_directions.items():
                    if (x, y) in self.player1_bomb_info:

                        self.player1_bomb_info.remove((x, y))
                        rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)                 
                        pygame.draw.rect(self.screen, "white", rect, 0)

                        box.remove_box(screen,(x,y))
                        
                self.player1_bomb_info.remove((self.player1_bomb_info[0]))
                               
            bomb_info_text = font.render(f"Bomb: {self.player1_bomb_info}, array size. {len(self.player1_bomb_info)}", True, "black")
            self.screen.blit(bomb_info_text, (10, 50))
       
    def drop_bomb_player2(self,player2_bomb_info):
        self.player2_bomb_info=player2_bomb_info
        
        font = pygame.font.Font(None, 25)

        for bomb_info in self.player2_bomb_info:
            bomb_x,bomb_y=bomb_info
            pygame.draw.circle(self.screen,"orange",(bomb_x,bomb_y),10)

            if  len(self.player2_bomb_info)==3:
                bomb_x_0,bomb_y_0=self.player2_bomb_info[0]

                box.remove_box(self.screen,self.player2_bomb_info[0])
                
                bomb_directions = { #if the bomb, near to other bombs                                            

                            "going right":  (bomb_x_0 + 40, bomb_y_0     ),
                            "going left":   (bomb_x_0 - 40, bomb_y_0     ),
                            "going up":     (bomb_x_0     , bomb_y_0 - 40),
                            "going down":   (bomb_x_0     , bomb_y_0 + 40)

                        }
                for direction, (x, y) in bomb_directions.items():
                    if (x, y) in self.player2_bomb_info:

                        self.player2_bomb_info.remove((x, y))
                        rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)                 
                        pygame.draw.rect(self.screen, "white", rect, 0)

                        box.remove_box(self.screen,(x,y))
                        
                self.player2_bomb_info.remove((self.player2_bomb_info[0]))
                               
            bomb_info_text = font.render(f"Bomb: {self.player2_bomb_info}, array size. {len(self.player2_bomb_info)}", True, "orange")
            self.screen.blit(bomb_info_text, (10, 100))

        