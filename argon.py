from structures.binnum import BinNum
from prngs.rc4 import RC4
from ciphers.streamcipher import StreamCipher

key = BinNum('1001001')
prng = RC4(key)
cipher = StreamCipher.build_from_prng(RC4, key)
print "Result: %s" % cipher
print cipher.encrypt(key)
