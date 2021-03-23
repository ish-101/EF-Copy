from keywords import abbr_keyword
from sys import argv
from db import DBCache
from keywords import expand_keyword, abbr_keyword
from dtypes import context_dtypes
import math

if __name__ == '__main__':
	try:
		table_name = argv[1]
	except:
		print('SyntaxError: invalid syntax')
		print('usage: python entity.py table_name')
		quit()

	db = DBCache()
	attrs = db.get_table_attrs(table_name=table_name)

	table_class_name = expand_keyword(table_name)
	ofile = open(f'./output/DbContext.{table_class_name}.cs', 'w')
	abbr = abbr_keyword(table_name)

	keys = list(filter(lambda attr: not math.isnan(attr.PK_POSITION), attrs))
	keys = sorted(keys, key=lambda key: key.PK_POSITION)
	key_names = [ expand_keyword(key.COLUMN_NAME) for key in keys ]
	has_key = f', {abbr}.'.join(key_names)
	has_key = f'{abbr}.{has_key}'

	ofile.write(
	    f'\t\t\tbuilder.Entity<{table_class_name}>({abbr} =>\n')
	ofile.write('\t\t\t{\n')

	ofile.write(f'\t\t\t\t{abbr}.HasKey({abbr} => new {{ {has_key} }});\n')

	for (i, key) in enumerate(keys):
		ofile.write(f'\t\t\t\t{abbr}.Property({abbr} => {abbr}.{key_names[i]}).ValueGeneratedNever();\n')

	for (i, attr) in enumerate(attrs):
		name = expand_keyword(attr.COLUMN_NAME)
		dtype = attr.DATA_TYPE
		max_len = attr.CHARACTER_MAXIMUM_LENGTH
		is_required = ''
		if attr.IS_NULLABLE == 'YES':
			is_required = '.IsRequired(false)'
		has_column_type = ''
		if dtype in context_dtypes:
			if dtype == 'char':
				dtype = f'{dtype}({int(max_len)})'
			has_column_type = f'.HasColumnType("{dtype}")'
		ofile.write(f'\t\t\t\t{abbr}.Property({abbr} => {abbr}.{name}){is_required}{has_column_type};\n')
	
	ofile.write('\t\t\t});\n')