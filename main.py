from load import LoadResources
import pygame
import math
import random


class Game:
    load = LoadResources()

    pygame.init()
    pygame.display.set_caption("DudeShoot")
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    keys = [False, False, False, False]
    player_position = [100, 100]
    shoot_accuracy = [0, 0]
    arrows = []
    player_pos_one = (0, 0)
    bad_timer = 100
    bad_timer_one = 0
    enemies = [[640, 100]]
    health_value = 194

    bad_rect = pygame.Rect(load.bad_guy_image.get_rect())

    def draw_background(self):
        for x in range(self.width / self.load.grass.get_width() + 1):
            for y in range(self.height / self.load.grass.get_height() + 1):
                self.screen.blit(self.load.grass, (x * 100, y * 100))

    def draw_elements_on_the_screen(self):
        self.screen.blit(self.load.castle, (0, 30))
        self.screen.blit(self.load.castle, (0, 135))
        self.screen.blit(self.load.castle, (0, 240))
        self.screen.blit(self.load.castle, (0, 345))

    def draw_arrows(self):
        for bullet in self.arrows:
            index = 0
            velx = math.cos(bullet[0]) * 10
            vely = math.sin(bullet[0]) * 10
            bullet[1] += velx
            bullet[2] += vely

            # check if the bullet in on the screen
            if bullet[1] <- 64 or bullet[1] > 640 or bullet[2] <- 64 or bullet[2] > 480:
                self.arrows.pop(index)
            index += 1

            # set the correct rotation for the arrows
            for projectile in self.arrows:
                arrow1 = pygame.transform.rotate(self.load.arrow, 360 - projectile[0] * 57.29)
                self.screen.blit(arrow1, (projectile[1], projectile[2]))

    def draw_enemies(self):
        if self.bad_timer == 0:
            self.enemies.append([640, random.randint(50, 430)])
            self.bad_timer = 100 - (self.bad_timer_one * 2)
            if self.bad_timer_one >= 35:
                self.bad_timer_one = 35
            else:
                self.bad_timer_one += 5

        index = 0
        for enemie in self.enemies:
            if enemie[0] <- 64:
                self.enemies.pop(index)
            enemie[0] -= 7
            self.enemies_attack(enemie, index)
            self.check_collision(index)
            index += 1

        for enemie in self.enemies:
            self.screen.blit(self.load.bad_guy_image, enemie)

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

    def player_movement(self, angle):
        player_rotation = pygame.transform.rotate(self.load.player, 360 - angle * 57.29)
        self.player_pos_one = (self.player_position[0] - player_rotation.get_rect().width / 2,
                               self.player_position[1] - player_rotation.get_rect().height / 2)

        self.screen.blit(player_rotation, self.player_pos_one)

    def arrow_movement(self, event):
        if event == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            self.shoot_accuracy[1] += 1
            self.arrows.append([math.atan2(mouse_position[1] - (self.player_pos_one[1] + 32),
                               mouse_position[0] - (self.player_pos_one[0] + 26)),
                               self.player_pos_one[0] + 32, self.player_pos_one[1] + 32])

    def enemies_attack(self, enemie, index):
        self.bad_rect.top = enemie[1]
        self.bad_rect.left = enemie[0]
        if self.bad_rect.left < 64:
            self.health_value -= random.randint(5, 20)
            self.enemies.pop(index)

    def check_collision(self, index):
        index1 = 0
        for bullet in self.arrows:
            bull_rect = pygame.Rect(self.load.arrow.get_rect())
            bull_rect.left = bullet[1]
            bull_rect.top = bullet[2]
            if self.bad_rect.colliderect(bull_rect):
                self.shoot_accuracy[0] += 1
                self.enemies.pop(index)
                self.arrows.pop(index1)
            index1 += 1

    def game_loop(self):
        while 1:
            self.bad_timer -= 1
            # 5 - clear the screen before drawing it again
            self.screen.fill(0)

            # 6 - draw the screen elements
            self.draw_background()
            self.draw_elements_on_the_screen()
            self.draw_arrows()
            self.draw_enemies()
            self.player_movement(self.angle_between_mouse_and_Player())

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

                self.arrow_movement(event.type)

            self.move_player()


if __name__ == "__main__":
    main = Game()
    main.game_loop()
