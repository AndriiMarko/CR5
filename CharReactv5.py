import pygame
import pygame_gui

import setings
import char_class

class Char_Img_Redact_App():
	def __init__(self):
		self.game_setings = setings.Setings()

		pygame.init()
		pygame.display.set_caption('CharReactorv5')
		if self.game_setings.full_screen :
			self.window_surface = pygame.display.set_mode((0,0),  pygame.FULLSCREEN |  pygame.HWSURFACE | pygame.DOUBLEBUF )
			self.game_setings.screen_width = pygame.display.Info().current_w
			self.game_setings.screen_height = pygame.display.Info().current_h
		else:
			self.window_surface = pygame.display.set_mode((self.game_setings.screen_width, self.game_setings.screen_height))
		
		self.manager = pygame_gui.UIManager((self.game_setings.screen_width,	self.game_setings.screen_height))
		self.clock = pygame.time.Clock()
		#windows_rect = window_surface.get_rect()
		self.is_running = True

		self.char = char_class.Character("Char")
		#self.char_img = self.char.apearence.draw_char()
		#print(char_img.get_width(), char_img.get_height())
		self.char_zone_width =  (self.game_setings.screen_width//4)*3
		#print(char_zone_width)
		if self.char_zone_width < char_class.CHAR_IMG_WIDTH:
			self.scale_coef = char_class.CHAR_IMG_WIDTH/(self.char_zone_width)
		else:
			self.scale_coef = 1.0
		#print(scale_coef)
		self.new_heigth = char_class.CHAR_IMG_HEIGHTT/self.scale_coef
		self.char_rect =  pygame.Rect(0,0, self.char_zone_width,	int(self.new_heigth))
		
		#print(char_rect.width, new_heigth, char_rect.height)
			#char_img.get_rect()
		self.char_img_list = []
		self.char.apearence.load_all_body_img_resized(self.char_img_list, (self.char_rect.width, self.char_rect.height))
		self.char_img = char_class.img_merge(self.char_img_list)
		#self.char_img = pygame.transform.scale(self.char_img, (self.char_rect.width, self.char_rect.height))

		self.bg =pygame.image.load("img/bg/crbg.png")
		self.bg = pygame.transform.scale(self.bg, (self.char_rect.width, self.char_rect.height))
		#bg = pygame.Surface((char_rect.width, char_rect.height))
		#bg.fill((200, 200, 200))


		self.char_rect.centery = self.window_surface.get_rect().centery
		self.char_rect.x = self.window_surface.get_rect().x

		#gui
		self.gui_rect =  pygame.Rect( self.char_zone_width ,0, (self.game_setings.screen_width//4), self.game_setings.screen_height )

		self.panel_options = pygame_gui.elements.UIPanel(self.gui_rect,
			starting_layer_height=1, manager = self.manager)
		self.panel_options_main = pygame_gui.elements.UIPanel(pygame.Rect(0,0,
			self.gui_rect.width, self.gui_rect.height//5),
			starting_layer_height=2,
			manager = self.manager,
			container = self.panel_options)
		self.button_exit = pygame_gui.elements.UIButton(
			relative_rect =	pygame.Rect((self.gui_rect.width-60, 10),(40, 40)),
			text = 'X',
			container = self.panel_options_main,
			manager = self.manager)
			
		self.panel_options_appear = pygame_gui.elements.UIPanel(pygame.Rect(0,self.gui_rect.height//5,
			self.gui_rect.width, (self.gui_rect.height//5)*4),
			starting_layer_height=1,
			manager = self.manager,
			container = self.panel_options)
		self.button_randomize = pygame_gui.elements.UIButton(
			relative_rect =	pygame.Rect((10, 10),(100, 30)),
			text = 'Randomize',
			container = self.panel_options_appear,
			manager = self.manager)
		self.tail_label =  pygame_gui.elements.UILabel(relative_rect = pygame.Rect((10, 50),(80,30)),
			text = 'Tail',
			manager = self.manager,
			container = self.panel_options_appear)
		self.tail_dropdown = pygame_gui.elements.UIDropDownMenu([tail[0] for tail in char_class.AP_TAILS],
			self.char.apearence.tail[0],
			pygame.Rect((10, 80), (100, 30) ),
			manager = self.manager,
			container = self.panel_options_appear)
		self.button_tail_color_pick = pygame_gui.elements.UIButton(
			relative_rect =	pygame.Rect((120, 50),(80, 30)),
			text = 'TailColor',
			container = self.panel_options_appear,
			manager = self.manager)
		self.button_tail_color_pick2 = pygame_gui.elements.UIButton(
			relative_rect =	pygame.Rect((120, 80),(80, 30)),
			text = 'TailColor2',
			container = self.panel_options_appear,
			manager = self.manager)
		self.button_tail_color_default = pygame_gui.elements.UIButton(
			relative_rect =	pygame.Rect((210, 80),(60, 30)),
			text = 'Default',
			container = self.panel_options_appear,
			manager = self.manager)
			
		self.colour_picker = None
		self.colour_type = char_class.COLOR_TYPE_NONE

	def screen_update(self, time_delta):
		self.window_surface.fill((134, 135, 138))
		self.window_surface.blit(self.bg, self.char_rect)
		self.window_surface.blit(self.char_img, self.char_rect)
		self.manager.update(time_delta)
		self.manager.draw_ui(self.window_surface)
		
		pygame.display.update()
	
	def events_proc(self, event):
		if event.type == pygame.QUIT:
			self.is_running = False
		if event.type == pygame.USEREVENT:
			if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
				
				if event.ui_element == self.button_randomize:
					#self.panel_options_appear.hide()
					if self.char.apearence.tail == char_class.AP_TAIL_FOXTAIL:
						self.char.apearence.tail = char_class.AP_TAIL_CATTAIL
					elif self.char.apearence.tail == char_class.AP_TAIL_CATTAIL:
						self.char.apearence.tail= char_class.AP_TAIL_FOXTAIL
					self.char.apearence.reload_img_in_list(self.char_img_list, char_class.LAYER_TAIL)
					self.char_img = char_class.img_merge(self.char_img_list)
					
				
				if event.ui_element == self.button_exit:
					self.is_running = False
					
				if event.ui_element == self.button_tail_color_pick:
					self.colour_picker = pygame_gui.windows.UIColourPickerDialog(pygame.Rect(160, 50, 420, 400),
																self.manager,
																window_title='Change Colour',
																initial_colour= pygame.Color(255, 255, 255))
					self.button_tail_color_pick.disable()
					self.button_tail_color_pick2.disable()
					self.colour_type = char_class.COLOR_TYPE_TAIL1
				
				if event.ui_element == self.button_tail_color_pick2:
					self.colour_picker = pygame_gui.windows.UIColourPickerDialog(pygame.Rect(160, 50, 420, 400),
																self.manager,
																window_title='Change Colour',
																initial_colour= pygame.Color(255, 255, 255))
					self.button_tail_color_pick.disable()
					self.button_tail_color_pick2.disable()
					self.colour_type = char_class.COLOR_TYPE_TAIL2
				
				if event.ui_element == self.button_tail_color_default:
					self.char.apearence.tail_color1 = 0
					self.char.apearence.tail_color2 = 0
					self.char.apearence.reload_img_in_list(self.char_img_list, char_class.LAYER_TAIL)
					self.char_img = char_class.img_merge(self.char_img_list)
					
			if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
				if event.ui_element == self.tail_dropdown:
					for tail in char_class.AP_TAILS:
						if tail[0] == self.tail_dropdown.selected_option:
							self.char.apearence.tail = tail
							self.char.apearence.reload_img_in_list(self.char_img_list, char_class.LAYER_TAIL)
							self.char_img = char_class.img_merge(self.char_img_list)
							break
			
			if event.user_type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED:
				if 	self.colour_type == char_class.COLOR_TYPE_TAIL1:
					self.char.apearence.tail_color1 = event.colour
					self.char.apearence.reload_img_in_list(self.char_img_list, char_class.LAYER_TAIL)
					self.char_img = char_class.img_merge(self.char_img_list)	
				if 	self.colour_type == char_class.COLOR_TYPE_TAIL2:
					self.char.apearence.tail_color2 = event.colour
					self.char.apearence.reload_img_in_list(self.char_img_list, char_class.LAYER_TAIL)
					self.char_img = char_class.img_merge(self.char_img_list)
			if event.user_type == pygame_gui.UI_WINDOW_CLOSE and    event.ui_element == self.colour_picker:
				self.button_tail_color_pick.enable()
				self.button_tail_color_pick2.enable()
				self.colour_picker = None
					
		self.manager.process_events(event)
		
	def run(self):
		while self.is_running:
			time_delta  = self.clock.tick(self.game_setings.fps)/1000.0
			for event in pygame.event.get():
				self.events_proc(event)
			self.screen_update(time_delta)
			
if __name__ == "__main__":
	app = Char_Img_Redact_App()
	app.run()
	
