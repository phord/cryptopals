#!/usr/bin/python

from mycrypto import *

#http://cryptopals.com/sets/1/challenges/7

b64 = ''.join([line.rstrip('\n') for line in open('7.txt')])
enc = b642bin(b64)

key = 'YELLOW SUBMARINE'
print bin2str(dec_ecb(enc, key))
