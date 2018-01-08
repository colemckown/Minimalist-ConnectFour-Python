rows = 6
columns = 7
end = False
player_turn = 1

board = [[0] * columns for i in range(rows + 1)]

def display_board():
	for row in range(rows-1, -1, -1):
		print(board[row])

def switch_player(player):
	if player == 1:
		return 2
	elif player == 2:
		return 1

def check_move(column):
	for row in range(rows):
		if board[row][column] == 0:
			return row
		elif row == 5 and board[row][column] != 0:
			return 6

def update(player, row, column):
	board[row][column] = player
	display_board()
	if check_win(player, row, column):
		return True
	else:
		return False

def end_game(player):
	print("Player {0} wins!".format(player))

def check_win(player, row, column):
	if check_win_vertical(player, column) or check_win_horizontal(player, row) or check_win_diagonal(player):
		return True
	else:
		return False

def check_illegal_move(player):
	if not player in board[6]:
		return False
	else:
		return True

def check_win_vertical(player, column):
	for i in range(3):
		connected = 0
		for j in range(4):
			if board[i + j][column] == player:
				connected += 1
		if connected >= 4:
			return True
			break
	return False

def check_win_horizontal(player, row):
	for i in range(4):
		connected = 0
		for j in range(4):
			if board[row][i + j] == player:
				connected += 1
		if connected >= 4:
			return True
			break
	return False

def check_win_diagonal(player):

	for starting_row in range(6):
		if starting_row >= 0 and starting_row <= 2:
			for i in range(3 - starting_row):
				connected = 0
				for j in range(4):
					if board[starting_row + j][starting_row + j] == player:
						connected += 1
				if connected >= 4:
					return True
					break
			return False
		elif starting_row >= 2 and starting_row <= 5:
			for i in range(starting_row - 3):
				connected = 0
				for j in range(4):
					if board[starting_row - j][starting_row + j] == player:
						connected +=1
				if connected >= 4:
					return True
					break
			return False
	for ending_row in range(6):
		if ending_row >= 0 and ending_row <= 2:
			for i in range(3 - ending_row):
				connected = 0
				for j in range(4):
					if board[ending_row + j][ending_row - j] == player:
						connected += 1
				if connected >= 4:
					return True
					break
			return False
		elif ending_row >= 2 and ending_row <= 5:
			for i in range(ending_row - 3):
				connected = 0
				for j in range(4):
					if board[ending_row - j][ending_row - j] == player:
						connected += 1
				if connected >= 4:
					return True
					break
			return False


while not end:
	move = int(input("Player {0}: ".format(player_turn)))
	end = update(player_turn, check_move(move), move)

	if end:
		end_game(player_turn)
		break
	elif check_illegal_move(player_turn):
		player_turn = switch_player(player_turn)
		end_game(player_turn)
		break
	else:
		player_turn = switch_player(player_turn)

print("GG")
winner = player_turn
print(winner)