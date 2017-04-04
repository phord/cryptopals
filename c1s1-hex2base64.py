#!/usr/bin/python

from mycrypto import *

#http://cryptopals.com/sets/1/challenges/1

src='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
bin = hex2bin(src)
print "   Hex: ", len(bin), bin2hex(bin)
dest = bin2b64(bin)
print "Base64: ", len(dest), dest
print src.upper() == bin2hex(bin)
print dest == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

print bin2hex(b642bin(dest))
print src
print bin2hex(b642bin(dest)) == src.upper()
