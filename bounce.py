import pygame #import pygame

class Ball(pygame.sprite.Sprite): #the class for the ball

	def __init__(self, x, y, xdir, ydir, speed): #create the ball
		pygame.sprite.Sprite.__init__(self) 
		self.image = pygame.Surface([20, 20])
		self.image.fill(pygame.Color(0, 0, 0))
		pygame.draw.circle(self.image, pygame.Color(255, 0, 0), (10, 10), 10, 0) #draw the circle
		self.rect = self.image.get_rect()
		self.x, self.y = x, y
		self.xdir, self.ydir = xdir, ydir
		self.speed = speed

	def update(self): #updates the position
		self.x = self.x + (self.xdir * self.speed)
		self.y = self.y + (self.ydir * self.speed)
		if (self.x < 10) | (self.x > 490): #if it hits a wall it bounces
			self.xdir = self.xdir * -1
		if (self.y < 10) | (self.y > 490):
			self.ydir = self.ydir * -1
		self.rect.center = (self.x, self.y)

pygame.init()#initialize pygame
fps = pygame.time.Clock() #the refresh rate
window = pygame.display.set_mode((500, 500)) #make the pygame window
# make the seprate balls
ball = Ball(100, 250, 1, 1, 5)
ball2 = Ball(400, 10, -1, -1, 8)
ball3 = Ball(90, 80, -1, 1, 7)

while True: # it goes on forever
	#update the balls
	ball.update()
	ball2.update()
	ball3.update()
	#draw the window and the balls
	window.fill(pygame.Color(0, 0, 0))
	window.blit(ball.image, ball.rect)
	window.blit(ball2.image, ball2.rect)
	window.blit(ball3.image, ball3.rect)
	pygame.display.update()
	fps.tick(30)
