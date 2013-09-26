#HUMAN IS X
#COMPUTER IS O
#COMPUTER WANTS 1
#HUMAN WANTS -1

board = [[" " for i in range(0, 3)] for i in range(0, 3)]

COMPUTER = True
HUMAN = False



class Move:
	def __init__(self):
		self.row = -1
		self.column = -1


class Best:
	def __init__(self, move, computer):
		self.move = move
		if computer:
			self.score = -2
		else:
			self.score = 2


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
			if board[r][c] != player:
				break
			if c == 2:
				return True

	#vertical
	for r in range(0, 3):
		for c in range(0, 3):
			if board[c][r] != player:
				break
			if c == 2:
				return True

	#diagonal
	for r in range(0, 3):
		if board[r][r] != player:
			break
		if r == 2:
			return True

	#reverse diagonal
	for r in range(0, 3):
		if board[2 - r][r] != player:
			break
		if r == 2:
			return True

def possible_moves():
	empty = []
	for r in range(0, 3):
		for c in range(0, 3):
			if board[r][c] == " ":
				m = Move()
				m.row = r
				m.column = c
				empty.append(m)
	return empty



def computer_move():
	best = choose_move(True)
	move = best.move
	#print move.row
	#print move.column
	board[move.row][move.column] = "O"

#if side is true, computers turn
#if side is false, humans turn
def choose_move(side):
	my_best = Best(Move(), side)
	moves = possible_moves()
	if not moves:
		my_best.score = calculate_board_score(side)
	else:
		for move in moves:
			if side is COMPUTER:
				board[move.row][move.column] = "O"
			else:
				board[move.row][move.column] = "X"
			response = choose_move(not side)
			board[move.row][move.column] = " "
			if side is COMPUTER and response.score >= my_best.score or side is HUMAN and response.score <= my_best.score:
				my_best.move = move
				my_best.score = response.score
	return my_best

def calculate_board_score(side):
	if not win("X") and not win("O"):
		return 0
	if side is COMPUTER:
		if win("O"):
			return 1
		else:
			return -1
	if side is HUMAN:
		if win("X"):
			return -1
		else:
			return 1


current_player = "X"
while True:
	print_board()
	choose_spot() if current_player == "X" else computer_move()
	if win(current_player):
		break
	if current_player == "X":
		current_player = "O"
	else:
		current_player = "X"

print_board()
print current_player + " has won."