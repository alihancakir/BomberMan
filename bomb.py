import pygame
from box import Box

pygame.mixer.init() 
#TILE_SIZE=40
box=Box()

player1_bomb_imagine = pygame.image.load("C:/Users/Nitro/Desktop/BomberMan3/pictures/p1_bomb.png")
player1_bomb_scaled_image = pygame.transform.scale(player1_bomb_imagine, (40, 40))

player2_bomb_imagine = pygame.image.load("C:/Users/Nitro/Desktop/BomberMan3/pictures/p2_bomb.png")
player2_bomb_scaled_image = pygame.transform.scale(player2_bomb_imagine, (40, 40))

default_bomb_imagine = pygame.image.load("C:/Users/Nitro/Desktop/BomberMan3/pictures/default_bomb.png")
default_bomb_scaled_image = pygame.transform.scale(default_bomb_imagine, (40, 40))

explode_bomb_sound = pygame.mixer.Sound("C:/Users/Nitro/Desktop/BomberMan3/sound/bomb_explode.mp3")

player1_live_event=True
player2_live_event=True

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
            global player1_live_event
            global player2_live_event

            self.font15 = pygame.font.Font(None, 25)

            #Player1 bomb events:
            for index, player1_bomb_info in enumerate(player1_bomb_location):

                player1_bomb_x_0,player1_bomb_y_0,player1_bomb_turn_0=player1_bomb_location[0]
                enemy_text = self.font15.render(f"{player1_bomb_location[0]}", True, "black")
                screen.blit(enemy_text, (200, 20))

                player1_bomb_x,player1_bomb_y,player1_turn=player1_bomb_info
                
                screen.blit(player1_bomb_scaled_image, (player1_bomb_x-20,player1_bomb_y-20))   #player1's bomb image


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
                
                

                if len(player1_bomb_location)==3:

                    for direction, (x, y) in bomb_directions_p1.items():   # it is for only default bomb close check

                        for bomb_p1_def in default_bomb_location:

                            if (x, y) == (bomb_p1_def[0],bomb_p1_def[1]):

                                bomb_p1_def[2]-=1  #decrease default bomb turn, when turn is not 0

                                player1_bomb_location.remove(player1_bomb_location[0])  # if there is a default bomb near Player1's bombs, Player1's bombs will explode
                                explode_bomb_sound.play()

                                if bomb_p1_def[2]==0:       #if default bomb turn's is 0, it will explode 
                                    default_bomb_location.remove(bomb_p1_def)
                                    box.remove_box(screen,(player1_bomb_x_0,player1_bomb_y_0))
                                    box.remove_box(screen,(bomb_p1_def[0],bomb_p1_def[1]))


                if len(player1_bomb_location)==3:

                    #player2 die algorithm
                    for direction, (x, y) in enemy_directions_p1.items():
                                    if (x, y) == (player2_position):

                                        player2_live_event=False

                                        enemy_text = self.font15.render(f"yakinda dusman var", True, "red")
                                        screen.blit(enemy_text, (20, 20))

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

                enemy_text = self.font15.render(f"{player2_position}", True, "blue")
                screen.blit(enemy_text, (200, 60))

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
                if len(player2_bomb_location)==3:

                    for direction, (x, y) in bomb_directions_p2.items():   # it is for only default bomb close check

                        for bomb_p2_def in default_bomb_location:

                            if (x, y) == (bomb_p2_def[0],bomb_p2_def[1]):

                            

                                bomb_p2_def[2]-=1  #decrease default bomb turn, when turn is not 0

                                player2_bomb_location.remove(player2_bomb_location[0])  # if there is a default bomb near Player1's bombs, Player1's bombs will explode
                                explode_bomb_sound.play()

                                if bomb_p2_def[2]==0:       #if default bomb turn's is 0, it will explode 
                                    default_bomb_location.remove(bomb_p2_def)
                                    box.remove_box(screen,(player2_bomb_x_0,player2_bomb_y_0))
                                    box.remove_box(screen,(bomb_p2_def[0],bomb_p2_def[1]))


                if len(player2_bomb_location)==3:
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
        return player1_live_event,player2_live_event


                

















        


        #to do:
        # 
        # if there is a player1's bomb close to the default bomb, explode or decrease the turn 
        #
        # explode added first bomb and maybe close other bomb when player's bomb count is 3
        # meabwhile decrease related default bomb turn if the turn is 0, explode it                       
                                

                               

                            
                            
                

                                                                                                


