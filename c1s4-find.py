#!/usr/bin/python

from mycrypto import *

#http://cryptopals.com/sets/1/challenges/4

codes = [line.rstrip('\n') for line in open('4.txt')]

results = [ find_byte_key(hex2bin(bin)) for bin in codes]
results = [ x for y in results for x in y if x[0]>0]
results.sort(reverse=True)

print "Key:",bin2hex([results[0][1]]), "  Msg:", bin2str(results[0][2])
# for x in results:
#     if x[0]>0:
#         print x[0], bin2hex([x[1]]), bin2str(x[2])
