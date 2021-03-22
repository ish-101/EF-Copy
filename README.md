# EF-Copy

Copies EF Core Entity and DbContext  definitions from an existing SQL table.

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

1) Load Definition:
```$ python db.py table_name```

2) Generate Entity:
```$ python entity.py table_name```

3) Generate DbContext:
```$ python context.py table_name```