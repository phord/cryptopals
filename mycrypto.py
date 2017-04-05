#!/usr/bin/python

import itertools

most_common_letters=' etaoinsrhld\ncumfpgwybvkxjqz'
digits='0123456789'
printable=[chr(32+i) for i in range(96)] + ['\n']

alpha=''.join([chr(65+i) for i in range(26)])
b64set=alpha + alpha.lower() + digits + "+/"

#____________________________________________________________________________ _
#                                                                     CONVERT
#_____________________
def xorbin(a,b):
    return [A^B for (A,B) in zip(a,b)]

def binxorbyte(bin,ky):
    return [a^ky for a in bin]

def find_byte_key(bin):
    """ Examines the bytes in a binary msg and tries to determine the most likely byte all bytes were
    xored with assuming that the original message was some English language ASCII.  The results are
    returned in an array of tuples of (Score, XOR-candidate, [Decoded-bytes, ...]).  The score is the
    measure of how good a match this XOR-candidate seems to be (producing printable letters). The array
    is sorted with the highest scores at the beginning.
    """
    histo = [(bin.count(x),x) for x in set(bin)]
    histo.sort(reverse=True)

    results = []
    keys = [a[1]^ord(b) for a in histo for b in most_common_letters]
    for ky in set(keys):
        msg = binxorbyte(bin, ky)
        score = score_readable(msg)
        results.append((score, ky, msg))

    results.sort(reverse=True)
    return results

#____________________________________________________________________________ _
#                                                                     ENCRYPT
#_____________________
def enc_xor(msg, key):
    return [x^y for x,y in zip(msg, itertools.cycle(key))]

def matrix_xor(msg, key):
    return [enc_xor(x,y) for x,y in zip(msg, itertools.cycle(key))]

#____________________________________________________________________________ _
#                                                                       CRACK
#_____________________
def hamming_distance(a,b):
    """ Returns hamming distance between two sequences.
        >>> print 37 == hamming_distance(txt2bin('this is a test'),txt2bin('wokka wokka!!!'))
        >>> True
    """
    diff = enc_xor(a,b)
    return sum([(x>>i)&1 for x in diff for i in range(8)])
#_____________________
def likely_key_sizes(enc, min_len=1, max_len=40):
    """Returns hamming-distance-scored key lengths from min_len to max_len for the given
       xor-key-encrypted binary.
       """
    dists = [ (hamming_distance(enc[:keysize],enc[keysize:keysize*2])*1.0/keysize, keysize) for keysize in range(min_len,max_len+1) ]
    dists.sort()
    return [x[1] for x in dists]

def blockSplit(vec, size=16):
    return  [vec[size*i:size*(i+1)] for i in range((len(vec)+size-1)/size)]

def transpose(blocks, size=16):
    return [ [a for a in [x[y] if len(x)>y else None for x in blocks] if a is not None] for y in range(size)]
#_____________________
def likely_keys(enc, min_len=1, max_len=40):
    """Find likely keys in a range of sizes for a given xor-encrypted binary"""

    # Probable key lengths in order of decreasing probability
    sizes = likely_key_sizes(enc)

    candidates = []
    for size in sizes:
        blocks = blockSplit(enc, size)
        transposed = transpose(blocks, size)
        key = [ find_byte_key(stripe)[0][1] for stripe in transposed]
        candidates += [(score_readable(enc_xor(enc, key)), key)]
    candidates.sort(reverse=True)
    return [x[1] for x in candidates]

#____________________________________________________________________________ _
#                                                                     SCORING
#_____________________
def score_letter(x):
    if chr(x) in most_common_letters:
        return len(most_common_letters) - most_common_letters.find(chr(x))
    return 0

def score_printable(x):
    score = score_letter(x)
    if chr(x) in digits:
        score += 15
    elif chr(x) in printable:
        score += 5
    else:
        score = -1
    return score

def score_readable(bin):
    scores = [score_printable(x) for x in bin]
    # if len([x for x in scores if x<0]):
    #     return -1000
    return sum(scores)

#____________________________________________________________________________ _
#                                                                      IMPORT
#_____________________
def hex2nybble(chr):
    if chr<48: raise Exception()
    chr -= 48
    if chr<10: return chr
    # Must be A-F or a-f
    chr -= 7
    if chr < 10: raise Exception()
    if chr < 16: return chr
    # Convert [a-f] => [10..15]
    chr -= 32
    if chr < 10 or chr > 15:
        raise Exception() #Not valid; should be
    return chr

def hex2byte(str):
    return hex2nybble(ord(str[0])) * 0x10 + hex2nybble(ord(str[1]))

def hex2bin(src):
    return [hex2byte(src[i*2:i*2+2]) for i in range(len(src)/2)]

def txt2bin(msg):
    return [ord(x) for x in msg]

#____________________________________________________________________________ _
#                                                                      EXPORT
#_____________________
def base64(byte):
    return b64set[byte&63]

def unbase64(ch):
    if ch == '=': return 0
    return b64set.find(ch)

def nybble2hex(n):
    return '0123456789ABCDEF'[n&15]

def bin2hex(bin):
    return ''.join([nybble2hex(x>>4) + nybble2hex(x) for x in bin])

def bin2b64(bin):
    pad = ((3-len(bin))%3)
    bin.extend([0,0])
    groups = [bin[i*3:i*3+3] for i in range(len(bin)/3)]
    squash = [x[0]*0x10000 + x[1]*0x100 + x[2] for x in groups]
    conv = [[base64(x>>(6*i)) for i in range(3,-1,-1) ] for x in squash ]
    enc = ''.join([''.join(x) for x in conv])
    if pad: enc=enc[:-pad] + pad*'='
    return enc

def b642bin(txt):
    pad=len(txt)-len(txt.rstrip('='))
    conv = [unbase64(x) for x in txt]
    groups = [conv[i*4:i*4+4] for i in range(len(conv)/4)]
    squash = [ sum([x[3-i] << (6*i) for i in range(3,-1,-1) ]) for x in groups]
    bin = [[(x>>(16-8*i))&0xff for i in range(3)] for x in squash]
    bin = [x for y in bin for x in y ]
    if pad: bin = bin[:-pad]
    return bin

def bin2str(bin):
    return ''.join([chr(x) if chr(x) in printable else '[{}]'.format(x) for x in bin])
