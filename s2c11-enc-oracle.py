#!/usr/bin/python

from mycrypto import *
from mycrypto_aes import *
from random import randint

#http://cryptopals.com/sets/2/challenges/11

def rand_vec(size):
    return [randint(0,255) for x in range(size)]

OracleHistory = []
def encryption_oracle(src):
    global OracleHistory
    key = rand_vec(16)
    iv = None
    if randint(0,1) == 1:
        iv = rand_vec(16)

    OracleHistory += [iv is None]

    head_salt = rand_vec(randint(5,10))
    tail_salt = rand_vec(randint(5,10))
    return aes_encrypt(head_salt+src+tail_salt, key, iv)

def is_ecb(vec):
    blocked = blockSplit(vec,16)
    tupled = set([tuple(x) for x in blocked])
    dupcount = 1.0 * len(tupled) / len(blocked)
    return dupcount < 1.0

# Load some sample text (we have to decrypt it, but no worries)

b64 = ''.join([line.rstrip('\n') for line in open('10.txt')])
enc = b642bin(b64)
key = txt2bin('YELLOW SUBMARINE')
iv = [0]*16
dvec = aes_decrypt(enc, key, iv)

Trials = 100
Guesses = []
print "Running {} trials".format(Trials)
for x in range(Trials):
    # encrypt it randomly via the oracle
    trial = encryption_oracle(dvec)
    Guesses += [is_ecb(trial)]

print "ECB guesses: ", len([x for x in Guesses if x])
if OracleHistory == Guesses:
    print "All guesses were correct"
else:
    print "Oh, we made a mistake"
    print Guesses
    print OracleHistory
