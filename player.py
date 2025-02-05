import pygame 
from box import Box
from bomb import Bomb

player1_position=pygame.Vector2(20,620)     #start position for player1
player2_position=pygame.Vector2(580,60)     #start position for player2

box=Box()
bomb=Bomb()

player1_imagine = pygame.image.load("C:/Users/Nitro/Desktop/BomberMan3/pictures/player2.png")
player1_scaled_image = pygame.transform.scale(player1_imagine, (40, 40))

player2_imagine = pygame.image.load("C:/Users/Nitro/Desktop/BomberMan3/pictures/robot.png")
player2_scaled_image = pygame.transform.scale(player2_imagine, (35, 35)) 

dropped_bomb_sound = pygame.mixer.Sound("C:/Users/Nitro/Desktop/BomberMan3/sound/drop_bomb.wav")
invalid_sound = pygame.mixer.Sound("C:/Users/Nitro/Desktop/BomberMan3/sound/invalid.mp3")

class Player():

    #player info:
    def __init__(self):

        # Player1 info
        self.player1_color="red"
        self.player1_radius=10

        # Player2 info
        self.player2_color="blue"
        self.player2_radius=10

        # Movement state
        self.new_position_x_player1 = 0
        self.new_position_y_player1 = 0
        self.new_position_x_player2 = 0
        self.new_position_y_player2 = 0

        # Bomb and event state
        self.space_event_for_toggle = False
        self.enter_event_for_toggle = False
        self.new_box_add_flag = False

        # Go to base
        self.live_toggle_flag_p1=False
        self.live_toggle_flag_p2=False


        # Player positions
        self.player1_position = pygame.Vector2(20, 580)
        self.player2_position = pygame.Vector2(580, 20)


        # Bomb information
                                    

        self.player1_bomb_location = []

        self.player2_bomb_location = []

        self.font15 = pygame.font.Font(None, 25)


        # Game objects
        self.box = Box()
        self.bomb = Bomb()

    def move(self,keys,screen,default_bomb_location_from_user):
        self.screen=screen
        self.keys=keys

        self.default_bomb_location = default_bomb_location_from_user
        box_location=box.box_event()
        
             
######################################################################################################################################################################################
####################################################################################  PLAYER1  #######################################################################################
######################################################################################################################################################################################

        if keys[pygame.K_w]:
            self.new_position_y_player1=(self.new_position_y_player1+2)%10             
            if self.new_position_y_player1== 0 and player1_position.y > 80:
                test_target=any(value_box_location == (player1_position.x-20,player1_position.y-60) for value_box_location in box_location)     
                if test_target==0:  
                    player1_position.y-=40

        if keys[pygame.K_s]:
            self.new_position_y_player1=(self.new_position_y_player1+2)%10             
            if self.new_position_y_player1== 0 and player1_position.y < 620:
                test_target=any(value_box_location == (player1_position.x-20,player1_position.y+20) for value_box_location in box_location)     
                if test_target==0:  
                    player1_position.y+=40

        if keys[pygame.K_a]: 
            self.new_position_x_player1= (self.new_position_x_player1+2) % 10                          
            if  self.new_position_x_player1== 0 and player1_position.x > 40:
                test_target=any(value_box_location == (player1_position.x-60,player1_position.y-20) for value_box_location in box_location)     
                if test_target==0: 
                    player1_position.x-=40

        if keys[pygame.K_d]:
            self.new_position_x_player1= (self.new_position_x_player1+2) % 10                          
            if self.new_position_x_player1== 0 and player1_position.x<560:
                test_target=any(value_box_location == (player1_position.x+20,player1_position.y-20) for value_box_location in box_location)     
                if test_target==0:
                    player1_position.x+=40

        if keys[pygame.K_SPACE]:                                
            self.space_event_for_toggle=True    

        if self.space_event_for_toggle and not keys[pygame.K_SPACE]:
            dropped_bomb_sound.play()
            current_player1_position = [int(player1_position.x), int(player1_position.y), 1]
            
            #do not drop player1's bomb , if the bomb in same grid with same bomb
            if current_player1_position not in self.player1_bomb_location:
                
                self.player1_bomb_location.append(current_player1_position)
            else:
                invalid_sound.play()

            self.space_event_for_toggle = False
            
        screen.blit(player1_scaled_image, (int(player1_position.x)-20,int(player1_position.y)-20))

######################################################################################################################################################################################
####################################################################################  PLAYER2   ######################################################################################
######################################################################################################################################################################################    

        if keys[pygame.K_UP]:
            self.new_position_y_player2=(self.new_position_y_player2+2)%10             
            if self.new_position_y_player2== 0 and player2_position.y > 80:
                test_target=any(value_box_location == (player2_position.x-20,player2_position.y-60) for value_box_location in box_location)     
                if test_target==0:  
                    player2_position.y-=40

        if keys[pygame.K_DOWN]:
            self.new_position_y_player2=(self.new_position_y_player2+2)%10             
            if self.new_position_y_player2== 0 and player2_position.y < 620:
                test_target=any(value_box_location == (player2_position.x-20,player2_position.y+20) for value_box_location in box_location)     
                if test_target==0:  
                    player2_position.y+=40

        if keys[pygame.K_LEFT]: 
            self.new_position_y_player2= (self.new_position_y_player2+2) % 10                          
            if self.new_position_y_player2== 0 and player2_position.x > 40:
                test_target=any(value_box_location == (player2_position.x-60,player2_position.y-20) for value_box_location in box_location)     
                if test_target==0: 
                    player2_position.x-=40

        if keys[pygame.K_RIGHT]:
            self.new_position_y_player2= (self.new_position_y_player2+2) % 10                          
            if self.new_position_y_player2== 0 and player2_position.x<560:
                test_target=any(value_box_location == (player2_position.x+20,player2_position.y-20) for value_box_location in box_location)     
                if test_target==0:
                    player2_position.x+=40

        if keys[pygame.K_RETURN]:                      
            self.enter_event_for_toggle=True    

        if self.enter_event_for_toggle==True and keys[pygame.K_RETURN]==False:
            dropped_bomb_sound.play()
            current_player2_position = [int(player2_position.x), int(player2_position.y), 1]
            #do not drop player2's bomb , if the bomb in same grid with same bomb
            if current_player2_position not in self.player2_bomb_location:
                self.player2_bomb_location.append(current_player2_position)
            else:
                invalid_sound.play()
            self.enter_event_for_toggle = False
                    
        screen.blit(player2_scaled_image, (int(player2_position.x)-20,int(player2_position.y)-18))
               
######################################################################################################################################################################################
####################################################################################   GENERAL  ######################################################################################
######################################################################################################################################################################################

        if keys[pygame.K_p]:                         
            self.new_box_add_flag=True
            
        if keys[pygame.K_p]==0 and self.new_box_add_flag==True:                  
            self.new_box_add_flag=False
            box.add_box()

        
        bomb.add_bomb_location(
                                screen,
                                    self.default_bomb_location,
                                        self.player1_bomb_location,
                                            self.player2_bomb_location,
                                                (int(player1_position.x),int(player1_position.y)),
                                                    (int(player2_position.x),int(player2_position.y))
                                )

   