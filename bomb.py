import pygame
from box import Box
TILE_SIZE=40
box=Box()

default_bomb_decreased_flag=False
len_of_bomb_info_from_player_handle=1

bomb_default_location=[##theese bomb could be random location add in here
    
                    #(bomb X    ,bomb Y  ,bomb TURN COUNT   ,PLAYER ID)
                    #(bomb_x    ,bomb_y  ,bomb_turn         ,by_player1 or 2)

                    [20, 580, 1, 0], [20, 380, 1, 0], [20, 100, 3, 0], [100, 20, 1, 0], [100, 220, 2, 0],
                    [300, 180, 2, 0], [420, 140, 1, 0], [420, 20, 1, 0], [540, 260, 1, 0], [540, 500, 3, 0]

                        ]

class Bomb():
  
    def add_bomb_location(self,screen,bomb_info_from_player):

        font = pygame.font.Font(None, 25)
        font2 = pygame.font.Font(None, 20)

            
        bomb_info_text = font.render(f"Bomb: {bomb_info_from_player}, array size. {len(bomb_info_from_player)}", True, "black")
        screen.blit(bomb_info_text, (10, 50))

        global default_bomb_decreased_flag
        global len_of_bomb_info_from_player_handle

        
        ##default bomb 
        for index in range(0,len(bomb_default_location)):

            if len_of_bomb_info_from_player_handle<len(bomb_info_from_player):
                default_bomb_decreased_flag=False
            
            default_bomb_x,default_bomb_y,default_bomb_turn,default_bomb_by=bomb_default_location[index]
            pygame.draw.circle(screen,"black",(default_bomb_x,default_bomb_y),15)

            bomb_info_text = font2.render(f"{default_bomb_turn}", True, "white")
            screen.blit(bomb_info_text, (default_bomb_x-3, default_bomb_y-5))


            ##drop bomb from player events
            for bomb_info in bomb_info_from_player:
                bomb_x,bomb_y,bomb_turn,bomb_by=bomb_info
                pygame.draw.circle(screen,"black",(bomb_x,bomb_y),10)

                bomb_directions = { #if the bomb, near to other bombs                                            

                        "going right":  (bomb_x + 40, bomb_y     ),
                        "going left":   (bomb_x - 40, bomb_y     ),
                        "going up":     (bomb_x     , bomb_y - 40),
                        "going down":   (bomb_x     , bomb_y + 40)

                    }
                
                for direction, (x, y) in bomb_directions.items():                       ## failure is here.  
                    if (x, y) == (default_bomb_x,default_bomb_y):                       ## changing only first close default bomb. solve it.                                                               
                        if not default_bomb_decreased_flag:                                                       
                            bomb_default_location[index][2] -= 1
                            default_bomb_decreased_flag= True

                        bomb_info_text = font.render(f"yakinda bomba var", True, "black")
                        screen.blit(bomb_info_text, (400, 50))
                        
                len_of_bomb_info_from_player_handle=len(bomb_info_from_player)       

 