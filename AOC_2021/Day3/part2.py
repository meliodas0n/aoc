def lifeSupport(x):
	x2 = x.copy()
	index1 = 0
	while len(x) > 1:
		one = 0
		zero = 0
		ones = []
		zeroes = []
		for i in range(len(x)):
			if x[i][index1] == '0':
				zero += 1
				zeroes.append(x[i])
			else:
				one += 1
				ones.append(x[i])
		if zero > one:
			x = zeroes
		else:
			x = ones
		index1 += 1
	o2 = int(x[0], 2)

	index2 = 0
	while len(x2) > 1:
		one = 0
		zero = 0
		ones = []
		zeroes = []
		for i in range(len(x2)):
			if x2[i][index2] == '0':
				zero += 1
				zeroes.append(x2[i])
			else:
				one += 1
				ones.append(x2[i])
		if one < zero:
			x2 = ones
		else:
			x2 = zeroes
		index2 += 1
	co2 = int(x2[0], 2)
	return o2 * co2

if __name__ == "__main__":
	data = open('inp2.txt').read().split('\n')
	print(lifeSupport(data))