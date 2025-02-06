import pygame
from box import Box

pygame.mixer.init() 
box=Box()

player1_bomb_imagine = pygame.image.load("C:/Users/Nitro/Desktop/BomberMan3/pictures/p1_bomb.png")
player1_bomb_scaled_image = pygame.transform.scale(player1_bomb_imagine, (40, 40))

player2_bomb_imagine = pygame.image.load("C:/Users/Nitro/Desktop/BomberMan3/pictures/p2_bomb.png")
player2_bomb_scaled_image = pygame.transform.scale(player2_bomb_imagine, (40, 40))

default_bomb_imagine = pygame.image.load("C:/Users/Nitro/Desktop/BomberMan3/pictures/default_bomb.png")
default_bomb_scaled_image = pygame.transform.scale(default_bomb_imagine, (40, 40))

explode_bomb_sound = pygame.mixer.Sound("C:/Users/Nitro/Desktop/BomberMan3/sound/bomb_explode.mp3")
invalid_sound = pygame.mixer.Sound("C:/Users/Nitro/Desktop/BomberMan3/sound/invalid.mp3")

died = pygame.mixer.Sound("C:/Users/Nitro/Desktop/BomberMan3/sound/died.mp3")

player1_score=0
player2_score=0




class Bomb():



    def add_bomb_location(
                        self,
                            screen,
                                default_bomb_location,
                                    player1_bomb_location,
                                        player2_bomb_location,
                                            player1_position,
                                                player2_position                                                                      
                        ):
            global player1_score
            global player2_score

            box_location=box.box_event()

            self.font15 = pygame.font.Font(None, 25)

            #Player1 bomb events:
            for index, player1_bomb_info in enumerate(player1_bomb_location):

                player1_bomb_x_0,player1_bomb_y_0,player1_bomb_turn_0=player1_bomb_location[0]

                player1_bomb_x,player1_bomb_y,player1_turn=player1_bomb_info

                bomb_info_text_player1 = self.font15.render(f"{player1_turn}", True, "white")
                screen.blit(bomb_info_text_player1, (player1_bomb_x-10, player1_bomb_y-6))

                bomb_directions_p1= { #if the bomb, close to other bombs                                            

                            "going right":  (player1_bomb_x + 40, player1_bomb_y     ),
                            "going left":   (player1_bomb_x - 40, player1_bomb_y     ),
                            "going up":     (player1_bomb_x     , player1_bomb_y - 40),
                            "going down":   (player1_bomb_x     , player1_bomb_y + 40)
                        }
                
                enemy_directions_p1 = { #if the bomb, close to player2                                             

                            "going right":  (player1_bomb_x_0 + 40, player1_bomb_y_0     ),
                            "going left":   (player1_bomb_x_0 - 40, player1_bomb_y_0     ),
                            "going up":     (player1_bomb_x_0     , player1_bomb_y_0 - 40),
                            "going down":   (player1_bomb_x_0     , player1_bomb_y_0 + 40)
                        }
                                  
                #do not drop player1's bomb , if the bomb in same grid with default bomb                
                for player1_bombs in player1_bomb_location:

                    for bomb_p1_def_check in default_bomb_location:
                        
                        if  (player1_bombs[0],player1_bombs[1]) == (bomb_p1_def_check[0],bomb_p1_def_check[1]):

                            invalid_sound.play()
                            player1_bomb_location.remove(player1_bombs)
                        
                    screen.blit(player1_bomb_scaled_image, (player1_bomb_x-20,player1_bomb_y-20))   #player1's bomb image
                    bomb_info_text_player1 = self.font15.render(f"{player1_turn}", True, "white")
                    screen.blit(bomb_info_text_player1, (player1_bomb_x-10, player1_bomb_y-6))

                if len(player1_bomb_location)==3:
           
                    for direction, (x, y) in bomb_directions_p1.items():   # it is for only default bomb close to player1 bomb check

                        for bomb_p1_def in default_bomb_location:

                            if (x, y) == (bomb_p1_def[0],bomb_p1_def[1]):   # There is a default bomb near the player1 bomb

                                bomb_p1_def[2]-=1  #decrease default bomb turn, when turn is not 0

                                player1_bomb_location.remove(player1_bomb_location[0])  # if there is a default bomb near Player1's bombs, Player1's bombs will explode
                                explode_bomb_sound.play()

                                if bomb_p1_def[2]==0:    #if default bomb turn's is 0, it will explode 

                                    bomb_directions_p1_close_to_default_check= { #if the bomb, close to other bombs                                            

                                            "going right":  (bomb_p1_def[0] + 40, bomb_p1_def[1]     ),
                                            "going left":   (bomb_p1_def[0] - 40, bomb_p1_def[1]     ),
                                            "going up":     (bomb_p1_def[0]     , bomb_p1_def[1] - 40),
                                            "going down":   (bomb_p1_def[0]     , bomb_p1_def[1] + 40)
                                        }

                                    # whatever close to default bomb, the stuff; will be died or exploded
                                    for bomb_p1_def_close_check in player1_bomb_location:
                                        for direection, (x,y) in bomb_directions_p1_close_to_default_check.items():                                          
                               
                                            if (x,y)== (bomb_p1_def_close_check[0],bomb_p1_def_close_check[1]):
                                                player1_bomb_location.remove(bomb_p1_def_close_check)

                                            elif (x,y)==(player1_position):

                                                #player1 died
                                                player2_score+=1
                                                player1_bomb_location.remove(bomb_p1_def_close_check)
                                                died.play()

                                            elif (x,y)==(player2_position):

                                                #player2 died
                                                player1_score+=1
                                                player1_bomb_location.remove(bomb_p1_def_close_check)
                                                died.play()

                                    default_bomb_location.remove(bomb_p1_def)
                                    box.remove_box(screen,(player1_bomb_x_0,player1_bomb_y_0))
                                    box.remove_box(screen,(bomb_p1_def[0],bomb_p1_def[1]))
                                    
                if len(player1_bomb_location)==3:

                    #player2 die algorithm
                    for direction, (x, y) in enemy_directions_p1.items():
                        if (x, y) == (player2_position):

                            #player2 died
                            player1_score+=1
                            died.play()

                    #the bomb if player2 is on top        
                    if  (player1_bomb_x_0,player1_bomb_y_0)==(player2_position):
                        
                        #player2 died
                        player1_score+=1
                        died.play()
                                                                
                    # remove first added player1's bomb if no default bomb close to the first bomb
                    for direction, (x, y) in bomb_directions_p1.items():
                        for bomb_p1 in player1_bomb_location:
                            if (x, y) == (bomb_p1[0],bomb_p1[1]):
                                box.remove_box(screen,(bomb_p1[0],bomb_p1[1]))
                                player1_bomb_location.remove(bomb_p1)
                                explode_bomb_sound.play()

                    box.remove_box(screen,(player1_bomb_x_0,player1_bomb_y_0))
                    player1_bomb_location.remove(player1_bomb_location[0])
                    explode_bomb_sound.play()

            #Player2 bomb events:
            for index, player2_bomb_info in enumerate(player2_bomb_location):

                player2_bomb_x_0,player2_bomb_y_0,player2_bomb_turn_0=player2_bomb_location[0]

                player2_bomb_x,player2_bomb_y,player2_turn=player2_bomb_info

                screen.blit(player2_bomb_scaled_image, (player2_bomb_x-20,player2_bomb_y-20))
                
                bomb_info_text_player2 = self.font15.render(f"{player2_turn}", True, "white")
                screen.blit(bomb_info_text_player2, (player2_bomb_x-10, player2_bomb_y-6))

                bomb_directions_p2 = { #if the bomb, close to other bombs                                            

                            "going right":  (player2_bomb_x + 40, player2_bomb_y     ),
                            "going left":   (player2_bomb_x - 40, player2_bomb_y     ),
                            "going up":     (player2_bomb_x     , player2_bomb_y - 40),
                            "going down":   (player2_bomb_x     , player2_bomb_y + 40)
                        }
                
                enemy_directions_p2 = { #if the bomb, close to player2                                             

                            "going right":  (player2_bomb_x_0 + 40, player2_bomb_y_0     ),
                            "going left":   (player2_bomb_x_0 - 40, player2_bomb_y_0     ),
                            "going up":     (player2_bomb_x_0     , player2_bomb_y_0 - 40),
                            "going down":   (player2_bomb_x_0     , player2_bomb_y_0 + 40)
                        }
                
                #do not drop player2's bomb , if theese in same grid                 
                for player2_bombs in player2_bomb_location:

                    for bomb_p2_def_check in default_bomb_location:
                        if  (player2_bombs[0],player2_bombs[1]) == (bomb_p2_def_check[0],bomb_p2_def_check[1]):
                            invalid_sound.play()
                            player2_bomb_location.remove(player2_bombs)
                        
                    screen.blit(player2_bomb_scaled_image, (player2_bomb_x-20,player2_bomb_y-20))   #player1's bomb image
                    bomb_info_text_player2 = self.font15.render(f"{player2_turn}", True, "white")
                    screen.blit(bomb_info_text_player2, (player2_bomb_x-10, player2_bomb_y-6))

                if len(player2_bomb_location)==3:

                    for direction, (x, y) in bomb_directions_p2.items():   # it is for only default bomb close check

                        for bomb_p2_def in default_bomb_location:

                            if (x, y) == (bomb_p2_def[0],bomb_p2_def[1]):                           

                                bomb_p2_def[2]-=1  #decrease default bomb turn, when turn is not 0

                                player2_bomb_location.remove(player2_bomb_location[0])  # if there is a default bomb near Player1's bombs, Player1's bombs will explode
                                explode_bomb_sound.play()

                                if bomb_p2_def[2]==0:       #if default bomb turn's is 0, it will explode

                                    bomb_directions_p2_close_to_default_check= { #if the bomb, close to other bombs                                            

                                            "going right":  (bomb_p2_def[0] + 40, bomb_p2_def[1]     ),
                                            "going left":   (bomb_p2_def[0] - 40, bomb_p2_def[1]     ),
                                            "going up":     (bomb_p2_def[0]     , bomb_p2_def[1] - 40),
                                            "going down":   (bomb_p2_def[0]     , bomb_p2_def[1] + 40)
                                        }

                                    # whatever close to default bomb, the stuff; will be died or exploded
                                    for bomb_p2_def_close_check in player2_bomb_location:
                                        for direection, (x,y) in bomb_directions_p2_close_to_default_check.items():
                                            if (x,y)== (bomb_p2_def_close_check[0],bomb_p2_def_close_check[1]):
                                                player2_bomb_location.remove(bomb_p2_def_close_check)

                                            elif (x,y)==(player1_position):

                                                #player1 died
                                                player2_score+=1
                                                player2_bomb_location.remove(bomb_p2_def_close_check)
                                                died.play()

                                            elif (x,y)==(player2_position):

                                                #player2 died
                                                player1_score+=1
                                                player2_bomb_location.remove(bomb_p2_def_close_check)
                                                died.play()

                                    default_bomb_location.remove(bomb_p2_def)

                                    box.remove_box(screen,(player2_bomb_x_0,player2_bomb_y_0))
                                    box.remove_box(screen,(bomb_p2_def[0],bomb_p2_def[1]))

                if len(player2_bomb_location)==3:
                    
                    #player1 die algorithm
                    for direction, (x, y) in enemy_directions_p2.items():
                        if (x, y) == (player1_position):

                            #player1 died.
                            player2_score+=1
                            died.play()
                            
                    #the bomb if player1 is on top
                    if  (player2_bomb_x_0,player2_bomb_y_0)==(player1_position):  

                        #player1 died
                        player2_score+=1
                        died.play()
                                        
                    for direction, (x, y) in bomb_directions_p2.items():
                        for bomb_p2 in player2_bomb_location:
                            if (x, y) == (bomb_p2[0],bomb_p2[1]):

                                box.remove_box(screen,(bomb_p2[0],bomb_p2[1]))
                                player2_bomb_location.remove(bomb_p2)
                                explode_bomb_sound.play()

                    box.remove_box(screen,(player2_bomb_x_0,player2_bomb_y_0))
                    player2_bomb_location.remove(player2_bomb_location[0])
                    explode_bomb_sound.play()

            #Default bomb events:
            for index, default_bomb_info in enumerate(default_bomb_location):

                default_bomb_x,default_bomb_y,default_bomb_turn=default_bomb_info

                screen.blit(default_bomb_scaled_image, (default_bomb_x-20,default_bomb_y-20))

                bomb_info_text_default = self.font15.render(f"{default_bomb_turn}", True, "white")
                screen.blit(bomb_info_text_default, (default_bomb_x-5, default_bomb_y-6))

    def live_event(self):
        return player1_score,player2_score
