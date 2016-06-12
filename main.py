from load import LoadResources
from fisics import GameFisics
import pygame


class Game:
    load = LoadResources()
    fisics = GameFisics()

    def game_loop(self):
        self.load.load_audio()

        while self.fisics.running:
            self.fisics.bad_timer -= 1

            # clear the screen before drawing it again
            self.load.screen.fill(0)

            self.load.draw_background()
            self.load.draw_elements_on_the_screen()
            self.fisics.arrows_fisics()
            self.fisics.enemies_fisics()
            self.fisics.clock_fisics()
            self.fisics.draw_health_bar()
            self.fisics.player_movement(self.fisics.angle_between_mouse_and_Player())

            # update the screen
            pygame.display.flip()

            # loop through the events
            for event in pygame.event.get():
                self.fisics.check_if_player_exit(event)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.fisics.keys[0] = True
                    elif event.key == pygame.K_a:
                        self.fisics.keys[1] = True
                    elif event.key == pygame.K_s:
                        self.fisics.keys[2] = True
                    elif event.key == pygame.K_d:
                        self.fisics.keys[3] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.fisics.keys[0] = False
                    elif event.key == pygame.K_a:
                        self.fisics.keys[1] = False
                    elif event.key == pygame.K_s:
                        self.fisics.keys[2] = False
                    elif event.key == pygame.K_d:
                        self.fisics.keys[3] = False

                self.fisics.arrow_movement(event.type)

            self.fisics.move_player()
            self.fisics.check_if_player_win_or_lose()
        self.fisics.display_win_or_lose()


if __name__ == "__main__":
    main = Game()
    main.game_loop()
