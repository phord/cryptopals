#!/usr/bin/python

from mycrypto import *

#http://cryptopals.com/sets/1/challenges/3

src='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

results = find_byte_key(hex2bin(src))
results.sort(reverse=True)

print "Key:",bin2hex([results[0][1]]), "  Msg:", bin2str(results[0][2])
# for x in results:
#     if x[0]>0:
#         print x[0], bin2hex([x[1]]), bin2str(x[2])
