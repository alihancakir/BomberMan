import pygame
from box import Box
TILE_SIZE=40
box=Box()



bomb_default_location=[
                    #(bomb X    ,bomb Y  ,bomb TURN COUNT   ,PLAYER ID)
                    #(bomb_x    ,bomb_y  ,bomb_turn         ,by_player1 or 2)

                    (20,580,1,0)      ,(20,380,1,0)     ,(20,100,3,0)     ,(100,20,1,0)     ,(100,220,2,0),
                    (300,180,2,0)     ,(420,140,1,0)    ,(420,20,1,0)    ,(540,260,1,0)    ,(540,500,3,0)

                        ]




class Bomb():


       
    def add_bomb_location(self,screen,bomb_info_from_player):

        font = pygame.font.Font(None, 25)
        font2 = pygame.font.Font(None, 20)

            
        bomb_info_text = font.render(f"Bomb: {bomb_info_from_player}, array size. {len(bomb_info_from_player)}", True, "black")
        screen.blit(bomb_info_text, (10, 50))

        for index in range(0,len(bomb_default_location)):
            bomb_x,bomb_y,turn,by=bomb_default_location[index]
            pygame.draw.circle(screen,"black",(bomb_x,bomb_y),15)

            bomb_info_text = font2.render(f"{turn}", True, "white")
            screen.blit(bomb_info_text, (bomb_x-3, bomb_y-5))


        for bomb_info in bomb_info_from_player:
            bomb_x,bomb_y,bomb_turn,bomb_owner=bomb_info

            pygame.draw.circle(screen,"black",(bomb_x,bomb_y),10)
    
            for default_bomb_info in bomb_default_location:
                default_bomb_x,default_bomb_y=default_bomb_info[0],default_bomb_info[1]

                bomb_directions = { #if the bomb, near to other bombs                                            

                                "going right":  (bomb_x + 40, bomb_y     ),
                                "going left":   (bomb_x - 40, bomb_y     ),
                                "going up":     (bomb_x     , bomb_y - 40),
                                "going down":   (bomb_x     , bomb_y + 40)
                            }
                
                for direction, (x, y) in bomb_directions.items():
                        if (x, y) ==(default_bomb_x,default_bomb_y):

                            new_bomb_info = (                                  
                                default_bomb_info[0],  
                                default_bomb_info[1],  
                                1,                                                       ####failure is here. infinite loop. stop it
                                default_bomb_info[3]   
                            )
                            
                        
                            index = bomb_default_location.index(default_bomb_info)
                            bomb_default_location[index] = new_bomb_info

                            bomb_info_text = font.render(f"yakinda bomba var", True, "black")
                            screen.blit(bomb_info_text, (400, 50))



                                                                                ########################                            
                                                                                ######## to do: ########
                                                                                ########################

                                                #if any default bomb close to dropped bomb, default bomb turn's will decrease and meanwhile dropped bomb will explode.

                                                #start bomb interaction when dropped bomb count is 3.

                                                #default bomb's have 3 color. 

            

