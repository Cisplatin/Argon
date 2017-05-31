from structures.binnum import BinNum
from prngs.rc4 import RC4


seed = BinNum('10010011')
prng = RC4(seed)
print "Result: %s" % prng.generate_output(10)
