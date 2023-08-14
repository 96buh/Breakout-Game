import pygame

PLAT_WIDTH = 50


class Player:
    def __init__(self, pos):
        self.pos = list(pos)
        self.plat = pygame.Rect((self.pos[0], self.pos[1]), (PLAT_WIDTH, 10))

    def update(self, surf, movement):
        pygame.draw.rect(surf, (0, 0, 0), self.plat)
        if self.pos[0] <= 0:
            self.pos[0] = 1
        if self.plat.right > 500:
            self.pos[0] = 450
        self.pos[0] += movement * 4

    def render(self, surf):
        self.plat = pygame.Rect((self.pos[0], self.pos[1]), (PLAT_WIDTH, 10))
        pygame.draw.rect(surf, 'white', self.plat)


class Ball:
    def __init__(self, pos, surf):
        self.pos = list(pos)
        self.surf = surf
        self.ball = pygame.draw.circle(self.surf, 'white', (self.pos[0], self.pos[1]), 7)
        self.movement = [3, -3]

    def update(self, bricks, colors, player):
        pygame.draw.circle(self.surf, (0, 0, 0), (self.pos[0], self.pos[1]), 7)
        # 球和邊界碰撞
        if self.ball.right >= 500 or self.ball.left <= 0:
            self.movement[0] *= -1
        if self.ball.top <= 0:
            self.movement[1] *= -1
        # 球和目標碰撞
        index = self.ball.collidelist(bricks)
        if index != -1 and colors[index] != (0, 0, 0):
            colors[index] = (0, 0, 0)
            self.check_direction(self.ball, bricks[index])
        # 球和玩家碰撞
        if self.ball.colliderect(player):
            self.check_direction(self.ball, player)

        self.pos[0] += self.movement[0]
        self.pos[1] += self.movement[1]

    def render(self):
        self.ball = pygame.draw.circle(self.surf, 'white', (self.pos[0], self.pos[1]), 7)

    def check_direction(self, rect1, rect2):
        dr = abs(rect1.right - rect2.left)
        dl = abs(rect1.left - rect2.right)
        db = abs(rect1.bottom - rect2.top)
        dt = abs(rect1.top - rect2.bottom)
        if min(dl, dr) < min(dt, db):
            self.movement[0] *= -1
        else:
            self.movement[1] *= -1

    def reset(self):
        self.pos[0] = 250
        self.pos[1] = 475
        self.movement[0] = 3
        self.movement[1] = -3
