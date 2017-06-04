from ciphers.streamcipher import StreamCipher
from prngs.rc4 import RC4 as RC4PRNG

class RC4(StreamCipher):
  PRNG = RC4PRNG

  def __init__(self, key):
    super(RC4, self).__init__(key)
    self.prng = RC4.PRNG(key)
