from ciphers.streamcipher import StreamCipher
from prngs.idempotent import Idempotent

class OTP(StreamCipher):
  PRNG = Idempotent
