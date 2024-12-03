countRights = {}
leftNums = []
rightNums = []
p1total = 0
p2total = 0

with open('input1.txt', 'r') as file:
	for line in file:
		newL = line[:-1].split(' ')
		leftNums.append(int(newL[0]))
		rightNums.append(int(newL[-1]))

		
leftNums.sort()
rightNums.sort()

for i, val in enumerate(rightNums):
	p1total += abs(val - leftNums[i])
	if val in countRights:
		countRights[val]+=1
	else:
		countRights[val]=1


for i in set(leftNums):
	if i in countRights:
		p2total += i*countRights[i]

print("Part 1: ", p1total, "\nPart 2: ", p2total)

	

