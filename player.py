
import pygame 
from box import Box
from bomb import Bomb

SCREEN_WIDTH=600
SCREEN_HEIGHT=600
TILE_SIZE=40

new_position_x_player1=0
new_position_y_player1=0

new_position_x_player2=0
new_position_y_player2=0

space_event_for_toggle=False

enter_event_for_toggle=False

new_box_add_flag=False

player1_position=pygame.Vector2(20,580)     #start position for player1
player2_position=pygame.Vector2(580,20)     #start position for player2

box=Box()
bomb=Bomb()

player1_bomb_location_size=0
player1_bomb_location=[]

player2_bomb_location_size=0
player2_bomb_location=[]


class Player():

    #player info:
    def __init__(self):
        self.player1_color="red"
        self.player1_radius=10

        self.player2_color="blue"
        self.player2_radius=10

        

    def move(self,keys,screen):
        self.screen=screen
        self.keys=keys

        global new_position_x_player1
        global new_position_y_player1

        global new_position_x_player2
        global new_position_y_player2


        
        global space_event_for_toggle
        global enter_event_for_toggle

        global player1_bomb_location_size
        global player2_bomb_location_size

        global new_box_add_flag
        

        box_location=box.draw_box(screen)
        
        
######################################################################################################################################################################################
####################################################################################  PLAYER1  #######################################################################################
######################################################################################################################################################################################

        if keys[pygame.K_w]:
            new_position_y_player1=(new_position_y_player1+2)%10             
            if new_position_y_player1== 0 and player1_position.y > 40:
                test_target=any(value_box_location == (player1_position.x-20,player1_position.y-60) for value_box_location in box_location)     
                if test_target==0:  
                    player1_position.y-=40

        if keys[pygame.K_s]:
            new_position_y_player1=(new_position_y_player1+2)%10             
            if new_position_y_player1== 0 and player1_position.y < 560:
                test_target=any(value_box_location == (player1_position.x-20,player1_position.y+20) for value_box_location in box_location)     
                if test_target==0:  
                    player1_position.y+=40


        if keys[pygame.K_a]: 
            new_position_x_player1= (new_position_x_player1+2) % 10                          
            if new_position_x_player1== 0 and player1_position.x > 40:
                test_target=any(value_box_location == (player1_position.x-60,player1_position.y-20) for value_box_location in box_location)     
                if test_target==0: 
                    player1_position.x-=40

        if keys[pygame.K_d]:
            new_position_x_player1= (new_position_x_player1+2) % 10                          
            if new_position_x_player1== 0 and player1_position.x<560:
                test_target=any(value_box_location == (player1_position.x+20,player1_position.y-20) for value_box_location in box_location)     
                if test_target==0:
                    player1_position.x+=40


        if keys[pygame.K_SPACE]:                                
            space_event_for_toggle=True    

        if space_event_for_toggle==True and keys[pygame.K_SPACE]==False:    
            player1_bomb_location_size+=1
            player1_bomb_location.append((int(player1_position.x), int(player1_position.y)))        
            space_event_for_toggle=False

        
        

        pygame.draw.circle(screen,self.player1_color,(int(player1_position.x),int(player1_position.y)),self.player1_radius)
        bomb.drop_bomb_player1(screen,player1_bomb_location,player1_bomb_location_size)

######################################################################################################################################################################################
####################################################################################  PLAYER2   ######################################################################################
######################################################################################################################################################################################    

        if keys[pygame.K_UP]:
            new_position_y_player2=(new_position_y_player2+2)%10             
            if new_position_y_player2== 0 and player2_position.y > 40:
                test_target=any(value_box_location == (player2_position.x-20,player2_position.y-60) for value_box_location in box_location)     
                if test_target==0:  
                    player2_position.y-=40

        if keys[pygame.K_DOWN]:
            new_position_y_player2=(new_position_y_player2+2)%10             
            if new_position_y_player2== 0 and player2_position.y < 560:
                test_target=any(value_box_location == (player2_position.x-20,player2_position.y+20) for value_box_location in box_location)     
                if test_target==0:  
                    player2_position.y+=40


        if keys[pygame.K_LEFT]: 
            new_position_y_player2= (new_position_y_player2+2) % 10                          
            if new_position_y_player2== 0 and player2_position.x > 40:
                test_target=any(value_box_location == (player2_position.x-60,player2_position.y-20) for value_box_location in box_location)     
                if test_target==0: 
                    player2_position.x-=40

        if keys[pygame.K_RIGHT]:
            new_position_y_player2= (new_position_y_player2+2) % 10                          
            if new_position_y_player2== 0 and player2_position.x<560:
                test_target=any(value_box_location == (player2_position.x+20,player2_position.y-20) for value_box_location in box_location)     
                if test_target==0:
                    player2_position.x+=40


        if keys[pygame.K_RETURN]:                      
            enter_event_for_toggle=True    

        if enter_event_for_toggle==True and keys[pygame.K_RETURN]==False and player2_bomb_location_size < 3:
            player2_bomb_location_size+=1  
            player2_bomb_location.append((int(player2_position.x), int(player2_position.y)))        
            enter_event_for_toggle=False
            
        

        pygame.draw.circle(screen,self.player2_color,(int(player2_position.x),int(player2_position.y)),self.player2_radius)
        bomb.drop_bomb_player2(player2_bomb_location)
        bomb.explode_bomb_player2(player2_bomb_location_size)


######################################################################################################################################################################################
####################################################################################   GENERAL  ######################################################################################
######################################################################################################################################################################################


        if keys[pygame.K_p]:                         
            new_box_add_flag=True
            
        if keys[pygame.K_p]==0 and new_box_add_flag==True:                  
            new_box_add_flag=False
            box.add_box()
        

        
