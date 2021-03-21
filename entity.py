from sys import argv
from keywords import expand_keyword
from dtypes import dtypes
from db import DBCache
import math
from ast import literal_eval

if __name__ == '__main__':
	try:
		table_name = argv[1]
	except:
		print('SyntaxError: invalid syntax')
		print('usage: python entity.py table_name')
		quit()

	db = DBCache()
	attrs = db.get_table_attrs(table_name=table_name)

	print(
f'''\t[Table("{table_name}", Schema = "{db.get_schema_name()}")]
\tpublic class {table_name}
\t{{''')
	for attr in attrs:
		name = expand_keyword(attr.COLUMN_NAME)
		dtype = dtypes[attr.DATA_TYPE]
		try:
		    max_len = int(attr.CHARACTER_MAXIMUM_LENGTH)
		except:
		    max_len = None
		optional_operator = ''
		if ((dtype != 'string') and (attr.IS_NULLABLE == 'YES')):
		    optional_operator = '?'
		default = attr.COLUMN_DEFAULT
		if isinstance(default, str):
			default = literal_eval(default)
		else:
			default = None
		
		print(f'\t\t[Column("{attr.COLUMN_NAME}")]')
		if max_len is not None:
		    print(f'\t\t[StringLength({max_len})]')
		if attr.DATA_TYPE == 'timestamp':
		    print('\t\t[Timestamp]')
		print(f'\t\tpublic {dtype}{optional_operator} {name} {{ get; set; }}')
	print('\t}')