def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf_8_sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines 

def convert(lines):
	t = []
	p = None
	for line in lines:
		if line == 'Allen':
			p = 'Allen'
			continue
		elif line == 'Tom':
			p = 'Tom'
			continue
		if p:
			t.append(p + ':' + line)
	return t				

def write_file(filename, lines):
	with open(filename, 'w', encoding='utf_8_sig') as f:
		for line in lines:
			f.write(line + '\n')




def main():    
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines) 
main()    
