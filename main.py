import pygame
import random
import time

from grid import Grid
from box import Box
from player import Player
from bomb import Bomb

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 640
TILE_SIZE = 40
FPS = 100

pygame.init()
font = pygame.font.Font(None, 25)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("BomberMan")
dt = 0

grid = Grid()
box = Box()
player = Player()
bomb = Bomb()

font25 = pygame.font.Font(None, 25)
font100 = pygame.font.Font(None, 100)

bomb_x = ""
bomb_y = ""
bomb_turn = ""

a_event_for_toggle = False
fail_log = ""

color_x = "yellow"
color_y = "white"
color_turn = "white"

color_add_bomb = "white"
color_go_with_default = "white"



main_imagine = pygame.image.load("C:/Users/Nitro/Desktop/BomberMan3/pictures/main2.png")
main_scaled_image = pygame.transform.scale(main_imagine, (600, 600))

running = True

g_event_for_toggle = False
game_finished = False
winner = None

default_bomb_info = []

chosen_default_bomb_info=[]

main_default_bomb_location = [
    [20, 580, 1], [20, 380, 1], [20, 100, 3], [100, 60, 1], [100, 220, 2],
    [300, 180, 2], [420, 140, 1], [420, 60, 1], [540, 260, 1], [540, 500, 3],
    [300, 580, 2], [420, 540, 3], [460, 500, 1], [540, 380, 1], [540, 580, 3]
]

previous_keys = [False] * 323  # Pygame'deki toplam tuş sayısı

while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            number = event.key

            if number == pygame.K_BACKSPACE:
                if  len(bomb_x)<3:
                    bomb_x=""
                elif len(bomb_turn)==0 and len(bomb_x)==3 and len(bomb_y)<3:
                    bomb_y=""

            elif pygame.K_0 <= number <= pygame.K_9:

                if len(bomb_x) < 3:
                    bomb_x += chr(number)
                    if int(bomb_x)>570:
                        bomb_x = ""
                        fail_log = "(bomb_x must be <570)"

                    if len(bomb_x) == 3:
                        if int(bomb_x) % 40 != 0:
                            fail_log = "(bomb x and bomb y must be multiples of 30)"
                            color_x = "red"
                            bomb_x = ""
                        else:
                            fail_log = ""
                            color_x = (92, 209, 20)
                            color_y = "yellow"
                    else:
                        color_y = "white"
                        color_turn = "white"

                elif len(bomb_turn) == 0 and len(bomb_x) == 3 and len(bomb_y) == 3:
                    bomb_turn += chr(number)
                    if int(bomb_x) % 40 == 0 and int(bomb_y) % 40 == 0:
                        default_bomb_info.append([int(bomb_x)+20, int(bomb_y)+20, int(bomb_turn)])

                        chosen_default_bomb_info= default_bomb_info

                        bomb_x = ""
                        bomb_y = ""
                        bomb_turn = ""
                        color_x = "yellow"
                        color_y = "white"
                        color_turn = "white"

                elif len(bomb_x) == 3 and len(bomb_y) < 3:
                    color_y = (92, 209, 20)
                    bomb_y += chr(number)

                    if len(bomb_y) == 3:
                        if int(bomb_y) % 40 != 0:
                            fail_log = "(bomb x and bomb y must be multiples of 40)"
                            color_y = "red"
                            bomb_y = ""
                        else:
                            color_turn = "yellow"
                            fail_log = ""
                            color_y = (92, 209, 20)

            print(f"dizi: {default_bomb_info} {bomb_x}, {bomb_y}, {bomb_turn}")

    if not g_event_for_toggle:
        screen.fill("black")
        screen.blit(main_scaled_image, (5, 10))
        

        default_bomb_header2 = font25.render("->Press G For Quick Start With Default Bomb Map", True, color_add_bomb)
        screen.blit(default_bomb_header2, (100, 350))

        default_bomb_header = font25.render("->Press A For Add Default Bomb Map", True, color_go_with_default)
        screen.blit(default_bomb_header, (100, 370))

        

        default_bomb_header2 = font25.render(f"{fail_log}", True, "red")
        screen.blit(default_bomb_header2, (20, 400))

    if keys[pygame.K_a] and not previous_keys[pygame.K_a]:
        a_event_for_toggle = True

    if a_event_for_toggle:
        color_add_bomb = "green"
        default_bomb_x = font25.render(f"default bomb x:{bomb_x}", True, color_x)
        screen.blit(default_bomb_x, (20, 430))
        default_bomb_y = font25.render(f"default bomb y:{bomb_y}", True, color_y)
        screen.blit(default_bomb_y, (20, 460))
        default_bomb_turn = font25.render(f"default bomb turn:{bomb_turn}", True, color_turn)
        screen.blit(default_bomb_turn, (20, 490))
        default_bomb = font25.render(f"{default_bomb_info}", True, "white")
        screen.blit(default_bomb, (20, 550))

    if keys[pygame.K_g] and not previous_keys[pygame.K_g]:
        g_event_for_toggle = True

    if g_event_for_toggle:
        screen.fill("white")

        box.draw_box(screen)

        grid.draw_grid(screen)

        player.move(keys, screen, main_default_bomb_location)

        player1_live_event, player2_live_event = bomb.live_event()

        p1_text = font25.render(f"P1 SCORE: {player1_live_event}", True, "red")
        screen.blit(p1_text, (10, 15))

        p2_text = font25.render(f"P2 SCORE: {player2_live_event}", True, "blue")
        screen.blit(p2_text, (490, 15))

        if player1_live_event == 3:
            winner = "PLAYER 1"
            game_finished = True

        if player2_live_event == 3:
            winner = "PLAYER 2"
            game_finished = True

        if game_finished:
            screen.fill("black")
            winner_text = font100.render(f"{winner} WON", True, "red")
            screen.blit(winner_text, (20, 300))

    pygame.display.flip()
    dt = clock.tick(FPS) / 1000

pygame.quit()
