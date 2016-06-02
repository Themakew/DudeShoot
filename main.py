import pygame
from load import LoadResources


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
        self.screen.blit(self.load.player, (100, 100))
        self.screen.blit(self.load.castle, (0, 30))
        self.screen.blit(self.load.castle, (0, 135))
        self.screen.blit(self.load.castle, (0, 240))
        self.screen.blit(self.load.castle, (0, 345))

    def game_loop(self):
        while 1:
            # 5 - clear the screen before drawing it again
            self.screen.fill(0)

            # 6 - draw the screen elements
            self.draw_background()
            self.draw_elements_on_the_screen()

            # 7 - update the screen
            pygame.display.flip()

            # 8 - loop through the events
            for event in pygame.event.get():
                # check if the event is the X button
                if event.type == pygame.QUIT:
                    # if it is quit the game
                    pygame.quit()
                    exit(0)


if __name__ == "__main__":
    main = Game()
    main.game_loop()
