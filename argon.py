# TODO: Fix the import order issue here
from structures.hexnum import HexNum
from structures.binnum import BinNum
from prngs.rc4 import RC4

a = BinNum('1111000011110000')
print a.get_byte(1)
