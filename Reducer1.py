#!/usr/bin/env python

import sys
import re

index = {}
	 
for line in sys.stdin:
	word, postings = line.split('\t')
	postings = postings.split('\n')[0]
	index.setdefault(word,[])        
	#for posting in postings.split(','):
        #file, count = postings.split(':')
	      #  count = int(count) 
	if postings not in index[word]:
		index[word].append(postings)
	      #  index[word][file] += count
  
for word in index:
	sys.stdout.write("{0}\t{1}\n".format(word, index[word]))
