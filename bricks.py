import pygame

color_type = {
    0: 'red',
    1: 'blue',
    2: 'green',
    3: 'yellow',
}


class Brick:
    def __init__(self, surf):
        self.bricks = []
        self.colors = []
        self.surf = surf
        self.create()

    def create(self):
        for i in range(8):
            color1 = color_type[i // 2]
            color2 = color_type[i // 2]
            for j in range(8):
                if j % 2 == 0:
                    color = color1
                else:
                    color = color2
                rect = pygame.Rect((15 + j * 60, 100 + i * 30), (50, 20))
                pygame.draw.rect(self.surf, color, rect)
                self.colors.append(color)
                self.bricks.append(rect)

    def render(self):
        for rect, color in zip(self.bricks, self.colors):
            pygame.draw.rect(self.surf, color, rect)
