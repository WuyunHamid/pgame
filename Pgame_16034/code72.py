# Pemrograman Game Praktikum 7
# latihan code 7.2 : Pgame

import pygame, sys
from pygame.locals import*

pygame.init ()

DYSPLAYSURF = pygame.display.set_mode ((800, 700))

pygame.display.set_caption ('Hello My Friends!')

while True: # main game loop
	for event in pygame.event.get ():
		if event.type == QUIT:
			pygame.quit ()
		sys.exit()
		pygame.display.update ()
	
