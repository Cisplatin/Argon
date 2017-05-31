# Argon

A collection of cryptographic primitives and challenges in Python.

## Examples

Running the RC4 algorithm using the seed `10010011`, getting the first 10 bits:

```
from structures.binnum import BinNum
from prngs.rc4 import RC4

seed = BinNum('10010011')
bits = 10
prng = RC4(seed)

print prng.generate_output(bits)
```
