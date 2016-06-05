import pygame


class LoadResources:
    player = pygame.image.load("resources/images/dude.png")
    grass = pygame.image.load("resources/images/grass.jpg")
    castle = pygame.image.load("resources/images/castle.png")
    arrow = pygame.image.load("resources/images/bullet.png")
    bad_guy_image_one = pygame.image.load("resources/images/badguy.png")
    bad_guy_image = bad_guy_image_one
    health_bar = pygame.image.load("resources/images/healthbar.png")
    health = pygame.image.load("resources/images/health.png")
    gameover = pygame.image.load("resources/images/gameover.png")
    you_win = pygame.image.load("resources/images/youwin.png")
