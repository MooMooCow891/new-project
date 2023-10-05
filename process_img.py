from PIL import Image
from screeninfo import get_monitors 
import pygame
import time

pygame.init()

maze1_path = "C:\\Users\\Lenovo\\Tony\\Code\\new project\\Assets\\maze1.png"

def get_screen_size():
	for monitor in get_monitors():
		return (monitor.width, monitor.height)

font = pygame.font.SysFont('arial', 20)
def show_mouse(x, y):
	text_1 = font.render(str(x) + ", " + str(y), True, (0, 0, 0))
	screen.blit(text_1, (x + 20, y - 5))

width_screen, height_screen = get_screen_size()
screen = pygame.display.set_mode((width_screen, height_screen))
print(width_screen, height_screen)

img = Image.open(maze1_path).resize((width_screen, height_screen), Image.ANTIALIAS).convert('L')
pixel_list = list(img.getdata())
pixel_matrix = [pixel_list[indx_y * width_screen: (indx_y + 1) * width_screen] for indx_y in range(height_screen)]
matrix_bool = [[True if x != 255 else False for x in y] for y in pixel_matrix]

list_test = []
for indx_y, y in enumerate(pixel_matrix):
	for indx_x, x in enumerate(y):
		if x != 255:
			list_test.append(True)
		else:
			list_test.append(False)

x = 20
y = 100
len_close_button = 25
close_button = False
w = a = s = d = False
while True:
	screen.fill((255, 255, 255))
	screen.blit(pygame.transform.scale(pygame.image.load(maze1_path), (width_screen, height_screen)), (0, 0))
	pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))

	mouse_x, mouse_y = pygame.mouse.get_pos()
	show_mouse(mouse_x, mouse_y)

	for event in pygame.event.get():
		if mouse_y <= len_close_button:
			pygame.draw.rect(screen, (255, 0, 0), (width_screen - len_close_button, 0, len_close_button, len_close_button))
			close_button = True
		else:
			close_button = False

		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and close_button and mouse_x >= width_screen - len_close_button and mouse_x <= width_screen and mouse_y >= 0 and mouse_y <= len_close_button:
			exit()

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

	if w and True not in matrix_bool[y + 3][x:x + 50]:
		y -= 5
	if a and True not in [lis[x + 8] for lis in matrix_bool[y:y + 50]]:
		x -= 5
	if s and True not in matrix_bool[y + 45][x:x + 50]:
		y += 5
	if d and True not in [lis[x + 41] for lis in matrix_bool[y:y + 50]]:
		x += 5

	pygame.display.flip()



# reconstruct = Image.new('RGB', (width_screen, height_screen), color='white')
# for y, lis in enumerate(pixel_matrix):
# 	for x, ele in enumerate(lis):
# 		reconstruct.putpixel((x, y), (ele, ele, ele))

# reconstruct.save('new_image.jpg')

# reconstruct = Image.new('RGB', (width_screen, height_screen), color='white')
# for indx, ele in enumerate(list_test):
# 	if ele == True:
# 		reconstruct.putpixel((indx % width_screen, indx // width_screen), (0, 0, 0))
# 	else:
# 		reconstruct.putpixel((indx % width_screen, indx // width_screen), (255, 255, 255))
# reconstruct.save("test_img.jpg")

