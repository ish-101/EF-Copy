# EF-Copy

Writes EF Core entity column definitions for a given list of column names.

## Usage

```$ python entity.py in_file out_file```

The ```in_file``` should be located in ```./input/``` and the ```out_file``` should be located in ```./output/```.

### Example

```$ python entity.py example.txt example.txt```

## Customization

Add keywords to keywords.py.

Change ```DTYPE``` (data type) in entity.py.

Change ```CASE``` (upper/lower/title) in entity.py.
