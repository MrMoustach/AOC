#parsing
file_name = "input1"
file = open(file_name)
#parsing
fishs = list(map(int,file.read().split(',')))
#logic
x = lambda a: a + 2
# fishs = fishs + list(map(x, fishs))
# print(fishs + list(map(x, fishs)))
for i in range(82):
	newFishs = []
	for i in range(len(fishs)):
		if fishs[i] > 0:
			fishs[i] -= 1
		else:
			fishs[i] = 6
			newFishs.append(8)
	fishs = fishs + newFishs
print("result :",len(fishs))