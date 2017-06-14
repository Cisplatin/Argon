from structures.hexnum import HexNum
from prngs.idempotent import Idempotent
from prngs.rc4 import RC4

seed = HexNum('A1B')
print Idempotent(seed).generate(2)
print RC4(seed).generate(2)
