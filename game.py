board = [[" " for i in range(0, 3)] for i in range(0, 3)]

def print_board():
	print "\n\n"	
	print "  1 2 3\n"
	for i in range(0,3):
		print i + 1,
		print "|".join(board[i])
		if i != 2:
			print "  - - -"
	print "\n\n"

def choose_spot():
	while True:
		row = input("Pick a row (1,2,3) > ")
		if row > 3 or row < 1:
			continue
		column = input("Pick a column(1,2,3) > ")
		if column > 3 or column < 1:
			continue
		break
	board[row - 1][column - 1] = "X"

def win(player):
	#horizontal
	for r in range(0, 3):
		for c in range(0, 3):
			if[r][c] != player:
				break
			if c == 2:
				return True

	#vertical
	for r in range(0, 3):
		for c in range(0, 3):
			if[c][r] != player:
				break
			if r == 2:
				return True

	#diagonal


current_player = "X"
while not win(current_player):
	print_board()
	choose_spot()