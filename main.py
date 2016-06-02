from load import LoadResources
import pygame
import math


class Game:
    load = LoadResources()

    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    keys = [False, False, False, False]
    player_position = [100, 100]

    def draw_background(self):
        for x in range(self.width / self.load.grass.get_width() + 1):
            for y in range(self.height / self.load.grass.get_height() + 1):
                self.screen.blit(self.load.grass, (x * 100, y * 100))

    def draw_elements_on_the_screen(self):
        self.screen.blit(self.load.castle, (0, 30))
        self.screen.blit(self.load.castle, (0, 135))
        self.screen.blit(self.load.castle, (0, 240))
        self.screen.blit(self.load.castle, (0, 345))

    def move_player(self):
        if self.keys[0]:
            self.player_position[1] -= 5
        elif self.keys[2]:
            self.player_position[1] += 5
        if self.keys[1]:
            self.player_position[0] -= 5
        elif self.keys[3]:
            self.player_position[0] += 5

    def angle_between_mouse_and_Player(self):
        mouse_position = pygame.mouse.get_pos()
        angle = math.atan2(mouse_position[1] - (self.player_position[1] + 32),
                           mouse_position[0] - (self.player_position[0] + 26))
        return angle

    def define_rotation_and_position_of_the_player(self, angle):
        player_rotation_number = pygame.transform.rotate(self.load.player, 360 - angle * 57.29)
        playerpos1 = (self.player_position[0] - player_rotation_number.get_rect().width / 2,
                      self.player_position[1] - player_rotation_number.get_rect().height / 2)

        self.screen.blit(player_rotation_number, playerpos1)

    def game_loop(self):
        while 1:
            # 5 - clear the screen before drawing it again
            self.screen.fill(0)

            # 6 - draw the screen elements
            self.draw_background()
            self.draw_elements_on_the_screen()
            self.define_rotation_and_position_of_the_player(self.angle_between_mouse_and_Player())

            # 7 - update the screen
            pygame.display.flip()

            # 8 - loop through the events
            for event in pygame.event.get():
                # check if the event is the X button
                if event.type == pygame.QUIT:
                    # if it is quit the game
                    pygame.quit()
                    exit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.keys[0] = True
                    elif event.key == pygame.K_a:
                        self.keys[1] = True
                    elif event.key == pygame.K_s:
                        self.keys[2] = True
                    elif event.key == pygame.K_d:
                        self.keys[3] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.keys[0] = False
                    elif event.key == pygame.K_a:
                        self.keys[1] = False
                    elif event.key == pygame.K_s:
                        self.keys[2] = False
                    elif event.key == pygame.K_d:
                        self.keys[3] = False
            self.move_player()


if __name__ == "__main__":
    main = Game()
    main.game_loop()
