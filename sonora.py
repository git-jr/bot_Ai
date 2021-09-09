import pygame
pygame.init()

pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()

clock = pygame.time.Clock()
while pygame.mixer.music.get_busy():
    clock.tick(60)
    pygame.event.poll()