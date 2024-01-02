from random import randrange  #It will generate the random number for the computer moves.

def display_board(board):   #defining the function  
    #the structure will be grid like structure
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")


def enter_move(board):   #for the input player input moves from 1- 9
    #by the knowing the validation of the number and of the board position
	ok = False	# fake assumption - we need it to enter the loop
	while not ok:
		move = input("Enter your move: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9' # is user's input valid?
		if not ok:
			print("Bad move - repeat your input!") # no, it isn't - do the input again
			continue
		move = int(move) - 1 	# cell's number from 0 to 8
		row = move // 3 	# cell's row
		col = move % 3		# cell's column
		sign = board[row][col]	# check the selected square
		ok = sign not in ['O','X'] 
		if not ok:	# it's occupied - to the input again
			print("Field already occupied - repeat your input!")
			continue
	board[row][col] = 'O' 	# set '0' at the selected square

#Row*Column=3*3
def make_list_of_free_fields(board):  #It will check the every free field of the column and the row
    #then it will contain it into the list
	free = []	  #value will be store int this empty array
	for row in range(3): # iterate through rows 3*3
		for col in range(3): # iterate through columns 3*3
			if board[row][col] not in ['O','X']: # is the cell free or not?
				free.append((row,col)) # yes, it is - append new tuple to the list
    #if free then it will append the moves of the player
	return free  


def victory_for(board,sgn):  #defining victory function
    #it examines all row and column and diagonal, and see the winnig line
	if sgn == "X":	# are we looking for X?
		who = 'Computer'	# yes - it's computer's side
	elif sgn == "O": # ... or for O?
		who = 'you'	# yes - it's our side
	else:
		who = None	# we should not fall here!
	cross1 = cross2 = True  # for diagonals
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
			return who
		if board[rc][rc] != sgn: # check 1st diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != sgn: # check 2nd diagonal
			cross2 = False
	if cross1 or cross2:
		return who
	return None


def draw_move(board):  #defining draw move funciton
    #It will again check the moves and the free list position on the board
	free = make_list_of_free_fields(board) # make a list of free fields
	cnt = len(free)
	if cnt > 0:	
		this = randrange(cnt) #again with the help of the random funciton for the position
		row, col = free[this]
		board[row][col] = 'X'  #computer

#Main Board Intialization
board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]  #Creating 3*3 board
board[1][1] = 'X' # first 'X' in the middle   #center of the 2D board
free = make_list_of_free_fields(board)
human_turn = True # which turn is it now?

#game loop
#by using the while loop it will continue the game board filled
while len(free):  #from the above defined function we will work on moves of the player
	display_board(board)
	if human_turn:
		enter_move(board)
		victor = victory_for(board,'O')  #checking that player won or not?
	else:	
		draw_move(board)
		victor = victory_for(board,'X')  #checking that Computer won or not?
	if victor != None:
		break
	human_turn = not human_turn		
	free = make_list_of_free_fields(board)
 
#result
display_board(board)
if victor == 'you':
	print("You won!") #player won
elif victor == 'Computer Won':
	print("Computer Won")  #computer won
else:
	print("Tie!") 
