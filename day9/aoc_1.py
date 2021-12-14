#parsing
file_name = "input2"
file = open(file_name)
lines = file.read().split("\n")
map = []
width = 0
for line in lines:
	width = len(line)
	map.append([int(x) for x in line])
height = len(map)
sum = 0
print(width, height)
for y in range(height):
	for x in range(width):
		lowest = True
		if (x > 0):
			if (map[y][x-1] <= map[y][x]):
				lowest = False
		if (x < width - 1):
			if (map[y][x+1] <= map[y][x]):
				lowest = False
		if (y > 0):
			if (map[y-1][x] <= map[y][x]):
				lowest = False
		if (y < height - 1):
			if (map[y+1][x] <= map[y][x]):
				lowest = False
		if lowest:
			print(f"\u001b[31m{map[y][x]}\u001b[0m", end=' ')
			sum += map[y][x] + 1
		else:
			print(map[y][x], end=' ')
	print()
print("Result :", sum)

