from structures.hexnum import HexNum
from prngs.idempotent import Idempotent

seed = HexNum('A1B')
print Idempotent(seed).generate(2)
