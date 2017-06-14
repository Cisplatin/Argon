from structures.hexnum import HexNum
from hashes.idempotent import Idempotent

text = HexNum('A1B')
print Idempotent().hash(text)
