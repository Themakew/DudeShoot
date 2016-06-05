import pygame


class LoadResources:
    pygame.init()
    pygame.mixer.init()

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
