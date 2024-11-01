def calculateDirection(x):
	h = 0
	d = 0
	for i in range(len(x)):
		if x[i] == 'forward':
			h += int(x[i + 1])
		elif x[i] == 'down':
			d += int(x[i + 1])
		elif x[i] == 'up':
			d -= int(x[i + 1])
	return h * d

if __name__ == "__main__":
	newData = []
	data = open('inp1.txt').read().split('\n')
	for i in data:
		i = i.split()
		newData.append(i[0])
		newData.append(i[1])
	print(calculateDirection(newData))