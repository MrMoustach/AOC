file_name = "input1"

file = open(file_name)
line = file.readline()
last = int(line)
times = 0
while 1:
	line = file.readline()
	if (line == ""):
		break
	if int(line) > last:
		times += 1
	last = int(line)
print("times : " + str(times))