from structures.binnum import BinNum
from structures.hexnum import HexNum
from prngs.rc4 import RC4


seed = BinNum('1111000011110001')
prng = RC4(seed)
print "Result: %s" % prng.generate_output(10)
