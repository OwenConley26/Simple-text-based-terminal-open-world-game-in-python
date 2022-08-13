x = 0
y = 0
def main():
	def checkloc():
		global x
		global y
		# maybe use ranges for entire areas!
		if x == 0 and y == 0:
			print ("you are in a field")
		elif x == 2 and y == 0:
			print ("you are on a dirt path next to a field")
		elif x == 2 and y == 7:
			print ("you are now at the entrance of a small town")
	def playerMove():
		global x
		global y
		move = input("> ")
		if move == "n":
			print("going north\n")
			y += 1
			checkloc()
			playerMove()
		elif move == "s":
			print("going south\n")
			y -= 1
			checkloc()
			playerMove()
		elif move == "e":
			print("going east\n")
			x += 1
			checkloc()
			playerMove()
		elif move == "w":
			print("going west\n")
			x -= 1
			checkloc()
			playerMove()
		elif move == "p":
			print (str(x) + " " + str(y) + "\n")
			playerMove()
		elif move == "q":
			print ("QUITING GAME!!!\n")
			pass
		elif move == "r":
			x = 0
			y = 0
			checkloc()
			playerMove()
		else:
			print("invalid input, try again...\n")
			playerMove()
	print ("### Open world text based game ###\np to check position, nswe to move, r to return to 0,0\n")
	checkloc()
	playerMove()
main()