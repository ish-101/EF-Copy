# EF-Copy

Writes EF Core entity column definitions for a given list of column names.

## Configuration

In the project root folder, create a ```.env``` file with the following fields:
```
DB_SERVER=
DB_UID=
DB_PWD=
DB_TABLE_CATALOG=
DB_TABLE_SCHEMA=
```

(Optional) Add ```keywords``` or  change ```CASE``` (upper/lower/title) in keywords.py.

## Usage

1) Load definitions:
```$ python db.py table_name```

2) Generate entities:
```$ python entity.py table_name```