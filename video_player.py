import pygame#import pygame
from time import sleep#import the time module

pygame.init()#start pygame
screen = pygame.display.set_mode((700, 400))#make the window
movie = pygame.movie.Movie("filename.mpg")#setting the file to play
pygame.mixer.quit()#stops the mixer from playing random audio
movie.play()#play the movie

while True:#forever loop
	if not(movie.get_busy()):#if the movie is'nt playing
		print("rewind")
		movie.rewind()#rewind it
		movie.play()#play it after rewinding
		#if the cross button is clicked close the program so you dont hve to control-C 
	if pygame.QUIT in [e.type for e in pygame.event.get()]:
		break
	
