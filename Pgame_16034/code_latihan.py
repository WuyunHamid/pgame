import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
done = False
warna_bg = (0, 0, 255)

pygame.display.set_caption("Hallo APP")

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and \
	event.key == pygame.K_ESCAPE:
			done = True

	screen.fill(warna_bg)
	pygame.draw.line(screen,(240, 24, 55),(0, 0),(350, 350), 5)
	pygame.draw.line(screen,(255, 0, 255),(350, 350),(640, 480), 5)

	pygame.display.flip()
