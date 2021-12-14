def calcUnder(x):
	sum = x
	for i in range(x):
		sum += i
	return sum

#parsing
file_name = "input2"
file = open(file_name)

poses = [int(x) for x in file.read().split(',')]
average = int(sum(poses)/len(poses))

effiecent = 0
for pos in poses:
	effiecent += calcUnder(abs(average - pos))

print("Result :",effiecent)


