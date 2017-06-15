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

Running the RC4 cipher to encrypt `1001` using the key `1010`:

```
from structures.binnum import BinNum
from ciphers.rc4 import RC4

key = BinNum('1010')
text = BinNum('1001')
cipher = RC4(key)

print cipher.encrypt(text)
```
