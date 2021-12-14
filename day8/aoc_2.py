# utils
def howManyIn(needle, haystack):
	count = 0
	for x in needle:
		if (x in haystack): count += 1
	return count
#parsing
file_name = "input2"
file = open(file_name)
# unique
# 1 7 4 8
# 2 3 4 7
# non unique
# 0 2 3 5 6 9
# 6 5 5 5 6 6
# x x 1 9   4

lines = file.read().split("\n")
allPatterns = [x.split(" | ")[0] for x in lines]
allOutputs = [x.split(" | ")[1] for x in lines]
sum = 0
for i in range(len(allPatterns)):
	patterns = allPatterns[i].split(' ')
	outputs = allOutputs[i].split(' ')
	numbers = [0]*10
	# while 0 in numbers:
	for i in range(4):
		for pattern in patterns:
			if (len(pattern) == 2): 
				numbers[1] = pattern
			if (len(pattern) == 4): 
				numbers[4] = pattern
			if (len(pattern) == 3): 
				numbers[7] = pattern
			if (len(pattern) == 7): 
				numbers[8] = pattern
			if (len(pattern) == 5 and numbers[1] != 0 and howManyIn(numbers[1], pattern) == 2): 
				numbers[3] = pattern
			if (len(pattern) == 6 and numbers[4] != 0 and howManyIn(numbers[4], pattern) == 4): 
				numbers[9] = pattern
			if (len(pattern) == 5 and numbers[9] != 0 and numbers[3] != 0 and numbers[3] != pattern and howManyIn(numbers[9], pattern) == 5):
				numbers[5] = pattern
			if (len(pattern) == 5 and numbers[5] != 0 and numbers[3] != 0 and pattern != numbers[5] and pattern != numbers[3]):
				numbers[2] = pattern
			if (len(pattern) == 6 and numbers[9] != 0 and numbers[1] != 0 and howManyIn(numbers[1], pattern) == 2 and pattern != numbers[9]):
				numbers[0] = pattern
	for pattern in patterns:
		if (pattern not in numbers):
			numbers[6] = pattern
	coef = 1000
	num = 0
	for output in outputs:
		index = 0
		for i in range(len(numbers)):
			if sorted(numbers[i]) == sorted(output):
				index = i
				break
		num += index * int(coef)
		coef /= 10
	print(num)
	sum += num
print("Result :",sum)