file_name = "input2"

file = open(file_name)
lines = file.read().split('\n')
gama_bits = ""
epsilon_bits = ""
for i in range(12):
	count_1 = 0
	count_0 = 0
	for line in lines:
		if (line[i] == '1'):
			count_1 += 1
		if (line[i] == '0'):
			count_0 += 1
	if (count_1 > count_0):
		gama_bits += "1"
		epsilon_bits += "0"
	else:
		gama_bits += "0"
		epsilon_bits += "1"
print("result : " + str(int(gama_bits, 2)*int(epsilon_bits, 2)));