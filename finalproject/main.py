import pygame

pygame.init()
pygame.mixer.init()

def play(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()
    
def main():
    song = "test.mp3"
    while True:
       
main()
