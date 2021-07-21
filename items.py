import pygame
import random

class rain_drop:
    def __init__(self, master, slope, length, width):
        self.master = master

        self.color = (0, 0, random.randrange(50, 255))

        self.slope = slope
        self.length = length
        self.width = width
        
        if slope < 0:
            self.x = random.randrange(0, master.get_width()*2)
        elif slope > 0:
            self.x = random.randrange(-master.get_width(), master.get_width())
        else:
            self.x = random.randrange(0, master.get_width())

        self.y = -length

    def update(self):
        self.y += 10
        self.x += self.slope

        pygame.draw.line(self.master, self.color, (self.x, self.y), (self.x+self.slope, self.y+self.length))
