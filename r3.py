lines = []
with open('yid.txt', 'r', encoding='utf_8_sig') as f:
	for line in f:
		lines.append(line.strip())
for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
print(lines)	
