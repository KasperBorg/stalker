#!/usr/bin/env python
import itertools
from textblob import TextBlob
from textblob import Word
import sys
import argparse
from argparse import RawTextHelpFormatter

# Encoding=utf8 
reload(sys)
sys.setdefaultencoding('utf8')

def get_parser():
		example_text = '''example usage:
			./stalker.py -i input.txt -o output.txt
			./stalker.py -i input.txt -o output.txt -p 2 -f 1
			./stalker.py -i input.txt -o output.txt -p 2 -f 1 -m 1 4'''

		description = '''description: Permutates a block og text into a wordlist'''

		parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, epilog=example_text, description=description)
		parser.add_argument('-i', '--input', required=True, help="File containing the data to be converted")
		parser.add_argument('-o', '--output', required=True, help="Filename of finished wordlist")
		parser.add_argument('-p', '--permutations', help="Amount of permutations generated. Default = 2", type=int, required=False, default=2)
		parser.add_argument('-f', '--frequency', help="Minimum word frequency to join wordlist. Default = 1", type=int, required=False, default=1)
		parser.add_argument('-m', '--mode', help="Mode. Default is 1 4\n1 = Lowercase\n2 = Uppercase\n3 = Capitalized\n4 = Alpha Numeric Only (No Special Characters)", type=int, nargs='*', required=False, default=[1, 4])

		# Fulhack to show help message if no arguments is passed.
		if len(sys.argv)==1:
			parser.print_help()
			sys.exit(1)

		return parser

def generate_permutations():
	print "Generating wordlist from " + args.input

	with open(args.input, 'r') as input_file:
		data = input_file.read()
	
	textblob = TextBlob(data)

	word_frequency =  textblob.word_counts

	chosen_words = set()

	alphaNum = False;
	lowercase = False;
	uppercase = False;
	capitalize = False;

	for mode in args.mode:
		if mode == 1:
			lowercase = True
		if mode == 2:
			uppercase = True
		if mode == 3:
			capitalize = True
		if mode == 4:
			alphaNum = True

	for word, pos in textblob.tags:
		if pos == 'NNS' or pos == 'NN' or pos == 'NNP':
			if word_frequency.get(word) >= args.frequency:
				if alphaNum:
					if word.isalnum():
						if lowercase:
							chosen_words.add(word.lower())
						if uppercase:
							chosen_words.add(word.upper())
						if capitalize:
							chosen_words.add(word.capitalize())
				else:
					if lowercase:
						chosen_words.add(word.lower())
					if uppercase:
						chosen_words.add(word.upper())
					if capitalize:
						chosen_words.add(word.capitalize())

	permutations = itertools.permutations(chosen_words, args.permutations)
	
	return map("".join, permutations)

if __name__ == '__main__':
	parser = get_parser()
	args = parser.parse_args()

	print "Stalker v1.0\n"

	permutations = generate_permutations()

	print "Saving data to: " + args.output
	with open(args.output, 'w') as f:
		for permutation in permutations:
			f.write(permutation+"\n")