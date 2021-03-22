from sys import argv
from entity import entity

if __name__ == '__main__':
	try:
		table_name = argv[1]
	except:
		print('SyntaxError: invalid syntax')
		print('usage: python dto.py table_name')
		quit()
	entity(table_name, dto=True)