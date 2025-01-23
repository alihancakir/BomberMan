
import pygame 
from box import Box
from bomb import Bomb

SCREEN_WIDTH=600
SCREEN_HEIGHT=600
TILE_SIZE=40


player1_position=pygame.Vector2(20,580)     #start position for player1
player2_position=pygame.Vector2(580,20)     #start position for player2

box=Box()
bomb=Bomb()

class Player():

    #player info:
    def __init__(self):
        self.player1_color="red"
        self.player1_radius=10

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

        # Player positions
        self.player1_position = pygame.Vector2(20, 580)
        self.player2_position = pygame.Vector2(580, 20)

        # Bomb information
        self.bomb_location = [
                                    ##theese bomb could be random location add in here
    
                                    #(bomb X    ,bomb Y  ,bomb TURN COUNT   ,PLAYER ID)
                                    #(bomb_x    ,bomb_y  ,bomb_turn         ,by_player1 or 2)

                                    [20, 580, 1, 0], [20, 380, 1, 0], [20, 100, 3, 0], [100, 20, 1, 0], [100, 220, 2, 0],
                                    [300, 180, 2, 0], [420, 140, 1, 0], [420, 20, 1, 0], [540, 260, 1, 0], [540, 500, 3, 0]
                                    #[20, 580, 1, 0]
        ]

        # Game objects
        self.box = Box()
        self.bomb = Bomb()

        

    def move(self,keys,screen):
        self.screen=screen
        self.keys=keys

        box_location=box.draw_box(screen)
        
        
######################################################################################################################################################################################
####################################################################################  PLAYER1  #######################################################################################
######################################################################################################################################################################################

        if keys[pygame.K_w]:
            self.new_position_y_player1=(self.new_position_y_player1+2)%10             
            if self.new_position_y_player1== 0 and player1_position.y > 40:
                test_target=any(value_box_location == (player1_position.x-20,player1_position.y-60) for value_box_location in box_location)     
                if test_target==0:  
                    player1_position.y-=40

        if keys[pygame.K_s]:
            self.new_position_y_player1=(self.new_position_y_player1+2)%10             
            if self.new_position_y_player1== 0 and player1_position.y < 560:
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

        if self.space_event_for_toggle==True and keys[pygame.K_SPACE]==False:    
            self.bomb_location.append([int(player1_position.x), int(player1_position.y),1,1])        
            self.space_event_for_toggle=False

        
        

        pygame.draw.circle(screen,self.player1_color,(int(player1_position.x),int(player1_position.y)),self.player1_radius)
        #bomb.drop_bomb_player1(screen,self.player1_bomb_location)

######################################################################################################################################################################################
####################################################################################  PLAYER2   ######################################################################################
######################################################################################################################################################################################    

        if keys[pygame.K_UP]:
            self.new_position_y_player2=(self.new_position_y_player2+2)%10             
            if self.new_position_y_player2== 0 and player2_position.y > 40:
                test_target=any(value_box_location == (player2_position.x-20,player2_position.y-60) for value_box_location in box_location)     
                if test_target==0:  
                    player2_position.y-=40

        if keys[pygame.K_DOWN]:
            self.new_position_y_player2=(self.new_position_y_player2+2)%10             
            if self.new_position_y_player2== 0 and player2_position.y < 560:
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
            self.bomb_location.append([int(player2_position.x), int(player2_position.y),1,2])        
            self.enter_event_for_toggle=False
            
        pygame.draw.circle(screen,self.player2_color,(int(player2_position.x),int(player2_position.y)),self.player2_radius)
        
       

######################################################################################################################################################################################
####################################################################################   GENERAL  ######################################################################################
######################################################################################################################################################################################


        if keys[pygame.K_p]:                         
            self.new_box_add_flag=True
            
        if keys[pygame.K_p]==0 and self.new_box_add_flag==True:                  
            self.new_box_add_flag=False
            box.add_box()
        
        bomb.add_bomb_location(screen,self.bomb_location)
        
