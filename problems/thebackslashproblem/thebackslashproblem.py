import sys

escapeTable = {
	'!':  r'\!',
	'"':  r'\"',
	'#':  r'\#',
	'$':  r'\$',
	'%':  r'\%',
	'&':  r'\&',
	'\'': r"\'",
	'(':  r'\(',
	')':  r'\)',
	'*':  r'\*',
	'\\': r'\\',
	'[':  r'\[',
	']':  r'\]'
}

try:
	while not sys.stdin.isatty():
		n = int(input())
		line = input().strip('\n')
		for i in range(n):
			line = line.translate(str.maketrans(escapeTable))
		print(line)
except EOFError:
	pass
