import pygame
import sys
from bricks import Brick
from player import Player, Ball


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Breakout Game")
        self.screen = pygame.display.set_mode((500, 625))
        self.clock = pygame.time.Clock()

        self.brick = Brick(self.screen)
        self.player = Player((250, 575))
        self.ball = Ball((250, 475), self.screen)
        self.movement = [False, False]

    def run(self):
        while True:
            self.brick.render()

            self.player.update(self.screen, self.movement[1] - self.movement[0])
            self.player.render(self.screen)

            self.ball.update(self.brick.bricks, self.brick.colors, self.player.plat)
            self.ball.render()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ball.pos[1] >= 625:
                        self.ball.reset()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick(60)


Game().run()
