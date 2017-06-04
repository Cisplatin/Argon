from ciphers.streamcipher import StreamCipher
from prngs.rc4 import RC4 as RC4PRNG

class RC4(StreamCipher):
  def __init__(self, key):
    super(RC4, self).__init__(key)
    self.prng = RC4PRNG(key)

  # @param text [BaseNum] The plaintext to encrypt
  # @return [BaseNum] The encrypted ciphertext
  def encrypt(self, text):
    return text ^ self.prng.generate_output(len(text))

  # @param text [BaseNum] The ciphertext to decrypt
  # @return [BaseNum] The plaintext decrypted
  def decrypt(self, text):
    return text ^ self.prng.generate_output(len(text))
