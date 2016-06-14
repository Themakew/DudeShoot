import pygame
from pygame.locals import *
from main import Game
from load import LoadResources
import sys


class Menu:
    load = LoadResources()
    lista = []
    pola = []
    font_size = 32
    font_path = 'data/coders_crux/coders_crux.ttf'
    font = pygame.font.Font
    image_surface = pygame.Surface
    ilosc_pol = 0
    background_color = (51, 51, 51)
    background = load.grass
    text_color = (255, 255, 153)
    seletion_color = (153, 102, 255)
    position = 0
    menu_position = (0, 0)
    menu_width = 0
    menu_height = 0

    class Pole:
        tekst = ''
        pole = pygame.Surface
        pole_rect = pygame.Rect
        zaznaczenie_rect = pygame.Rect

    def get_position(self):
        return self.position

    def init(self, lista, image_surface):
        self.lista = lista
        self.image_surface = image_surface
        self.ilosc_pol = len(self.lista)
        self.menu_structure()

    def draw(self, przesun=0):
        if przesun:
            self.position += przesun
            if self.position == -1:
                self.position = self.ilosc_pol - 1
            self.position %= self.ilosc_pol
        menu = pygame.Surface((self.menu_width, self.menu_height))
        menu.blit(self.background, (-1, -1))
        zaznaczenie_rect = self.pola[self.position].zaznaczenie_rect
        pygame.draw.rect(menu, self.seletion_color, zaznaczenie_rect)

        for i in xrange(self.ilosc_pol):
            menu.blit(self.pola[i].pole, self.pola[i].pole_rect)
        self.image_surface.blit(menu, self.menu_position)
        return self.position

    def menu_structure(self):
        przesuniecie = 0
        self.menu_height = 0
        self.font = pygame.font.Font(self.font_path, self.font_size)
        for i in xrange(self.ilosc_pol):
            self.pola.append(self.Pole())
            self.pola[i].tekst = self.lista[i]
            self.pola[i].pole = self.font.render(self.pola[i].tekst, 1, self.text_color)

            self.pola[i].pole_rect = self.pola[i].pole.get_rect()
            przesuniecie = int(self.font_size * 0.2)

            height = self.pola[i].pole_rect.height
            self.pola[i].pole_rect.left = przesuniecie
            self.pola[i].pole_rect.top = przesuniecie + (przesuniecie * 2 + height) * i

            width = self.pola[i].pole_rect.width + przesuniecie * 2
            height = self.pola[i].pole_rect.height + przesuniecie * 2
            left = self.pola[i].pole_rect.left - przesuniecie
            top = self.pola[i].pole_rect.top - przesuniecie

            self.pola[i].zaznaczenie_rect = (left, top, width, height)
            if width > self.menu_width:
                    self.menu_width = width
            self.menu_height += height
        x = self.image_surface.get_rect().centerx - self.menu_width / 2
        y = self.image_surface.get_rect().centery - self.menu_height / 2
        mx, my = self.menu_position
        self.menu_position = (x + mx, y + my)


if __name__ == "__main__":
    menu = Menu()

    menu.load.screen.blit(menu.background, (0, 0))
    menu.init(['Play', 'Quit'], menu.load.screen)
    menu.draw()
    pygame.key.set_repeat(199, 69)  # (delay,interval)
    pygame.display.update()

    while 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    menu.draw(-1)
                if event.key == K_DOWN:
                    menu.draw(1)
                if event.key == K_RETURN:
                    if menu.get_position() == 0:
                        game = Game()
                        game.game_loop()
                    if menu.get_position() == 1:
                        pygame.display.quit()
                        sys.exit()
                if event.key == K_ESCAPE:
                    pygame.display.quit()
                    sys.exit()
                pygame.display.update()
            elif event.type == QUIT:
                pygame.display.quit()
                sys.exit()
        pygame.time.wait(8)
