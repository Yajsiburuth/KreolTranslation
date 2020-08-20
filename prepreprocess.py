# Only use this if the english and kreol sentences are separated in two files.
#	Check out English.txt and Kreol.txt as an example
# This file will create a Dataset.txt file based on the english and kreol text files which are the direct translation between each lines
import io

def prepreprocess(English, Kreol, NumLines):
	lines1 = io.open(English).read().strip().split('\n')
	lines2 = io.open(Kreol).read().strip().split('\n')
	lines = io.open("Dataset.txt", "w+")
	for i in range(0,NumLines):
		lines.write(lines1[i] + '\t' + lines2[i] + '\n')

#example
prepreprocess("english.txt", "kreol.txt", 1006)