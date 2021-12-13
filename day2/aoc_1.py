file_name = "input2"

file = open(file_name)
lines = file.read().split('\n')
horizontal = 0
depth = 0
for line in lines:
	command = line.split(' ')
	if (command[0] == "forward"):
		horizontal += int(command[1])
	elif (command[0] == "down"):
		depth += int(command[1])
	elif (command[0] == "up"):
		depth -= int(command[1])
print(str(horizontal) + " | " + str(depth) + " | final : " +str(horizontal * depth))