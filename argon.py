from structures.binnum import BinNum
from prngs.rc4 import RC4
from prngs.idempotent import Idempotent
from ciphers.streamcipher import StreamCipher
from ciphers.otp import OTP

key = BinNum('1001001')
a = RC4(key)
print a.generate_output(10)
cipher = StreamCipher.build_from_prng(Idempotent, key)
print cipher.encrypt(BinNum(key.data[0]))
print cipher.encrypt(BinNum(key.data[2:4]))
cipher.reset()

print cipher.encrypt(key)
print cipher.encrypt(key)
