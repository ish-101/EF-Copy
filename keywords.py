CASE = lambda word: word.title()

keywords = {
    # Upper case / Case Blacklisted
    'id': 'ID',
    'dl': 'DL',
    'ss': 'SS',
    'oa65': 'OA65',
    'hs': 'HS',
    'tsRowVersion': 'RowVersion',
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
    'exmpt': 'exempt',
    'nm': 'name',
    'sup': 'supplement',
    'sp': 'special',
    'amt': 'amount',
    'desc': 'description',
    'tm': 'time',
    'cmnt': 'comment',
    'auth': 'authority',
    'appl': 'application',
    'eff': 'effective',
    'exp': 'expiration',
    'assoc': 'association',
    'ent': 'entity',
    'chg': 'change',
    'sys': 'system',
}

case_blacklist = [
    'RowVersion'
]

def abbr_keyword(key):
    value = ''
    words = key.split('_')
    for word in words:
        value += word[0]
    return value

def expand_keyword(key):
	value = ''
	words = key.split('_')
	for word in words:
		if word in keywords:
			word = keywords[word]
		if not ((word.isupper()) or (word in case_blacklist)):
			word = CASE(word)
		value += word
	return value