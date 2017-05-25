import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((700, 400))
movie = pygame.movie.Movie("russian hacker.mpg")
pygame.mixer.quit()
movie.play()

while True:
	if not(movie.get_busy()):
		print("rewind")
		movie.rewind()
		movie.play()
	if pygame.QUIT in [e.type for e in pygame.event.get()]:
		break
	