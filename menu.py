from sys import argv
from functions import *
from replacements import replacements
from os import listdir
from os.path import isfile, join

command = str(argv[1])
directory = str(argv[2]) # currently '/Users/jmason/writing/deus' for publish
stylesheet = str(argv[3]) 
def get_files():
	"""gets all of the files in a directory"""
	files = [f for f in listdir(directory) if isfile(join(directory, f))]
	return files

if command == 'publish':
	files = get_files()
	for file in files:
		process_file(file, replacements, '/Users/jmason/writing/deus/', '/Users/jmason/writing/published/', stylesheet)

