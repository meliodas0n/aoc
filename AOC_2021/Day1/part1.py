def depthMeasurement(x):
	count = 0
	for i in range(len(x) - 1):
		if int(x[i + 1]) > int(x[i]):
			count += 1

	return count

if __name__ == "__main__":
	data = open('inp1.txt', 'r').read().split('\n')
	print(depthMeasurement(data))