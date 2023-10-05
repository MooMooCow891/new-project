	# 	touching_left_list = []
	# 	touching_right_list = []
	# 	touching_top_list = []
	# 	touching_bottom_list = []

	# 	# So basically, if the player character touches a wall, that wall will tell that the player is
	# 	# touching it. Since there are multiple walls, each of their reports will be stored in a list
	# 	# to make tracking easier. So if one of the walls is being touched by the player, it'll report back
	# 	# to the HQ and the player will not be able to move anymore so they can't phase through the walls.
	# 	for list in list_of_info: 
	# 		if list != [self.x_position, self.y_position, self.length, self.width]:
	# 			x_stuff, y_stuff, len_stuff, width_stuff = list[0], list[1], list[2], list[3]
				
	# 			# Check if the player sprite is touching anything
	# 			if self.x_position + len_player == x_stuff and self.y_position + self.width > y_stuff and self.y_position < y_stuff + width_stuff:
	# 				touching_left_list.append(True)
	# 			else:
	# 				touching_left_list.append(False)

	
	# 			if self.x_position == x_stuff + len_stuff and self.y_position + self.width > y_stuff and self.y_position < y_stuff + width_stuff:
	# 				touching_right_list.append(True)
	# 			else:
	# 				touching_right_list.append(False)

	# 			if self.y_position + self.width == y_stuff and self.x_position + len_player > x_stuff and self.x_position < x_stuff + len_stuff:
	# 				touching_top_list.append(True)
	# 			else:
	# 				touching_top_list.append(False)

	# 			if self.y_position == y_stuff + width_stuff and self.x_position + len_player > x_stuff and self.x_position < x_stuff + len_stuff:
	# 				touching_bottom_list.append(True)
	# 			else:
	# 				touching_bottom_list.append(False)
		
	# 	if True in touching_left_list:
	# 		self.touching_left = True
	# 	else:
	# 		self.touching_left = False

	# 	if True in touching_right_list:
	# 		self.touching_right = True
	# 	else:
	# 		self.touching_right = False

	# 	if True in touching_top_list:
	# 		self.touching_top = True
	# 	else:
	# 		self.touching_top = False

	# 	if True in touching_bottom_list:
	# 		self.touching_bottom = True
	# 	else:
	# 		self.touching_bottom = False

	# def check_left(self):
	# 	return self.touching_left
	
	# def check_right(self):
	# 	return self.touching_right
	
	# def check_left(self):
	# 	return 

# A class that is similar to the Rectangle object, but is slightly different.
# class EndPoint(Rectangle):
# 	def if_in(self, info_list):
# 		x_obj, y_obj, len_obj, width_obj = info_list[0], info_list[1], info_list[2], info_list[3]

# 		if x_obj + len_obj > self.x_position and x_obj < self.x_position + self.length and y_obj + width_obj > self.y_position and y_obj < self.y_position + self.width:
# 			return True