import pygame.mixer#import pygame audio mixer
from time import sleep# import the sleep function

pygame.mixer.init(48000, -16, 1, 1024)#initialize pygame mixer

sound = pygame.mixer.Sound("lotr.wav")#set the audio file
channelA = pygame.mixer.Channel(1) #set the channel
channelA.play(sound)#play the auidio
sleep(60.0)#let it play for 
