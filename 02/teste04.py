#tocando uma musica mp3 no python
import pygame

pygame.init()
pygame.mixer.music.load('ea.mp3.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
