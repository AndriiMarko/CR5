import pygame
import pygame_gui

import setings

game_setings = setings.Setings()

pygame.init()
pygame.display.set_caption('CharReactorv5')
window_surface = pygame.display.set_mode((game_setings.screen_width, 
	game_setings.screen_hight))
manager = pygame_gui.UIManager((game_setings.screen_width, 
	game_setings.screen_hight))
clock = pygame.time.Clock()
windows_rect = window_surface.get_rect()
is_running = True

button_randomize = pygame_gui.elements.UIButton(
	relative_rect =	pygame.Rect((200, 200),(100, 100)),
	text = 'Randomize',
	manager = manager)

while is_running:
	time_delta  = clock.tick(game_setings.fps)/1000.0
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False
		if event.type == pygame.USEREVENT:
			if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
				if event.ui_element == button_randomize:
					print("randomize click")
		manager.process_events(event)

	manager.update(time_delta)
	manager.draw_ui(window_surface)
	pygame.display.update()
