#parsing
file_name = "input2"
file = open(file_name)
#parsing
fishs = list(map(int,file.read().split(',')))
# #logic
# x = lambda a: a + 2
# # fishs = fishs + list(map(x, fishs))
# # print(fishs + list(map(x, fishs)))
# for i in range(80):
# 	newFishs = []
# 	for i in range(len(fishs)):
# 		if fishs[i] > 0:
# 			fishs[i] -= 1
# 		else:
# 			fishs[i] = 6
# 			newFishs.append(8)
# 	fishs = fishs + newFishs
# print("result :",len(fishs))
test = [fishs.count(i) for i in range(9)]
for i in range(256):
	test[(i + 7) % 9] += test[i % 9]
	# print(test)
print(sum(test))