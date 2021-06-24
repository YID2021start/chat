def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf_8_sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines 


def convert(lines):
	p = None
	j_image_count = 0
	y_image_count = 0
	y_sticker_count = 0
	j_sticker_count = 0
	y_word_count = 0
	j_word_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == '易政樟':
			if '貼圖' == s[2]:
				y_sticker_count + 1
			elif '圖片' == s[2]:
				y_image_count +1	
			else:
				for m in s[2:]:
					y_word_count += len(m)				
		elif name == 'Justin':
			if '貼圖' == s[2]:
				y_sticker_count + 1
			elif '圖片' == s[2]:
				y_image_count +1	
			else:
				for m in s[2:]:
					j_word_count += len(m)

	print('Justin說了', j_word_count, '個字,傳了', j_sticker_count, '個貼圖,',j_image_count, '圖片')
	print('易政樟說了', y_word_count, '個字,傳了', y_sticker_count, '個貼圖,', y_image_count, '圖片')	


def write_file(filename, lines):
	with open(filename, 'w', encoding='utf_8_sig') as f:
		for line in lines:
			f.write(line + '\n')




def main():    
    lines = read_file('yid.txt')
    lines = convert(lines)
    #write_file('output.txt', lines) 
main()    
