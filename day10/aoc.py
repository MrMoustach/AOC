def getParen(key):
	parens = "([{<)]}>"
	i = 0
	for c in parens:
		if (c == key):
			return i
		i += 1
	return i



file = "input2"
scores = [3, 57, 1197, 25137]
f = open(file);
score = 0;
while 1:
	line = f.readline()
	if (line == ""):
		break ;
	stack = []
	for key in line:
		keyIndex = getParen(key)
		if (keyIndex < 4):
			stack.append(keyIndex)
		elif keyIndex >= 4 and keyIndex < 8:
			if (len(stack) == 0):
				score += scores[keyIndex%4]
				break
			elif stack[-1] == keyIndex % 4:
				stack.pop()
			else:
				score += scores[keyIndex%4]
				break
print("score : ", str(score))
