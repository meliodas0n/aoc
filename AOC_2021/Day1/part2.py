def depthMeasurement(x):
	count = 0
	for i in range(len(x) - 2):
		if sum(x[i : i + 3]) < sum(x[i + 1 : i + 4]):
			count += 1
	return count

if __name__ == "__main__":
	data = open('inp2.txt', 'r').read().split('\n')
	newData = [int(i) for i in data]
	print(depthMeasurement(newData))