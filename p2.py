def checkdec(report):
	l = len(report)
	if l in (0,1):
		return 1
	for i in range(1,l):
		if int(report[i]) not in {int(report[i-1])-1, int(report[i-1])-2, int(report[i-1])-3}:
			return 0
	return 1

def checkinc(report):
	l = len(report)
	if l in (0,1):
		return 1
	for i in range(1,l):
		if int(report[i]) not in {int(report[i-1])+1, int(report[i-1])+2, int(report[i-1])+3}:
			return 0
	return 1

reports = {}
p1total = 0
p2total = 0
r = 0
with open('input2.txt', 'r') as file:
	for line in file:
		newL = line[:-1].split(' ')
		p1run = max(checkdec(newL), checkinc(newL))
		p2run = p1run
		for i in range(len(newL)):
			if p2run == 0:
				upL = [item for item in newL]
				del upL[i]
				p2run = max(checkdec(upL), checkinc(upL))
		p1total += p1run
		p2total += p2run


print("Part 1: ", p1total, "\nPart 2: ", p2total)

	

