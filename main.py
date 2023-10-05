# invite link: https://prod.liveshare.vsengsaas.visualstudio.com/join?35834D5A3EDFEAE1872B9FB073B2AC9CC7B3
# "close button.jpg" taken from DownloadClipart.net

import os

os.system("pip install pygame")
os.system("pip install screeninfo")
os.system("pip install time")
os.system("pip install PIL")

import pygame
from screeninfo import get_monitors # a library that allows you to get the size of your screen, among other things
import time # a library that allows you to keep track of the time
from PIL import Image

# compulsory stuff for pygame to work without breaking
pygame.init()

# get width and height of the monitor
def get_screen_size():
	for monitor in get_monitors():
		return (monitor.width, monitor.height)

width_screen, height_screen = get_screen_size()
screen = pygame.display.set_mode((width_screen, height_screen))
# display the window so that it exactly fits with the screen. 

exit_button_path = "Assets\\close_button.png"
close_button = False
# a bunch of variables that will later be used for the exit close button

# a bunch of prerequisiting variables for the player sprite
running1 = True
running2 = False
running3 = False
running4 = False
w = a = s = d = False
mouse_x, mouse_y = pygame.mouse.get_pos()
len_close_button = 25
len_player = 50
player_speed = 1
touching_left = touching_right = touching_top = touching_bottom = False
x_position = 10
y_position = 10
show_list = []
thinkness = 11
get_event = pygame.event.get()

mr_daniel_path = "mr daniel.png"
maze1_path = "Assets\\maze1.png"


pixel_list = list(Image.open(maze1_path).resize((width_screen, height_screen), Image.ANTIALIAS).convert('L').getdata())
pixel_matrix = [pixel_list[indx_y * width_screen: (indx_y + 1) * width_screen] for indx_y in range(height_screen)]

start_time = pygame.time.get_ticks()
def get_time():
	return (pygame.time.get_ticks() - start_time)/1000

# conviniently shows the precise (x, y) coordinates of the mouse so you know where to put stuff more easily
font = pygame.font.SysFont('arial', 20)
font_200 = pygame.font.SysFont('arial', 200)
def show_mouse(x, y):
	text_1 = font.render(str(x) + ", " + str(y), True, (0, 0, 0))
	screen.blit(text_1, (x + 20, y - 5))

# A Rectangle object, the equivalent of a blueprint to create more sprites conviniently
class Rectangle:
	def __init__(self, *args): # By using *args, you can input any amount of parameters you want.
		if len(args) == 5:     # I did this because I want the function to be able to handle different
			color = args[0]    # amount of inputs. So, if you don't specify the color you want; you tell
			x_position = args[1] # the program the x coordinate, y coordinate, height, and width, but
			y_position = args[2] # not the color, the function will immediately default the color of the
			length = args[3]   # rectangle to black unless specified otherwise.
			width = args[4]
		else:
			color = (0, 0, 0)
			x_position = args[0]
			y_position = args[1]
			length = args[2]
			width = args[3]	

		self.color = color
		self.x_position = x_position
		self.y_position = y_position
		self.length = length
		self.width = width

		# To draw a rectangle, you need to tell what surface to draw it on (it's drawn onto the "screen"
		# surface in this case). Then, you specify the coordinates and the size of the rectangle.
		pygame.draw.rect(screen, color, (self.x_position, self.y_position, self.length, self.width))

		# this just collect the information of all the sprites so it can be processed later
	def info(self):
		return [self.x_position, self.y_position, self.length, self.width]
		
	def collision(self, list_of_info):
		global x_position, y_position, w, a, s, d
		touching_left_list = []
		touching_right_list = []
		touching_top_list = []
		touching_bottom_list = []

		for list in list_of_info: 
			if list != [self.x_position, self.y_position, self.length, self.width]:
				x_stuff, y_stuff, len_stuff, width_stuff = list[0], list[1], list[2], list[3]
				
				[touching_left_list.append(True) if self.x_position + len_player == x_stuff
				 and self.y_position + self.width > y_stuff 
				 and self.y_position < y_stuff + width_stuff  
				 else touching_left_list.append(False)]


				[touching_right_list.append(True) if self.x_position == x_stuff + len_stuff 
				 and self.y_position + self.width > y_stuff 
				 and self.y_position < y_stuff + width_stuff 
				 else touching_right_list.append(False)]


				[touching_top_list.append(True) if self.y_position + self.width == y_stuff 
				and self.x_position + len_player > x_stuff 
				and self.x_position < x_stuff + len_stuff 
				else touching_top_list.append(False)]
				

				[touching_bottom_list.append(True) if self.y_position == y_stuff + width_stuff 
				and self.x_position + len_player > x_stuff 
				and self.x_position < x_stuff + len_stuff 
				else touching_bottom_list.append(False)]

		for event in get_event:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_d: 
					d = True
				if event.key == pygame.K_a:
					a = True
				if event.key == pygame.K_w:
					w = True
				if event.key == pygame.K_s:
					s = True

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_d:
					d = False
				if event.key == pygame.K_a:
					a = False
				if event.key == pygame.K_w:
					w = False
				if event.key == pygame.K_s:
					s = False
		
		if d and True not in touching_left_list and x_position + len_player < width_screen:
			x_position += player_speed
		if a and True not in touching_right_list and x_position > 0:
			x_position -= player_speed
		if w and True not in touching_bottom_list and y_position > 0:
			y_position -= player_speed
		if s and True not in touching_top_list and y_position + len_player < height_screen:
			y_position += player_speed

