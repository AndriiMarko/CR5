import pygame
import pygame_gui

import setings
import char_class
game_setings = setings.Setings()

pygame.init()
pygame.display.set_caption('CharReactorv5')
if(game_setings.screen_mode == pygame.FULLSCREEN):
	window_surface = pygame.display.set_mode((0,0),  pygame.FULLSCREEN)
else:
	window_surface = pygame.display.set_mode((game_setings.screen_width, 
		game_setings.screen_height))
manager = pygame_gui.UIManager((game_setings.screen_width, 
	game_setings.screen_height))
clock = pygame.time.Clock()
#windows_rect = window_surface.get_rect()
is_running = True

char = char_class.Character("Tail")
char_img = char.Draw_Char() 
char_rect = char_img.get_rect()

surf1 = pygame.Surface((char_img.get_width(), char_img.get_height()))
surf1.fill((200, 200, 200))


char_rect.centery = window_surface.get_rect().centery
char_rect.x = window_surface.get_rect().x

#gui
gui_rect =  pygame.Rect( (game_setings.screen_width//4)*3 ,0, 
	(game_setings.screen_width//4),game_setings.screen_height )

panel_options = pygame_gui.elements.UIPanel(gui_rect,
	starting_layer_height=1, manager = manager)
panel_options_main = pygame_gui.elements.UIPanel(pygame.Rect(0,0,
	gui_rect.width, gui_rect.height//5),
	starting_layer_height=2,
	manager = manager,
	container = panel_options)
button_exit = pygame_gui.elements.UIButton(
	relative_rect =	pygame.Rect((gui_rect.width-60, 10),(40, 40)),
	text = 'X',
	container = panel_options_main,
	manager = manager)
	
panel_options_appear = pygame_gui.elements.UIPanel(pygame.Rect(0,gui_rect.height//5,
	gui_rect.width, (gui_rect.height//5)*4),
	starting_layer_height=1,
	manager = manager,
	container = panel_options)
button_randomize = pygame_gui.elements.UIButton(
	relative_rect =	pygame.Rect((20, 20),(100, 40)),
	text = 'Randomize',
	container = panel_options_appear,
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
					
				if event.ui_element == button_exit:
					is_running = False
		manager.process_events(event)
		
	window_surface.blit(surf1, char_rect)
	window_surface.blit(char_img, char_rect)
	manager.update(time_delta)
	manager.draw_ui(window_surface)
	
	pygame.display.update()
