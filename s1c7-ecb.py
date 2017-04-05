#!/usr/bin/python

from mycrypto import *
from mycrypto_aes import *

#http://cryptopals.com/sets/1/challenges/7
# openssl enc -d -a -nosalt -aes-128-ecb -K 59454c4c4f57205355424d4152494e45 -in 7.txt

b64 = ''.join([line.rstrip('\n') for line in open('7.txt')])
enc = b642bin(b64)
key = txt2bin('YELLOW SUBMARINE')

dvec = aes_decrypt(enc, key)
print bin2str(dvec),
