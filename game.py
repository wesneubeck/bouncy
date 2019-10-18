#!usr/bin/env python3

import os
import sys
import pygame
from pygame.locals import *

W = 400
H = 400


#   paddle object
class Paddle(pygame.sprite.Sprite):
	def __init__(self):
		self.image = pygame.Surface((90, 15))
		self.rect = self.image.get_rect()
		self.image.fill((0, 0, 255))
		self.rect.x = (W//2 - 45) 
		self.rect.y = 380

	def handles(self):
		self.key = pygame.key.get_pressed()
		if self.key[pygame.K_v]:
			self.rect.x -= 5
		if self.key[pygame.K_n]:
			self.rect.x += 5
	

#   ball object
class Ball(pygame.sprite.Sprite):
	def __init__(self):
		self.image = pygame.draw.circle(screen, (255, 0, 0), (200,200), 5)


		

pygame.init()
screen = pygame.display.set_mode((W, H))
paddle = Paddle()
ball = Ball()

running = True
while running:
	screen.fill((33, 176, 219))
	screen.blit(paddle.image, paddle.rect)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.unicode == 'q':
				pygame.quit()
				sys.exit()
	
	screen.blit(paddle.image, paddle.rect)
	paddle.handles()
	pygame.display.update()

