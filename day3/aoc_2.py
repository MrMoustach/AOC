
def getMostBitsInCol(numbers, col):
	count_1 = 0
	count_0 = 0
	for number in numbers:
		if (number[col] == '1'):
			count_1 += 1
		if (number[col] == '0'):
			count_0 += 1
	if (count_1 > count_0):
		return 1
	elif (count_0 > count_1):
		return 0
	return -1
def getLeastBitsInCol(numbers, col):
	count_1 = 0
	count_0 = 0
	for number in numbers:
		if (number[col] == '1'):
			count_1 += 1
		if (number[col] == '0'):
			count_0 += 1
	if (count_1 > count_0):
		return 0
	elif (count_0 > count_1):
		return 1
	return -1
def removeWithBits(numbers, col, bit):
	newNumbers = []
	for number in numbers:
		if number[col] != bit :
			newNumbers.append(number)
	return newNumbers
def getRating(numbers, func, fallback):
	for i in range(len(numbers[0])):
		if (len(numbers) == 1): break
		bitIndex = func(numbers, i)
		if bitIndex == 1:
			numbers = removeWithBits(numbers, i, '0')
		elif bitIndex == 0:
			numbers = removeWithBits(numbers, i, '1')
		else:
			numbers = removeWithBits(numbers, i, fallback)
	return int(numbers[0], 2)
file_name = "input2"

file = open(file_name)
lines = file.read().split('\n')
oxyNumbers = getRating(lines, getMostBitsInCol, '0')
co2Numbers = getRating(lines, getLeastBitsInCol, '1')

print("result : " + str(oxyNumbers * co2Numbers))