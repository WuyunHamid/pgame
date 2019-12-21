import pygame

pygame.init()
screen = pygame.display.set_mode((700, 550))
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
	pygame.draw.line(screen,(12, 12, 12),(500,200,),(500, 500), 3)
	pygame.draw.line(screen,(12, 12, 12),(200,500,),(500, 500), 3)
	pygame.draw.line(screen,(12, 12, 12),(500,200,),(200, 200), 3)
	pygame.draw.line(screen,(12, 12, 12),(200,500,),(200, 200), 3)
	pygame.display.flip()
