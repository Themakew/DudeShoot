from load import LoadResources
import math
import random
import pygame


# 90 seconds
GAMEPLAY_RUNNING_TIME = 90000


class GameFisics:

    keys = [False, False, False, False]
    player_position = [100, 100]
    shoot_accuracy = [0, 0]
    arrows = []
    player_pos_one = (0, 0)
    bad_timer = 100
    bad_timer_one = 0
    enemies = [[640, 100]]
    health_value = 194
    running = 1
    exit_code = 1
    accuracy = 0

    load = LoadResources()
    bad_rect = load.bad_rect

    def arrows_fisics(self):
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
                self.load.screen.blit(arrow1, (projectile[1], projectile[2]))

    def enemies_fisics(self):
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
            self.load.screen.blit(self.load.bad_guy_image, enemie)

    def clock_fisics(self):
        font = pygame.font.Font(None, 24)
        survived_text = font.render(str((GAMEPLAY_RUNNING_TIME - pygame.time.get_ticks()) / 60000) +
                                    ":" +
                                    str((GAMEPLAY_RUNNING_TIME - pygame.time.get_ticks()) / 1000 % 60).zfill(2) +
                                    "s",
                                    True,
                                    (255, 255, 255))
        text_rect = survived_text.get_rect()
        text_rect.topright = [635, 5]
        self.load.screen.blit(survived_text, text_rect)

    def draw_health_bar(self):
        self.load.screen.blit(self.load.health_bar, (5, 5))
        for health_one in range(self.health_value):
            self.load.screen.blit(self.load.health, (health_one + 8, 8))

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

        self.load.screen.blit(player_rotation, self.player_pos_one)

    def arrow_movement(self, event):
        if event == pygame.MOUSEBUTTONDOWN:
            self.load.shoot.play()
            mouse_position = pygame.mouse.get_pos()
            self.shoot_accuracy[1] += 1
            self.arrows.append([math.atan2(mouse_position[1] - (self.player_pos_one[1] + 32),
                               mouse_position[0] - (self.player_pos_one[0] + 26)),
                               self.player_pos_one[0] + 32, self.player_pos_one[1] + 32])

    def enemies_attack(self, enemie, index):
        self.bad_rect.top = enemie[1]
        self.bad_rect.left = enemie[0]
        if self.bad_rect.left < 64:
            self.load.hit.play()
            self.health_value -= random.randint(5, 20)
            self.enemies.pop(index)

    def check_collision(self, index):
        index_one = 0
        for bullet in self.arrows:
            bull_rect = pygame.Rect(self.load.arrow.get_rect())
            bull_rect.left = bullet[1]
            bull_rect.top = bullet[2]
            if self.bad_rect.colliderect(bull_rect):
                self.load.enemy.play()
                self.shoot_accuracy[0] += 1
                self.enemies.pop(index)
                self.arrows.pop(index_one)
            index_one += 1

    def check_if_player_win_or_lose(self):
        if pygame.time.get_ticks() >= 90000:
            self.running = 0
            self.exit_code = 1
        if self.health_value <= 0:
            self.running = 0
            self.exit_code = 0
        if self.shoot_accuracy[1] != 0:
            self.accuracy = self.shoot_accuracy[0] * 1.0 / self.shoot_accuracy[1] * 100
        else:
            self.accuracy = 0

    def check_if_player_exit(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    def display_win_or_lose(self):
        if self.exit_code == 0:
            font = pygame.font.Font(None, 24)
            text = font.render("Accuracy: " + str(self.accuracy) + "%", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.centerx = self.load.screen.get_rect().centerx
            text_rect.centery = self.load.screen.get_rect().centery + 24
            self.load.screen.blit(self.load.gameover, (0, 0))
            self.load.screen.blit(text, text_rect)
        else:
            pygame.font.init()
            font = pygame.font.Font(None, 24)
            text = font.render("Accuracy: " + str(self.accuracy) + "%", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.centerx = self.load.screen.get_rect().centerx
            text_rect.centery = self.load.screen.get_rect().centery + 24
            self.load.screen.blit(self.load.you_win, (0, 0))
            self.load.screen.blit(text, text_rect)
        while 1:
            for event in pygame.event.get():
                self.check_if_player_exit(event)
            pygame.display.flip()
