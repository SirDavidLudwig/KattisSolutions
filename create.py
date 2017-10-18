#!/usr/bin/python3
import os
import io
import sys
import zipfile
import requests

LANG_MAP = {
	"cpp": '#include <iostream>\n\nusing namespace std;\n\nint main()\n{\n\t\n\treturn 0;\n}\n',
	"python": 'import sys\n\n\ndef main():\n\t\n\treturn 0\n\n\nif __name__ == "__main__":\n\tsys.exit(main())'
}

LANG_EXT = {
	"cpp": ".cpp",
	"python": ".py"
}

URL = "https://open.kattis.com/problems/"

def main(argv):

	if len(argv) != 3:
		print("Usage: problem.py <problem name> <lang(cpp, python)>")
		return 1

	problem = argv[1].lower()
	lang    = argv[2].lower()

	try:
		r = requests.get(URL + problem + "/file/statement/samples.zip", stream=True)
		z = zipfile.ZipFile(io.BytesIO(r.content))
	except:
		print("Unable to find problem \"" + problem + '"')
		return 1

	if not os.path.exists(problem):
		os.mkdir(problem)

	if not os.path.exists(problem + "/samples"):
		os.mkdir(problem + "/samples")

	if lang not in LANG_MAP:
		print("'" + lang + "' is not a valid language. Available languages: "
	          + ", ".join(list(LANG_MAP.keys())))
		return 1

	z.extractall(problem + "/samples/")

	f = open(problem + "/" + problem + LANG_EXT[lang], "w")
	f.write(LANG_MAP[lang])
	f.close()


if __name__ == '__main__':
	sys.exit(main(sys.argv))
