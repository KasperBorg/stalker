# stalker
Python script that extracts all nouns from a block of text, then permutates them into a wordlist

```
usage: stalker.py [-h] -i INPUT -o OUTPUT [-p PERMUTATIONS] [-f FREQUENCY]
                  [-m [MODE [MODE ...]]]

description: Permutates a block og text into a wordlist

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        File containing the data to be converted
  -o OUTPUT, --output OUTPUT
                        Filename of finished wordlist
  -p PERMUTATIONS, --permutations PERMUTATIONS
                        Amount of permutations generated. Default = 2
  -f FREQUENCY, --frequency FREQUENCY
                        Minimum word frequency to join wordlist. Default = 1
  -m [MODE [MODE ...]], --mode [MODE [MODE ...]]
                        Mode. Default is 1 4
                        1 = Lowercase
                        2 = Uppercase
                        3 = Capitalized
                        4 = Alpha Numeric Only (No Special Characters)

example usage:
			./stalker.py -i input.txt -o output.txt
			./stalker.py -i input.txt -o output.txt -p 2 -f 1
			./stalker.py -i input.txt -o output.txt -p 2 -f 1 -m 1 4
```
