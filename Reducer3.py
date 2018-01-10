#!/usr/bin/env python

import sys

index = {}

for line in sys.stdin:
	author, words = line.split('\t')
	index.setdefault(author, {})
	word, count = words.split(':')
	count = int(count)   
	index[author].setdefault(word, 0)
	index[author][word] += count

for word in index:
	sys.stdout.write("{0}\t{1}\n".format(word, index[word]))
