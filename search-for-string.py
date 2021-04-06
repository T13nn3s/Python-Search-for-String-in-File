import os
import argparse
from time import sleep
from tqdm import tqdm

parser = argparse.ArgumentParser()

parser.add_argument(
	'-f', '--filepath', help='Specify filepath with databreach files which needs to be searched.', required=True
)
parser.add_argument(
	'-s', '--search', help='Specify search string.', required=True
)

args = parser.parse_args()

if args.filepath is None:
	parser.error(
		'Please specify the filepath (-f) with databreach files to be searched.'
	)

if args.search is None:
	parser.error(
		'Plese specify your search query (-s).'
	)

# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

def files(file_path, search_query):
	for files in os.listdir(args.filepath):
		if files.endswith('.txt'):
			with open(args.filepath+files, 'r', encoding='utf8') as openfile:
				num_lines = sum(1 for line in open(args.filepath+files, 'r'))
				for line in openfile:
					for line in tqdm(openfile, total=num_lines):
						if search_query in line:
							print(openfile)
							print(line)

files(args.filepath, args.search)
