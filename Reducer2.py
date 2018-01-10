#!/usr/bin/env python

import sys

index = {}

for line in sys.stdin:
	word, fileName = line.split('\t')
	index.setdefault(word, {})        
	file, count = fileName.split(':')
	count = int(count)     
	index[word].setdefault(file, 0)
	index[word][file] += count

for word in index:
	sys.stdout.write("{0}\t{1}\n".format(word, index[word]))