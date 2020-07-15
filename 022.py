alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def score_name(name, index):
	score = 0
	for c in list(name):
		score += (alphabet.index(c) + 1)
	return score * (index + 1)

file = open("p022_names.txt")

names = file.read().replace("\"", "").split(',')
names.sort()

file.close()

sum = 0

for i in range(len(names)):
	sum += score_name(names[i], i)
	
print(sum)
