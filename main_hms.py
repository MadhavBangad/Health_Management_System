
# While Making GUI Just Note that a new window should appear to type Drank and also, Make it run in loop of 30 minutes

import pygame
# from pygame import mixer, event
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M")

file = "C:\\Coding\\Health_Management_System\\Resources\\ringtone_water.mp3"


def play_music(file):
    pygame.mixer.pre_init(44100, -16, 2, 2048)  # setup mixer to avoid sound lag
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)


def timer():
    play_music(file)

    print('Type "Drank"')
    i = input('>>>  ').lower()
    if i == 'drank':
        pygame.mixer.music.stop()


if __name__ == '__main__':
    timer()
            

