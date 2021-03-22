from sys import argv
from keywords import expand_keyword
from dtypes import dtypes
from db import DBCache
import math
from ast import literal_eval


def entity(table_name, dto=False):
	db = DBCache()
	attrs = db.get_table_attrs(table_name=table_name)

	table_class_name = expand_keyword(table_name)
	dto_postfix = ''
	class_public = ''
	if dto:
		dto_postfix = 'Dto'
		class_public = 'public '
	ofile = open(f'./output/{table_class_name}{dto_postfix}.cs', 'w')
	if not dto:
		ofile.write(f'\t[Table("{table_name}", Schema = "{db.get_schema_name()}")]')
	ofile.write(f'\tpublic class {table_class_name}{dto_postfix}\n\t{{\n')
	for (i, attr) in enumerate(attrs):
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
		if dto and (attr.DATA_TYPE == 'timestamp'):
			continue
		if not dto:
			ofile.write(f'\t\t[Column("{attr.COLUMN_NAME}")]\n')
		if max_len is not None:
			ofile.write(f'\t\t[StringLength({max_len})]\n')
		if attr.DATA_TYPE == 'timestamp':
			ofile.write('\t\t[Timestamp]\n')
		ofile.write(
			f'\t\tpublic {dtype}{optional_operator} {name} {{ get; set; }}\n')
		if i < len(attrs)-1:
			ofile.write('\n')
	ofile.write('\t}\n')


if __name__ == '__main__':
	try:
		table_name = argv[1]
	except:
		print('SyntaxError: invalid syntax')
		print('usage: python entity.py table_name')
		quit()
	entity(table_name)