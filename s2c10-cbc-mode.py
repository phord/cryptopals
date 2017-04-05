#!/usr/bin/python

from mycrypto import *
from mycrypto_aes import *

#http://cryptopals.com/sets/2/challenges/10

# CBC = Cipher Block Chaining

b64 = ''.join([line.rstrip('\n') for line in open('10.txt')])
enc = b642bin(b64)
key = txt2bin('YELLOW SUBMARINE')
iv = [0]*16

dvec = aes_decrypt(enc, key, iv)
print bin2str(dvec),

reenc = aes_encrypt(dvec, key, iv)
dvec = aes_decrypt(reenc, key, iv)
print reenc == enc
