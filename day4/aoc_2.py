

#utils
def getRow(board, row):
	return board[row]

def getColumn(board, col):
	column = []
	for line in board:
		column.append(line[col])
	return column

def splitLineInBoard(boards):
	tmp = []
	for line in boards:
		line = line.split(' ')
		while '' in line:
			line.remove('')
		tmp.append(line)
	return tmp

def isLineComplete(line, nums):
	for num in line:
		if int(num) not in nums:
			return False
	return True

def isBoardWon(board, nums):
	for i in range(5):
		if (isLineComplete(getRow(board, i), nums)):
			return True
		if (isLineComplete(getColumn(board, i), nums)):
			return True
	return False
def printBoard(board):
	for i in range(5):
		for j in range(5):
			print(board[i][j], end=' ')
		print('\n', end='')
	print('\n', end='')
#parsing
file_name = "input2"
file = open(file_name)
numbers = list(map(int, file.readline().split(',')))
file.readline()
splitBoards = file.read().split('\n')
while "" in splitBoards:
	splitBoards.remove("")
splitBoards = splitLineInBoard(splitBoards)
boards = []
for i in range(0, len(splitBoards), 5):
	boards.append([splitBoards[i], splitBoards[i + 1], splitBoards[i + 2], splitBoards[i + 3], splitBoards[i + 4]])
#sim
j = 0
i = 0
boardsWon = []
for i in range(len(numbers)):
	j = 0
	finish = False
	for board in boards:
		# printBoard(board)
		if (isBoardWon(board, numbers[:i+1]) and j not in boardsWon):
			print("board won : " + str(j))
			printBoard(board)
			boardsWon.append(j)
		if (len(boardsWon) == len(boards)):
			break
		j += 1
	if (len(boardsWon) == len(boards)):
		break
sum = 0
for row in boards[j]:
	for num in row:
		if int(num) not in numbers[:i+1]:
			sum += int(num)
sum = sum * numbers[i]
print("result : " + str(sum))