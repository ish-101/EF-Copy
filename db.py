from os import getenv
from dotenv import load_dotenv
import pyodbc
from collections import namedtuple
from datetime import date
import numpy as np
import pandas as pd
import math
from sys import argv


class DB:
	_TABLE_ATTRS = [
	    'ORDINAL_POSITION', 'COLUMN_NAME', 'DATA_TYPE',
	    'CHARACTER_MAXIMUM_LENGTH', 'IS_NULLABLE', 'COLUMN_DEFAULT'
	]
	_CATALOG = None
	_SCHEMA = None

	def __init__(self):
		load_dotenv()
		self._CATALOG = getenv('DB_TABLE_CATALOG')
		self._SCHEMA = getenv('DB_TABLE_SCHEMA')

	def get_schema_name(self):
		return self._SCHEMA


class DBExt(DB):
	__cnxn = None

	def __init__(self):
		DB.__init__(self)
		DB_SERVER = getenv('DB_SERVER')
		DB_UID = getenv('DB_UID')
		DB_PWD = getenv('DB_PWD')

		self.__cnxn = pyodbc.connect(f'''
			DRIVER={{ODBC Driver 17 for SQL Server}};
			SERVER={DB_SERVER};
			DATABASE={self._CATALOG};
			UID={DB_UID};
			PWD={DB_PWD};
		''')

	def __del__(self):
		if (self.__cnxn != None):
			self.__cnxn.close()

	def load_table_attrs(self, table_name):
		ATTRS_STR = ', '.join(self._TABLE_ATTRS)

		query = f'''
			SELECT {ATTRS_STR}
			FROM INFORMATION_SCHEMA.COLUMNS
			WHERE (
				TABLE_CATALOG=? AND
				TABLE_SCHEMA=? AND 
				TABLE_NAME=?
			)
			ORDER BY ORDINAL_POSITION;
		'''
		cursor = self.__cnxn.cursor()
		cursor.execute(query, self._CATALOG, self._SCHEMA, table_name)

		attrs = []
		while True:
			data_row = cursor.fetchone()
			if not data_row:
				break
			attrs.append(data_row)
		if len(attrs) > 0:
			attrs_save = pd.DataFrame(np.array(attrs),
			                          columns=self._TABLE_ATTRS)
			attrs_save.to_csv(f'./dbcache/{table_name}.csv', index=False)


class DBCache(DB):
	def get_table_attrs(self, table_name):
		Attribute = namedtuple('Attribute', self._TABLE_ATTRS)
		df = pd.read_csv(f'./dbcache/{table_name}.csv', index_col=0)
		data = df.values.tolist()
		attrs = [Attribute(i, *x) for (i, x) in enumerate(data)]
		return attrs


if __name__ == '__main__':
	try:
		table_name = argv[1]
	except:
		print('SyntaxError: invalid syntax')
		print('usage: python db.py table_name')
		quit()

	db = DBExt()
	db.load_table_attrs(table_name=table_name)