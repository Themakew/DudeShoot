import pygame


class LoadResources:

    # load pygame
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

    # load screen
    pygame.display.set_caption("DudeShoot")
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))

    # sprite sheets
    player = pygame.image.load("resources/images/dude.png")
    grass = pygame.image.load("resources/images/grass.jpg")
    castle = pygame.image.load("resources/images/castle.png")
    arrow = pygame.image.load("resources/images/bullet.png")
    bad_guy_image = pygame.image.load("resources/images/badguy.png")
    health_bar = pygame.image.load("resources/images/healthbar.png")
    health = pygame.image.load("resources/images/health.png")
    gameover = pygame.image.load("resources/images/gameover.png")
    you_win = pygame.image.load("resources/images/youwin.png")

    # audio
    hit = pygame.mixer.Sound("resources/audio/explode.wav")
    enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
    shoot = pygame.mixer.Sound("resources/audio/shoot.wav")

    bad_rect = pygame.Rect(bad_guy_image.get_rect())

    def load_audio(self):
        self.hit.set_volume(0.05)
        self.enemy.set_volume(0.05)
        self.shoot.set_volume(0.05)
        pygame.mixer.music.load('resources/audio/moonlight.wav')
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.25)

    def draw_background(self):
        self.screen.blit(self.grass, (0, 0))

    def draw_elements_on_the_screen(self):
        self.screen.blit(self.castle, (0, 30))
        self.screen.blit(self.castle, (0, 135))
        self.screen.blit(self.castle, (0, 240))
        self.screen.blit(self.castle, (0, 345))
