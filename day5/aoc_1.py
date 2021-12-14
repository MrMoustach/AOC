#parsing
file_name = "input2"
file = open(file_name)

lines = []
for line in file.read().split('\n'):
	arr = line.split(' ')
	lines.append([list(map(int,arr[0].split(','))), list(map(int,arr[2].split(',')))])

n = 0
for line in lines:
	if (n < line[0][0]):
		n = line[0][0]
	if (n < line[1][0]):
		n = line[1][0]
	if (n < line[0][1]):
		n = line[0][1]
	if (n < line[1][1]):
		n = line[1][1]

planes = []
for i in range(n+1):
	planes.append([0]*(n+1))
for line in lines:
	p1,p2 = line
	if p1[0] == p2[0] or p1[1] == p2[1]:
		# print(line)
		for x in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
			for y in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
				planes[y][x] += 1

sum = 0
i = 0
for line in planes:
	for num in line:
		# print(num, end=' ')
		if num > 1:
			sum += 1
	# print("|",i)
	i += 1
print("result :",sum)