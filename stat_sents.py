#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import fileinput
from collections import OrderedDict

print(sys.argv[-1])

def countf(filename):
    count = 0  
    thefile = open(filename,'rb') 
    while True:  
        buffer = thefile.read(1024 * 8192)  
        if not buffer:  
            break  
        count += buffer.count('\n')  
    thefile.close()  
    return count * 10

def main():
    import numpy as np
    counts=np.array([0]*countf(sys.argv[1]))
    for filename in sys.argv[1:-1]:
        print 'Processing', filename
        len_freqs = OrderedDict()
        i = 0
        with open(filename, 'r') as f:
            for line in f:
		words_in = [w for w in line.strip().split(' ') if w not in [' ', ''] ]
                length = len(words_in)
                if length > int(sys.argv[-1]):counts[i]+=1
                if length not in len_freqs:
                    len_freqs[length] = 1
                else:
                    len_freqs[length] += 1
                i+=1
        a = [0]*(max(len_freqs.keys())+1)
        for t in len_freqs.keys():a[t]=len_freqs[t]
        print [(i+10,sum(a[i:i+10])) for i in range(1, min(len(a), 150), 10)]
        print sum(a[150:])
        print 'Done'

    total = len(sys.argv[1:-1])
    counts = (counts > 0)
    import pickle as pk
    pk.dump(counts, open('split_or_not', 'wb'))
    for filename in sys.argv[1:-1]:
        i = 0
        print 'Saving', filename
        with open(filename, 'r') as f, open(filename+'.a', 'w') as f_a, open(filename+'.b', 'w') as f_b:
            for line in f:
                if counts[i] == True:f_b.write(line)
                else:f_a.write(line)
                i+=1

if __name__ == '__main__':
    main()
