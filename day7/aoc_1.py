import statistics
#parsing
file_name = "input2"
file = open(file_name)

poses = [int(x) for x in file.read().split(',')]
median = int(statistics.median(poses))
effiecent = 0
for pos in poses:
	effiecent += abs(median - pos)

print("Result :",effiecent)

