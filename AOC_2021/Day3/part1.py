def powerConsumption(x):
	gamma = ''
	epsilon = ''
	for i in range(len(x[0])):
		one = 0
		zero = 0
		for j in range(len(x)):
			if x[j][i] == '1':
				one += 1
			else:
				zero += 1
		if one > zero:
			gamma += '1'
			epsilon += '0'
		else:
			gamma += '0'
			epsilon += '1'
	g = int(gamma, 2)
	e = int(epsilon, 2)
	return g * e


if __name__ == "__main__":
	data = open('inp1.txt').read().split('\n')
	print(powerConsumption(data))