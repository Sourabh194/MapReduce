#!/usr/bin/env python

import sys
import re

index = {}
	 
for line in sys.stdin:
	word, fileName = line.split('\t')
	fileName = fileName.split('\n')[0]
	index.setdefault(word,[])
	if FileName not in index[word]:
		index[word].append(FileName)
		
for word in index:
	sys.stdout.write("{0}\t{1}\n".format(word, index[word]))
