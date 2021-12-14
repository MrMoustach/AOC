#parsing
file_name = "input2"
file = open(file_name)

lines = [x.split(" | ")[1] for x in file.read().split("\n")]

segs = []
# 1 7 4 8
# 2 3 4 7
for line in lines:
	segs += [len(x) for x in line.split(" ")]
while 1 in segs or 5 in segs or 6 in segs:
	if 1 in segs:
		segs.remove(1)
	if 5 in segs:
		segs.remove(5)
	if 6 in segs:
		segs.remove(6)
print(len(segs))