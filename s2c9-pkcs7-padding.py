#!/usr/bin/python

from mycrypto import *
from mycrypto_aes import *

#http://cryptopals.com/sets/2/challenges/9

msg = txt2bin('YELLOW SUBMARINE')

for x in range(21):
    padded=pad(msg,x)
    unpadded=unpad(padded) if x>0 else []
    print "Pad({}): Unpad-test={},  Len={}, {}".format(x, unpadded==msg, len(padded), bin2str(padded))
