import pygame
import items
import random

pygame.init()

root = pygame.display.set_mode((1000,700), pygame.RESIZABLE)
clock = pygame.time.Clock()

rain_drops = []

white_noise = pygame.mixer.Sound("01-White-Noise-10min.wav")

thunder_sounds = [
    pygame.mixer.Sound("thun1.wav"),
    pygame.mixer.Sound("thun2.wav"),
    pygame.mixer.Sound("thun3.wav")
]

white_noise.play()

while 1:

    if random.randrange(1,500) == 1:
        root.fill((100,100,100))
        thunder_sounds[random.randrange(0,2)].play()
    else:
        root.fill((0,0,15))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    for i in range(50):
        rain_drops.append(items.rain_drop(root, 10, 10, 1))

    for drop in rain_drops:
        if drop.y >= root.get_height():
            rain_drops.remove(drop)
        else:
            drop.update()

    temp = 0

    for drop in rain_drops:
        temp += 1
        
    print(temp)

    clock.tick(60)
    pygame.display.update()