# A class that is similar to the Rectangle object, but is slightly different.
class EndPoint(Rectangle):
	def if_in(self, info_list):
		x_obj, y_obj, len_obj, width_obj = info_list[0], info_list[1], info_list[2], info_list[3]

		if x_obj + len_obj > self.x_position and x_obj < self.x_position + self.length and y_obj + width_obj > self.y_position and y_obj < self.y_position + self.width:
			return True

def rudimentary_controls():
	mouse_x, mouse_y = pygame.mouse.get_pos()
	# if you hover close to the top of your screen, the close button will appear. Just a cool ornamental
	# feature. 
	if mouse_y <= len_close_button:
		screen.blit(pygame.transform.scale(pygame.image.load(exit_button_path), (len_close_button, len_close_button)), (width_screen - len_close_button, 0))
		#pygame.draw.rect(screen, (255, 0, 0), (width_screen - len_close_button, 0, len_close_button, len_close_button))
		close_button = True
	else:
		close_button = False

	for event in get_event:
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if close_button and mouse_x >= width_screen - len_close_button and mouse_x <= width_screen and mouse_y >= 0 and mouse_y <= len_close_button:
					exit() 

# the running1 variable is just a remnant of the code I copied and pasted. "while True:" works fine too	
# also, this is basically the first level/stage						
while running1:
	get_event = pygame.event.get()
	# color the screen with a white background
	screen.fill((255,255,255))
	# show the position of the mouse
	mouse_x, mouse_y = pygame.mouse.get_pos()
	show_mouse(mouse_x, mouse_y)
	screen.blit(font.render(str(get_time()), True, (0, 0, 0)), (50, 50))

	# create the player sprite as well as 2 other random blocks of barrier
	Player = Rectangle((0, 0, 255), x_position, y_position, len_player, len_player)

	Wall1 = Rectangle(0, 75, 265, 10)
	Wall2 = Rectangle(130, 0, width_screen - 131, 10)
	Wall3 = Rectangle(255, 75, 10, 285)
	Wall4 = Rectangle(255, 360, 260, 10)
	Wall5 = Rectangle(130, 145, 10, 285)
	Wall6 = Rectangle(130, 430, 1310, 10)
	Wall7 = Rectangle(390, 290, 10, 70)
	Wall8 = Rectangle(260, 215, 895, 10)
	Wall9 = Rectangle(510, 220, 10, 70)
	Wall10 = Rectangle(765, 145, 10, 145)
	Wall11 = Rectangle(635, 285, 140, 10)
	Wall12 = Rectangle(635, 285, 10, 75)

	Wall13 = Rectangle(1020, 220, 10, 70)
	Wall14 = Rectangle(1020, 285, 380, 10)
	Wall15 = Rectangle(1400, 215, 10, 145)
	Wall16 = Rectangle(765, 360, 10, 70)
	Wall17 = Rectangle(635, 435, 10, 70)
	Wall18 = Rectangle(385, 435, 10, 70)
	Wall19 = Rectangle(255, 500, 140, 10)
	Wall20 = Rectangle(1020, 435, 10, 140)

	Wall21 = Rectangle(380, 0, 10, 145)
	Wall22 = Rectangle(380, 140, 270, 10)
	Wall23 = Rectangle(640, 75, 10, 75)
	Wall24 = Rectangle(510, 75, 265, 10)
	Wall25 = Rectangle(890, 0, 10, 150)
	Wall26 = Rectangle(890, 145, 140, 10)
	Wall27 = Rectangle(1020, 75, 10, 75)
	Wall28 = Rectangle(1020, 75, 390, 10)
	Wall29 = Rectangle(1145, 145, 515, 10)
	Wall30 = Rectangle(1275, 145, 10, 75)
	Wall31 = Rectangle(1525, 70, 10, 80)
	Wall32 = Rectangle(1655, 70, 10, 290)
	Wall33 = Rectangle(1780, 0, 10, 150)
	
	Wall34 = Rectangle(1655, 215, 135, 10)
	Wall35 = Rectangle(1780, 220, 10, 70)
	Wall36 = Rectangle(1655, 355, 265, 10)
	Wall37 = Rectangle(1780, 360, 10, 75)
	Wall38 = Rectangle(890, 285, 10, 75)
	Wall39 = Rectangle(890, 355, 395, 10)
	Wall40 = Rectangle(1275, 360, 10, 145)
	Wall41 = Rectangle(1275, 495, 135, 10)
	Wall42 = Rectangle(1400, 495, 10, 150)
	Wall43 = Rectangle(1275, 640, 135, 10)
	Wall44 = Rectangle(1275, 640, 10, 150)
	Wall45 = Rectangle(1405, 570, 130, 10)
	Wall46 = Rectangle(1525, 215, 10, 360)
	Wall47 = Rectangle(1530, 430, 135, 10)

	Wall48 = Rectangle(1650, 500, 420, 10)
	Wall49 = Rectangle(1650, 500, 10, 145)
	Wall50 = Rectangle(1530, 640, 10, 290)
	Wall51 = Rectangle(1530, 640, 130, 10)
	Wall52 = Rectangle(1530, 925, 130, 10)
	Wall53 = Rectangle(1650, 925, 10, 80)
	Wall54 = Rectangle(1280, 710, 510, 10)
	Wall55 = Rectangle(1780, 570, 10, 150)
	Wall56 = Rectangle(1910, 0, 10, 1005)
	Wall57 = Rectangle(1655, 780, 265, 10)
	Wall58 = Rectangle(1655, 850, 135, 10)
	Wall59 = Rectangle(1780, 855, 10, 150)
	Wall60 = Rectangle(1785, 995, 135, 10)
	Wall61 = Rectangle(1525, 990, 10, 90)
	Wall62 = Rectangle(1525, 215, 10, 360)
	Wall63 = Rectangle(1530, 430, 135, 10)

	Wall64 = Rectangle(0, 495, 140, 10)
	Wall65 = Rectangle(125, 500, 10, 75)
	Wall66 = Rectangle(125, 565, 140, 10)
	Wall67 = Rectangle(255, 575, 10, 75)
	Wall68 = Rectangle(0, 640, 135, 10)
	Wall69 = Rectangle(125, 645, 10, 75)
	Wall70 = Rectangle(125, 710, 260, 10)
	Wall71 = Rectangle(380, 570, 10, 220)
	Wall72 = Rectangle(380, 640, 140, 10)
	Wall73 = Rectangle(510, 500, 10, 150)
	Wall74 = Rectangle(515, 570, 380, 10)
	Wall75 = Rectangle(765, 495, 135, 10)
	Wall76 = Rectangle(890, 500, 10, 140)
	Wall77 = Rectangle(890, 640, 260, 10)
	Wall78 = Rectangle(1020, 645, 10, 75)
	Wall79 = Rectangle(1145, 500, 10, 290)
	Wall80 = Rectangle(890, 780, 260, 10)
	Wall80 = Rectangle(1150, 565, 135, 10)
	Wall81 = Rectangle(1020, 780, 10, 80)
	Wall82 = Rectangle(1025, 850, 380, 10)
	Wall83 = Rectangle(1400, 785, 10, 215)
	Wall84 = Rectangle(890, 715, 10, 70)
	Wall85 = Rectangle(760, 710, 140, 10)
	Wall86 = Rectangle(760, 645, 10, 65)
	Wall87 = Rectangle(635, 645, 10, 145)
	Wall88 = Rectangle(635, 645, 135, 10)
	Wall89 = Rectangle(635, 780, 135, 10)
	Wall90 = Rectangle(510, 710, 130, 10)
	Wall91 = Rectangle(1525, 215, 10, 360)

	Wall92 = Rectangle(380, 780, 140, 10)
	Wall93 = Rectangle(510, 780, 10, 80)
	Wall94 = Rectangle(510, 855, 390, 10)
	Wall95 = Rectangle(890, 855, 10, 75)
	Wall96 = Rectangle(890, 925, 265, 10)
	Wall97 = Rectangle(1145, 925, 10, 825)
	Wall98 = Rectangle(1270, 925, 10, 190)
	Wall99 = Rectangle(1020, 1000, 10, 80)

	Wall100 = Rectangle(0, 925, 520, 10)
	Wall101 = Rectangle(510, 925, 10, 80)
	Wall102 = Rectangle(510, 1000, 140, 10)
	Wall103 = Rectangle(130, 785, 10, 75)
	Wall104 = Rectangle(130, 785, 140, 10)
	Wall105 = Rectangle(260, 785, 10, 220)
	Wall106 = Rectangle(125, 995, 140, 10)
	Wall107 = Rectangle(265, 850, 130, 10)
	Wall108 = Rectangle(0, 925, 520, 10)
	Wall109 = Rectangle(510, 925, 10, 80)
	Wall110 = Rectangle(0, 1070, 1790, 10)
	Wall111 = Rectangle(380, 1000, 10, 80)
	Wall112 = Rectangle(640, 925, 135, 10)
	Wall113 = Rectangle(765, 925, 10, 155)
	Wall114 = Rectangle(765, 995, 225, 10)

	#Wall6 = Rectangle(129, 43)

	EndPoint1 = EndPoint((255, 255, 255), 1800, 1020, 100, 100)



	register = [
				Player.info(), 
				Wall1.info(), 
				Wall2.info(), 
				Wall3.info(), 
				Wall4.info(),
				Wall5.info(),
				Wall6.info(), 
				Wall7.info(), 
				Wall8.info(), 
				Wall9.info(), 
				Wall10.info(), 
				Wall11.info(),
				Wall12.info(),
				Wall13.info(), 
				Wall14.info(),
				Wall15.info(),
				Wall16.info(), 
				Wall17.info(), 
				Wall18.info(), 
				Wall19.info(),
				Wall20.info(),
				Wall21.info(), 
				Wall22.info(), 
				Wall23.info(), 
				Wall24.info(), 
				Wall25.info(),
				Wall26.info(),
				Wall27.info(), 
				Wall28.info(),
				Wall29.info(),
				Wall30.info(), 
				Wall31.info(), 
				Wall32.info(), 
				Wall33.info(),
				Wall34.info(),
				Wall35.info(),
				Wall36.info(), 
				Wall37.info(), 
				Wall38.info(), 
				Wall39.info(), 
				Wall40.info(),
				Wall41.info(),
				Wall42.info(), 
				Wall43.info(),
				Wall44.info(),
				Wall45.info(), 
				Wall46.info(), 
				Wall47.info(),
				Wall48.info(),
				Wall49.info(), 
				Wall50.info(), 
				Wall51.info(), 
				Wall52.info(), 
				Wall53.info(),
				Wall54.info(),
				Wall55.info(), 
				Wall56.info(),
				Wall57.info(),
				Wall58.info(), 
				Wall59.info(), 
				Wall60.info(), 
				Wall61.info(), 
				Wall62.info(),
				Wall63.info(), 
				Wall64.info(),
				Wall65.info(),
				Wall66.info(), 
				Wall67.info(), 
				Wall68.info(), 
				Wall69.info(),
				Wall70.info(),
				Wall71.info(), 
				Wall72.info(), 
				Wall73.info(), 
				Wall74.info(), 
				Wall75.info(),
				Wall76.info(),
				Wall77.info(), 
				Wall78.info(),
				Wall79.info(),
				Wall80.info(), 
				Wall81.info(), 
				Wall82.info(), 
				Wall83.info(),
				Wall84.info(),
				Wall85.info(),
				Wall86.info(), 
				Wall87.info(), 
				Wall88.info(), 
				Wall89.info(), 
				Wall90.info(),
				Wall91.info(),
				Wall92.info(), 
				Wall93.info(),
				Wall94.info(),
				Wall95.info(), 
				Wall96.info(), 
				Wall97.info(),
				Wall98.info(),
				Wall99.info(), 
				Wall100.info(), 
				Wall101.info(), 
				Wall102.info(), 
				Wall103.info(),
				Wall104.info(),
				Wall105.info(), 
				Wall106.info(),
				Wall107.info(),
				Wall108.info(), 
				Wall109.info(), 
				Wall110.info(), 
				Wall111.info(), 
				Wall112.info(), 
				Wall113.info(), 
				Wall114.info(), 
			   ]
	Player.collision(register)

	if EndPoint1.if_in(Player.info()):
		running2 = True
		running1 = False

	rudimentary_controls()
	pygame.display.flip()

x_position = 0
y_position = 315
while running2:
	get_event = pygame.event.get()
	screen.fill((255, 255, 255))
	rudimentary_controls()

	screen.blit(font_200.render("YOU WIN!", True, (0, 0, 0)), (600, 50))
	screen.blit(font.render("You escaped the Teacher", True, (0, 0, 0)), (800, 400))
	screen.blit(pygame.transform.scale(pygame.image.load(mr_daniel_path), (800, 500)), (500, 500))
	#screen.blit(pygame.transform.scale(pygame.image.load(exit_button_path), (len_close_button, len_close_button)), (width_screen - len_close_button, 0))
	pygame.display.flip()
