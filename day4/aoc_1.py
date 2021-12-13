


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



file_name = "input1"
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
print(getColumn(boards[0], 0))