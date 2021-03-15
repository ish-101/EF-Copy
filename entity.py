import sys
from keywords import keywords

DTYPE = 'decimal'
CASE = lambda word : word.title()

try:
	f_in_name = f'./input/{sys.argv[1]}'
	f_out_name = f'./output/{sys.argv[2]}'
except:
	print('SyntaxError: invalid syntax')
	print('usage: python entity.py in_file out_file')
	print('example: python entity.py example.txt example.txt')
	quit()
try:
	f_in = open(f_in_name, 'r')
except:
	print(f'ReadError: Cannot open ./input/{f_in_name}')
	quit()
attrs = []
attr = 'attr'
while True:
	attr = f_in.readline().strip()
	if len(attr) > 0:
		attrs.append(attr)
	else:
		break
f_in.close()
try:
	f_out = open(f_out_name, 'w')
except:
	print(f'WriteError: Cannot open ./output/{f_out_name}')
	quit()
for attr in attrs:
	words = attr.split('_')
	camel = ''
	for word in words:
		if word in keywords:
			word = keywords[word]
		if not word.isupper():
			word = CASE(word)
		camel += word
	f_out.writelines([
		f'[Column("{attr}")]\n',
		f'public {DTYPE} {camel} {{ get; set; }}\n'])
f_out.close()