import pygame
import pygame_gui

import setings
import char_class

class Char_Img_Redact_App():
	def __init__(self):
		self.game_setings = setings.Setings()

		pygame.init()
		pygame.display.set_caption('CharReactorv5')
		if(self.game_setings.screen_mode == pygame.FULLSCREEN):
			self.window_surface = pygame.display.set_mode((0,0),  pygame.FULLSCREEN)
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
			relative_rect =	pygame.Rect((20, 20),(100, 40)),
			text = 'Randomize',
			container = self.panel_options_appear,
			manager = self.manager)

	def screen_update(self, time_delta):
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
					if self.char.apearence.tail == char_class.AP_TAIL_FOXTAIL:
						self.char.apearence.tail = char_class.AP_TAIL_CATTAIL
					elif self.char.apearence.tail == char_class.AP_TAIL_CATTAIL:
						self.char.apearence.tail= char_class.AP_TAIL_FOXTAIL
					self.char.apearence.reload_img_in_list(self.char_img_list, char_class.LAYER_TAIL)
					self.char_img = char_class.img_merge(self.char_img_list)
					
				
				if event.ui_element == self.button_exit:
					self.is_running = False
					
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
	
