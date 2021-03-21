CASE = lambda word: word.title()

keywords = {
    # Values in ALL CAPS  are copied exactly
    'id': 'ID',
    # Rest get converted to Titlecase
    'val': 'value',
    'num': 'number',
    'rgn': 'region',
    'yr': 'year',
    'dt': 'date',
    'cd': 'code',
    'pct': 'percent',
    'prop': 'property',
    'prev': 'previous',
}


def expand_keyword(key):
	value = ''
	words = key.split('_')
	for word in words:
		if word in keywords:
			word = keywords[word]
		if not word.isupper():
			word = CASE(word)
		value += word
	return value