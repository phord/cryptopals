#!/usr/bin/python

from mycrypto import *
from mycrypto_aes import *

#http://cryptopals.com/sets/1/challenges/8

samples = [hex2bin(line) for line in open('8.txt')]
blocked = [ blockSplit(s,16) for s in samples ]
tupled = [ (set([tuple(x) for x in s]),s) for s in blocked ]
dupcount = [ (1.0 * len(t) / len(s), s) for t,s in tupled ]
dupcount.sort()

if dupcount[0][0] < 1.0:
    for dup, samp in dupcount:
        if dup == 1.0: break
        # TODO: Find the line number that has the dup at the head of our list.
        print "Found ECB pattern: Line {} Duplication: {}%", 0, 100*(1.0-dup)
else:
    print "Did not detect any ECB pattern"
