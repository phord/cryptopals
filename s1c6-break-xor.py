#!/usr/bin/python

from mycrypto import *

#http://cryptopals.com/sets/1/challenges/6

b64 = ''.join([line.rstrip('\n') for line in open('6.txt')])
enc = b642bin(b64)

keys = likely_keys(enc)

print bin2str(keys[0])
print '='*len(keys[0])
print bin2str(enc_xor(enc, keys[0]))
