if player1_live_event==3:
            winner="PLAYER 1"
            game_finished=True

        if player2_live_event==3:
            winner="PLAYER 2"
            game_finished=True

        if game_finished==True:

            screen.fill("black")
            winner_text =font100.render(f" {winner} WON", True, "red")
            screen.blit(winner_text, (20, 300))

            restart_text =font25.render(f" PRESS R FOR RESTART", True, "white")
            screen.blit(restart_text, (20, 500))


            if keys[pygame.K_r]:
                restart_event_toggle= True

            if restart_event_toggle and not keys[pygame.K_r]:
                enter_event_for_toggle=False
                game_finished=False