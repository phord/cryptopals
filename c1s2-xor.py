#!/usr/bin/python

from mycrypto import *

#http://cryptopals.com/sets/1/challenges/2

a='1c0111001f010100061a024b53535009181c'
b='686974207468652062756c6c277320657965'
c='746865206b696420646f6e277420706c6179'
bin = xorbin(hex2bin(a),hex2bin(b))

print c.upper() == bin2hex(bin)
