file_name = "input2"

file = open(file_name)
line = file.read()
parts = list(map(int, line.split('\n')))
times = -1
last = 0
for i in range(2, len(parts)):
	sum = parts[i-2] + parts[i-1] + parts[i]
	if (sum > last):
		times += 1
	last = sum
print(times)