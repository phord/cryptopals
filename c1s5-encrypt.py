#!/usr/bin/python

from mycrypto import *

#http://cryptopals.com/sets/1/challenges/5

stanza = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
enc = enc_xor(txt2bin(stanza), txt2bin('ICE'))
print bin2hex(enc)
sol="0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
print hex2bin(sol) == enc
